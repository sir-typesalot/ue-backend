"""_summary_
"""
from enum import Enum
from abc import ABC, ABCMeta

class AbstractEnumMeta(ABCMeta, type(Enum)):
    """Meta abstract class for the abstract base class to inherit from
    """

class EnumBase(ABC, Enum, metaclass=AbstractEnumMeta):
    """Base enumeration class for child classes to inherit from
    """

    @classmethod
    def has_value(cls, value):
        """Check if attribute exists in class

        Args:
            value (str): Attribute to check

        Returns:
            bool: Whether it exists in class
        """
        return any(value == item.value for item in cls)

    @classmethod
    def get_item(cls, search_item):
        """Get specified item from class

        Args:
            value (str): Key of value to return

        Returns:
            any: Attribute
        """
        for item in cls:
            if search_item == item.value:
                return item
        return None
