import os
import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options
import time
import requests


@pytest.fixture(scope="session")
def driver():
    edge_options = Options()

    # Detect if running in Jenkins (CI environment)
    is_ci = os.getenv("JENKINS_HOME") is not None  # Or use another env var like CI

    if is_ci:
        # Run in headless mode on Jenkins
        edge_options.add_argument("--headless")
        edge_options.add_argument("--disable-gpu")  # Recommended for headless
        print("Running Edge in headless mode (Jenkins)")

    else:
        # Run normally with GUI locally
        edge_options.add_argument("-inprivate")
        print("Running Edge in headed mode (local)")

    # Common prefs and options
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2,
        "autofill.profile_enabled": False,
        "autofill.credit_card_enabled": False,
        "profile.default_content_setting_values.popups": 0,
        "profile.default_content_setting_values.automatic_downloads": 1
    }
    edge_options.add_experimental_option("prefs", prefs)

    edge_options.add_argument("--disable-save-password-bubble")
    edge_options.add_argument("--disable-notifications")
    edge_options.add_argument("--disable-popup-blocking")
    edge_options.add_argument("--disable-infobars")
    edge_options.add_argument("--disable-blink-features=AutomationControlled")
    edge_options.add_argument("--disable-features=PasswordManagerOnboarding,PasswordCheck")

    edge_options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

    driver = webdriver.Edge(options=edge_options)
    driver.maximize_window()
    time.sleep(2)

    URL = "https://www.saucedemo.com/"
    driver.get(URL)
    print(URL, "This is the URL")
    time.sleep(5)

    yield driver
    driver.quit()
