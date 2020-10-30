from flask import Blueprint


token_manager_blueprint = Blueprint('manager', __name__)


@token_manager_blueprint.route('/token')
def get_token():
    return ''
