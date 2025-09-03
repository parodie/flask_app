import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_route(client):
    rv = client.get('/')
    assert rv.data == b"Hello from Flask!"

def test_health_check(client):
    rv = client.get('/health')
    assert rv.status_code == 200
    assert rv.data == b"OK"