import datetime

from flask import Blueprint, jsonify, request, current_app, after_this_request
import jwt

from token_manager.blueprints.token.models import User, Role


TOKEN_LIFESPAN = datetime.timedelta(minutes=15)

token_manager_blueprint = Blueprint('manager', __name__)


@token_manager_blueprint.route('/token', methods=['POST'])
def token_manager():
    @after_this_request
    def add_header(response):
        response.headers['Content-Type'] = 'application/json'
        return response

    auth = request.authorization
    if auth:
        temp_user = User.query.filter_by(username=auth.username).first()
        if temp_user and temp_user.check_password(auth.password):
            token_message = {
                'user': temp_user.username,
                'role': temp_user.role_id,
                'exp': datetime.datetime.utcnow() + TOKEN_LIFESPAN
            }
            token = jwt.encode(token_message, str(current_app.config['SECRET_KEY']))
            response_body = {'token': token.decode('UTF-8'),
                             'exp': 15 * 60}
            return jsonify(response_body)
        return jsonify({'msg': 'Wrong credentials'}), 401
    return jsonify({'msg': 'Missing credentials'}), 400
