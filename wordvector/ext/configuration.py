from flask import Flask
from wordvector.ext import handlers, cors


def init_app(app: Flask) -> Flask:
    """
    Adiciona as configurações
    """
    handlers.init_app(app)
    cors.init_app(app)
    return app
