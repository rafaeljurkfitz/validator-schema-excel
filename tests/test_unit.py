""" Testes unitários para o módulo principal do programa. """

from datetime import datetime

import pytest
from pydantic import ValidationError

from app.contract import Sales


def test_sales_with_valid_data():
    """Testa a classe Sales com dados válidos.

    Este teste verifica se a classe Sales é instanciada com os atributos corretos.

    Asserts:
        A classe Sales deve ser instânciada com os seguintes atributos:
            email
            data
            valor
            produto
            quantidade
            categoria

    Raises:
        AssertionError: Se a classe Sales não for instanciada com os atributos corretos.
    """
    data_valid = {
        "email": "comprador@example.com",
        "data": datetime.now(),
        "valor": 100.50,
        "produto": "Produto X",
        "quantidade": 3,
        "categoria": "categoria3",
    }

    # A sintaxe **data_valid é o caminho para desempacotar dicionários no Python.
    # Isso permite passar os valores do dicionário como argumentos nomeados.

    sale = Sales(**data_valid)

    assert sale.email == data_valid["email"]
    assert sale.data == data_valid["data"]
    assert sale.valor == data_valid["valor"]
    assert sale.produto == data_valid["produto"]
    assert sale.quantidade == data_valid["quantidade"]
    assert sale.categoria == data_valid["categoria"]


def test_sales_with_invalid_data():
    """Testa a classe Sales com dados inválidos.

    Este teste verifica se a classe Sales é instanciada com dados inválidos.

    Raises:
        ValidationError: Se a classe Sales for instanciada com dados válidos.
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


def test_category_validation():
    """Testa a validação da categoria.

    Este teste verifica se a classe Sales é instanciada com uma categoria válida.

    Raises:
        ValidationError: Se a classe Sales for instanciada com uma categoria inválida.
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
