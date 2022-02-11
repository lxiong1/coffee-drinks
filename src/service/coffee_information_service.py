"""Business logic for retrieving coffee information"""

from uuid import UUID
from domain.model.coffee_drink import CoffeeDrink
from domain.model.coffee_information import CoffeeInformation
from exception.invalid_uuid_exception import InvalidUUIDException
from exception.not_found_exception import NotFoundException
from utility.validator import Validator


class CoffeeInformationService:
    """Service for retrieving coffee information based on context of request"""

    def __init__(self, coffee_information_repository):
        self._coffee_information_repository = coffee_information_repository
        self._coffee_information = (
            self._coffee_information_repository.get_coffee_information()
        )

    def get_all_information(self) -> CoffeeInformation:
        """Returns all coffee drink information

        Returns:
            CoffeeInformation: Object that contains information of all coffee drinks
        """
        return self._coffee_information

    def get_drink_by_id(self, coffee_drink_id: UUID) -> CoffeeDrink:
        """Returns information about a coffee drink when found by given id

        Args:
            coffee_drink_id (UUID): Unique identifier for a coffee drink

        Raises:
            InvalidUUIDException: Raises exception when given UUID is not version 4
            NotFoundException: Raises exception when coffee drink not found by given id

        Returns:
            CoffeeDrink: Object that contains information about a coffee drink based on given id
        """
        coffee_drink_id_string = str(coffee_drink_id)
        if not Validator.validate_uuid4(coffee_drink_id_string):
            raise InvalidUUIDException(message="UUID given must be version 4")

        coffee_drink = self.__get_drink_by_value(coffee_drink_id_string)
        if not coffee_drink:
            raise NotFoundException(
                message=(
                    "Coffee drink information was not found"
                    f" by given uuid: {coffee_drink_id_string}"
                )
            )

        return coffee_drink

    def get_drink_by_title(self, coffee_title: str) -> CoffeeDrink:
        """Returns information about a coffee drink when found by given title

        Args:
            coffee_title (str): Name of a coffee drink

        Raises:
            NotFoundException: Raises exception when coffee drink not found by given id

        Returns:
            CoffeeDrink: Object that contains information about a coffee drink based on given title
        """
        coffee_drink = self.__get_drink_by_value(coffee_title)
        if not coffee_drink:
            raise NotFoundException(
                message=(
                    "Coffee drink information was not found"
                    f" by given title: {coffee_title}"
                )
            )

        return coffee_drink

    def __get_drink_by_value(self, value: str):
        normalized_value = value.casefold()

        for coffee_drink in self._coffee_information.coffee_drinks:
            if coffee_drink.id.casefold() == normalized_value:
                return coffee_drink

            if coffee_drink.title.casefold() == normalized_value:
                return coffee_drink

        return None  # pragma: no cover
