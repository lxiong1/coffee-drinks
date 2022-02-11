"""Generic exception for when expected data from database does not exist"""

from dataclasses import dataclass
from http import HTTPStatus
from exception.base__custom_exception import BaseCustomException


@dataclass
class NoDataException(BaseCustomException):
    """Model for exceptions pertaining to non-existent data from database"""

    def __init__(
        self,
        status_code=HTTPStatus.BAD_GATEWAY,
        message="Requested data from database does not exist",
    ):
        super().__init__(status_code, message)
