"""Run the flask application
"""
import logging
from datetime import datetime
from flask import request
from waitress import serve
from app import create_app

app = create_app()

# Set up app logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('werkzeug')
logger.setLevel(logging.INFO)

# Log information about each request after it is processed
@app.after_request
def log_request(response):
    """Log traffic of requests to the application
    For local server, this will result in duplicate logging.
    The purpose of this is to record logs in LIVE since the prod server
    does not have default logging
    """
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logger.info(
        "[%s] - %s %s %s", timestamp, request.method, request.path, response.status_code)
    return response

if __name__ == '__main__':
    if app.debug:
        # Use Flask's development server with auto-reloading
        app.run(debug=True, use_reloader=True, host='0.0.0.0', port=5000)
    else:
        # Use Waitress for production
        serve(app, host='0.0.0.0', port=5000)
