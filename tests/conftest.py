"""Configuration setup for pytest unit tests
"""
import pytest
from lib.db import DB
from app.config import Config

def get_db():
    """Return DB connection for unit tests

    Returns:
        _type_: _description_
    """
    Config.SCHEMA = "_test_db"
    db_con = DB(Config.SCHEMA).db_connect
    return db_con()

@pytest.fixture
def db():
    """DB Fixture to pass into tests
    """
    Config.SCHEMA = "_test_db"
    yield
    tables = ["portal_user", "dashboard_user", "garden", "garden_group"]
    with get_db() as cursor:
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
        for table in tables:
            cursor.execute(f"TRUNCATE TABLE {table}")
