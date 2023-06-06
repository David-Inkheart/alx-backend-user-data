#!/usr/bin/env python3
"""Auth Module
"""

import bcrypt


def _hash_password(password: str) -> str:
    """Hash a password and return the salted hash
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
