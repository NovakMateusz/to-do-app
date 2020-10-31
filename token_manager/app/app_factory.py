from flask import Flask
from token_manager.config import settings
from token_manager.app.extensions import db
from token_manager.blueprints.token.views import token_manager_blueprint


def extensions(app):
    """
    Register 0 or more extensions (mutates the app passed in).
    :param app: Flask application instance
    """
    db.init_app(app)


def create_app():
    """
    Create a Flask app, using the application factory pattern.
    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(settings)
    app.config.from_pyfile('settings.py')

    # Register blueprints
    app.register_blueprint(token_manager_blueprint)

    extensions(app)

    return app
