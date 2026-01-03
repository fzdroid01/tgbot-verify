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
    },
    {
        "first_name": "WILLIS",
        "last_name": "HAYCOCK",
        "birth_date": "1940-12-12",
        "discharge_date": "2023-08-01",
        "organization_id": "4070"
    },
    {
        "first_name": "MARK",
        "last_name": "HEALY",
        "birth_date": "1961-03-09",
        "discharge_date": "2024-10-27",
        "organization_id": "4070"
    },
    {
        "first_name": "MATTHEW",
        "last_name": "HEALY",
        "birth_date": "1990-08-27",
        "discharge_date": "2023-05-23",
        "organization_id": "4070"
    },
    {
        "first_name": "JERRY",
        "last_name": "HEBERT",
        "birth_date": "1946-11-12",
        "discharge_date": "2005-09-24",
        "organization_id": "4070"
    },
    {
        "first_name": "GARY",
        "last_name": "HEFLIN",
        "birth_date": "1946-05-25",
        "discharge_date": "2006-01-10",
        "organization_id": "4070"
    },
    {
        "first_name": "LYNN",
        "last_name": "HELFERD",
        "birth_date": "1928-10-20",
        "discharge_date": "2025-02-20",
        "organization_id": "4070"
    },
    {
        "first_name": "DENNIS",
        "last_name": "HELSEL",
        "birth_date": "1947-12-31",
        "discharge_date": "2025-01-16",
        "organization_id": "4070"
    },
    {
        "first_name": "CLINTON",
        "last_name": "HELTON",
        "birth_date": "1929-12-25",
        "discharge_date": "2023-10-19",
        "organization_id": "4070"
    },
    {
        "first_name": "JAMES",
        "last_name": "HENDERSON",
        "birth_date": "1947-11-14",
        "discharge_date": "2023-01-12",
        "organization_id": "4070"
    },
    {
        "first_name": "STEPHEN",
        "last_name": "HENLEY",
        "birth_date": "1925-11-27",
        "discharge_date": "2025-06-07",
        "organization_id": "4070"
    },
    {
        "first_name": "WILLIAM",
        "last_name": "HENRY",
        "birth_date": "1945-12-16",
        "discharge_date": "2025-09-08",
        "organization_id": "4070"
    },
    {
        "first_name": "KENNETH",
        "last_name": "HERBERGER",
        "birth_date": "1936-08-27",
        "discharge_date": "2025-01-03",
        "organization_id": "4070"
    },
    {
        "first_name": "VINCENT",
        "last_name": "HERBERT",
        "birth_date": "1946-11-30",
        "discharge_date": "2021-11-29",
        "organization_id": "4070"
    },
    {
        "first_name": "MARK",
        "last_name": "HERRENBRUCK",
        "birth_date": "1946-08-24",
        "discharge_date": "2023-06-09",
        "organization_id": "4070"
    },
    {
        "first_name": "JAMES",
        "last_name": "HESSON",
        "birth_date": "1931-11-28",
        "discharge_date": "2024-02-24",
        "organization_id": "4070"
    },
    {
        "first_name": "GUSTAV",
        "last_name": "HEYER",
        "birth_date": "1941-08-30",
        "discharge_date": "2016-03-12",
        "organization_id": "4070"
    },
    {
        "first_name": "WILLIAM",
        "last_name": "HIGGINS",
        "birth_date": "1944-12-05",
        "discharge_date": "2023-09-22",
        "organization_id": "4070"
    },
    {
        "first_name": "EDWARD",
        "last_name": "HILDEBRAND",
        "birth_date": "1947-07-20",
        "discharge_date": "2020-07-28",
        "organization_id": "4070"
    },
    {
        "first_name": "HUBERT",
        "last_name": "HILL",
        "birth_date": "1941-05-23",
        "discharge_date": "2025-04-10",
        "organization_id": "4070"
    },
    {
        "first_name": "RAYMOND",
        "last_name": "HILL",
        "birth_date": "1939-09-18",
        "discharge_date": "2023-04-16",
        "organization_id": "4070"
    },
    {
        "first_name": "JOSEPH",
        "last_name": "HOPKO",
        "birth_date": "1947-01-25",
        "discharge_date": "2023-12-30",
        "organization_id": "4070"
    },
    {
        "first_name": "LEIGH",
        "last_name": "HOPP",
        "birth_date": "1931-09-28",
        "discharge_date": "2025-03-12",
        "organization_id": "4070"
    },
    {
        "first_name": "JERRY",
        "last_name": "HOPPER",
        "birth_date": "1931-08-11",
        "discharge_date": "2025-01-25",
        "organization_id": "4070"
    },
    {
        "first_name": "GREGORY",
        "last_name": "HORAN",
        "birth_date": "1949-01-22",
        "discharge_date": "2021-11-06",
        "organization_id": "4070"
    },
    {
        "first_name": "CRAIG",
        "last_name": "HORTEN",
        "birth_date": "1948-08-19",
        "discharge_date": "2025-09-03",
        "organization_id": "4070"
    },
    {
        "first_name": "ROBERT",
        "last_name": "HOSTETTER",
        "birth_date": "1953-05-11",
        "discharge_date": "2025-01-19",
        "organization_id": "4070"
    },
    {
        "first_name": "DAVID",
        "last_name": "HOTTEL",
        "birth_date": "1934-09-03",
        "discharge_date": "2024-01-30",
        "organization_id": "4070"
    },
    {
        "first_name": "LARRY",
        "last_name": "HOUNTZ",
        "birth_date": "1938-04-22",
        "discharge_date": "2023-02-02",
        "organization_id": "4070"
    },
    {
        "first_name": "JEREMIAH",
        "last_name": "HOWALD",
        "birth_date": "1927-11-19",
        "discharge_date": "2020-09-23",
        "organization_id": "4070"
    },
    {
        "first_name": "MALCOLM",
        "last_name": "HOWARD",
        "birth_date": "1939-06-24",
        "discharge_date": "2025-01-12",
        "organization_id": "4070"
    },
    # Data baru dari pencarian huruf "A" - scraped 2026-01-03
    {
        "first_name": "CLAUDIA",
        "last_name": "AAKER",
        "birth_date": "1949-11-28",
        "discharge_date": "2015-04-01",
        "organization_id": "4070"
    },
    {
        "first_name": "DONALD",
        "last_name": "AAKER",
        "birth_date": "1934-07-11",
        "discharge_date": "2022-11-22",
        "organization_id": "4070"
    },
    {
        "first_name": "DENNIS",
        "last_name": "AANDERUD",
        "birth_date": "1943-01-18",
        "discharge_date": "2021-12-20",
        "organization_id": "4070"
    },
    {
        "first_name": "JACQUELINE",
        "last_name": "AANENSON",
        "birth_date": "1923-02-18",
        "discharge_date": "2018-01-11",
        "organization_id": "4070"
    },
    {
        "first_name": "QUENTIN",
        "last_name": "AANENSON",
        "birth_date": "1921-04-21",
        "discharge_date": "2008-12-28",
        "organization_id": "4070"
    },
    {
        "first_name": "DONALD",
        "last_name": "AANERUD",
        "birth_date": "1925-02-27",
        "discharge_date": "1966-11-21",
        "organization_id": "4070"
    },
    {
        "first_name": "EDWARD",
        "last_name": "AANSTOOS",
        "birth_date": "1926-06-07",
        "discharge_date": "1998-01-21",
        "organization_id": "4070"
    },
    {
        "first_name": "VIRGINIA",
        "last_name": "AANSTOOS",
        "birth_date": "1923-10-18",
        "discharge_date": "2005-12-27",
        "organization_id": "4070"
    },
    {
        "first_name": "JAMES",
        "last_name": "AARESTAD",
        "birth_date": "1924-12-03",
        "discharge_date": "2022-01-13",
        "organization_id": "4070"
    },
    {
        "first_name": "ALBERT",
        "last_name": "AARON",
        "birth_date": "1927-07-20",
        "discharge_date": "2013-01-26",
        "organization_id": "4070"
    },
    {
        "first_name": "ALICE",
        "last_name": "AARON",
        "birth_date": "1937-05-26",
        "discharge_date": "2017-08-29",
        "organization_id": "4070"
    },
    {
        "first_name": "ALTON",
        "last_name": "AARON",
        "birth_date": "1913-09-07",
        "discharge_date": "1999-06-05",
        "organization_id": "4070"
    },
    {
        "first_name": "DONALD",
        "last_name": "AARON",
        "birth_date": "1923-08-19",
        "discharge_date": "1992-03-08",
        "organization_id": "4070"
    },
    {
        "first_name": "HAROLD",
        "last_name": "AARON",
        "birth_date": "1921-06-21",
        "discharge_date": "1980-04-30",
        "organization_id": "4070"
    },
    {
        "first_name": "JACK",
        "last_name": "AARON",
        "birth_date": "1933-09-11",
        "discharge_date": "2019-01-24",
        "organization_id": "4070"
    },
    {
        "first_name": "JEROME",
        "last_name": "AARON",
        "birth_date": "1921-02-18",
        "discharge_date": "1986-09-09",
        "organization_id": "4070"
    },
    {
        "first_name": "JUNE",
        "last_name": "AARON",
        "birth_date": "1919-06-18",
        "discharge_date": "2008-02-13",
        "organization_id": "4070"
    },
    {
        "first_name": "LIESELOTTE",
        "last_name": "AARON",
        "birth_date": "1924-11-29",
        "discharge_date": "2022-12-04",
        "organization_id": "4070"
    },
    {
        "first_name": "LILLIAN",
        "last_name": "AARON",
        "birth_date": "1914-06-07",
        "discharge_date": "1997-06-13",
        "organization_id": "4070"
    },
    {
        "first_name": "MARGARET",
        "last_name": "AARON",
        "birth_date": "1925-05-01",
        "discharge_date": "2022-06-22",
        "organization_id": "4070"
    },
    {
        "first_name": "MARIANNE",
        "last_name": "AARON",
        "birth_date": "1922-08-31",
        "discharge_date": "2012-10-26",
        "organization_id": "4070"
    },
    {
        "first_name": "MAX",
        "last_name": "AARON",
        "birth_date": "1921-08-03",
        "discharge_date": "1973-09-05",
        "organization_id": "4070"
    },
    {
        "first_name": "MONEITA",
        "last_name": "AARON",
        "birth_date": "1936-04-19",
        "discharge_date": "2003-03-15",
        "organization_id": "4070"
    },
    {
        "first_name": "PATRICIA",
        "last_name": "AARON",
        "birth_date": "1922-01-29",
        "discharge_date": "1987-04-14",
        "organization_id": "4070"
    },
    {
        "first_name": "ROBERT",
        "last_name": "AARON",
        "birth_date": "1924-04-12",
        "discharge_date": "2017-03-08",
        "organization_id": "4070"
    },
    {
        "first_name": "ROY",
        "last_name": "AARON",
        "birth_date": "1929-11-17",
        "discharge_date": "2007-06-02",
        "organization_id": "4070"
    },
    {
        "first_name": "RUTH",
        "last_name": "AARON",
        "birth_date": "1928-05-20",
        "discharge_date": "2021-11-16",
        "organization_id": "4070"
    },
    {
        "first_name": "STANLEY",
        "last_name": "AARON",
        "birth_date": "1916-12-13",
        "discharge_date": "1996-09-05",
        "organization_id": "4070"
    },
    {
        "first_name": "THOMAS",
        "last_name": "AARON",
        "birth_date": "1918-01-04",
        "discharge_date": "2014-05-02",
        "organization_id": "4070"
    },
    {
        "first_name": "TITUS",
        "last_name": "AARON",
        "birth_date": "1932-07-15",
        "discharge_date": "1979-10-24",
        "organization_id": "4070"
    },
    {
        "first_name": "WILLIAM",
        "last_name": "AARON",
        "birth_date": "1930-05-31",
        "discharge_date": "1997-11-12",
        "organization_id": "4070"
    },
    {
        "first_name": "ERMA",
        "last_name": "AARONS",
        "birth_date": "1916-04-21",
        "discharge_date": "2000-09-07",
        "organization_id": "4070"
    },
    {
        "first_name": "ROY",
        "last_name": "AARONS",
        "birth_date": "1929-07-26",
        "discharge_date": "2020-01-15",
        "organization_id": "4070"
    },
    {
        "first_name": "ALBERT",
        "last_name": "AARONSON",
        "birth_date": "1940-11-15",
        "discharge_date": "2021-10-27",
        "organization_id": "4070"
    },
    {
        "first_name": "LEONARD",
        "last_name": "AARONSON",
        "birth_date": "1917-07-14",
        "discharge_date": "2008-02-13",
        "organization_id": "4070"
    },
    {
        "first_name": "RUTH",
        "last_name": "AARONSON",
        "birth_date": "1917-11-23",
        "discharge_date": "2009-01-29",
        "organization_id": "4070"
    },
    {
        "first_name": "JORGEN",
        "last_name": "AARSTAD",
        "birth_date": "1920-08-13",
        "discharge_date": "1993-06-06",
        "organization_id": "4070"
    }
]