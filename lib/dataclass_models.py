"""Dataclass Module
"""
from dataclasses import dataclass, asdict
from datetime import datetime
from enum import Enum
import json


class BaseModel:
    """Base model for dataclasses
    """
    def dict(self):
        """Returns a dict representation of the dataclass

        Returns:
            dict: Dataclass attributes
        """
        return {k: str(v) for k, v in asdict(self).items()}

    def to_json(self, field: dict):
        """Converts a dict to a JSON object

        Returns:
            str: JSON object
        """
        return json.dumps(field)

    @classmethod
    def attributes(cls):
        """Return a list of the dataclass attributes

        Returns:
            list: Attributes of the dataclass
        """
        return list(cls.__annotations__.keys())

@dataclass
class PortalUser(BaseModel):
    """Portal User Dataclass
    """
    username: str
    email: str
    pass_hash: str
    create_datetime: datetime
    update_datetime: datetime
    is_active: bool


class ClearanceLevel(str, Enum):
    """Enum class for clearance level
    """
    BASE = "standard"
    MASTER = "master"
    SUPER = "super"


@dataclass
class DashboardUser(BaseModel):
    """Dasboard User Dataclass
    """
    username: str
    pass_hash: str
    create_datetime: datetime
    is_active: bool
    clearance: ClearanceLevel


class SourceTable(str, Enum):
    """Enum class for source table
    """
    PORTAL = "portal_user"
    DASHBOARD = "dashboard_user"

@dataclass
class UserContact(BaseModel):
    """User Contact Dataclass
    """
    user_id: int
    source_table: SourceTable
    email: str
    phone: int
