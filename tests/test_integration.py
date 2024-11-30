"""Tests of integration"""

import os

import pandas as pd
from dotenv import load_dotenv

load_dotenv(".env")

# Load the environment variables
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")

# Create the connection URL to the database
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"


def test_read_data_and_check_schema():
    """Test the read data and check schema.

    This test reads the data from the database and checks the schema.

    Asserts:
        The DataFrame should not be empty.
        The schema of the DataFrame should match the expected schema.
    """

    df = pd.read_sql("SELECT * FROM sales", con=DATABASE_URL)

    # Verify if the DataFrame is not empty
    assert not df.empty, "The data frame is empty."

    # Define the expected schema
    expected_dtype = {
        "email": "object",
        "date": "datetime64[ns]",
        "value": "float64",
        "product": "object",
        "quantity": "int64",
        "category": "object",
    }

    assert (
        df.dtypes.to_dict() == expected_dtype
    ), "The schema of the DataFrame does not match the expected schema."
