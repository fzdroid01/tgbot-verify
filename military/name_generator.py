"""Generator util untuk nama, email, dan tanggal untuk verifikasi ChatGPT Military."""
import random
import logging
from datetime import date

import military.config as config
from military.data import REAL_VETERANS
from military.used_identities import is_identity_burned, get_tracker

logger = logging.getLogger(__name__)


class NameGenerator:
    """Pembuat nama Inggris sederhana."""

    ROOTS = {
        "prefixes": [
            "Al",
            "Bri",
            "Car",
            "Dan",
            "El",
            "Fer",
            "Gar",
            "Har",
            "Jes",
            "Kar",
            "Lar",
            "Mar",
            "Nor",
            "Par",
            "Quin",
            "Ros",
            "Sar",
            "Tar",
            "Val",
            "Wil",
        ],
        "middles": [
            "an",
            "en",
            "in",
            "on",
            "ar",
            "er",
            "or",
            "ur",
            "al",
            "el",
            "il",
            "ol",
            "am",
            "em",
            "im",
            "om",
            "ay",
            "ey",
            "oy",
            "ian",
        ],
        "suffixes": [
            "ton",
            "son",
            "man",
            "ley",
            "field",
            "ford",
            "wood",
            "stone",
            "worth",
            "berg",
            "stein",
            "bach",
            "heim",
            "gard",
            "land",
            "wick",
            "shire",
            "dale",
            "brook",
            "ridge",
        ],
        "name_roots": [
            "Alex",
            "Bern",
            "Crist",
            "Dav",
            "Edw",
            "Fred",
            "Greg",
            "Henr",
            "Ivan",
            "John",
            "Ken",
            "Leon",
            "Mich",
            "Nick",
            "Oliv",
            "Paul",
            "Rich",
            "Step",
            "Thom",
            "Will",
        ],
        "name_endings": [
            "a",
            "e",
            "i",
            "o",
            "y",
            "ie",
            "ey",
            "an",
            "en",
            "in",
            "on",
            "er",
            "ar",
            "or",
            "el",
            "al",
            "iel",
            "ael",
            "ine",
            "lyn",
        ],
    }

    PATTERNS = {
        "first_name": [
            ["prefix", "ending"],
            ["name_root", "ending"],
            ["prefix", "middle", "ending"],
            ["name_root", "middle", "ending"],
        ],
        "last_name": [
            ["prefix", "suffix"],
            ["name_root", "suffix"],
            ["prefix", "middle", "suffix"],
            ["compound"],
        ],
    }

    @classmethod
    def _generate_component(cls, pattern):
        parts = []
        for part in pattern:
            if part == "prefix":
                component = random.choice(cls.ROOTS["prefixes"])
            elif part == "middle":
                component = random.choice(cls.ROOTS["middles"])
            elif part == "suffix":
                component = random.choice(cls.ROOTS["suffixes"])
            elif part == "name_root":
                component = random.choice(cls.ROOTS["name_roots"])
            elif part == "ending":
                component = random.choice(cls.ROOTS["name_endings"])
            elif part == "compound":
                part1 = random.choice(cls.ROOTS["prefixes"])
                part2 = random.choice(cls.ROOTS["suffixes"])
                component = part1 + part2
            else:
                component = ""
            parts.append(component)
        return "".join(parts)

    @staticmethod
    def _fmt(val: str) -> str:
        return val.capitalize()

    @classmethod
    def generate(cls, max_attempts: int = 100):
        """
        Pick from REAL_VETERANS if available, avoiding burned identities.
        Returns dict with keys: first_name, last_name, full_name, (optional) birth_date, discharge_date, org_id
        
        Args:
            max_attempts: Jumlah maksimal percobaan untuk menemukan identitas yang belum burned
        
        Returns:
            dict: Data identitas veteran
            
        Raises:
            RuntimeError: Jika semua identitas sudah burned
        """
        # Always use real data if available
        if REAL_VETERANS:
            # Buat salinan list untuk di-shuffle
            available_veterans = REAL_VETERANS.copy()
            random.shuffle(available_veterans)
            
            # Cek berapa banyak identitas yang burned
            tracker = get_tracker()
            burned_count = tracker.get_burned_count()
            total_count = len(REAL_VETERANS)
            
            # Coba temukan identitas yang belum burned
            attempts = 0
            for veteran in available_veterans:
                attempts += 1
                if attempts > max_attempts:
                    break
                    
                first_name = cls._fmt(veteran["first_name"])
                last_name = cls._fmt(veteran["last_name"])
                birth_date = veteran.get("birth_date")
                
                # Cek apakah identitas ini sudah burned
                if birth_date and is_identity_burned(first_name, last_name, birth_date):
                    logger.debug(f"Skipping burned identity: {first_name} {last_name}")
                    continue
                
                logger.info(f"Selected identity: {first_name} {last_name} (attempt {attempts}, burned: {burned_count}/{total_count})")
                return {
                    "first_name": first_name,
                    "last_name": last_name,
                    "full_name": f"{first_name} {last_name}",
                    "birth_date": birth_date,
                    "discharge_date": veteran.get("discharge_date"),
                    "organization_id": veteran.get("organization_id"),
                    "is_real": True
                }
            
            # Jika semua identitas sudah burned, berikan pesan error
            if burned_count >= total_count:
                error_msg = (
                    f"❌ SEMUA IDENTITAS SUDAH BURNED! "
                    f"({burned_count}/{total_count} identitas sudah rate limited). "
                    f"Silakan tambahkan data veteran baru ke military/data.py"
                )
                logger.error(error_msg)
                raise RuntimeError(error_msg)
            
            # Jika masih ada yang tersedia tapi tidak ditemukan dalam max_attempts
            logger.warning(f"Tidak menemukan identitas yang belum burned dalam {max_attempts} percobaan")

        # Fallback only if no real data
        first_name_pattern = random.choice(cls.PATTERNS["first_name"])
        last_name_pattern = random.choice(cls.PATTERNS["last_name"])
        first_name = cls._fmt(cls._generate_component(first_name_pattern))
        last_name = cls._fmt(cls._generate_component(last_name_pattern))
        logger.info(f"Using generated identity (fallback): {first_name} {last_name}")
        return {"first_name": first_name, "last_name": last_name, "full_name": f"{first_name} {last_name}", "is_real": False}


