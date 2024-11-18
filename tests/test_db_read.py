import pytest
from pymongo import MongoClient

@pytest.fixture
def mongo_client():
    # Set up the MongoDB client
    client = MongoClient("mongodb+srv://c0921720:c821rlLlBkepjS32@shop-db.av3ee.mongodb.net/?retryWrites=true&w=majority&appName=shop-db")
    yield client
    client.close()

def test_mongo_ping(mongo_client):
    # Try pinging the MongoDB server
    try:
        mongo_client.admin.command('ping')  # This checks the connection
        success = True
    except Exception:
        success = False
    
    # Assert that the connection is successful
    assert success is True
