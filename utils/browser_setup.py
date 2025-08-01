from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import tempfile
import shutil
import time


def create_browser(headless=False):
    """
    Initializes and returns a Chrome WebDriver with custom options.

    Args:
        headless (bool): Whether to run Chrome in headless mode.

    Returns:
        tuple: WebDriver instance, temporary profile path
    """
    chrome_options = Options()
    temp_profile = tempfile.mkdtemp()
    chrome_options.add_argument(f"--user-data-dir={temp_profile}")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    if headless:
        chrome_options.add_argument("--headless=new")

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

    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1920, 1080)
    time.sleep(2)
    return driver, temp_profile


def cleanup_browser(driver, temp_profile):
    """Closes the browser and deletes temporary profile."""
    driver.quit()
    shutil.rmtree(temp_profile, ignore_errors=True)
