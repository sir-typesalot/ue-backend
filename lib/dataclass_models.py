"""Dataclass Module
"""
import json
from dataclasses import dataclass, asdict
from datetime import datetime
from decimal import Decimal
from lib.helpers.enum_base import EnumBase


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
    id: int
    username: str
    email: str
    pass_hash: str
    create_datetime: datetime
    update_datetime: datetime = None
    is_active: bool


class ClearanceLevel(EnumBase):
    """Enum class for clearance level
    """
    BASE = "base"
    MID = "medium"
    HIGH = "high"


@dataclass
class DashboardUser(BaseModel):
    """Dasboard User Dataclass
    """
    id: int
    username: str
    pass_hash: str
    create_datetime: datetime
    is_active: bool
    clearance: ClearanceLevel


class SourceTable(EnumBase):
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
    email: str = None
    phone: int = None

@dataclass
# pylint: disable=too-many-instance-attributes
class Garden(BaseModel):
    """Garden Dataclass
    """
    id: int
    name: str
    address1: str
    address2: str
    state: str
    zip: str
    sq_ft: int = None
    plot_count: int = None
    lat: Decimal = None
    lng: Decimal = None
    is_active: bool

@dataclass
class CustomContent(BaseModel):
    """Custom Content Dataclass
    """
    garden_id: int
    open_hours: dict = None
    contact_email: str = None
    contact_phone: int = None

@dataclass
class GardenAdmin(BaseModel):
    """Garden Admin Dataclass
    """
    garden_id: int
    admin_id: int

@dataclass
class GardenGroup(BaseModel):
    """Garden Group Dataclass
    """
    user_id: int
    garden_id: int
