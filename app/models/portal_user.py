"""Data model for the portal user
"""
# pylint: disable=unused-import
from datetime import datetime
import bcrypt
from mysql.connector.errors import ProgrammingError
from app.models.base import BaseModel
from lib.dataclass_models import PortalUser
import lib.helpers.dataclass_helpers as helpers

class PortalUserModel(BaseModel):
    """Data model for the Portal user
    """

    def __init__(self):
        super().__init__()
        self.id = None

    def create(self, username: str, pw: str) -> int:
        """Create a new portal user

        Args:
            username (str): Username of new user
            pw (str): Password of new user

        Returns:
            int: User ID of created user
        """
        password = self.create_password(pw)
        # Create dataclass and convert to dict
        user = PortalUser(
            username=username,
            pass_hash=password,
            create_datetime=datetime.now()
        )
        user = helpers.to_dict(user)
        try:
            # Exctract columns and values from dict
            columns, values = self.split(user)
            self.id = self.db.insert('portal_user', columns, values)
        except ProgrammingError as e:
            # add logging at some point
            print(f"Unable to create user - {e}")

        return self.id

    def user_exists(self, user_id: str):
        """Check if a user exists

        Args:
            user_id (str): User ID to check

        Returns:
            bool: Whether user exists
        """
        data = self.get({'id': user_id})
        return bool(data)

    def get(self, search_term: dict):
        """Get a portal user

        Args:
            search_term (dict): _description_

        Returns:
            PortalUser: portal user object
        """
        user = self.db.read('portal_user', search_term)
        if not user:
            return None

        self.id = user['id']
        user = self.sanitize(user, helpers.attributes(PortalUser))
        return PortalUser(**user)

    def create_password(self, pw: str):
        """Hash password string into bcrypt hash

        Args:
            pw (str): Password string to hash

        Returns:
            str: Hashed password
        """
        return bcrypt.hashpw(pw.encode('utf8'), bcrypt.gensalt())

    def check_password(self, hash_string: str, pw: str):
        """Check hash against password string

        Args:
            hash (str): Hashed password
            pw (str): Password string

        Returns:
            bool: Whether or not hashes match
        """
        return bcrypt.checkpw(pw.encode('utf8'), hash_string.encode('utf8'))

    def authenticate_user(self, username: str, password: str):
        """Authenticate provided credentials against existing record

        Args:
            username (str): Username to authenticate
            password (str): Password to authenticate

        Returns:
            tuple: tuple with bool whether the username and pass matched
        """
        user = self.get({'username': username})

        if not user:
            return False

        username_auth = user.username == username
        password_auth = self.check_password(user.pass_hash, password)
        return password_auth and username_auth

    # Change email
    # Change pw
