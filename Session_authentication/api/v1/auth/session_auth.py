#!/usr/bin/env python3
"""
class BasicAuth that inherits from Auth
"""


from api.v1.auth.auth import Auth
from models.user import User
from uuid import uuid4


class SessionAuth(Auth):
    """ Basic Authentication class """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ create a session method """
        if user_id is None:
            return None

        if type(user_id) is not str:
            return None

        session_id = str(uuid4())

        SessionAuth.user_id_by_session_id[session_id] = user_id

        return session_id


    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ user_id for session id method """
        if session_id is None:
            return None

        if type(session_id) is not str:
            return None

        return SessionAuth.user_id_by_session_id.get(session_id)
