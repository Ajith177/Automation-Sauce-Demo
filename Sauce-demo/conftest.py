import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests
import tempfile
import shutil


def pytest_addoption(parser):
    parser.addoption(
        "--headless", action="store_true", default=False,
        help="Run browser in headless mode"
    )


@pytest.fixture(scope="session")
def driver(pytestconfig):
    chrome_options = Options()

    # Temporary profile directory for isolated sessions
    temp_profile = tempfile.mkdtemp()
    chrome_options.add_argument(f"--user-data-dir={temp_profile}")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Enable headless mode only if --headless is passed
    if pytestconfig.getoption("headless"):
        chrome_options.add_argument("--headless=new")

    # Disable various Chrome services/features that interfere with automation
    chrome_options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2,
        "autofill.profile_enabled": False,
        "autofill.credit_card_enabled": False,
        "profile.default_content_setting_values.popups": 0,
        "profile.default_content_setting_values.automatic_downloads": 1
    })

    chrome_options.add_argument("--disable-save-password-bubble")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-features=PasswordManagerOnboarding,PasswordCheck")
    chrome_options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

    # Start Chrome
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1920, 1080)
    time.sleep(2)

    # Open the application
    url = "https://www.saucedemo.com/"
    driver.get(url)
    print(url, "This is the URL")
    time.sleep(3)

    yield driver

    # Cleanup after tests
    driver.quit()
    shutil.rmtree(temp_profile, ignore_errors=True)


@pytest.fixture(scope="session")
def api_session():
    return requests.Session()
