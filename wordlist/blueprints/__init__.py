from flask import Flask
from .api import api_blueprint
from .docs import SWAGGER_URL, SWAGGERUI_BLUEPRINT

def init_blueprints(app: Flask):
    app.register_blueprint(api_blueprint)
    app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
