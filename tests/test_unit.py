""" This module contains the unit tests for the Sales class."""

from datetime import datetime

import pytest
from pydantic import ValidationError

from app.contract import Sales


# Test with valid data
def test_sales_with_valid_data():
    """Test the Sales class with valid data.

    This test verifies if the Sales class can be instantiated with valid data.

    Asserts:
        The Sales class should be instantiated with the following attributes:
            email
            date
            value
            product
            quantity
            category

    Raises:
        AssertionError: If the Sales class is not instantiated with valid data.
    """
    data_valid = {
        "email": "comprador@example.com",
        "date": datetime.now(),
        "value": 100.50,
        "product": "product X",
        "quantity": 3,
        "category": "category3",
    }

    # The **data_valid syntax is a way of unpacking dectionaries in Python.
    # What this does is pass the key-value pairs in the valid_data dictionary as named arguments to the constructor of the Sales class.

    sale = Sales(**data_valid)

    assert sale.email == data_valid["email"]
    assert sale.data == data_valid["date"]
    assert sale.value == data_valid["value"]
    assert sale.product == data_valid["product"]
    assert sale.quantity == data_valid["quantity"]
    assert sale.category == data_valid["category"]


# Test with invalid data
def test_sales_with_invalid_data():
    """Test the Sales class with invalid data.

    This test verifies if the Sales class raises a ValidationError when instantiated with invalid data.

    Raises:
        ValidationError: If the Sales class is instantiated with invalid data.
    """
    data_invalid = {
        "email": "buyer",
        "data": "its not a datetime valid",
        "value": -100,
        "product": "",
        "quantity": -1,
        "category": "category3",
    }

    with pytest.raises(ValidationError):
        Sales(**data_invalid)


# Category Validation Test
def test_category_validation():
    """Test the category validation.

    This test verifies if the Sales class raises a ValidationError when instantiated with an invalid category.

    Raises:
        ValidationError: If the Sales class is instantiated with an invalid category.
    """
    data = {
        "email": "comprador@example.com",
        "data": datetime.now(),
        "value": 100.50,
        "product": "product Y",
        "quantity": 1,
        "category": "category invalid",
    }

    with pytest.raises(ValidationError):
        Sales(**data)
