"""SheerID verifikasi ChatGPT Military."""
import logging
import random
import re
from typing import Dict, Optional, Tuple

import httpx

from . import config
from .name_generator import (
    NameGenerator,
    generate_birth_date,
    generate_discharge_date,
    generate_email,
)
from .used_identities import mark_identity_burned, mark_identity_used

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)


class SheerIDVerifier:
    """Verifikator Military (dua langkah: status lalu data pribadi)."""

    def __init__(self, verification_id: str, status: str = None, org_id: str = None):
        self.verification_id = verification_id
        self.status = (status or config.DEFAULT_STATUS).upper()
        self.org_id = org_id or config.DEFAULT_ORG_ID
        self.device_fingerprint = self._generate_device_fingerprint()
        self.http_client = httpx.Client(timeout=30.0)

    def __del__(self):
        if hasattr(self, "http_client"):
            self.http_client.close()

    @staticmethod
    def _generate_device_fingerprint() -> str:
        chars = "0123456789abcdef"
        return "".join(random.choice(chars) for _ in range(32))

    @staticmethod
    def parse_verification_id(url: str) -> Optional[str]:
        match = re.search(r"verificationId=([a-f0-9]+)", url, re.IGNORECASE)
        if match:
            return match.group(1)
        return None

    @staticmethod
    def normalize_url(url: str) -> str:
        return url

    def _sheerid_request(
        self, method: str, url: str, body: Optional[Dict] = None
    ) -> Tuple[Dict, int]:
        headers = {"Content-Type": "application/json"}
        response = self.http_client.request(method=method, url=url, json=body, headers=headers)
        try:
            data = response.json()
        except Exception:
            data = response.text
        return data, response.status_code

    def _build_metadata(self) -> Dict:
        program_id = config.PROGRAM_ID_FALLBACK
        referer = f"{config.SHEERID_BASE_URL}/verify/{program_id}/?verificationId={self.verification_id}"
        return {
            "marketConsentValue": False,
            "refererUrl": referer,
            "verificationId": self.verification_id,
            "flags": config.DEFAULT_FLAGS,
            "submissionOptIn": (
                "By submitting the personal information above, I acknowledge that my personal "
                "information is being collected under the privacy policy of the business from which "
                "I am seeking a discount, and I understand that my personal information will be "
                "shared with SheerID as a processor/third-party service provider in order for "
                "SheerID to confirm my eligibility for a special offer."
            ),
        }

    def verify(self, max_retries: int = 10) -> Dict:
        """
        Verifikasi dengan sistem retry otomatis.
        Jika identitas A gagal (rate limited), otomatis coba identitas B, C, dst.
        
        Args:
            max_retries: Jumlah maksimal percobaan dengan identitas berbeda (default: 10)
            
        Returns:
            Dict dengan hasil verifikasi
        """
        last_error = None
        tried_identities = []
        
        for attempt in range(1, max_retries + 1):
            # Variabel untuk menyimpan data identitas yang digunakan
            first_name = None
            last_name = None
            birth_date = None
            
            try:
                logger.info(f"🔄 Percobaan verifikasi ke-{attempt}/{max_retries}")
                
                # generate profile data
                profile = NameGenerator.generate()
                first_name = profile["first_name"]
                last_name = profile["last_name"]
                email = generate_email(first_name, last_name)
                
                # Use real dates and org if available (from real data), otherwise generate random
                if profile.get("is_real"):
                    birth_date = profile.get("birth_date")
                    discharge_date = profile.get("discharge_date")
                    self.org_id = profile.get("organization_id", self.org_id)
                else:
                    birth_date = generate_birth_date()
                    discharge_date = generate_discharge_date(birth_date)
                
                org_name = config.ORGANIZATIONS.get(self.org_id, "Army")
                
                # Simpan identitas yang dicoba
                tried_identities.append(f"{first_name} {last_name}")

                logger.info(
                    f"Military profile ({'REAL' if profile.get('is_real') else 'RANDOM'}): "
                    f"{first_name} {last_name}, org {self.org_id} {org_name}, "
                    f"birth {birth_date}, discharge {discharge_date}, email {email}"
                )
                
                # Tandai identitas sebagai sudah digunakan
                if birth_date:
                    mark_identity_used(first_name, last_name, birth_date, self.verification_id)

                # step 1: collectMilitaryStatus
                step1_body = {"status": self.status}
                step1_url = (
                    f"{config.SHEERID_BASE_URL}/rest/v2/verification/"
                    f"{self.verification_id}/step/collectMilitaryStatus"
                )
                step1_data, step1_status = self._sheerid_request("POST", step1_url, step1_body)
                
                # Cek apakah ada error verificationLimitExceeded
                if step1_status == 429 or (isinstance(step1_data, dict) and
                    "verificationLimitExceeded" in str(step1_data.get("errorIds", []))):
                    if birth_date:
                        mark_identity_burned(first_name, last_name, birth_date, "verificationLimitExceeded")
                    logger.warning(f"⚠️ Identitas {first_name} {last_name} burned (step 1), mencoba identitas lain...")
                    last_error = f"verificationLimitExceeded - Identitas {first_name} {last_name}"
                    continue  # Coba identitas berikutnya
                
                if step1_status != 200:
                    raise Exception(f"collectMilitaryStatus gagal (status {step1_status}): {step1_data}")

                submission_url = None
                if isinstance(step1_data, dict):
                    submission_url = step1_data.get("submissionUrl")
                    current_step = step1_data.get("currentStep")
                    if current_step == "error":
                        error_ids = step1_data.get("errorIds", ["unknown error"])
                        err = ", ".join(error_ids)
                        # Cek apakah error adalah verificationLimitExceeded
                        if "verificationLimitExceeded" in error_ids:
                            if birth_date:
                                mark_identity_burned(first_name, last_name, birth_date, "verificationLimitExceeded")
                            logger.warning(f"⚠️ Identitas {first_name} {last_name} burned (step 1 error), mencoba identitas lain...")
                            last_error = f"verificationLimitExceeded - Identitas {first_name} {last_name}"
                            continue  # Coba identitas berikutnya
                        raise Exception(f"collectMilitaryStatus error: {err}")
                if not submission_url:
                    raise Exception("submissionUrl tidak ditemukan dari langkah pertama")

                # step 2: collectInactiveMilitaryPersonalInfo
                step2_body = {
                    "firstName": first_name,
                    "lastName": last_name,
                    "birthDate": birth_date,
                    "email": email,
                    "phoneNumber": "",
                    "organization": {"id": int(self.org_id), "name": org_name},
                    "dischargeDate": discharge_date,
                    "locale": "en-US",
                    "country": "US",
                    "metadata": self._build_metadata(),
                }
                step2_data, step2_status = self._sheerid_request("POST", submission_url, step2_body)
                
                # Cek apakah ada error verificationLimitExceeded di step 2
                if step2_status == 429 or (isinstance(step2_data, dict) and
                    "verificationLimitExceeded" in str(step2_data.get("errorIds", []))):
                    if birth_date:
                        mark_identity_burned(first_name, last_name, birth_date, "verificationLimitExceeded")
                    logger.warning(f"⚠️ Identitas {first_name} {last_name} burned (step 2), mencoba identitas lain...")
                    last_error = f"verificationLimitExceeded - Identitas {first_name} {last_name}"
                    continue  # Coba identitas berikutnya
                
                if step2_status != 200:
                    raise Exception(f"collectInactiveMilitaryPersonalInfo gagal (status {step2_status}): {step2_data}")
                if isinstance(step2_data, dict) and step2_data.get("currentStep") == "error":
                    error_ids = step2_data.get("errorIds", ["unknown error"])
                    err = ", ".join(error_ids)
                    # Cek apakah error adalah verificationLimitExceeded
                    if "verificationLimitExceeded" in error_ids:
                        if birth_date:
                            mark_identity_burned(first_name, last_name, birth_date, "verificationLimitExceeded")
                        logger.warning(f"⚠️ Identitas {first_name} {last_name} burned (step 2 error), mencoba identitas lain...")
                        last_error = f"verificationLimitExceeded - Identitas {first_name} {last_name}"
                        continue  # Coba identitas berikutnya
                    raise Exception(f"collectInactiveMilitaryPersonalInfo error: {err}")

                # BERHASIL!
                redirect_url = step2_data.get("redirectUrl") if isinstance(step2_data, dict) else None
                logger.info(f"✅ Verifikasi berhasil dengan identitas {first_name} {last_name} (percobaan ke-{attempt})")
                return {
                    "success": True,
                    "pending": True,
                    "message": f"Dokumen dikirim, menunggu review (berhasil pada percobaan ke-{attempt})",
                    "verification_id": self.verification_id,
                    "redirect_url": redirect_url,
                    "status": step2_data,
                    "identity_used": f"{first_name} {last_name}",
                    "attempts": attempt,
                }
                
            except RuntimeError as e:
                # RuntimeError dari NameGenerator ketika semua identitas burned
                logger.error(f"❌ Semua identitas sudah burned: {e}")
                return {
                    "success": False,
                    "message": str(e),
                    "verification_id": self.verification_id,
                    "tried_identities": tried_identities,
                    "attempts": attempt,
                }
            except Exception as e:
                error_msg = str(e)
                # Cek apakah error message mengandung verificationLimitExceeded
                if "verificationLimitExceeded" in error_msg:
                    if birth_date:
                        mark_identity_burned(first_name, last_name, birth_date, "verificationLimitExceeded")
                    logger.warning(f"⚠️ Identitas {first_name} {last_name} burned (exception), mencoba identitas lain...")
                    last_error = error_msg
                    continue  # Coba identitas berikutnya
                else:
                    # Error lain yang bukan rate limit - langsung return error
                    logger.error(f"❌ Military verify gagal (error non-retry): {e}")
                    return {
                        "success": False,
                        "message": error_msg,
                        "verification_id": self.verification_id,
                        "tried_identities": tried_identities,
                        "attempts": attempt,
                    }
        
        # Semua percobaan gagal
        logger.error(f"❌ Gagal setelah {max_retries} percobaan. Identitas yang dicoba: {tried_identities}")
        return {
            "success": False,
            "message": f"Gagal setelah {max_retries} percobaan dengan identitas berbeda. Error terakhir: {last_error}",
            "verification_id": self.verification_id,
            "tried_identities": tried_identities,
            "attempts": max_retries,
        }