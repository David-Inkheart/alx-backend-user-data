#!/usr/bin/env python3
""" Inherits from Auth class to manage the API authentication
"""

from api.v1.auth.auth import Auth
from base64 import b64decode


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
