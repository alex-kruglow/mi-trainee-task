'''Secrets API router.'''

from fastapi import APIRouter

secrets_router: APIRouter = APIRouter(prefix='/')


@secrets_router.get('/secrets/{secret_key}')
def get_secrets(secret_key: str):
    '''Return saved secret.

    Params:
        secret_key (str): secret key to return the secret.
    '''
    pass


@secrets_router.post('/')
def set_secret(secret_key: str, password: str = '', expired_min: int = 60*24):
    '''Save secret.

    Params:
        secret (str): secret string.
        password (str): password for the secret. Default is empty pass.
        expired (int): expired time. Default is 1 day 60 * 24 min.
    '''
    pass
