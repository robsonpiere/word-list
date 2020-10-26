from flask import Blueprint


def home():
    return {
        'message': 'Olá eu sou a api de lista de palavras! veja a documentação em /docs'
    }


def register_route(blueprint: Blueprint):
    blueprint.add_url_rule('/', view_func=home)
