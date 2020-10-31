from flask import Blueprint, jsonify, request
import jwt


token_manager_blueprint = Blueprint('manager', __name__)


@token_manager_blueprint.route('/token', methods=['POST'])
def token_manager():
    return ''
