# pylint: disable=redefined-outer-name,missing-class-docstring,missing-function-docstring,unused-variable,implicit-str-concat,bare-except

"""Locust user configuration for making API requests"""

from locust import HttpUser, task, tag, between
from coffee_endpoint import BASE_URL, COFFEE_DRINKS, COFFEE_ID, COFFEE_TITLE


class User(HttpUser):
    wait_time = between(0, 0.01)
    host = BASE_URL

    @tag(COFFEE_DRINKS)
    @task
    def get_coffee_drinks_endpoint(self):
        self.client.get(f"/{COFFEE_DRINKS}")

    @tag(COFFEE_ID)
    @task
    def get_coffee_drinks_by_id_endpoint(self):
        self.client.get(f"/{COFFEE_DRINKS}/{COFFEE_ID}")

    @tag(COFFEE_TITLE)
    @task
    def get_coffee_drinks_by_title_endpoint(self):
        self.client.get(f"/{COFFEE_DRINKS}/{COFFEE_TITLE}")
