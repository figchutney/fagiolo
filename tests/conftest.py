import pytest
from flask.testing import FlaskClient

from fagiolo import fagiolo


@pytest.fixture
def client() -> FlaskClient:
    fagiolo.app.config["DEBUG"] = True
    fagiolo.app.config["TESTING"] = True
    fagiolo.app.config["PROPAGATE_EXCEPTIONS"] = False
    fagiolo.app.config["PRESERVE_CONTEXT_ON_EXCEPTION"] = False

    with fagiolo.app.test_client() as client:
        yield client
