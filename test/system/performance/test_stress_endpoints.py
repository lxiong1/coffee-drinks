# pylint: disable=missing-module-docstring,missing-function-docstring,unused-variable,unnecessary-lambda,import-error

import pytest
import gevent
from expects import expect, equal
from locust.env import Environment
from locust.stats import stats_history
from coffee_endpoint import COFFEE_DRINKS, COFFEE_ID, COFFEE_TITLE
from user import User


def describe_get_coffee_drinks_information():
    @pytest.mark.parametrize(
        "user_spawn_rate",
        [25, 50, 75, 100],
    )
    def test_should_have_no_failures_with_varied_requests_per_second_in_5_seconds(
        user_spawn_rate,
    ):
        env = Environment(user_classes=[User], tags=[COFFEE_DRINKS])
        env.create_local_runner()
        runner = env.runner

        gevent.spawn(stats_history, runner)
        runner.start(1, spawn_rate=user_spawn_rate)
        gevent.spawn_later(5, lambda: runner.quit())
        runner.greenlet.join()

        expect(env.stats.total.num_failures).to(equal(0))


def describe_get_coffee_drink_information_by_id():
    @pytest.mark.parametrize(
        "user_spawn_rate",
        [25, 50, 75, 100],
    )
    def test_should_have_no_failures_with_varied_requests_per_second_in_5_seconds(
        user_spawn_rate,
    ):
        env = Environment(user_classes=[User], tags=[COFFEE_ID])
        env.create_local_runner()
        runner = env.runner

        gevent.spawn(stats_history, runner)
        runner.start(1, spawn_rate=user_spawn_rate)
        gevent.spawn_later(5, lambda: runner.quit())
        runner.greenlet.join()

        expect(env.stats.total.num_failures).to(equal(0))


def describe_get_coffee_drink_information_by_title():
    @pytest.mark.parametrize(
        "user_spawn_rate",
        [25, 50, 75, 100],
    )
    def test_should_have_no_failures_with_varied_requests_per_second_in_5_seconds(
        user_spawn_rate,
    ):
        env = Environment(user_classes=[User], tags=[COFFEE_TITLE])
        env.create_local_runner()
        runner = env.runner

        gevent.spawn(stats_history, runner)
        runner.start(1, spawn_rate=user_spawn_rate)
        gevent.spawn_later(5, lambda: runner.quit())
        runner.greenlet.join()

        expect(env.stats.total.num_failures).to(equal(0))


def describe_use_all_endpoints_simultaneously():
    @pytest.mark.parametrize(
        "user_spawn_rate",
        [25, 50, 75, 100],
    )
    def test_should_have_no_failures_with_varied_requests_per_second_in_5_seconds(
        user_spawn_rate,
    ):
        env = Environment(
            user_classes=[User], tags=[COFFEE_DRINKS, COFFEE_ID, COFFEE_TITLE]
        )
        env.create_local_runner()
        runner = env.runner

        gevent.spawn(stats_history, runner)
        runner.start(1, spawn_rate=user_spawn_rate)
        gevent.spawn_later(5, lambda: runner.quit())
        runner.greenlet.join()

        expect(env.stats.total.num_failures).to(equal(0))
