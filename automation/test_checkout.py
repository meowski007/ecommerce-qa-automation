"""
Automated Test Suite: Checkout Workflows & Validation
Target: SauceDemo Checkout Flow (/checkout-step-one.html, /checkout-step-two.html, /checkout-complete.html)
Covers End-to-End Successful Purchase, Pricing Calculations, and Negative Form Validation
"""
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCheckout:
    """Test suite covering checkout steps 1, 2, order completion, and negative validations."""

    def test_checkout_with_valid_data(self, logged_in_driver):
        """
        TC_CHK_001, TC_CHK_003, TC_CHK_009, TC_CHK_010, TC_CHK_012:
        Complete end-to-end checkout with valid customer info, verify pricing breakdown,
        and verify order confirmation.
        """
        driver = logged_in_driver

        # Add 2 items
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()

        # Open Cart
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        WebDriverWait(driver, 10).until(EC.url_contains("/cart.html"))

        # Click Checkout
        driver.find_element(By.ID, "checkout").click()
        WebDriverWait(driver, 10).until(EC.url_contains("/checkout-step-one.html"))

        # Fill Customer Details
        driver.find_element(By.ID, "first-name").send_keys("Jane")
        driver.find_element(By.ID, "last-name").send_keys("QA")
        driver.find_element(By.ID, "postal-code").send_keys("90210")
        driver.find_element(By.ID, "continue").click()

        # Step Two: Overview Verification
        WebDriverWait(driver, 10).until(EC.url_contains("/checkout-step-two.html"))

        overview_items = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(overview_items) == 2, f"Expected 2 overview items, found {len(overview_items)}"

        # Validate pricing calculation
        subtotal_text = driver.find_element(By.CLASS_NAME, "summary_subtotal_label").text
        tax_text = driver.find_element(By.CLASS_NAME, "summary_tax_label").text
        total_text = driver.find_element(By.CLASS_NAME, "summary_total_label").text

        subtotal = float(subtotal_text.split("$")[1])
        tax = float(tax_text.split("$")[1])
        total = float(total_text.split("$")[1])

        # Backpack ($29.99) + Bike Light ($9.99) = $39.98
        assert subtotal == 39.98, f"Expected subtotal 39.98, got {subtotal}"
        assert round(subtotal + tax, 2) == total, f"Total mismatch: {subtotal} + {tax} != {total}"

        # Complete Purchase
        driver.find_element(By.ID, "finish").click()

        # Complete page
        WebDriverWait(driver, 10).until(EC.url_contains("/checkout-complete.html"))
        complete_header = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
        )
        assert complete_header.text == "Thank you for your order!"

        # Ensure cart badge is cleared
        badges = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        assert len(badges) == 0, "Cart badge was not cleared after completing purchase."

    def test_checkout_missing_first_name(self, logged_in_driver):
        """
        TC_CHK_004: Verify validation error when First Name is omitted.
        """
        driver = logged_in_driver

        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        driver.find_element(By.ID, "checkout").click()

        WebDriverWait(driver, 10).until(EC.url_contains("/checkout-step-one.html"))

        # Leave First Name empty, enter Last Name and Postal Code
        driver.find_element(By.ID, "last-name").send_keys("Tester")
        driver.find_element(By.ID, "postal-code").send_keys("12345")
        driver.find_element(By.ID, "continue").click()

        error_elem = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
        )
        assert "Error: First Name is required" in error_elem.text

    def test_checkout_missing_last_name(self, logged_in_driver):
        """
        TC_CHK_005: Verify validation error when Last Name is omitted.
        """
        driver = logged_in_driver

        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        driver.find_element(By.ID, "checkout").click()

        WebDriverWait(driver, 10).until(EC.url_contains("/checkout-step-one.html"))

        # Enter First Name and Postal Code, leave Last Name empty
        driver.find_element(By.ID, "first-name").send_keys("Alex")
        driver.find_element(By.ID, "postal-code").send_keys("12345")
        driver.find_element(By.ID, "continue").click()

        error_elem = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
        )
        assert "Error: Last Name is required" in error_elem.text

    def test_checkout_missing_postal_code(self, logged_in_driver):
        """
        TC_CHK_006: Verify validation error when Postal Code is omitted.
        """
        driver = logged_in_driver

        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        driver.find_element(By.ID, "checkout").click()

        WebDriverWait(driver, 10).until(EC.url_contains("/checkout-step-one.html"))

        # Enter First Name and Last Name, leave Postal Code empty
        driver.find_element(By.ID, "first-name").send_keys("Alex")
        driver.find_element(By.ID, "last-name").send_keys("Tester")
        driver.find_element(By.ID, "continue").click()

        error_elem = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
        )
        assert "Error: Postal Code is required" in error_elem.text

    def test_checkout_cancel_button_returns_to_cart(self, logged_in_driver):
        """
        TC_CHK_008: Verify 'Cancel' button on checkout step one returns user to cart.
        """
        driver = logged_in_driver

        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        driver.find_element(By.ID, "checkout").click()

        WebDriverWait(driver, 10).until(EC.url_contains("/checkout-step-one.html"))

        driver.find_element(By.ID, "cancel").click()
        WebDriverWait(driver, 10).until(EC.url_contains("/cart.html"))
        assert "/cart.html" in driver.current_url
