from flask import Flask


def create_app():
    """
    Create a Flask app, using the application factory pattern.
    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')
    app.config.from_pyfile('config.py', silent=True)
    return app
