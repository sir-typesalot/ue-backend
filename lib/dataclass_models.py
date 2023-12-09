"""Dataclass Module
"""
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from lib.helpers.enum_base import EnumBase

@dataclass
class PortalUser:
    """Portal User Dataclass
    """
    username: str
    pass_hash: str
    create_datetime: datetime
    update_datetime: datetime = None
    is_active: bool = True
    id: int = None


class ClearanceLevel(EnumBase):
    """Enum class for clearance level
    """
    BASE = "base"
    MID = "medium"
    HIGH = "high"


@dataclass
class DashboardUser:
    """Dasboard User Dataclass
    """
    username: str
    pass_hash: str
    create_datetime: datetime
    is_active: bool = True
    id: int = None
    clearance: ClearanceLevel = None


class SourceTable(EnumBase):
    """Enum class for source table
    """
    PORTAL = "portal_user"
    DASHBOARD = "dashboard_user"

@dataclass
class UserContact:
    """User Contact Dataclass
    """
    user_id: int
    source_table: SourceTable
    email: str = None
    phone: int = None

@dataclass
# pylint: disable=too-many-instance-attributes
class Garden:
    """Garden Dataclass
    """
    name: str
    state: str
    zip: str
    sq_ft: int
    plot_count: int
    address1: str
    address2: str = None
    lat: Decimal = None
    lng: Decimal = None
    is_active: bool = True
    id: int = None

@dataclass
class CustomContent:
    """Custom Content Dataclass
    """
    garden_id: int
    open_hours: dict = None
    contact_email: str = None
    contact_phone: int = None

@dataclass
class GardenAdmin:
    """Garden Admin Dataclass
    """
    garden_id: int
    admin_id: int

@dataclass
class GardenGroup:
    """Garden Group Dataclass
    """
    user_id: int
    garden_id: int
