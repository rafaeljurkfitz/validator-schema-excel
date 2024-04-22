from backend import process_excel
from frontend import ExcelValidadorUI


def main():
    ui = ExcelValidadorUI()
    ui.display_header()

    uploaded_file = ui.upload_file()

    if uploaded_file:
        result, error = process_excel(uploaded_file)
        ui.display_results(result, error)


if __name__ == "__main__":
    main()
