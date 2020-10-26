from flask import Blueprint
from . import home, vocabulary, historic

api_blueprint = Blueprint('api', __name__)

home.register_route(api_blueprint)
vocabulary.register_route(api_blueprint)
historic.register_route(api_blueprint)


