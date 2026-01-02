"""
Real military data scraped from public sources.
Format:
{
    "first_name": "Str",
    "last_name": "Str",
    "birth_date": "YYYY-MM-DD",
    "discharge_date": "YYYY-MM-DD",  # approximate or actual
    "organization_id": "4070" # Default Army, need mapping for others
}
"""

REAL_VETERANS = [
    # From ancexplorer.army.mil
    {
        "first_name": "STEVEN",
        "last_name": "HABER",
        "birth_date": "1947-01-21",
        "discharge_date": "2023-12-12", # Using death date as proxy for discharge/end of service
        "organization_id": "4070" # Army (assumed from source)
    },
    {
        "first_name": "EUGENE",
        "last_name": "HAECKEL",
        "birth_date": "1930-06-12",
        "discharge_date": "2025-03-25",
        "organization_id": "4070"
    },
    {
        "first_name": "FRANCIS",
        "last_name": "HAGEN",
        "birth_date": "1934-09-19",
        "discharge_date": "2024-10-12",
        "organization_id": "4070"
    },
    {
        "first_name": "HAROLD",
        "last_name": "HALE",
        "birth_date": "1950-12-19",
        "discharge_date": "2022-08-31",
        "organization_id": "4070"
    },
    {
        "first_name": "MARY",
        "last_name": "HALIN",
        "birth_date": "1918-09-01",
        "discharge_date": "2025-01-31",
        "organization_id": "4070"
    },
    {
        "first_name": "JAMES",
        "last_name": "HALL",
        "birth_date": "1945-09-27",
        "discharge_date": "2024-05-31",
        "organization_id": "4070"
    },
    {
        "first_name": "MARY",
        "last_name": "HALL",
        "birth_date": "1952-01-08",
        "discharge_date": "2024-12-26",
        "organization_id": "4070"
    },
    {
        "first_name": "TIMOTHY",
        "last_name": "HALL",
        "birth_date": "1980-06-15",
        "discharge_date": "2025-02-12",
        "organization_id": "4070"
    },
    {
        "first_name": "JACK",
        "last_name": "HALTERMAN",
        "birth_date": "1934-10-07",
        "discharge_date": "2024-07-07",
        "organization_id": "4070"
    },
    {
        "first_name": "WILLIAM",
        "last_name": "HAMILTON",
        "birth_date": "1973-10-01",
        "discharge_date": "2024-01-03",
        "organization_id": "4070"
    },
    {
        "first_name": "DON",
        "last_name": "HAMPTON",
        "birth_date": "1967-08-23",
        "discharge_date": "2025-10-18",
        "organization_id": "4070"
    },
    {
        "first_name": "RONALD",
        "last_name": "HAMPTON",
        "birth_date": "1949-12-31",
        "discharge_date": "2018-06-02",
        "organization_id": "4070"
    },
    {
        "first_name": "BERNHART",
        "last_name": "HANENBERGER",
        "birth_date": "1945-10-22",
        "discharge_date": "2024-09-08",
        "organization_id": "4070"
    },
    {
        "first_name": "THOMAS",
        "last_name": "HANLON",
        "birth_date": "1942-02-16",
        "discharge_date": "2024-03-05",
        "organization_id": "4070"
    },
    {
        "first_name": "PHILIP",
        "last_name": "HANSEN",
        "birth_date": "1933-06-02",
        "discharge_date": "2023-09-15",
        "organization_id": "4070"
    },
    {
        "first_name": "EARNEST",
        "last_name": "HANSLEY",
        "birth_date": "1959-08-16",
        "discharge_date": "2025-01-15",
        "organization_id": "4070"
    },
    {
        "first_name": "JOHN",
        "last_name": "HARAR",
        "birth_date": "1944-09-30",
        "discharge_date": "2024-11-21",
        "organization_id": "4070"
    },
    {
        "first_name": "WILLARD",
        "last_name": "HARDMAN",
        "birth_date": "1938-11-04",
        "discharge_date": "2024-09-19",
        "organization_id": "4070"
    },
    {
        "first_name": "THOMAS",
        "last_name": "HARE",
        "birth_date": "1925-05-30",
        "discharge_date": "2021-04-12",
        "organization_id": "4070"
    },
    {
        "first_name": "BRUCE",
        "last_name": "HARRIS",
        "birth_date": "1934-08-13",
        "discharge_date": "2023-10-26",
        "organization_id": "4070"
    }
]