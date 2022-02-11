# pylint: disable=redefined-outer-name,missing-module-docstring,missing-function-docstring,unused-variable,implicit-str-concat,bare-except

from http import HTTPStatus
import pytest
import requests
from expects import be_empty, equal, expect, have_key, have_keys
from coffee_endpoint import BASE_URL, COFFEE_DRINKS, COFFEE_DRINKS_ENDPOINT

ID = "id"
TITLE = "title"
DESCRIPTION = "description"
INGREDIENTS = "ingredients"

STATUS_CODE = "status_code"
MESSAGE = "message"


def describe_get_coffee_drinks_information():
    def test_should_return_successful_response_with_coffee_information():
        result = requests.get(COFFEE_DRINKS_ENDPOINT)

        expect(result.status_code).to(equal(HTTPStatus.OK))

        coffee_information = result.json()
        expect(coffee_information).to(have_key(COFFEE_DRINKS))

        coffee_drinks = coffee_information[COFFEE_DRINKS]
        expect(coffee_drinks).not_to(be_empty)
        for coffee_drink in coffee_drinks:
            expect(coffee_drink).to(have_keys(ID, TITLE, DESCRIPTION, INGREDIENTS))


def describe_get_coffee_drink_information_by_id():
    def test_should_return_successful_response_with_coffee_drink_information():
        coffee_id = "209f4328-001c-48ff-925a-bc4319443340"

        result = requests.get(f"{COFFEE_DRINKS_ENDPOINT}/{coffee_id}")

        expect(result.status_code).to(equal(HTTPStatus.OK))

        coffee_drink_information = result.json()
        expect(coffee_drink_information).to(
            have_keys(ID, TITLE, DESCRIPTION, INGREDIENTS)
        )
        expect(coffee_drink_information[ID]).to(equal(coffee_id))

    def test_should_handle_and_return_invalid_uuid_exception_when_id_is_invalid():
        invalid_id = "706d78da-577a-11ec-bf63-0242ac130002"

        result = requests.get(f"{COFFEE_DRINKS_ENDPOINT}/{invalid_id}")

        expect(result.status_code).to(equal(HTTPStatus.OK))

        exception = result.json()
        expect(exception[STATUS_CODE]).to(equal(HTTPStatus.BAD_REQUEST))
        expect(exception[MESSAGE]).to(equal("UUID given must be version 4"))

    def test_should_handle_and_return_not_found_exception_when_id_does_not_exist():
        non_existent_id = "2baac55d-9873-4c2b-89f8-b39c8091d6c4"

        result = requests.get(f"{COFFEE_DRINKS_ENDPOINT}/{non_existent_id}")

        expect(result.status_code).to(equal(HTTPStatus.OK))

        exception = result.json()
        expect(exception[STATUS_CODE]).to(equal(HTTPStatus.NOT_FOUND))
        expect(exception[MESSAGE]).to(
            equal(
                (
                    "Coffee drink information was not found "
                    f"by given uuid: {non_existent_id}"
                )
            )
        )


def describe_get_coffee_drink_information_by_title():
    def test_should_return_successful_response_with_coffee_drink_information():
        coffee_title = "Black"

        result = requests.get(f"{COFFEE_DRINKS_ENDPOINT}/{coffee_title}")

        expect(result.status_code).to(equal(HTTPStatus.OK))

        coffee_drink_information = result.json()
        expect(coffee_drink_information).to(
            have_keys(ID, TITLE, DESCRIPTION, INGREDIENTS)
        )
        expect(coffee_drink_information[TITLE]).to(equal(coffee_title))

    def test_should_handle_and_return_not_found_exception_when_title_does_not_exist():
        non_existent_title = "foo"

        result = requests.get(f"{COFFEE_DRINKS_ENDPOINT}/{non_existent_title}")

        expect(result.status_code).to(equal(HTTPStatus.OK))

        exception = result.json()
        expect(exception[STATUS_CODE]).to(equal(HTTPStatus.NOT_FOUND))
        expect(exception[MESSAGE]).to(
            equal(
                (
                    "Coffee drink information was not found "
                    f"by given title: {non_existent_title}"
                )
            )
        )


def describe_get_non_existent_endpoint():
    @pytest.mark.parametrize(
        "non_existent_endpoint",
        ["/", "/ ", "/foo", "/%$^", f"/{COFFEE_DRINKS}/"],
    )
    def test_should_handle_and_return_not_found_exception_when_endpoint_does_not_exist(
        non_existent_endpoint,
    ):
        result = requests.get(f"{BASE_URL}{non_existent_endpoint}")

        expect(result.status_code).to(equal(HTTPStatus.OK))

        exception = result.json()
        expect(exception[STATUS_CODE]).to(equal(HTTPStatus.NOT_FOUND))
        expect(exception[MESSAGE]).to(equal("Specified resource does not exist"))
