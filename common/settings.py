import pathlib

import environ
from pydantic import BaseSettings

import os


BASE_DIR = pathlib.Path(__file__).parent.parent


env = environ.Env()
env.__class__.read_env(BASE_DIR / '.env')


class ProjectSettings(BaseSettings):
    BASE_DIR: str = str(BASE_DIR)
    mongo_host: str = env('MONGO_HOST')
    mongo_port: int = env('MONGO_PORT', int)
    mongo_users_db: str = env('MONGO_USERS_DB', default='users-db')
    mongo_users_collection: str = env('MONGO_USERS_COLLECTION', default='users')


settings = ProjectSettings()
