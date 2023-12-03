"""Private facing endpoints that require authentication
"""
from flask import Blueprint

internal = Blueprint('private', __name__)

@internal.route('/private')
def private():
    """Basic private endpoint for now

    Returns:
        str: Response
    """
    return "helllo"
