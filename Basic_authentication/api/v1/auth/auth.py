#!/usr/bin/env python3
"""
Route module for the API
"""


from flask import request
from typing import List, TypeVar


class Auth():
    """ Class Auth """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Require function """
        return (False)

    def authorization_header(self, request=None) -> str:
        """ authorization header function """
        if request is None:
            return (None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ current user function """
        if request is None:
            return (None)
