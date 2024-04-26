""" test app """

import os
import subprocess
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver


@pytest.fixture
def driver():
    """Fixture to start the Streamlit app and the WebDriver.

    This fixture starts the Streamlit app in the background and the WebDriver in headless mode.

    Yields:
        WebDriver: The WebDriver instance.
    """
    # Start the Streamlit in background
    process = subprocess.Popen(["streamlit", "run", "app/app.py"])
    # Execute in mode headless
    options = webdriver.FirefoxOptions()
    options.add_argument("-headless")
    # We need define out driver
    driver = webdriver.Firefox(options=options)
    driver.set_page_load_timeout(5)
    yield driver

    # Close the WebDriver and the Streamlit after the tests
    driver.quit()
    process.kill()


def test_app_opens(driver: WebDriver):
    """Test if the app opens.

    This test verifies if the app opens.

    Args:
        driver (WebDriver): The WebDriver instance.
    """
    # Verify if the page opens
    driver.get("http://localhost:8501")
    sleep(2)


def test_check_title_is(driver: WebDriver):
    """Test if the title is correct.

    This test verifies if the title of the page is correct.

    Args:
        driver (WebDriver): The WebDriver instance.
    """
    # Verify if the page opens
    driver.get("http://localhost:8501")
    # Verify if the page's title is
    sleep(2)
    # Capture the page's title
    page_title = driver.title

    # Verify if the page's title is the expected
    expected_title = (
        "Validador de schema excel"  # Replace with the actual expected title
    )
    assert page_title == expected_title


def test_check_streamlit_h1(driver: WebDriver):
    """Test if the h1 is correct.

    This test verifies if the h1 of the page is correct.

    Args:
        driver (WebDriver): The WebDriver instance.
    """
    # Verify if the page opens
    driver.get("http://localhost:8501")
    # Verify if the page's title is
    sleep(2)
    # Capture the h1 page's title (<h1></h1>)
    h1_element = driver.find_element(By.TAG_NAME, "h1")

    # Verify if the h1 page's title is the expected
    expected_element = (
        "Insira o seu excel para validação."  # Replace with the actual expected title
    )
    assert h1_element.text == expected_element


def test_check_user_can_insert_a_excel_and_receive_a_message(driver: WebDriver):
    """Test if the user can insert a excel and receive a message.

    This test verifies if the user can insert a excel and receive a message.

    Args:
        driver (WebDriver): The WebDriver instance.
    """

    # Verify if the page opens
    driver.get("http://localhost:8501")

    sleep(3)

    # Upload the file successfully
    success_file_path = os.path.abspath("data/file.xlsx")
    driver.find_element(By.CSS_SELECTOR, 'input[type="file"]').send_keys(
        success_file_path
    )

    # Aguardar a mensagem de sucesso
    sleep(3)
    assert "O schema do arquivo Excel está correto!" in driver.page_source
