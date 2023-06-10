from dependency_injector.containers import DeclarativeContainer, WiringConfiguration
from dependency_injector.providers import Factory
import pymongo

from common.settings import settings
from repositories.users.mongo import UsersMongoRepository


class UserContainer(DeclarativeContainer):
    wiring_config: WiringConfiguration = WiringConfiguration(
        modules=['api.handlers.users'],
    )
    mongo_client: pymongo.MongoClient = Factory(
        pymongo.MongoClient,
        host=settings.mongo_host,
        port=settings.mongo_port,
    )
    user_repository: UsersMongoRepository = Factory(
        UsersMongoRepository,
        client=mongo_client,
        db_name=settings.mongo_users_db,
        collection_name=settings.mongo_users_collection,
    )
