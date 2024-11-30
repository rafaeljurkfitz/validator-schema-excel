# Validator-schema-excel

![Image Alt Text](static/home.png)

This is a Python project that provides a web application using Streamlit as the frontend, a backend for validating Excel files based on a predefined schema, and saving the data to a database.

## Deploy

[![](https://img.shields.io/badge/Launch-Cloud%20Instance-brightgreen?style=for-the-badge)](https://validator-schema-excel-yn8pdttx5ciq69gn3xejsv.streamlit.app/)

## Database

A cloud-based `PostgreSQL` instance was used as the database to store validated data. It is hosted for free on [Render](https://render.com/).

## Main Features

- **Intuitive Frontend**: Uses the `Streamlit` framework to provide a user-friendly and visually appealing web interface. It's easy and fast to build for any type of developer and allows for cost-free deployment.
- **Excel File Validation**: Enables users to upload Excel files and validates them against a predefined schema in the project.
- **Secure Data Saving**: If the file's data passes validation, it is securely saved for further processing in the database.

## Main Technologies

- Python: Main programming language for backend development and validation logic.
- Streamlit: Used to create the interactive web frontend.
- Pandas: Library used for manipulating data in Excel format.
- Pytest: Used to run integration, unit, and functional tests for the application.
- [Sentry.io](https://sentry.io/): Provides observability for project logging. Sentry allows proactive monitoring of errors and exceptions in real-time, delivering valuable insights into application performance and stability.

## Contribution

Contributions are welcome! If you'd like to improve this project, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
