#!/usr/bin/env python3
""" Inherits from SessionExpAuth class to manage the API authentication
"""

from api.v1.auth.session_exp_auth import SessionExpAuth
from datetime import datetime, timedelta
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """ SessionDBAuth class
    """

    def create_session(self, user_id=None):
        """ creates and stores new instance of UserSession and
        returns the Session ID
        """
        if user_id is None:
            return None
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        user_session = UserSession(user_id=user_id, session_id=session_id)
        user_session.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """ returns the User ID by requesting UserSession in
        the database based on session_id
        """
        if session_id is None:
            return None
        try:
            user_session = UserSession.search({'session_id': session_id})
        except Exception:
            return None
        if not user_session:
            return None
        if user_session[0].created_at + timedelta(
                seconds=self.session_duration) < datetime.now():
            return None
        return user_session[0].user_id

    def destroy_session(self, request=None):
        """ destroys the UserSession based on the Session ID
        from the request cookie
        """
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        try:
            user_session = UserSession.search({'session_id': session_id})
        except Exception:
            return False
        if not user_session:
            return False
        try:
            user_session[0].remove()
        except Exception:
            return False
        return True
