"""
Automated Test Suite: Shopping Cart Operations
Target: SauceDemo Cart (/cart.html)
Covers Adding, Item Details Verification, Multiple Items, Cart Removal, Navigation, and Persistence
"""
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCart:
    """Test suite covering shopping cart workflows and validations."""

    def test_cart_opens_and_displays_added_item(self, logged_in_driver):
        """
        TC_CART_001 & TC_CART_002: Verify adding an item, opening cart, and verifying item details.
        """
        driver = logged_in_driver

        # Add Sauce Labs Backpack
        add_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
        )
        add_btn.click()

        # Navigate to Cart
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        WebDriverWait(driver, 10).until(EC.url_contains("/cart.html"))

        # Verify page header
        header = driver.find_element(By.CLASS_NAME, "title").text
        assert header == "Your Cart", f"Expected 'Your Cart', got '{header}'"

        # Verify item presence and properties
        cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(cart_items) == 1, f"Expected 1 item in cart, found {len(cart_items)}"

        item_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
        item_price = driver.find_element(By.CLASS_NAME, "inventory_item_price").text
        item_qty = driver.find_element(By.CLASS_NAME, "cart_quantity").text

        assert item_name == "Sauce Labs Backpack"
        assert item_price == "$29.99"
        assert item_qty == "1"

    def test_add_multiple_items_to_cart(self, logged_in_driver):
        """
        TC_CART_002 & TC_PROD_013: Verify adding 3 distinct items updates badge and cart list.
        """
        driver = logged_in_driver

        # Add 3 items
        items_to_add = [
            "add-to-cart-sauce-labs-backpack",
            "add-to-cart-sauce-labs-bike-light",
            "add-to-cart-sauce-labs-bolt-t-shirt"
        ]
        for btn_id in items_to_add:
            driver.find_element(By.ID, btn_id).click()

        # Check badge
        badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert badge.text == "3", f"Expected cart badge count 3, got '{badge.text}'"

        # Open cart and verify 3 items
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        WebDriverWait(driver, 10).until(EC.url_contains("/cart.html"))

        cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(cart_items) == 3, f"Expected 3 items in cart, found {len(cart_items)}"

    def test_remove_item_from_cart_page(self, logged_in_driver):
        """
        TC_CART_004: Verify removing an item directly from the cart page updates item list and badge.
        """
        driver = logged_in_driver

        # Add 2 items
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()

        # Open cart
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        WebDriverWait(driver, 10).until(EC.url_contains("/cart.html"))

        # Remove backpack from cart
        driver.find_element(By.ID, "remove-sauce-labs-backpack").click()

        # Verify only 1 item remains in cart
        remaining_items = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(remaining_items) == 1, f"Expected 1 item remaining, found {len(remaining_items)}"

        remaining_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
        assert remaining_name == "Sauce Labs Bike Light"

        badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert badge.text == "1"

    def test_continue_shopping_navigation(self, logged_in_driver):
        """
        TC_CART_006: Verify 'Continue Shopping' button navigates back to inventory with state intact.
        """
        driver = logged_in_driver

        # Add 1 item
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

        # Go to cart
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        WebDriverWait(driver, 10).until(EC.url_contains("/cart.html"))

        # Click Continue Shopping
        driver.find_element(By.ID, "continue-shopping").click()
        WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))

        # Verify item still marked as added
        remove_btn = driver.find_element(By.ID, "remove-sauce-labs-backpack")
        assert remove_btn.is_displayed()

    def test_cart_persistence_on_page_refresh(self, logged_in_driver):
        """
        TC_CART_007: Verify cart items persist across page refresh.
        """
        driver = logged_in_driver

        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        WebDriverWait(driver, 10).until(EC.url_contains("/cart.html"))

        # Refresh browser
        driver.refresh()
        WebDriverWait(driver, 10).until(EC.url_contains("/cart.html"))

        cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(cart_items) == 1, "Cart item lost after page refresh."
        assert driver.find_element(By.CLASS_NAME, "inventory_item_name").text == "Sauce Labs Backpack"
