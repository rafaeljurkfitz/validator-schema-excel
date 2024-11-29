"""Testes de integração."""

import os

import pandas as pd
from dotenv import load_dotenv

load_dotenv(".env")

# Lê as variáveis de ambiente
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")

# Cria a URL de conexão com o banco de dados
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"


def test_read_data_and_check_schema():
    """Testa a leitura dos dados e verifica o schema do DataFrame.

    Este teste verifica se os dados estão sendo lidos corretamente e se o schema do DataFrame está correto.

    Asserts:
        O DataFrame não deve estar vazio.
        O schema do DataFrame deve corresponder ao esperado.
    """

    df = pd.read_sql("SELECT * FROM sales", con=DATABASE_URL)

    # Verificar se o DataFrame não está vazio
    assert not df.empty, "O DataFrame está vazio."

    # Verificar o schema (colunas e tipos de dados)
    expected_dtype = {
        "email": "object",  # object em Pandas corresponde a string em SQL
        "data": "datetime64[ns]",
        "valor": "float64",
        "produto": "object",
        "quantidade": "int64",
        "categoria": "object",
    }

    assert (
        df.dtypes.to_dict() == expected_dtype
    ), "O schema do DataFrame não corresponde ao esperado."
