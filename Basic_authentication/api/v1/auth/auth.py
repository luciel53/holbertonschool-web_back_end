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
        if path is None:
            return (True)

        if excluded_paths is None or len(excluded_paths) == 0:
            return (True)

        if excluded_paths[-1] != '/':
            excluded_paths += '/'

        if path[-1] != '/':
            path += '/'

        if path in excluded_paths:
            return (False)

        return (True)

    def authorization_header(self, request=None) -> str:
        """ authorization header function """
        if request is None:
            return (None)

        header_key = request.headers.get('Authorization', None)

        return header_key

    def current_user(self, request=None) -> TypeVar('User'):
        """ current user function """
        return (None)
