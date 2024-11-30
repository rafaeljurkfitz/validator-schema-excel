"""Module to run the application."""

import logging
import os

import sentry_sdk
from backend import process_excel, save_dataframe_to_sql
from dotenv import load_dotenv
from frontend import ExcelValidadorUI

load_dotenv(".env")

sentry_sdk.init(
    dsn=os.getenv("SENTRY_DNS"),
    # * Set traces_sample_rate to 1.0 to capture 100%
    # * of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # * Set profiles_sample_rate to 1.0 to profile 100%
    # * of sampled transactions.
    # * We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)


def main():
    """Run the application.

    The main function initializes the ```ExcelValidadorUI``` class and displays the header. It then calls the upload_file function to upload the Excel file. The function processes the Excel file and validates it against a schema.

    It then displays the results in the graphical interface and, if there are no errors, allows the user to save the data to a database.

    The function also logs error or success messages using the ```sentry_sdk``` library and the ```logging``` module.
    """
    ui = ExcelValidadorUI()
    ui.display_header()

    uploaded_file = ui.upload_file()

    if uploaded_file:
        df, result, errors = process_excel(uploaded_file)
        ui.display_results(result, errors)

        if errors:
            ui.display_wrong_message()
            sentry_sdk.capture_message("Error in the excel")
            logging.error("Test error excel")
        elif ui.display_save_button():
            # Save the data to the database if the user clicks the button to save the data to the database and there are no errors in the Excel file schema validation process.
            save_dataframe_to_sql(df)
            ui.display_success_message()
            sentry_sdk.capture_message("Data saved successfully")
            logging.info("Test sucess excel")


if __name__ == "__main__":
    main()
