import logging
import os
from http import HTTPStatus
from logging.handlers import TimedRotatingFileHandler

from flask import Flask, request

from src.commons.database import (
    close_session,
    get_connection_uri,
    initialize_session,
    rollback_session,
)

logging.basicConfig(
    level=logging.DEBUG,
    handlers=[
        TimedRotatingFileHandler(
            "logs/system.log", when="midnight", interval=1
        ),
        logging.StreamHandler(),
    ],
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)
logging.getLogger("faker").setLevel(logging.CRITICAL)
logging.getLogger("factory").setLevel(logging.CRITICAL)


def create_app(test_config=None):
    app = Flask(__name__)

    app.config.from_pyfile(
        os.path.dirname(os.path.dirname(__file__)) + os.path.sep + "config.py"
    )

    if test_config:
        app.config.update(test_config)

    setup_handlers(app)
    setup_database(app)

    return app


def setup_database(app):
    if app.config.get("TESTING") is True:
        # to avoid estabilishing connection globally
        # when running unit test cases.
        return
    if app.config.get("SQLALCHEMY_DATABASE_URI"):
        connection_uri = app.config["SQLALCHEMY_DATABASE_URI"]
    else:
        db_credentials = {
            "username": os.getenv("DB_USER"),
            "password": os.getenv("DB_PASSWORD"),
            "hostname": os.getenv("DB_HOSTNAME"),
            "database": os.getenv("DB_DATABASE"),
            "port": os.getenv("DB_PORT"),
        }
        connection_uri = get_connection_uri(**db_credentials)
    initialize_session(connection_uri)


def setup_handlers(app):
    @app.before_request
    def before_request():
        logging.info(f"[{request.method}] ::: {request.full_path}")
        if request.method in ["POST", "PUT", "PATCH"]:
            logging.info(f"Request payload {request.data}")

    @app.after_request
    def after_request(response):
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type, Authorization"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS"
        )
        return response

    @app.teardown_request
    def remove_session(exception=None):
        close_session()

    @app.errorhandler(Exception)
    def all_exception_handler(error):
        rollback_session()
        error_message = getattr(error, "message", str(error))
        logging.getLogger("root").error(error_message, exc_info=True)
        response = {
            "status": "error",
            "code": HTTPStatus.INTERNAL_SERVER_ERROR,
            "data": [],
            "message": "Something went wrong. "
            "Please contact the site admin.",
        }
        if app.config["DEBUG"]:
            response["data"] = error_message
        return response, HTTPStatus.INTERNAL_SERVER_ERROR

    @app.errorhandler(404)
    def api_not_found(error):
        error_message = getattr(error, "message", str(error))
        logging.getLogger("root").error(error_message, exc_info=True)
        return (
            {
                "status": "error",
                "code": HTTPStatus.NOT_FOUND,
                "data": {},
                "message": "API does not exist",
            },
            HTTPStatus.NOT_FOUND,
        )
