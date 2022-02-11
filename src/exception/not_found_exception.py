"""Generic exception for when an item can't be found"""

from dataclasses import dataclass
from http import HTTPStatus
from exception.base__custom_exception import BaseCustomException


@dataclass
class NotFoundException(BaseCustomException):
    """Model for exceptions pertaining to an item not found"""

    def __init__(self, status_code=HTTPStatus.NOT_FOUND, message="Item not found"):
        super().__init__(status_code, message)
