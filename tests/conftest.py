import pytest
from flask.testing import FlaskClient

from pantry import pantry


@pytest.fixture
def client() -> FlaskClient:
    pantry.app.config["DEBUG"] = True
    pantry.app.config["TESTING"] = True
    pantry.app.config["PROPAGATE_EXCEPTIONS"] = False
    pantry.app.config["PRESERVE_CONTEXT_ON_EXCEPTION"] = False

    with pantry.app.test_client() as client:
        yield client
