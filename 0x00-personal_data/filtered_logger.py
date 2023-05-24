#!/usr/bin/env python3
"""personal data filter and logging module"""
import re
from typing import List


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
