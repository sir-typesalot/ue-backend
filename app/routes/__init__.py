import os
from flask import Flask

from .private import internal
from .public import external

webapp = Flask(__name__,)
webapp.secret_key = os.environ.get('WEBAPP_SECRET')
# Register Blueprints
webapp.register_blueprint(external)
webapp.register_blueprint(internal)
