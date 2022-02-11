# pylint: disable=redefined-outer-name,missing-module-docstring,missing-function-docstring,unused-variable,implicit-str-concat

import pytest
from expects import be_a, be_empty, expect
from testcontainers.mongodb import MongoDbContainer
from domain.model.coffee_information import CoffeeInformation
from domain.repository.coffee_information_repository import CoffeeInformationRepository
from exception.no_data_exception import NoDataException


DATABASE = "coffee"
COLLECTION = "coffee_information"


def describe_get_coffee_information():
    def test_should_return_coffee_information(database_mock, coffee_drinks):
        with MongoDbContainer() as mongodb:
            mongo_client = mongodb.get_connection_client()
            mongo_client[DATABASE][COLLECTION].insert_many(coffee_drinks)
            database_mock.client = mongo_client
            coffee_information_repository = CoffeeInformationRepository(database_mock)

            result = coffee_information_repository.get_coffee_information()

            expect(result).to(be_a(CoffeeInformation))
            expect(result.coffee_drinks).not_to(be_empty)

    def test_should_raise_no_data_exception_when_coffee_information_has_no_data(
        database_mock,
    ):
        with MongoDbContainer() as mongodb:
            database_mock.client = mongodb.get_connection_client()
            coffee_information_repository = CoffeeInformationRepository(database_mock)

            with pytest.raises(Exception) as exception:
                coffee_information_repository.get_coffee_information()

            expect(exception.value).to(be_a(NoDataException))


@pytest.fixture
def database_mock(mocker):
    return mocker.Mock(client=None)


@pytest.fixture
def coffee_drinks():
    return [
        {
            "_id": "209f4328-001c-48ff-925a-bc4319443340",
            "title": "Black",
            "description": "Coffee served as a beverage without cream or milk.",
            "ingredients": ["Coffee"],
        },
        {
            "_id": "17575fe7-034c-4f5a-97c9-9ee8fc762c9a",
            "title": "Latte",
            "description": "A coffee drink of Italian origin made with espresso and steamed milk.",
            "ingredients": ["Espresso", "Steamed Milk", "Foamed Milk"],
        },
        {
            "_id": "01d8ddd3-f437-4313-991d-7d8bea95aee1",
            "title": "Cappuccino",
            "description": (
                "An espresso-based coffee drink that originated in Austria with later development "
                "taking place in Italy, and is prepared with steamed milk foam."
            ),
            "ingredients": ["Espresso", "Steamed Milk"],
        },
    ]
