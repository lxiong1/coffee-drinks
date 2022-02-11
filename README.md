# Coffee Drinks

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

API that retrieves information about coffee drinks.

## Getting Started

### Prerequisites

**Disclaimer:** The instructions below assume MacOS. If you're on a Windows machine, you will have to use `scoop` or `chocolatey` to install `pyenv`, `pipenv`, and `docker`. The setup may be different.

Local machine dependencies:

- `pyenv`: Install by running `brew install pyenv`
- `pipenv`: Install by running `brew install pipenv`
- `docker`: Install by running `brew install docker`

### Usage

#### Setup

To get the project set up to run as an application, run the following command in this project directory:

```bash
pipenv sync --dev
```

This will install the necessary project dependencies as well as developed-related tools based on the `Pipfile.lock`. This file is our source of truth for all things dependency.

#### Run

After installing dependencies, you can run the application with the following command:

```bash
invoke run
```

You should eventually see an output like this:

```bash
 * Serving Flask app 'coffee' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

#### Request

There are three available endpoints as defined in [src/coffee.py](src/coffee.py):

- `coffee_drinks`
- `coffee_drinks/<coffee_drink_id>`
- `coffee_drinks/<coffee_title>`

For example, to get information about `cappuccino`, run the following command:

```bash
curl http://127.0.0.1:5000/coffee_drinks/cappuccino
```

You should see a response like this:

```bash
{
    "_id": "01d8ddd3-f437-4313-991d-7d8bea95aee1", 
    "title": "Cappuccino", 
    "description": "An espresso-based coffee drink that originated in Austria with later development taking place in Italy, and is prepared with steamed milk foam.", 
    "ingredients": [
        "Espresso", 
        "Steamed Milk"
    ]
}
```

### Development

When adding a new feature or modifying the code, always run static code analysis while developing to ensure you are compliant with development standards. There are tasks defined in [tasks.py](tasks.py) to assist you in doing this.

#### Pre-commit hooks

The project is setup with pre-commit hooks to help ensure that we are compliant with coding standards. These hooks will run on a commit to version control and will either stop or allow you to commit based on the analyzed code.

If for some reason the hooks aren't already set up, please run the following command to intall them:

```bash
invoke install-hooks
```

#### Static Analysis

These are tasks that you can run to help you develop smarter and more efficiently:

```bash
invoke format
invoke lint
invoke complexity
invoke security
```

You can do all of these tasks at once with:

```bash
invoke check
```

#### Test

##### Verify

Tests should be ran multiple times during development to ensure we are working torwards expected behavior.

To run unit tests:

```bash
invoke unit
```

To run integration tests:

```bash
invoke integration
```

To run system functional tests:

```bash
invoke system-func
```

To run system performance tests:

```bash
invoke system-perf
```

To run all system tests:

```bash
invoke system
```

To run all tests:

```bash
invoke test
```

##### Coverage

Tests should be checked for gaps or missing coverages for the source code.

To run test coverage check:

```bash
invoke coverage
```

You will be able to determine from a quick glance how much of the source code is covered from this command in the terminal. For a more detailed look, you can take a look at the produced report in `htmlcov/index.html`. The report will tell you line by line per file where you may have missed test coverage.
