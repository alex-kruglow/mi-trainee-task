'''Config module.'''

from pydantic import BaseSettings


class Config(BaseSettings):
    title: str
    port: int
    mongodb_connect: str
    secret_key: str


config: Config = Config()


def get_config():
    return config
