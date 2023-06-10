import os
from pymongo import MongoClient
from common.settings import settings

import json


def fill_database():
    client = MongoClient(host=settings.mongo_host, port=settings.mongo_port)
    collection = client[settings.mongo_users_db][settings.mongo_users_collection]

    with open(os.path.join(settings.BASE_DIR, 'employees.json')) as file:
        objects = json.load(file)

    collection.insert_many(objects)


if __name__ == '__main__':
    fill_database()
