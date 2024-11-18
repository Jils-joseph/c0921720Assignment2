import pytest
from app import app

@pytest.fixture
def client():
    # Set up the test client for Flask
    with app.test_client() as client:
        yield client

def test_home_route_invalid_method(client):
    # Simulate a POST request to the /home route, which expects GET
    response = client.post('/')

    # Assert that the status code is 405 (Method Not Allowed)
    assert response.status_code == 405
