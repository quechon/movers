import pytest
from .app import app
from .config import TestingConfig

@pytest.fixture
def client():

    app.config.from_object(TestingConfig)

    client = app.test_client()

    yield client


def test_index(client):

    resp = client.get('/')
    assert resp.status_code == 200
    assert b'index' in resp.data
    assert b'Jose Rodriguez' in resp.data

def test_review_submit(client):

    resp = client.post('api/review', json={'first_name': '', 'last_name': '',
                                           'email': '', 'message': ''})

    print(resp.get_json)
