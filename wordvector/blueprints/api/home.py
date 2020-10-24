from flask import Blueprint


def home():
    return {'message': 'Hello! Im word vector Api!'}


def add_rules(blueprint: Blueprint):
    blueprint.add_url_rule('/', view_func=home)
