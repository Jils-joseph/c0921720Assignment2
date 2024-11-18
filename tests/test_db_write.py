import pytest
from pymongo import MongoClient

@pytest.fixture
def mongo_client():
    # Set up the MongoDB client
    client = MongoClient("mongodb+srv://c0921720:c821rlLlBkepjS32@shop-db.av3ee.mongodb.net/?retryWrites=true&w=majority&appName=shop-db")
    yield client
    client.close()

@pytest.fixture
def products_collection(mongo_client):
    # Get the products collection from the database
    db = mongo_client.shop_db
    return db.products

def test_insert_product(products_collection):
    # Create a sample product document
    product = {
        'name': 'Test Product',
        'tag': 'Test Tag',
        'price': 10.99
    }

    # Insert the product into the collection
    result = products_collection.insert_one(product)
    
    # Retrieve the inserted product
    inserted_product = products_collection.find_one({'_id': result.inserted_id})

    # Assert that the product matches the inserted data
    assert inserted_product['name'] == 'Test Product'
    assert inserted_product['tag'] == 'Test Tag'
    assert inserted_product['price'] == 10.99
