from wordlist.database.mongo import connect, get_vocabulary_historic
from flask import Blueprint
from bson import json_util
from json import loads


def historic():
    database = connect()
    result = get_vocabulary_historic(database)
    return {
        'historico': serialize(result)
    }


def serialize(data):
    data = json_util.dumps(data)
    return loads(data)


def register_route(blueprint: Blueprint):
    blueprint.add_url_rule('/historico', view_func=historic)
