"""
PyTest Configuration and Reusable Fixtures for E-Commerce QA Automation Suite.
Provides browser setup/teardown, base URL, login helper, and failure screenshot capture.
"""
import os
import pytest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.saucedemo.com/"


def pytest_addoption(parser):
    """Command line flags for test execution."""
    parser.addoption(
        "--headless",
        action="store_true",
        default=True,
        help="Run browser in headless mode (default: True)"
    )
    parser.addoption(
        "--headed",
        action="store_false",
        dest="headless",
        help="Run browser in visible GUI mode"
    )


@pytest.fixture(scope="session")
def base_url():
    """Returns application base URL."""
    return BASE_URL


@pytest.fixture
def driver(request):
    """
    Initializes Chrome WebDriver using Selenium Manager.
    Automatically manages browser lifecycle (setup and teardown).
    """
    headless = request.config.getoption("--headless")
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--ignore-certificate-errors")

    browser = webdriver.Chrome(options=chrome_options)
    browser.implicitly_wait(2)
    request.node.driver = browser

    yield browser

    browser.quit()


@pytest.fixture
def logged_in_driver(driver, base_url):
    """
    Pre-authenticated browser fixture.
    Logs in as standard_user and verifies inventory page is loaded.
    """
    driver.get(base_url)
    username_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )
    username_input.clear()
    username_input.send_keys("standard_user")

    password_input = driver.find_element(By.ID, "password")
    password_input.clear()
    password_input.send_keys("secret_sauce")

    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("/inventory.html")
    )
    return driver


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    PyTest hook that captures a screenshot whenever a test fails.
    Screenshots are saved in the project's 'screenshots/' folder.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver_instance = getattr(item, "driver", None)
        if driver_instance is None:
            driver_instance = item.funcargs.get("driver") or item.funcargs.get("logged_in_driver")
        if driver_instance:
            project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            screenshots_dir = os.path.join(project_root, "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            safe_name = item.name.replace("/", "_").replace("::", "_").replace("[", "_").replace("]", "_")
            screenshot_path = os.path.join(screenshots_dir, f"FAIL_{safe_name}_{timestamp}.png")
            try:
                driver_instance.save_screenshot(screenshot_path)
                print(f"\n[Test Failure Screenshot Captured]: {screenshot_path}")
            except Exception as exc:
                print(f"\n[Screenshot Capture Error]: {exc}")
