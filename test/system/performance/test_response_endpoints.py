# pylint: disable=missing-module-docstring,missing-function-docstring,unused-variable,unnecessary-lambda,import-error

import gevent
from expects import expect, be_below_or_equal
from locust.env import Environment
from locust.stats import stats_history
from coffee_endpoint import COFFEE_DRINKS, COFFEE_ID, COFFEE_TITLE
from user import User


def describe_get_coffee_drinks_information():
    def test_should_respond_in_or_under_100_milliseconds():
        env = Environment(user_classes=[User], tags=[COFFEE_DRINKS])
        env.create_local_runner()
        runner = env.runner

        gevent.spawn(stats_history, runner)
        runner.start(1, spawn_rate=1)
        gevent.spawn_later(1, lambda: runner.quit())
        runner.greenlet.join()

        expect(env.stats.total.avg_response_time).to(be_below_or_equal(100))


def describe_get_coffee_drink_information_by_id():
    def test_should_respond_in_or_under_100_milliseconds():
        env = Environment(user_classes=[User], tags=[COFFEE_ID])
        env.create_local_runner()
        runner = env.runner

        gevent.spawn(stats_history, runner)
        runner.start(1, spawn_rate=1)
        gevent.spawn_later(1, lambda: runner.quit())
        runner.greenlet.join()

        expect(env.stats.total.avg_response_time).to(be_below_or_equal(100))


def describe_get_coffee_drink_information_by_title():
    def test_should_respond_in_or_under_100_milliseconds():
        env = Environment(user_classes=[User], tags=[COFFEE_TITLE])
        env.create_local_runner()
        runner = env.runner

        gevent.spawn(stats_history, runner)
        runner.start(1, spawn_rate=1)
        gevent.spawn_later(1, lambda: runner.quit())
        runner.greenlet.join()

        expect(env.stats.total.avg_response_time).to(be_below_or_equal(100))


def describe_use_all_endpoints_simultaneously():
    def test_should_respond_in_or_under_100_milliseconds():
        env = Environment(
            user_classes=[User], tags=[COFFEE_DRINKS, COFFEE_ID, COFFEE_TITLE]
        )
        env.create_local_runner()
        runner = env.runner

        gevent.spawn(stats_history, runner)
        runner.start(1, spawn_rate=1)
        gevent.spawn_later(1, lambda: runner.quit())
        runner.greenlet.join()

        expect(env.stats.total.avg_response_time).to(be_below_or_equal(100))
