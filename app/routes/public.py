"""Public facing endpoints that don't require authentication
"""
from flask import Blueprint

external = Blueprint('public', __name__)

@external.route('/', methods=['GET'])
def public():
    """Base endpoint for the application
    provides a formatted dict that contains basic info about the application.

    Returns:
        dict: Endpoint response
    """
    html = "Join us in the joy of tending to plots bursting with colorful blooms, aromatic herbs,"\
        " and a tapestry of vegetables. Discover the beauty of sustainable living and the"\
        " profound sense of community that blossoms in our little corner of urban paradise."

    return {
        "title": "Urban Eden",
        "content": html,
        "contact": {
            "email": "sample@gmail.com",
            "phone": "800-900-1000"
        }
    }
