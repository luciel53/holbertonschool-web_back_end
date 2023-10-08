#!/usr/bin/env python3
"""
class BasicAuth that inherits from Auth
"""


from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
from base64 import b64decode
from models.user import User


class SessionAuth(Auth):
    """ Basic Authentication class """
    pass
