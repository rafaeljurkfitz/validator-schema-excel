""" This module contains the unit tests for the Sales class."""

from datetime import datetime

import pytest
from pydantic import ValidationError

from app.contract import Sales


# Test with valid data
def test_sales_with_valid_data():
    """Test the Sales class with valid data.

    This test verifies if the Sales class can be instantiated with valid data.
    """
    data_valid = {
        "email": "comprador@example.com",
        "data": datetime.now(),
        "valor": 100.50,
        "produto": "Produto X",
        "quantidade": 3,
        "categoria": "categoria3",
    }

    # The **data_valid syntax is a way of unpacking dectionaries in Python.
    # What this does is pass the key-value pairs in the valid_data dictionary as named arguments to the constructor of the Sales class.

    sale = Sales(**data_valid)

    assert sale.email == data_valid["email"]
    assert sale.data == data_valid["data"]
    assert sale.valor == data_valid["valor"]
    assert sale.produto == data_valid["produto"]
    assert sale.quantidade == data_valid["quantidade"]
    assert sale.categoria == data_valid["categoria"]


# Test with invalid data
def test_sales_with_invalid_data():
    """Test the Sales class with invalid data.

    This test verifies if the Sales class raises a ValidationError when instantiated with invalid data.

    Raises:
        ValidationError: If the Sales class is instantiated with invalid data.
    """
    data_invalid = {
        "email": "comprador",
        "data": "não é uma data",
        "valor": -100,
        "produto": "",
        "quantidade": -1,
        "categoria": "categoria3",
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
        "valor": 100.50,
        "produto": "Produto Y",
        "quantidade": 1,
        "categoria": "categoria inexistente",
    }

    with pytest.raises(ValidationError):
        Sales(**data)
