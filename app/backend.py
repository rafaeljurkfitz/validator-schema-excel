import os

import pandas as pd
from contract import Sales
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

# Carrega as variáveis de ambiente
load_dotenv()


def process_excel(uploaded_file):
    try:
        df = pd.read_excel(uploaded_file)

        # Verificar se há colunas extras no DataFrame
        extra_cols = set(df.columns) - set(Sales.model_fields.keys())
        if extra_cols:
            return False, f"Colunas extras detectadas no Excel: {', '.join(extra_cols)}"

        # Validar cada linha com o schema escolhido
        for index, row in df.iterrows():
            try:
                _ = Sales(**row.to_dict())
            except Exception as e:
                raise ValueError(f"Erro na linha {index + 2}: {e}")

        # Retorna tanto o resultado da validação, os erros, quanto o DataFrame
        return df, True, None

    except ValueError as ve:
        return df, False, str(ve)
    except Exception as e:
        return df, False, f"Erro inesperado: {str(e)}"


def save_dataframe_to_sql(df):
    # Salva o DataFrame no banco de dados
    df.to_sql("sales", con=DATABASE_URL, if_exists="replace", index=False)
