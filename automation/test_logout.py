"""
Automated Test Suite: User Session Termination & Navigation Menu
Target: SauceDemo Sidebar Menu & Session Invalidation
Covers Logout, Direct URL Protected Access, and Sidebar Interaction
"""
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLogout:
    """Test suite covering user logout and session security."""

    def test_successful_logout(self, logged_in_driver, base_url):
        """
        TC_LOG_010: Verify user can log out via sidebar menu.
        Expected: Session terminates, redirected to login page, login button visible.
        """
        driver = logged_in_driver

        # Open hamburger menu
        menu_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))
        )
        menu_btn.click()

        # Click logout link
        logout_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
        )
        logout_link.click()

        # Assert redirection to login portal
        login_btn = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "login-button"))
        )
        assert login_btn.is_displayed(), "Login button not displayed after logout."
        assert driver.current_url.rstrip("/") == base_url.rstrip("/"), f"Unexpected URL: {driver.current_url}"

    def test_prevent_access_to_inventory_after_logout(self, logged_in_driver, base_url):
        """
        TC_LOG_010: Verify session invalidation prevents back-navigation or direct URL access.
        Expected: Navigating to /inventory.html after logout denies access and shows error.
        """
        driver = logged_in_driver

        # Logout
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        logout_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
        )
        logout_link.click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "login-button"))
        )

        # Attempt to access inventory directly
        driver.get(f"{base_url.rstrip('/')}/inventory.html")

        # Expect error message or forced redirect to login
        error_elem = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
        )
        assert "You can only access '/inventory.html' when you are logged in" in error_elem.text

    def test_sidebar_menu_open_and_close(self, logged_in_driver):
        """
        TC_UI_001 & TC_UI_002: Verify sidebar menu opens and can be dismissed via close button.
        """
        driver = logged_in_driver

        # Open menu
        driver.find_element(By.ID, "react-burger-menu-btn").click()

        # Verify close button is visible
        close_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "react-burger-cross-btn"))
        )
        assert close_btn.is_displayed()

        # Close menu
        close_btn.click()

        # Wait for menu container to become hidden
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.ID, "react-burger-cross-btn"))
        )
