#!/usr/bin/env python3
"""
class BasicAuth that inherits from Auth
"""


from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """ Basic Authentication class """
    pass

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """ Extract base64 authorization header method """
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith('Basic '):
            return None

        return authorization_header[6:]
