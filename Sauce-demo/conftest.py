import pytest
from selenium import webdriver
import time
import requests
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture(scope="session")
def driver():
    chrome_options = Options()
    chrome_options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
    driver = webdriver.Chrome(options=chrome_options)
    time.sleep(2)
    URL = "https://www.saucedemo.com/"
    driver.get(URL)
    print(URL,"This is the URL")
    time.sleep(10)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def api_session():
    session = requests.Session()
    return session
