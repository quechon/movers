import pytest
from .app import app

@pytest.fixture
def client():

    app.config['TESTING'] = True

    client = app.test_client()

    yield client


def test_index(client):

    resp = client.get('/')
    assert resp.status_code == 200
    assert b'index' in resp.data
