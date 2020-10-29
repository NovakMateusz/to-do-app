from flask import Flask


def create_app():
    """
    Create a Flask app, using the application factory pattern.
    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    return app