def generate_email(first_name=None, last_name=None):
    """Generate email generik (gmail/outlook) untuk profil veteran."""
    if not first_name or not last_name:
        name = NameGenerator.generate()
        first_name = name["first_name"]
        last_name = name["last_name"]
    
    first = first_name.lower()
    last = last_name.lower()
    rand = random.randint(1000, 9999)
    domains = ["gmail.com", "outlook.com", "hotmail.com", "yahoo.com", "icloud.com"]
    return f"{first}.{last}{rand}@{random.choice(domains)}"


def _rand_date(year_min: int, year_max: int) -> date:
    year = random.randint(year_min, year_max)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return date(year, month, day)


def generate_birth_date() -> str:
    """Tanggal lahir veteran (range dikontrol di config)."""
    y0, y1 = config.BIRTH_YEAR_RANGE
    d = _rand_date(y0, y1)
    return d.strftime("%Y-%m-%d")


def generate_discharge_date(birth_date: str) -> str:
    """Tanggal discharge setelah usia dewasa, dalam range config."""
    y_min, y_max = config.DISCHARGE_YEAR_RANGE
    birth_year = int(birth_date.split("-")[0])
    # minimal usia 18 saat discharge
    y_min = max(y_min, birth_year + 18)
    if y_min > y_max:
        y_min = y_max
    d = _rand_date(y_min, y_max)
    return d.strftime("%Y-%m-%d")