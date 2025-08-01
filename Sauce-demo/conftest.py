import pytest
import time
import requests
from utils.browser_setup import create_browser, cleanup_browser


def pytest_addoption(parser):
    parser.addoption(
        "--headless", action="store_true", default=False,
        help="Run browser in headless mode"
    )


@pytest.fixture(scope="session")
def driver(pytestconfig):
    headless_mode = pytestconfig.getoption("headless")
    driver, temp_profile = create_browser(headless=headless_mode)

    driver.get("https://www.saucedemo.com/")
    print("Navigated to https://www.saucedemo.com/")
    time.sleep(3)

    yield driver

    cleanup_browser(driver, temp_profile)


@pytest.fixture(scope="session")
def api_session():
    return requests.Session()
