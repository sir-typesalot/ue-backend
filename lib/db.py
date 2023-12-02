"""DB Manager module"""
import os
import contextlib
import mysql.connector
from dotenv import load_dotenv

class DB():
    """Initialize DB connection"""
    def __init__(self, db='urban_eden'):
        self.db = db

    @contextlib.contextmanager
    def db_connect(self, cur_type=None):
        """Create DB Connection

        Args:
            cur_type (str, optional): Cursor type. Defaults to None.

        Yields:
            MySQLCursor: Cursor Object
        """
        config = self._get_config()
        cnx = mysql.connector.MySQLConnection(**config)

        if cur_type == 'dict':
            cursor = cnx.cursor(dictionary=True, buffered=True)
        else:
            cursor = cnx.cursor(buffered=True)

        try:
            yield cursor
        finally:
            cnx.commit()
            cursor.close()
            cnx.close()

    def _get_config(self) -> dict:
        load_dotenv()
        return {
            "host": os.environ.get('DB_HOST'),
            "user": os.environ.get('DB_USER'),
            "passwd": os.environ.get('DB_PASSWORD'),
            "database": self.db
        }

    def change_db(self, db: str):
        """Change active database

        Args:
            db (str): Database name to change to
        """
        self.db = db
