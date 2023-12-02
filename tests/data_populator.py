"""Module handling the population of DB tables for unit testing
"""
from .conftest import get_db

def populate_dashboard_user():
    """Populate dashboard_user table
    """
    with get_db() as cursor:
        cursor.execute("""
            INSERT INTO urban_eden.dashboard_user (username, pass_hash, create_datetime, is_active, clearance) VALUES
            ('test_user', '$2y$04$Lfxl0lAeEvh1/ek62Z81Yuaq7h.Qa2oGxh9l7uItscmkMGaDIon.C', NOW(), true, 'standard');
        """)

def populate_portal_user():
    """Populate portal_user table
    """
    with get_db() as cursor:
        cursor.execute("""
            INSERT INTO portal_user (username, pass_hash, create_datetime, is_active) VALUES
            ('test_user', '$2y$04$Lfxl0lAeEvh1/ek62Z81Yuaq7h.Qa2oGxh9l7uItscmkMGaDIon.C', NOW(), true)
        """)

table_map = {
    'portal_user': populate_dashboard_user,
    'dashboard_user': populate_portal_user
}
def populate_tables(tables: list):
    """Populate tables for unit tests

    Args:
        tables (list): List of tables to populate
    """
    for table in tables:
        table_map[table]()
