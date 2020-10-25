from flask import Flask
from .api import api_blueprint


def init_blueprints(app: Flask):
    app.register_blueprint(api_blueprint)
