import pytest
from token_manager.app.app_factory import create_app


def test_factory_app():
    new_app = create_app()
    assert new_app
