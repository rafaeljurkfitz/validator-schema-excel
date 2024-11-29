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
    # * Define o traces_sample_rate para 1.0 para capturar 100%
    # * das transações de monitoramento de performance.
    traces_sample_rate=1.0,
    # * Define o profiles_sample_rate para 1.0 para perfilar 100%
    # * das transações de amostras.
    # * É recomendado ajustar esses valores em produção, não é necessário capturar todas, pois pode ser custoso.
    profiles_sample_rate=1.0,
)


def main():
    """
    Função principal que chama a interface gráfica e processa o arquivo excel.

    A função main é responsável por iniciar a execução do programa. Ela chama a classe ```ExcelValidadorUI``` para exibir a interface gráfica, permite ao usuário fazer o upload de um arquivo excel e processa esse arquivo utilizando a função ***process_excel***.

    Em seguida, exibe os resultados na interface gráfica e, se não houver erros, permite ao usuário salvar os dados em um banco de dados.

    A função também registra mensagens de erro ou sucesso utilizando a ```biblioteca sentry_sdk``` e o ```módulo logging```.
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
            logging.error("Teste erro excel")
        elif ui.display_save_button():
            # Se não houver erros e o botão for exibido, exibir o botão e fazer o log
            save_dataframe_to_sql(df)
            ui.display_success_message()
            sentry_sdk.capture_message("Banco de dados foi atualizado")
            logging.info("Teste sucesso excel")


if __name__ == "__main__":
    main()
