#!/usr/bin/env python3
"""
class BasicAuth that inherits from Auth
"""


from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
from base64 import b64decode
from models.user import User


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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ decode_base64_authorization_header method """
        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decode = b64decode(base64_authorization_header).decode('utf-8')
            return decode
        except(ValueError, TypeError):
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """ extract_user_credentials method """
        if decoded_base64_authorization_header is None:
            return None, None

        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        split_code = decoded_base64_authorization_header.split(':')
        return (split_code[0], split_code[1])

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """ user_object_from_credentials method """
        if not isinstance(user_email, str) or user_email is None:
            return None

        if not isinstance(user_pwd, str) or user_pwd is None:
            return None

        # Search for User instance on email
        user = User.search({"email": user_email})

        if not user:
            return None

        # function is_valid_password in user.py
        if not user[0].is_valid_password(user_pwd):
            return None

        return user[0]
