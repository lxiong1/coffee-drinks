# pylint: disable=redefined-outer-name,missing-module-docstring,missing-function-docstring,unused-variable,implicit-str-concat

import pytest
from expects import be_a, equal, expect, have_property
from domain.model.coffee_drink import CoffeeDrink
from domain.model.coffee_information import CoffeeInformation
from service.coffee_information_service import CoffeeInformationService
from exception.invalid_uuid_exception import InvalidUUIDException
from exception.not_found_exception import NotFoundException
from utility.validator import Validator


def describe_get_all_information():
    def test_should_return_coffee_information(
        coffee_information_repository_mock, coffee_information
    ):
        coffee_information_repository_mock.get_coffee_information.return_value = (
            coffee_information
        )
        coffee_information_service = CoffeeInformationService(
            coffee_information_repository_mock
        )

        result = coffee_information_service.get_all_information()

        expect(result).to(be_a(type(coffee_information)))
        expect(result).to(equal(coffee_information))


def describe_get_information_by_id():
    @pytest.mark.parametrize(
        "coffee_drink_id",
        [
            "209f4328-001c-48ff-925a-bc4319443340",
            "17575fe7-034c-4f5a-97c9-9ee8fc762c9a",
            "01d8ddd3-f437-4313-991d-7d8bea95aee1",
        ],
    )
    def test_should_return_coffee_drink(
        coffee_information_repository_mock, coffee_information, coffee_drink_id
    ):
        coffee_information_repository_mock.get_coffee_information.return_value = (
            coffee_information
        )
        coffee_information_service = CoffeeInformationService(
            coffee_information_repository_mock
        )

        result = coffee_information_service.get_drink_by_id(coffee_drink_id)

        coffee_drink = __get_drink_by_value(coffee_information, coffee_drink_id)
        expect(result).to(be_a(type(coffee_drink)))
        expect(result).to(equal(coffee_drink))

    def test_should_raise_invalid_uuid_exception_when_uuid_not_version_4(
        mocker, coffee_information_repository_mock, coffee_information
    ):
        mocker.patch.object(Validator, "validate_uuid4", return_value=False)
        coffee_information_repository_mock.get_coffee_information.return_value = (
            coffee_information
        )
        coffee_information_service = CoffeeInformationService(
            coffee_information_repository_mock
        )

        with pytest.raises(Exception) as exception:
            invalid_uuid = "b997a730-51f6-11ec-bf63-0242ac130002"
            coffee_information_service.get_drink_by_id(invalid_uuid)

        expect(exception.value).to(be_a(InvalidUUIDException))

    def test_should_raise_not_found_exception_when_coffee_drink_not_found_by_id(
        mocker, coffee_information_repository_mock, coffee_information
    ):
        mocker.patch.object(
            CoffeeInformationService,
            "_CoffeeInformationService__get_drink_by_value",
            return_value=None,
        )
        coffee_information_repository_mock.get_coffee_information.return_value = (
            coffee_information
        )
        coffee_information_service = CoffeeInformationService(
            coffee_information_repository_mock
        )

        with pytest.raises(Exception) as exception:
            non_existing_uuid = "5000929d-8835-47a1-8e0c-cbe2146c0208"
            coffee_information_service.get_drink_by_id(non_existing_uuid)

        expect(exception.value).to(be_a(NotFoundException))


def describe_get_drink_by_title():
    @pytest.mark.parametrize(
        "coffee_drink_title",
        [
            "black",
            "Black",
            "BLACK",
            "latte",
            "Latte",
            "LATTE",
            "cappuccino",
            "Cappuccino",
            "CAPPUCCINO",
        ],
    )
    def test_should_return_coffee_drink(
        coffee_information_repository_mock, coffee_information, coffee_drink_title
    ):
        coffee_information_repository_mock.get_coffee_information.return_value = (
            coffee_information
        )
        coffee_information_service = CoffeeInformationService(
            coffee_information_repository_mock
        )

        result = coffee_information_service.get_drink_by_title(coffee_drink_title)

        expect(result).to(have_property("title", coffee_drink_title.title()))

    @pytest.mark.parametrize(
        "non_existing_title",
        ["", " ", "123", "$@!" "foo", "Foo", "FOO", "foo bar"],
    )
    def test_should_raise_not_found_exception_when_coffee_drink_not_found_by_title(
        mocker,
        coffee_information_repository_mock,
        coffee_information,
        non_existing_title,
    ):
        mocker.patch.object(
            CoffeeInformationService,
            "_CoffeeInformationService__get_drink_by_value",
            return_value=None,
        )
        coffee_information_repository_mock.get_coffee_information.return_value = (
            coffee_information
        )
        coffee_information_service = CoffeeInformationService(
            coffee_information_repository_mock
        )

        with pytest.raises(Exception) as exception:
            coffee_information_service.get_drink_by_title(non_existing_title)

        expect(exception.value).to(be_a(NotFoundException))


@pytest.fixture
def coffee_information_repository_mock(mocker):
    return mocker.Mock()


@pytest.fixture
def coffee_information():
    return CoffeeInformation(
        [
            CoffeeDrink(
                id="209f4328-001c-48ff-925a-bc4319443340",
                title="Black",
                description="Coffee served as a beverage without cream or milk.",
                ingredients=["Coffee"],
            ),
            CoffeeDrink(
                id="17575fe7-034c-4f5a-97c9-9ee8fc762c9a",
                title="Latte",
                description="A coffee drink of Italian origin made with espresso and steamed milk.",
                ingredients=["Espresso", "Steamed Milk", "Foamed Milk"],
            ),
            CoffeeDrink(
                id="01d8ddd3-f437-4313-991d-7d8bea95aee1",
                title="Cappuccino",
                description=(
                    "An espresso-based coffee drink that originated in Austria with later "
                    "development taking place in Italy, and is prepared with steamed milk foam."
                ),
                ingredients=["Espresso", "Steamed Milk"],
            ),
        ]
    )


def __get_drink_by_value(coffee_information, value):
    normalized_value = value.casefold().strip()

    for coffee_drink in coffee_information.coffee_drinks:
        if coffee_drink.id.casefold().strip() == normalized_value:
            return coffee_drink

        if coffee_drink.title.casefold().strip() == normalized_value:
            return coffee_drink

    return None
