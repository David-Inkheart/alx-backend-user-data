#!/usr/bin/env python3
""" Inherits from Auth class to manage the API authentication
"""

from api.v1.auth.auth import Auth
from base64 import b64decode
from models.user import User
from typing import TypeVar, Tuple


class BasicAuth(Auth):
    """ BasicAuth class for API authentication
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Returns the Base64 part of the Authorization header
        """
        if authorization_header is None or type(authorization_header)\
                is not str or authorization_header[:6] != 'Basic ':
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str)\
            -> str:
        """ Returns the decoded value of a Base64 string
        """
        if base64_authorization_header is None or\
                type(base64_authorization_header) is not str:
            return None
        try:
            return b64decode(base64_authorization_header).decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str)\
            -> Tuple[str, str]:
        """ Returns the user email and password from the Base64
        decoded value
        """
        if decoded_base64_authorization_header is None or\
                type(decoded_base64_authorization_header) is not str or\
                ':' not in decoded_base64_authorization_header:
            return (None, None)
        return tuple(decoded_base64_authorization_header.split(':', 1))

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """ Returns the User instance based on his email and password
        """
        if user_email is None or type(user_email) is not str or\
                user_pwd is None or type(user_pwd) is not str:
            return None
        try:
            users = User.search({'email': user_email})
        except Exception:
            return None
        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None
