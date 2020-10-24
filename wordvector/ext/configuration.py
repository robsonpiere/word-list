from flask import Flask
from wordvector.ext import handlers

def init_app(app: Flask) -> Flask:
    """
    Adiciona as configurações
    """
    handlers.init_app(app)
    return app