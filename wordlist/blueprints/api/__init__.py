from flask import Blueprint
from . import home, vocabulary

api_blueprint = Blueprint('api', __name__)

home.add_rules(api_blueprint)
vocabulary.add_rules(api_blueprint)


