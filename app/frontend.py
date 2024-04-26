"""Frontend da aplicação."""

import streamlit as st


class ExcelValidadorUI:
    """Classe responsável por exibir a interface gráfica da aplicação."""

    def __init__(self):
        """Inicializa a classe ExcelValidadorUI.

        A função __init__ é responsável por inicializar a classe ExcelValidadorUI e chamar a função set_page_config para configurar a página.
        """
        self.set_page_config()

    def set_page_config(self):
        """Configura a página do Streamlit.

        A função set_page_config é responsável por configurar a página do Streamlit, definindo o título da página.
        """
        st.set_page_config(page_title="Validador de schema excel")

    def display_header(self):
        """Exibe o cabeçalho da aplicação.

        A função display_header é responsável por exibir o cabeçalho da aplicação, com o título da aplicação.
        """
        st.title("Insira o seu excel para validação.")

    def upload_file(self):
        """Exibe o botão de upload de arquivo Excel.

        A função upload_file é responsável por exibir o botão de upload de arquivo Excel e retornar o arquivo carregado pelo usuário.
        """
        return st.file_uploader("Carregue seu arquivo Excel aqui", type=["xlsx"])

    def display_results(self, result, errors):
        """Exibe o resultado da validação do arquivo Excel.

        A função display_results é responsável por exibir o resultado da validação do arquivo Excel, exibindo uma mensagem de erro ou sucesso.

        Args:
            result (bool): Resultado da validação.
            errors (List[str]): Lista de erros encontrados na validação.
        """
        if errors:
            for error in errors:
                st.error(f"Erro na validação: {error}")
        else:
            st.success("O schema do arquivo Excel está correto!")

    def display_save_button(self):
        """Exibe o botão para salvar no banco de dados.

        A função display_save_button é responsável por exibir o botão para salvar os dados no banco de dados.
        """
        return st.button("Salvar no Banco de Dados")

    def display_wrong_message(self):
        """Exibe uma mensagem de erro.

        A função display_wrong_message é responsável por exibir uma mensagem de erro na tela.
        """
        return st.error("Necessário corrigir a planilha!")

    def display_success_message(self):
        """Exibe uma mensagem de sucesso.

        A função display_success_message é responsável por exibir uma mensagem de sucesso na tela.
        """
        return st.success("Dados salvos com sucesso no banco de dados!")
