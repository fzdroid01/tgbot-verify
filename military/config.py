"""Konfigurasi dasar untuk verifikasi ChatGPT Military."""
SHEERID_BASE_URL = "https://services.sheerid.com"

# Status militer default yang dikirim ke collectMilitaryStatus
DEFAULT_STATUS = "VETERAN"

# Daftar organisasi militer yang diizinkan (id -> name)
ORGANIZATIONS = {
    "4070": "Army",
    "4073": "Air Force",
    "4072": "Navy",
    "4071": "Marine Corps",
    "4074": "Coast Guard",
    "4544268": "Space Force",
}
DEFAULT_ORG_ID = "4070"

# Rentang tahun untuk tanggal lahir dan discharge
BIRTH_YEAR_RANGE = (1960, 1985)
DISCHARGE_YEAR_RANGE = (2015, 2023)

# Flags/metadata default
DEFAULT_FLAGS = (
    '{"doc-upload-considerations":"default","doc-upload-may24":"default",'
    '"doc-upload-redesign-use-legacy-message-keys":false,'
    '"docUpload-assertion-checklist":"default",'
    '"include-cvec-field-france-student":"not-labeled-optional",'
    '"org-search-overlay":"default","org-selected-display":"default"}'
)

# Placeholder programId untuk referer; jika link memuat programId akan ditimpa.
PROGRAM_ID_FALLBACK = "UPDATE_PROGRAM_ID"