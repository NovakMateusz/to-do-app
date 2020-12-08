from base64 import b64encode
import json
import os
import tempfile

import pytest
import jwt

from token_manager.app.app_factory import create_app
from token_manager.app.extensions import db
from token_manager.blueprints.token.models import User


@pytest.fixture
def app():
    yield create_app()


@pytest.fixture(name='secret')
def app_secret(app):
    yield app.config['SECRET']


@pytest.fixture
def client(app):
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            test_user = User(username='testUser', email='test@test.com', role_id=1)
            test_user.set_password('test')
            db.session.add(test_user)
            yield client
            User.query.filter_by(username='testUser').delete()

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])


def test_factory_app(client):
    assert client


def test_added_test_user(app):
    with app.app_context():
        assert User.query.filter_by(username='testUser')


def test_get_token(client, secret):
    username = 'testUser'
    password = 'test'
    role = 1
    auth = b64encode(f"{username}:{password}".encode('UTF-8')).decode("ascii")
    response = client.post('/token', headers=dict(Authorization=f'Basic {auth}'))
    assert response.status_code == 200
    json_body = json.loads(response.data)
    token = json_body['token']
    decoded = jwt.decode(token, secret, algorithms=['HS256'], options=dict(verify_signature=False))
    assert decoded['user'] == username
    assert decoded['role'] == role


def test_get_token_field(client):
    username = 'NoneExistingUser'
    password = 'NoneExistingUserPassword'
    auth = b64encode(f"{username}:{password}".encode('UTF-8')).decode("ascii")
    response = client.post('/token', headers=dict(Authorization=f'Basic {auth}'))
    assert response.status_code != 200
