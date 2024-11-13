'''MongoDB module.'''

from datetime import datetime

from motor.motor_asyncio import AsyncIOMotorClient
from motor.motor_asyncio import AsyncIOMotorCollection

from uuid import uuid4

from common.passwd import get_hashed_password
from db.base_db import BaseDB
from models.secrets import Secret, SecretFromUser


class CannotWriteInDB(Exception):
    '''Raised when a record cannot be added in a DB.'''
    print('Something was wrong. The record was not added in the DB.')


class MongoDB(BaseDB):
    '''MongoDB class to work with DB.'''

    def __init__(
        self,
        motor_db_connect_url: str,
        db_name: str,
        collection_name: str
    ) -> None:
        '''Init MongoDB class.

        Args:
            motor_db_connect_url (str): string to connect to MongoDB.
            db_name (str): name of db in MongoDB.
            collection_name (str): collection name in MongoDB DB.

        Return None.
        '''
        self.motor_db_connect_url: str = motor_db_connect_url
        self.db_name: str = db_name
        self.collection_name: str = collection_name
        self.mongo_db: AsyncIOMotorClient = AsyncIOMotorClient(
            self.motor_db_connect_url
        )[self.db_name]
        self.collection: AsyncIOMotorCollection = self.mongo_db[
            self.collection_name
        ]

    async def get_secret(self, key: str) -> Secret | None:
        '''Return Secret object of None.

        Args:
            key (str): string to find a secret.

        Returns:
            Secret | None. Return Secret object if there is one in DB or None.
        '''
        result = await self.collection.find_one({'key': key})
        now: datetime = datetime.now()
        if result and now < datetime(result['expiration_datetime']):
            return Secret(
                key=result['key'],
                secret=result['secret'],
                password=result['password']
            )

    async def _get_uuid(self):
        '''Return key. It has to be free in the DB.'''
        while True:
            key: str = str(uuid4())[:8]
            if not await self.collection.find_one({'key': key}):
                return key

    async def save_secret(self, secret: SecretFromUser) -> Secret:
        '''Save a secret in the DB.

        Args:
            secret (SecretFromUser): data from user.

        Returns:
            Secret: Saved secret in the DB.
        '''
        s = Secret(
            key=self._get_uuid,
            secret=secret.secret,
            password=get_hashed_password(secret['password'])
        )
        inserted = await self.collection.insert_one(s)
        if inserted:
            return s
        else:
            raise CannotWriteInDB
