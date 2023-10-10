#!/usr/bin/env python3
"""
Auth file
"""


import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4


def _hash_password(password: str) -> bytes:
    """
    method that takes in a password string arguments and returns bytes.

    The returned bytes is a salted hash of the input password,
    hashed with bcrypt.hashpw
    """
    # password to encode in bytes
    password_encoded = password.encode()

    # generates random salt
    salt = bcrypt.gensalt()

    # hash the password with salt
    hashed_password = bcrypt.hashpw(password_encoded, salt)

    return hashed_password


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ method to register a user """
        try:
            # try to find user by email
            user = self._db.find_user_by(email=email)

        except NoResultFound:
            # if none user is found, create add the user
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)
            return user
        else:
            # if user is already registered, raise value error
            raise ValueError("User {} already exists.".format(email))

    def valid_login(self, email: str, password:str) -> bool:
        """ valid login method """
        try:
            # try to locate user by email
            user = self._db.find_user_by(email=email)

            if user is not None:
                # if user exists check password, convert password to bytes
                hashed_password = password.encode('utf-8')

                # check password with bcrypt
                pwd = bcrypt.checkpw(hashed_password, user.hashed_password)

                return pwd

        except Exception:
            return False
