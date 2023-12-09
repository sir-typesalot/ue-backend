"""Helper module for dataclasses
"""
import json
from dataclasses import dataclass, asdict

def to_dict(cls: dataclass):
    """Returns a dict representation of the dataclass

    Returns:
        dict: Dataclass attributes
    """
    return {k: str(v) for k, v in asdict(cls).items()}

def to_json(field: dict):
    """Converts a dict to a JSON object

    Returns:
        str: JSON object
    """
    return json.dumps(field)

def attributes(cls: dataclass):
    """Return a list of the dataclass attributes

    Returns:
        list: Attributes of the dataclass
    """
    return list(cls.__annotations__.keys())
