#!/usr/bin/env python3
"""
Main file
"""


import bcrypt


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
