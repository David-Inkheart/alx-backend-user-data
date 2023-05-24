#!/usr/bin/env python3
"""personal data filter and logging module"""
import re
from typing import List, Union, Tuple, Any
import logging
import os
import mysql.connector
from mysql.connector.connection import MySQLConnection


PII_FIELDS = ("name", "email", "phone", "ssn", "password")

# def filter_datum(fields: List[str], redaction: str,
#                  message: str, separator: str) -> str:
#     """obfuscates a log message with redaction"""
#     for input in fields:
#         message = re.sub(rf"{input}=.*?{separator}",
#                          f"{input}={redaction}{separator}", message)
#     return message


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ obfuscates a log message with redaction """
    pattern = rf"({'|'.join(fields)})=.*?{separator}"
    return re.sub(pattern, rf"\1={redaction}{separator}", message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class"""
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """constructor that initializes class"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """uses filter_datum to filter values in incoming records"""
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def get_logger() -> logging.Logger:
    """returns a logging.Logger object"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    strm_hndlr = logging.StreamHandler()
    formatter = RedactingFormatter(list(PII_FIELDS))
    strm_hndlr.setFormatter(formatter)
    logger.addHandler(strm_hndlr)
    return logger


def get_db() -> Union[MySQLConnection, Any]:
    """returns a connector object to the database"""
    user = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME")
    db_connector = mysql.connector.connect(
        user=user,
        password=password,
        host=host,
        database=db_name
    )
    return db_connector
