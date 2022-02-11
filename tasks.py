"""File that defines available tasks intended to be used during development"""

import textwrap
from os.path import dirname, realpath
from invoke import task

PROJECT_DIRECTORY = dirname(realpath(__file__))
SOURCE_CODE_DIRECTORY = f"{PROJECT_DIRECTORY}/src"
TEST_DIRECTORY = f"{PROJECT_DIRECTORY}/test"
UNIT_TEST_DIRECTORY = f"{TEST_DIRECTORY}/unit"
INTEGRATION_TEST_DIRECTORY = f"{TEST_DIRECTORY}/integration"
SYSTEM_TEST_DIRECTORY = f"{TEST_DIRECTORY}/system"
SYSTEM_FUNC_TEST_DIRECTORY = f"{SYSTEM_TEST_DIRECTORY}/functional"
SYSTEM_PERF_TEST_DIRECTORY = f"{SYSTEM_TEST_DIRECTORY}/performance"
ENTRYPOINT = f"{PROJECT_DIRECTORY}/entrypoint.sh"
DOCKERFILE = f"{PROJECT_DIRECTORY}/Dockerfile"
PYTHONPATH = "src"


@task
def format(context):
    """
    Formats Python code using black
    """
    print(f"\nFormatting Python code...\n")
    context.run(f"black .")


@task()
def lint(context):
    """
    Lints Python code using pylint
    """
    print(f"\nLinting Python code...\n")

    # Known issue with pylint not being able to lint directories so the
    # workaround is to use find for python files
    # Please reference issue: https://github.com/PyCQA/pylint/issues/352.
    context.run(f'pylint $(find . -iname "*.py")')


@task()
def lint_docker(context):
    """
    Lints Dockerfile using hadolintw
    """
    print(f"\nLinting Dockerfile from {DOCKERFILE}...\n")
    context.run(f"hadolintw --use-docker {DOCKERFILE}")


@task()
def complexity(context):
    """
    Calculates cyclomatic complexity of Python code
    """
    print(f"\nCalculating cyclomatic complexity in {SOURCE_CODE_DIRECTORY}...\n")
    context.run(f"radon cc -a {SOURCE_CODE_DIRECTORY}")


@task()
def security(context):
    """
    Finds common security issues in Python code
    """
    print(f"\nLooking for common security issues in {SOURCE_CODE_DIRECTORY}...\n")
    context.run(f"bandit -r {SOURCE_CODE_DIRECTORY}")


@task(format, lint, lint_docker, complexity, security)
def check(context):
    """
    Format, lint, complexity analyze, and security scan on code
    """


@task()
def install_hooks(context):
    """
    Creates pre-commit configuration file and installs hooks
    """
    print("\nCreating pre-commit configuration file...\n")
    context.run(
        textwrap.dedent(
            """
            cat > .pre-commit-config.yaml <<-EOF
            default_language_version:
              python: python3.10

            repos:
            - repo: https://github.com/ambv/black
              rev: 21.12b0
              hooks:
              - id: black
            - repo: https://github.com/PyCQA/pylint
              rev: v2.12.2
              hooks:
              - id: pylint
                entry: pipenv run pylint
            - repo: https://github.com/PyCQA/bandit
              rev: 1.7.1
              hooks:
              - id: bandit
                entry: pipenv run bandit -r -x test
            EOF
            """
        )
    )

    print(f"\nInstalling pre-commit hooks...\n")
    context.run(f"pre-commit install && pre-commit autoupdate")


@task()
def coverage(context):
    """
    Check test coverage using pytest-cov
    """
    print(
        f"\nChecking test coverage with {UNIT_TEST_DIRECTORY} and {INTEGRATION_TEST_DIRECTORY}...\n"
    )
    context.run(
        (
            f"PYTHONPATH={PYTHONPATH} pipenv run pytest --cov-report=html --cov-report=term "
            f"--cov=src {UNIT_TEST_DIRECTORY} {INTEGRATION_TEST_DIRECTORY}"
        )
    )


@task()
def unit(context):
    """
    Runs unit tests
    """
    print(f"\nRunning unit tests in {UNIT_TEST_DIRECTORY}...\n")
    context.run(f"PYTHONPATH={PYTHONPATH} pipenv run pytest {UNIT_TEST_DIRECTORY}")


@task()
def integration(context):
    """
    Runs integration tests
    """
    print(f"\nRunning integration tests in {INTEGRATION_TEST_DIRECTORY}...\n")
    context.run(
        f"PYTHONPATH={PYTHONPATH} pipenv run pytest {INTEGRATION_TEST_DIRECTORY}"
    )


@task()
def system_func(context):
    """
    Runs functional system tests
    """
    print(f"\nRunning system tests in {SYSTEM_FUNC_TEST_DIRECTORY}...\n")
    context.run(
        f"PYTHONPATH={PYTHONPATH} pipenv run pytest {SYSTEM_FUNC_TEST_DIRECTORY}"
    )


@task()
def system_perf(context):
    """
    Runs performance system tests
    """
    print(f"\nRunning system tests in {SYSTEM_PERF_TEST_DIRECTORY}...\n")
    context.run(
        f"PYTHONPATH={PYTHONPATH} pipenv run pytest {SYSTEM_PERF_TEST_DIRECTORY}"
    )


@task(system_func, system_perf)
def system(context):
    """
    Runs system tests
    """


@task(unit, integration, system)
def test(context):
    """
    Runs all tests
    """


@task()
def run(context):
    """
    Starts the flask application
    """
    print("\nStarting the flask application...\n")
    context.run(ENTRYPOINT)
