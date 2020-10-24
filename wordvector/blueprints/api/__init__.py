from flask import Blueprint
from . import home

api_blueprint = Blueprint('api', __name__)

home.add_rules(api_blueprint)


