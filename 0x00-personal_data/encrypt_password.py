#!/usr/bin/env python3
"""
Using the bcrypt package to encrypts a password
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """returns a salted, hashed password, which is a byte string"""
    hashed_pass = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed_pass


def is_valid(hashed_password: bytes, password: str) -> bool:
    """validates that the provided password matches the hashed
    password"""
    if bcrypt.checkpw(password.encode(), hashed_password):
        return True
    else:
        return False
