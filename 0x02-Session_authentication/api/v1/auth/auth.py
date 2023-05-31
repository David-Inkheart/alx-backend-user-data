#!/usr/bin/env python3
""" Module of Index Auth class to manage the API authentication
"""

from flask import request
from typing import List, TypeVar
import os


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
        for excluded_path in excluded_paths:
            if excluded_path[-1] == '*':
                if path.startswith(excluded_path[:-1]):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """ authorization_header that returns None
        """
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """ current_user
        """
        return None

    def session_cookie(self, request=None):
        """ session_cookie: returns a cookie value from a request
        """
        if request is None:
            return None
        return request.cookies.get(os.getenv('SESSION_NAME'))
