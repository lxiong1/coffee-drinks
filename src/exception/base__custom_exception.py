"""Generic base exception"""

from dataclasses import dataclass


@dataclass
class BaseCustomException(Exception):
    """Base model for exceptions"""

    def __init__(self, status_code, message):
        super().__init__(message)
        self.status_code = status_code
        self.message = message

    status_code: int
    message: str
