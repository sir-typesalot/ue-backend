"""_summary_
"""
from enum import Enum
from abc import ABC, abstractmethod

class BaseEnum(Enum, ABC):
    """Abstract enum class to be utilized by child enum classes
    """

    @abstractmethod
    def has_member_key(self, key):
        """Check if enum has member

        Args:
            key (str): Key to check

        Returns:
            bool: Whether key is in enum
        """
        return key in self.__members__

    @abstractmethod
    def get_member_key(self, key):
        """Get the value of key from enum

        Args:
            key (str): _description_

        Returns:
            str | None: Value or None if does not exist
        """
        key = self[key].value if self.has_member_key(key) else None
        return key
