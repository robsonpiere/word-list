from pymongo import MongoClient
from pymongo.database import Database, Collection
from pymongo.errors import ConnectionFailure
from os import environ
from datetime import datetime

MONGO_STRING_CONNECTION = environ.get('MONGO_STRING_CONNECTION', None)


def connect():
    if MONGO_STRING_CONNECTION:
        try:
            client = MongoClient(host=MONGO_STRING_CONNECTION, retryWrites=False)
            return client['lista-de-palavras']
        except ConnectionFailure:
            print("Database Server not available")
    return None


def save(database: Database, document: dict):
    document['createdAt'] = datetime.utcnow()
    historic: Collection = database.requisicoes
    return historic.insert_one(document)


def get_vocabulary_historic(database: Database):
    historic: Collection = database.requisicoes
    return list(historic.find({}))

