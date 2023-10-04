#!/usr/bin/env python3
"""
User passwords should NEVER be stored in plain text in a database.

Implement a hash_password function that expects one string argument name
password and returns a salted, hashed password, which is a byte string.

Use the bcrypt package to perform the hashing (with hashpw).
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """ hash password function """
    password_encoded = password.encode()
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_encoded, salt)
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ is_valid function """
    password_encoded = password.encode()
    if bcrypt.checkpw(password_encoded, hashed_password):
        return True
    else:
        return False
