""" test app """

import subprocess
from time import sleep

import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    # Start the Streamlit in background
    process = subprocess.Popen(["streamlit", "run", "app/app.py"])

    # We need define out driver
    driver = webdriver.Firefox()
    driver.set_page_load_timeout(5)
    yield driver

    # Close the WebDriver and the Streamlit after the tests
    driver.quit()
    process.kill()


def test_app_opens(driver):
    # Verify if the page opens
    driver.get("http://localhost:8501")
    sleep(5)
