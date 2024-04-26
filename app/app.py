"""Módulo principal do programa."""

import logging
import os

import sentry_sdk
from backend import process_excel, save_dataframe_to_sql
from dotenv import load_dotenv
from frontend import ExcelValidadorUI

load_dotenv(".env")

sentry_sdk.init(
    dsn=os.getenv("SENTRY_DNS"),
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)


def main():
    """
    Função principal que chama a interface gráfica e processa o arquivo excel.

    A função main é responsável por iniciar a execução do programa. Ela chama a classe ExcelValidadorUI para exibir a interface gráfica,
    permite ao usuário fazer o upload de um arquivo excel e processa esse arquivo utilizando a função process_excel.
    Em seguida, exibe os resultados na interface gráfica e, se não houver erros, permite ao usuário salvar os dados em um banco de dados.
    A função também registra mensagens de erro ou sucesso utilizando a biblioteca sentry_sdk e o módulo logging.
    """
    ui = ExcelValidadorUI()
    ui.display_header()

    uploaded_file = ui.upload_file()

    if uploaded_file:
        df, result, errors = process_excel(uploaded_file)
        ui.display_results(result, errors)

        if errors:
            ui.display_wrong_message()
            sentry_sdk.capture_message("Erro ao subir excel")
            logging.error("Test error excel")
        elif ui.display_save_button():
            # Se não houver erros e o botão for exibido, exibir o botão e fazer o log
            save_dataframe_to_sql(df)
            ui.display_success_message()
            sentry_sdk.capture_message("Banco de dados foi atualizado")
            logging.info("Test sucess excel")


if __name__ == "__main__":
    """Executa a função main quando o módulo é executado diretamente."""
    main()
