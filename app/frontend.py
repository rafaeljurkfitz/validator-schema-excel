"""Frontend of the application."""

import streamlit as st


class ExcelValidadorUI:
    """Class to define the frontend of the application."""

    def __init__(self):
        """Initialize the ExcelValidadorUI class.

        The function __init__ Initialize the ExcelValidadorUI class, setting the page configuration.
        """
        self.set_page_config()

    def set_page_config(self):
        """Set the page configuration.

        The function set_page_config is responsible for setting the page configuration of the application.
        """
        st.set_page_config(page_title="Validador Schema Excel")

    def display_header(self):
        """Display the header of the application.

        The function display_header is responsible for displaying the header of the application.
        """
        st.title("Insert here your Excel for validation.")

    def upload_file(self):
        """Upload the Excel file.

        The function upload_file is responsible for uploading the Excel file to the application. It uses the file_uploader function from the streamlit library.
        """
        return st.file_uploader("Upload your Excel file here", type=["xlsx"])

    def display_results(self, result, errors):
        """Display the validation results.

        The function display_results is responsible for displaying the validation results on the screen.

        Args:
            result (bool): Result of the validation.
            errors (List[str]): List of errors found during the validation.
        """
        if errors:
            for error in errors:
                st.error(f"Validation error: {error}")
        else:
            st.success("The Excel file schema is correct!")

    def display_save_button(self):
        """Display the save button.

        The function display_save_button is responsible for displaying the save button on the screen.
        """
        return st.button("Save data to the database")

    def display_wrong_message(self):
        """Show an error message.

        The function display_wrong_message is responsible for displaying an error message on the screen.
        """
        return st.error(
            "Error in the Excel file. Please check the schema. And upload the correct file again."
        )

    def display_success_message(self):
        """Show a success message.

        The function display_success_message is responsible for displaying a success message on the screen.
        """
        return st.success("Data saved successfully.")
