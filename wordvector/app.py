from flask import Flask
from wordvector.ext import configuration

def basic_app() -> Flask:
    """
    Cria um app básico
    """
    app = Flask(__name__)
    return app

def create_app() -> Flask:
    app = basic_app()
    configuration.init_app(app)
    return app
