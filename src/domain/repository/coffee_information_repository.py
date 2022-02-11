"""Middleman between database and data needed for services"""

from domain.model.coffee_drink import CoffeeDrink
from domain.model.coffee_information import CoffeeInformation
from exception.no_data_exception import NoDataException


class CoffeeInformationRepository:
    """Accesses database for information about coffee drinks"""

    ID = "_id"
    TITLE = "title"
    DESCRIPTION = "description"
    INGREDIENTS = "ingredients"
    DATABASE = "coffee"
    COLLECTION = "coffee_information"

    def __init__(self, database):
        self._database_client = database.client

    def get_coffee_information(self) -> CoffeeInformation:
        """Returns all information about coffee drinks available in the database

        Returns:
            CoffeeInformation: Object that contains information of all coffee drinks
        """
        database = self._database_client[self.DATABASE]
        collection = database[self.COLLECTION]

        coffee_drinks = [
            CoffeeDrink(
                id=coffee_drink[self.ID],
                title=coffee_drink[self.TITLE],
                description=coffee_drink[self.DESCRIPTION],
                ingredients=coffee_drink[self.INGREDIENTS],
            )
            for coffee_drink in collection.find()
        ]

        if not coffee_drinks:
            raise NoDataException(
                (
                    f"Collection '{self.COLLECTION}' requested from database '{self.DATABASE}'"
                    "does not contain expected data"
                )
            )

        return CoffeeInformation(coffee_drinks=coffee_drinks)
