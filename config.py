import json
import os

from starlette.config import Config

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

env_location: list = __location__.split("/")
env_location.append(".env")
env_location: str = "/".join(env_location)

config = Config(env_location)

NODE_LIST = config("APP_NODES", cast=str, default=[])
NODE_LIST = NODE_LIST.split(',')

PORT = config("APP_PORT", cast=int)
