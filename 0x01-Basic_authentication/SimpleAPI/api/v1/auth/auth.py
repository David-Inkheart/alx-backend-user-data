#!/usr/bin/env python3
""" Module of Index Auth class to manage the API authentication
"""

from flask import request
from typing import List, TypeVar


class Auth():
    """ Auth class for API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require_auth that returns False """
        if excluded_paths is None or len(excluded_paths) == 0 or path is None:
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ authorization_header that returns None
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ current_user
        """
        return None
