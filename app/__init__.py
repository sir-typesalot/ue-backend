"""
    Import the app object from routes and make accessible to higher levels.
"""
from flask import Flask
from app.config import Config

from app.routes.private import internal
from app.routes.public import external

def create_app():
    """Create flask app

    Returns:
        Flask: Flask application
    """
    # Create instance of app
    app = Flask(__name__)

    app.secret_key = Config.SECRET_KEY
    app.debug = Config.DEBUG

    # Register Blueprints
    app.register_blueprint(external)
    app.register_blueprint(internal)

    return app
