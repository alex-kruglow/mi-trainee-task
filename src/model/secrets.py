'''Secrets models module.'''

from pydantyc import BaseModel


class Secret(BaseModel):
    key: str
    secret: str
    password: str


class SecretFromUser(BaseModel):
    secret: str
    password: str
    expire_time_min: int
