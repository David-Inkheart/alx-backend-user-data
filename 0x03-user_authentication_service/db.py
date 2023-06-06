#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Save the user to the database and return a User object
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """Return the users object filtered by input kwargs
        as filtered by the method’s input arguments
        """
        if not kwargs:
            raise InvalidRequestError
        # first row returned by query, or None if no row present.
        user_obj = self._session.query(User).filter_by(**kwargs).first()
        if user_obj is None:
            raise NoResultFound
        return user_obj

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update the user’s attributes as passed in the method’s arguments
        then commit changes to the database
        """
        user_obj = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            if key not in user_obj.__dict__:
                raise ValueError
            user_obj.__setattr__(key, value)
        self._session.commit()
