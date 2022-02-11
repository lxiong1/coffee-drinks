"""Generic exception for when UUID does not conform to a UUID context-based standard"""

from dataclasses import dataclass
from http import HTTPStatus
from exception.base__custom_exception import BaseCustomException


@dataclass
class InvalidUUIDException(BaseCustomException):
    """Model for exceptions pertaining to invalid UUIDs"""

    def __init__(
        self, status_code=HTTPStatus.BAD_REQUEST, message="UUID given is not valid"
    ):
        super().__init__(status_code, message)
