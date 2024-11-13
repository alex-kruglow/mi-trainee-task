'''Secrets service module.'''

from db.base_db import BaseDB


class SecretsService():
    '''Service to work with secrets.'''

    def __init__(self, db: BaseDB) -> None:
        self.db: BaseDB = db


def get_secrets_service(db: BaseDB) -> SecretsService:
    service = SecretsService()
    return service
