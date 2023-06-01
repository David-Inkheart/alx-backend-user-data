#!/usr/bin/env python3
""" UserSession module for SessionDBAuth
"""
from models.base import Base


class UserSession(Base):
    """ UserSession class for SessionDBAuth
    """

    def __init__(self, *args: list, **kwargs: dict):
        """ Initialize a UserSession instance
        """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
