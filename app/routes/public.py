"""Public facing endpoints that don't require authentication
"""
from flask import Blueprint

external = Blueprint('public', __name__)

@external.route('/', methods=['GET'])
def public():
    """Basic endpoint

    Returns:
        str: Endpoint response
    """
    return "Hello World"
