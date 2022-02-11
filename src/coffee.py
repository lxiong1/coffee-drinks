"""The main file containing all available API endpoints"""

from uuid import UUID
from flask import Flask
from flask.json import jsonify
from flask.wrappers import Response
from werkzeug.exceptions import InternalServerError
from domain.database.mongo import Mongo
from domain.repository.coffee_information_repository import CoffeeInformationRepository
from exception.not_found_exception import NotFoundException
from service.coffee_information_service import CoffeeInformationService


app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True

coffee_information_repository = CoffeeInformationRepository(Mongo())
coffee_information_service = CoffeeInformationService(coffee_information_repository)


@app.route("/coffee_drinks")
def get_coffee_drinks_information() -> Response:
    """Endpoint that retrieves all information about the coffee drink varieties

    Returns:
        Response: JSON Object that contains information about all coffee drinks
    """
    return jsonify(coffee_information_service.get_all_information())


@app.route("/coffee_drinks/<uuid:coffee_drink_id>")
def get_coffee_drink_information_by_id(coffee_drink_id: UUID) -> Response:
    """Endpoint that retrieves information about a coffee drink when found by given id

    Args:
        coffee_drink_id (UUID): Unique identifier for a coffee drink

    Returns:
        Response: JSON Object that contains information about a coffee drink based on given id
    """
    return jsonify(coffee_information_service.get_drink_by_id(coffee_drink_id))


@app.route("/coffee_drinks/<string:coffee_title>")
def get_coffee_drink_information_by_title(coffee_title: str) -> Response:
    """Endpoint that retrieves information about a coffee drink when found by given title

    Args:
        coffee_title (str): Name of a coffee drink

    Returns:
        Response: JSON Object that contains information about a coffee drink based on given title
    """
    return jsonify(coffee_information_service.get_drink_by_title(coffee_title))


@app.errorhandler(Exception)
def handle_exception(exception: Exception) -> Response:
    """Captures any exception raised and converts them to into a JSON format as a response

    Args:
        exception (Exception): Exception raised to be handled

    Returns:
        Response: JSON Object that contains information about the exception that was raised
    """
    return jsonify(exception)


# pylint: disable=unused-argument
@app.errorhandler(InternalServerError)
def handle_internal_server_error(
    internal_server_error: InternalServerError,
) -> Response:
    """Captures InternalServerError raised and converts it to into a JSON format as a response

    Args:
        internal_server_error (InternalServerError): InternalServerError raised to be handled

    Returns:
        Response: JSON Object that contains NotFoundException
    """
    return jsonify(NotFoundException(message="Specified resource does not exist"))
