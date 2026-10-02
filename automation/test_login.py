"""
Automated Test Suite: User Authentication & Login Verification
Target: SauceDemo Login Portal
Covers Positive and Negative Login Scenarios
"""
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLogin:
    """Test suite covering authentication workflows."""

    def test_valid_login(self, driver, base_url):
        """
        TC_LOG_001: Verify successful login with valid credentials (standard_user).
        Expected: User is redirected to inventory page and 'Products' header is displayed.
        """
        driver.get(base_url)

        # Enter credentials
        username_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        )
        username_field.clear()
        username_field.send_keys("standard_user")

        password_field = driver.find_element(By.ID, "password")
        password_field.clear()
        password_field.send_keys("secret_sauce")

        # Submit form
        driver.find_element(By.ID, "login-button").click()

        # Assertions
        WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))
        assert "/inventory.html" in driver.current_url, "User was not redirected to inventory page."

        title_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "title"))
        )
        assert title_element.text == "Products", f"Expected header 'Products', got '{title_element.text}'"

    def test_invalid_username(self, driver, base_url):
        """
        TC_LOG_002: Verify login failure with an unregistered username.
        Expected: Error banner displays mismatch notification.
        """
        driver.get(base_url)

        username_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        )
        username_field.send_keys("non_existent_user")

        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("secret_sauce")

        driver.find_element(By.ID, "login-button").click()

        error_elem = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
        )
        expected_msg = "Epic sadface: Username and password do not match any user in this service"
        assert expected_msg in error_elem.text, f"Expected '{expected_msg}', got '{error_elem.text}'"

    def test_invalid_password(self, driver, base_url):
        """
        TC_LOG_003: Verify login failure with valid username but incorrect password.
        Expected: Error banner displays mismatch notification.
        """
        driver.get(base_url)

        username_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        )
        username_field.send_keys("standard_user")

        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("invalid_pass_123")

        driver.find_element(By.ID, "login-button").click()

        error_elem = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
        )
        expected_msg = "Epic sadface: Username and password do not match any user in this service"
        assert expected_msg in error_elem.text, f"Expected '{expected_msg}', got '{error_elem.text}'"

    def test_empty_username_field(self, driver, base_url):
        """
        TC_LOG_004: Verify validation error when username is omitted.
        Expected: Error banner displays 'Epic sadface: Username is required'.
        """
        driver.get(base_url)

        password_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "password"))
        )
        password_field.send_keys("secret_sauce")

        driver.find_element(By.ID, "login-button").click()

        error_elem = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
        )
        assert "Epic sadface: Username is required" in error_elem.text

    def test_empty_password_field(self, driver, base_url):
        """
        TC_LOG_005: Verify validation error when password is omitted.
        Expected: Error banner displays 'Epic sadface: Password is required'.
        """
        driver.get(base_url)

        username_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        )
        username_field.send_keys("standard_user")

        driver.find_element(By.ID, "login-button").click()

        error_elem = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
        )
        assert "Epic sadface: Password is required" in error_elem.text

    def test_locked_out_user(self, driver, base_url):
        """
        TC_LOG_007: Verify login failure for locked out persona.
        Expected: Error banner displays 'Epic sadface: Sorry, this user has been locked out.'
        """
        driver.get(base_url)

        username_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        )
        username_field.send_keys("locked_out_user")

        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("secret_sauce")

        driver.find_element(By.ID, "login-button").click()

        error_elem = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
        )
        assert "Epic sadface: Sorry, this user has been locked out." in error_elem.text
