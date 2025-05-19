import pytest

@pytest.fixture
def user_data():
    return {
        "username" : "vamshidhar",
        "email" : "vamshidhar@gmail.com",
        "age" : 29
    }

@pytest.fixture
def product_data():
    return{
        "product" : "1001",
        "name" : "Macbook_Mini",
        "price" : 99999
    }

def test_user_data(user_data):
    assert isinstance(user_data, dict)
    assert user_data["username"] == "vamshidhar"
    assert "email" in user_data
    assert user_data["age"] > 18

def test_product_data(product_data):
    assert isinstance(product_data, dict)
    assert product_data["product"] == "1001"
    assert product_data["price"] > 0