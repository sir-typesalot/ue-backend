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
    DEBUG = os.environ.get('WEBAPP_SECRET')
    SECRET_KEY = os.environ.get('WEBAPP_SECRET')
    VERSION = "0.1.0"

    # Database configuration
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SCHEMA = 'urban_eden'

    # Session configuration
    SESSION_TYPE = 'filesystem'
    SESSION_PERMANENT = False

    # Security configuration
    WTF_CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = 'your_wtf_csrf_secret_key'

    # Mail configuration
    MAIL_SERVER = 'smtp.example.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'your_email@example.com'
    MAIL_PASSWORD = 'your_email_password'

    # Uploads configuration
    UPLOAD_FOLDER = 'uploads'
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
