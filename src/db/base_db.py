from abc import ABC, abstractmethod


class BaseDB(ABC):
    '''Base class to work with DB.'''

    @abstractmethod
    def save_secret():
        pass

    @abstractmethod
    def get_secret(key: str):
        pass
