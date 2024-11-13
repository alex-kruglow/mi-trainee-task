'''common.passwd module to work with passwords.'''

from werkzeug.security import generate_password_hash, check_password_hash


def get_hashed_password(plain_text_password: str) -> str:
    '''Hash a password for the first time.
    Using bcrypt, the salt is saved into the hash itself.

    Args:
        plain_text_password (str): password string.

    Returns:
        str: Hashed password.
    '''
    return generate_password_hash(plain_text_password, method='sha256')


def check_password(plain_text_password: str, hashed_password: str):
    '''Check hashed password.
    Using bcrypt, the salt is saved into the hash itself.

    Args:
        plain_text_password (str): password string.
        hashed_password (str): hashed password string.

    Returns:
        bool: Return True if the password is right.
    '''
    return check_password_hash(hashed_password, plain_text_password)
