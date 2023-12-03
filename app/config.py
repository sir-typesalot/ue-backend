"""Configuration class for the application
"""
import os
from dotenv import load_dotenv

load_dotenv()

# pylint: disable=too-few-public-methods
class Config:
    """Static class that holds config settings for the app
    """
    # Flask app configuration
    DEBUG = os.environ.get('DEBUG')
    SECRET_KEY = os.environ.get('WEBAPP_SECRET')
    VERSION = "0.1.0"

    # Database configuration
    DB_HOST = os.environ.get('DB_HOST')
    DB_USER = os.environ.get('DB_USER')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')
    SCHEMA = 'urban_eden'

    # Uploads configuration
    UPLOAD_SERVER = 'uploads'
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg'}
