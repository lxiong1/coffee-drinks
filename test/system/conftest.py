# pylint: disable=missing-function-docstring,bare-except

"""Common and reusable fixtures for system-level related tests"""

import os
from http import HTTPStatus
from time import sleep
import requests
import pytest
from coffee_endpoint import BASE_URL


@pytest.fixture(autouse=True, scope="session")
def before_and_after_test():
    __start_app()

    yield

    __shutdown_app()


def __start_app():
    os.system("./entrypoint.sh &")

    while True:
        try:
            request = requests.get(BASE_URL)
            if request.status_code == HTTPStatus.OK:
                break
        except:
            sleep(2)
            continue


def __shutdown_app():
    os.system(
        """
        kill $(pgrep -f flask) || True
        docker rm -f $(docker ps -aq) || True
        """
    )
