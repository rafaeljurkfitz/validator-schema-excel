"""Módulo to process the Excel file and save the data to the database."""

import os

import pandas as pd
from contract import Sales
from dotenv import load_dotenv

load_dotenv(".env")

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")

# Create the connection URL to the database
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

# Load the environment variables
load_dotenv()


def process_excel(uploaded_file) -> tuple:
    """Process the Excel file and validate it against a schema.

    Args:
        uploaded_file (str): The uploaded Excel file.

    Returns:
        tuple: ```A tuple containing the DataFrame, the validation result, and the errors.```
        dataframe (pd.DataFrame): The DataFrame containing the data from the Excel file.
        response_validation (bool): The result of the validation.
        erros (List[str]): The list of errors found during the validation.
    """
    try:
        df = pd.read_excel(uploaded_file)
        errors = []

        # Check if the columns in the Excel file match the schema
        extra_cols = set(df.columns) - set(Sales.model_fields.keys())
        if extra_cols:
            return False, f"Extra columns blocked in Excel: {', '.join(extra_cols)}"

        # Check if the data types in the Excel file match the schema
        for index, row in df.iterrows():
            try:
                _ = Sales(**row.to_dict())
            except Exception as e:
                errors.append(f"Line error {index + 2}: {e}")

        return df, True, errors

    except Exception as e:
        # Return an empty DataFrame and the error message
        return pd.DataFrame(), f"Unexpected error: {str(e)}"


def save_dataframe_to_sql(df: pd.DataFrame) -> None:
    """Save the DataFrame to the database.

    Args:
        df (pd.DataFrame): The DataFrame to be saved to the database.

    Returns:
        None
    """
    # Save the DataFrame to the database
    df.to_sql("sales", con=DATABASE_URL, if_exists="replace", index=False)
