"""
Sistem pelacakan identitas yang sudah digunakan untuk verifikasi military.
Menyimpan identitas yang sudah "burned" (rate limited) di SheerID.
"""
import json
import os
import logging
from datetime import datetime
from typing import Dict, List, Optional, Set

logger = logging.getLogger(__name__)

# Path untuk menyimpan data identitas yang sudah digunakan
USED_IDENTITIES_FILE = os.path.join(os.path.dirname(__file__), "used_identities.json")


class UsedIdentitiesTracker:
    """Kelas untuk melacak identitas yang sudah digunakan dan burned."""
    
    def __init__(self, file_path: str = USED_IDENTITIES_FILE):
        self.file_path = file_path
        self._used_identities: Dict[str, dict] = {}
        self._burned_identities: Set[str] = set()
        self._load()
    
    def _generate_key(self, first_name: str, last_name: str, birth_date: str) -> str:
        """Generate unique key untuk identitas berdasarkan nama dan tanggal lahir."""
        return f"{first_name.upper()}_{last_name.upper()}_{birth_date}"
    
    def _load(self) -> None:
        """Load data dari file JSON."""
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self._used_identities = data.get("used", {})
                    self._burned_identities = set(data.get("burned", []))
                    logger.info(f"Loaded {len(self._used_identities)} used identities, {len(self._burned_identities)} burned")
            except Exception as e:
                logger.error(f"Error loading used identities: {e}")
                self._used_identities = {}
                self._burned_identities = set()
        else:
            logger.info("No existing used identities file found, starting fresh")
    
    def _save(self) -> None:
        """Save data ke file JSON."""
        try:
            data = {
                "used": self._used_identities,
                "burned": list(self._burned_identities),
                "last_updated": datetime.now().isoformat()
            }
            with open(self.file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            logger.debug("Saved used identities to file")
        except Exception as e:
            logger.error(f"Error saving used identities: {e}")
    
    def is_burned(self, first_name: str, last_name: str, birth_date: str) -> bool:
        """Cek apakah identitas sudah burned (rate limited)."""
        key = self._generate_key(first_name, last_name, birth_date)
        return key in self._burned_identities
    
    def is_used(self, first_name: str, last_name: str, birth_date: str) -> bool:
        """Cek apakah identitas sudah pernah digunakan."""
        key = self._generate_key(first_name, last_name, birth_date)
        return key in self._used_identities
    
    def mark_as_used(self, first_name: str, last_name: str, birth_date: str, 
                     verification_id: str = None, success: bool = None) -> None:
        """Tandai identitas sebagai sudah digunakan."""
        key = self._generate_key(first_name, last_name, birth_date)
        self._used_identities[key] = {
            "first_name": first_name,
            "last_name": last_name,
            "birth_date": birth_date,
            "verification_id": verification_id,
            "success": success,
            "used_at": datetime.now().isoformat()
        }
        self._save()
        logger.info(f"Marked identity as used: {first_name} {last_name}")
    
    def mark_as_burned(self, first_name: str, last_name: str, birth_date: str,
                       reason: str = "verificationLimitExceeded") -> None:
        """Tandai identitas sebagai burned (rate limited)."""
        key = self._generate_key(first_name, last_name, birth_date)
        self._burned_identities.add(key)
        
        # Update info di used_identities juga
        if key in self._used_identities:
            self._used_identities[key]["burned"] = True
            self._used_identities[key]["burned_reason"] = reason
            self._used_identities[key]["burned_at"] = datetime.now().isoformat()
        else:
            self._used_identities[key] = {
                "first_name": first_name,
                "last_name": last_name,
                "birth_date": birth_date,
                "burned": True,
                "burned_reason": reason,
                "burned_at": datetime.now().isoformat()
            }
        
        self._save()
        logger.warning(f"Marked identity as BURNED: {first_name} {last_name} - {reason}")
    
    def get_burned_count(self) -> int:
        """Dapatkan jumlah identitas yang burned."""
        return len(self._burned_identities)
    
    def get_used_count(self) -> int:
        """Dapatkan jumlah identitas yang sudah digunakan."""
        return len(self._used_identities)
    
    def get_all_burned_keys(self) -> Set[str]:
        """Dapatkan semua key identitas yang burned."""
        return self._burned_identities.copy()
    
    def clear_all(self) -> None:
        """Hapus semua data (gunakan dengan hati-hati)."""
        self._used_identities = {}
        self._burned_identities = set()
        self._save()
        logger.warning("Cleared all used identities data")


# Singleton instance untuk digunakan di seluruh aplikasi
_tracker_instance: Optional[UsedIdentitiesTracker] = None


def get_tracker() -> UsedIdentitiesTracker:
    """Dapatkan singleton instance dari tracker."""
    global _tracker_instance
    if _tracker_instance is None:
        _tracker_instance = UsedIdentitiesTracker()
    return _tracker_instance


def is_identity_burned(first_name: str, last_name: str, birth_date: str) -> bool:
    """Helper function untuk cek apakah identitas burned."""
    return get_tracker().is_burned(first_name, last_name, birth_date)


def mark_identity_burned(first_name: str, last_name: str, birth_date: str, 
                         reason: str = "verificationLimitExceeded") -> None:
    """Helper function untuk tandai identitas sebagai burned."""
    get_tracker().mark_as_burned(first_name, last_name, birth_date, reason)


def mark_identity_used(first_name: str, last_name: str, birth_date: str,
                       verification_id: str = None, success: bool = None) -> None:
    """Helper function untuk tandai identitas sebagai sudah digunakan."""
    get_tracker().mark_as_used(first_name, last_name, birth_date, verification_id, success)