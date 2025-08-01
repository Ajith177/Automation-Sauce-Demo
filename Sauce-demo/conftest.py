import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests
import tempfile
import shutil


@pytest.fixture(scope="session")
def driver():
    chrome_options = Options()

    # ✅ Use a temporary profile directory (avoids shared profile conflicts in CI)
    temp_profile = tempfile.mkdtemp()
    chrome_options.add_argument(f"--user-data-dir={temp_profile}")

    # ✅ Recommended arguments for CI environments
    chrome_options.add_argument("--headless=new")  # Use 'new' for recent Chrome versions
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # ✅ Browser preference settings
    chrome_options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2,
        "autofill.profile_enabled": False,
        "autofill.credit_card_enabled": False,
        "profile.default_content_setting_values.popups": 0,
        "profile.default_content_setting_values.automatic_downloads": 1
    })

    # ✅ Disable unnecessary features for automation
    chrome_options.add_argument("--disable-save-password-bubble")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-features=PasswordManagerOnboarding,PasswordCheck")
    chrome_options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

    # ✅ Launch the browser
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1920, 1080)
    time.sleep(2)

    # ✅ Navigate to target site
    URL = "https://www.saucedemo.com/"
    driver.get(URL)
    print(URL, "This is the URL")
    time.sleep(3)

    yield driver

    # ✅ Cleanup after session
    driver.quit()
    shutil.rmtree(temp_profile, ignore_errors=True)


@pytest.fixture(scope="session")
def api_session():
    return requests.Session()
