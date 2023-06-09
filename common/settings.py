import pathlib

import environ
from pydantic import BaseSettings


BASE_DIR = pathlib.Path(__file__).parent


env = environ.Env()
env.__class__.read_env(BaseException / '.env')


class ProjectSettings(BaseSettings):
    BASE_DIR: str = BASE_DIR
    mongo_host: str = env('MONGO_HOST')
    mongo_port: int = env('MONGO_PORT', int) 


settings = ProjectSettings()
