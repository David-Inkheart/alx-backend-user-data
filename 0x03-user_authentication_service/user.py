#!/usr/bin/env python3
"""
SQLAlchemy model named User for a database table named users
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create declarative base
Base = declarative_base()


class User(Base):
    """
    User class
    """
    __tablename__ = 'users'

    # Create id column
    id = Column(Integer, primary_key=True)

    # Create email column
    email = Column(String(250), nullable=False)

    # hashed_password column
    hashed_password = Column(String(250), nullable=False)

    # session_id column
    session_id = Column(String(250), nullable=True)

    # reset_token column
    reset_token = Column(String(250), nullable=True)
