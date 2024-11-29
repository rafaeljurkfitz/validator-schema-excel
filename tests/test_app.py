""" Testes Funcionais """

import os
import subprocess
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver


@pytest.fixture
def driver():
    """Dispositivo de teste(fixture)  para iniciar o aplicativo Straemlit e o WebDriver

    Essa fixture começa o aplicativo Streamlit no background e o WebDriver em modo headless.

    Yields:
        driver (WebDriver): A instância WebDriver.
    """
    # Começa o Streamlit no background
    process = subprocess.Popen(["streamlit", "run", "app/app.py"])
    # Executa no modo headless
    options = webdriver.FirefoxOptions()
    options.add_argument("-headless")
    # Precisamos definir o driver
    driver = webdriver.Firefox(options=options)
    driver.set_page_load_timeout(5)
    yield driver

    # Fecha o WebDriver e o Streamlit depois dos testes
    driver.quit()
    process.kill()


def test_app_opens(driver: WebDriver):
    """Testa se o aplicativo abre.

    Este teste verifica se o aplicativo abre.

    Args:
        driver (WebDriver): A instância WebDriver.
    """
    driver.get("http://localhost:8501")
    sleep(2)


def test_check_title_is(driver: WebDriver):
    """Testa se o título da página está correto.

    Este teste verifica se o título da página está correto.

    Args:
        driver (WebDriver): A instância WebDriver.

    Asserts:
        O título deve ser "Validador de schema excel". Se o título não for o esperado, o teste falhará.
    """
    # Verifica se a página abre
    driver.get("http://localhost:8501")
    # Verifica se o título da página é correto
    sleep(2)
    # Captura o título da página
    page_title = driver.title

    # Verifica se o título da página é o esperado
    expected_title = "Validador de schema excel"  # Substitua pelo título esperado
    assert page_title == expected_title


def test_check_streamlit_h1(driver: WebDriver):
    """Testa se o h1 da página está correto.

    Este teste verifica se o h1 da página está correto.

    Args:
        driver (WebDriver): A instância WebDriver.

    Asserts:
        O h1 deve ser "Insira o seu excel para validação.". Se o h1 não for o esperado, o teste falhará.
    """
    # Verifica se a página abre
    driver.get("http://localhost:8501")
    # Aguarda a página carregar
    sleep(2)
    # Captura o elemento h1 da página
    h1_element = driver.find_element(By.TAG_NAME, "h1")

    # Verifica se o h1 da página é o esperado
    expected_element = (
        "Insira o seu excel para validação."  # Substitua pelo elemento esperado
    )
    assert h1_element.text == expected_element


def test_check_user_can_insert_a_excel_and_receive_a_message(driver: WebDriver):
    """Testa se o usuário pode inserir um excel e receber uma mensagem.

    Este teste verifica se o usuário pode inserir um arquivo Excel e receber uma mensagem.

    Args:
        driver (WebDriver): A instância WebDriver.

    Asserts:
        A mensagem "O schema do arquivo Excel está correto!" deve ser exibida na página. Se a mensagem não for exibida, o teste falhará.
    """

    # Abre a página
    driver.get("http://localhost:8501")

    sleep(3)

    # Envia o arquivo
    success_file_path = os.path.abspath("data/file.xlsx")
    driver.find_element(By.CSS_SELECTOR, 'input[type="file"]').send_keys(
        success_file_path
    )

    # Aguarda a página carregar
    sleep(3)
    assert "O schema do arquivo Excel está correto!" in driver.page_source
