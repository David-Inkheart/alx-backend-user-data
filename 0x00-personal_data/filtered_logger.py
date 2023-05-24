#!/usr/bin/env python3
"""personal data filter and logging module"""
import re
from typing import List
import logging


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
