"""Database Factory Module

Auto-detects and loads the appropriate database implementation based on environment variables.
Supports MySQL and PostgreSQL.

Usage:
    from database import Database, db
    
    # Use the singleton instance
    user = db.get_user(123)
    
    # Or create a new instance
    database = Database()
"""
import os
import logging
from typing import Optional

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

logger = logging.getLogger(__name__)


def detect_database_type() -> str:
    """
    Detect which database type to use based on environment variables.
    
    Priority:
    1. DB_TYPE environment variable (explicit choice)
    2. POSTGRES_HOST presence (implies PostgreSQL)
    3. MYSQL_HOST presence (implies MySQL)
    4. Default to MySQL for backward compatibility
    
    Returns:
        str: 'mysql' or 'postgres'
    """
    # Check explicit DB_TYPE setting
    db_type = os.getenv('DB_TYPE', '').lower().strip()
    
    if db_type in ('postgres', 'postgresql', 'pg'):
        logger.info("Database type: PostgreSQL (from DB_TYPE)")
        return 'postgres'
    elif db_type in ('mysql', 'mariadb'):
        logger.info("Database type: MySQL (from DB_TYPE)")
        return 'mysql'
    
    # Auto-detect based on available environment variables
    has_postgres = bool(os.getenv('POSTGRES_HOST'))
    has_mysql = bool(os.getenv('MYSQL_HOST'))
    
    if has_postgres and not has_mysql:
        logger.info("Database type: PostgreSQL (auto-detected from POSTGRES_HOST)")
        return 'postgres'
    elif has_mysql and not has_postgres:
        logger.info("Database type: MySQL (auto-detected from MYSQL_HOST)")
        return 'mysql'
    elif has_postgres and has_mysql:
        # Both are set, prefer explicit DB_TYPE or default to MySQL
        logger.warning("Both POSTGRES_HOST and MYSQL_HOST are set. Defaulting to MySQL. Set DB_TYPE to override.")
        return 'mysql'
    else:
        # Neither is set, default to MySQL for backward compatibility
        logger.info("Database type: MySQL (default)")
        return 'mysql'


def get_database_class():
    """
    Get the appropriate database class based on detected type.
    
    Returns:
        Database class (MySQLDatabase or PostgreSQLDatabase)
    """
    db_type = detect_database_type()
    
    if db_type == 'postgres':
        from database_postgres import PostgreSQLDatabase
        return PostgreSQLDatabase
    else:
        from database_mysql import MySQLDatabase
        return MySQLDatabase


# Create the Database alias for compatibility
Database = get_database_class()

# Create a singleton instance for convenience
_db_instance: Optional[object] = None


def get_db():
    """
    Get the singleton database instance.
    Creates one if it doesn't exist.
    
    Returns:
        Database instance
    """
    global _db_instance
    if _db_instance is None:
        _db_instance = Database()
    return _db_instance


# Convenience alias
db = property(lambda self: get_db())


# For direct import: from database import db
class _DBProxy:
    """Proxy class to allow `from database import db` to work as a singleton."""
    
    def __getattr__(self, name):
        return getattr(get_db(), name)
    
    def __repr__(self):
        return f"<DBProxy: {get_db().__class__.__name__}>"


db = _DBProxy()


# Export information about current database type
def get_database_info() -> dict:
    """
    Get information about the current database configuration.
    
    Returns:
        dict with database type and connection info (without sensitive data)
    """
    db_type = detect_database_type()
    
    if db_type == 'postgres':
        return {
            'type': 'PostgreSQL',
            'host': os.getenv('POSTGRES_HOST', os.getenv('MYSQL_HOST', 'localhost')),
            'port': int(os.getenv('POSTGRES_PORT', os.getenv('MYSQL_PORT', 5432))),
            'database': os.getenv('POSTGRES_DATABASE', os.getenv('MYSQL_DATABASE', 'tgbot_verify')),
        }
    else:
        return {
            'type': 'MySQL',
            'host': os.getenv('MYSQL_HOST', 'localhost'),
            'port': int(os.getenv('MYSQL_PORT', 3306)),
            'database': os.getenv('MYSQL_DATABASE', 'tgbot_verify'),
        }


if __name__ == '__main__':
    # Test the database detection
    print("Database Configuration:")
    info = get_database_info()
    for key, value in info.items():
        print(f"  {key}: {value}")
    
    print(f"\nDatabase class: {Database.__name__}")
    print(f"DB proxy: {db}")