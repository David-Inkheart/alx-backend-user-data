#!/usr/bin/env python3
""" Inherits from SessionExpAuth class to manage the API authentication
"""

from api.v1.auth.session_exp_auth import SessionExpAuth
from datetime import datetime, timedelta
import os


class SessionDBAuth(SessionExpAuth):
    """ SessionDBAuth class for session authentication with expiration
    """

    def create_session(self, user_id: str = None) -> str:
        """ Create a Session ID for a user_id
        """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None

        session_dict = {
            "user_id": user_id,
            "created_at": datetime.now()
        }

        self.user_id_by_session_id[session_id] = session_dict

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Return a User ID based on a Session ID
        """
        if session_id is None:
            return None
        session_dict = self.user_id_by_session_id.get(session_id)
        if session_dict is None:
            return None
        if self.session_duration <= 0:
            return session_dict.get("user_id")
        created_at = session_dict.get("created_at")
        if created_at is None:
            return None
        expiration_time = created_at + timedelta(seconds=self.session_duration
                                                 )
        if expiration_time < datetime.now():
            return None
        return session_dict.get("user_id")

    def destroy_session(self, request=None):
        """ Destroy the User Session based on the Session ID
        """
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        if not self.user_id_for_session_id(session_id):
            return False
        del self.user_id_by_session_id[session_id]
        return True
