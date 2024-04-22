from datetime import datetime

import pytest
from pydantic import ValidationError

from app.contract import Sales


# Test with valid data
def test_sales_with_valid_data():
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
