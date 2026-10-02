"""
Automated Test Suite: Product Catalog & Inventory Verification
Target: SauceDemo Inventory (/inventory.html)
Covers Listing, Sorting, Product Details Navigation, and Item Cart Toggling
"""
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestProducts:
    """Test suite covering product browsing, sorting, and item interaction."""

    def test_product_catalog_displays_six_items(self, logged_in_driver):
        """
        TC_PROD_001: Verify product catalog displays exactly 6 products with titles and prices.
        """
        driver = logged_in_driver
        items = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
        )
        assert len(items) == 6, f"Expected 6 items in catalog, found {len(items)}"

        # Verify each item has non-empty title and price
        for item in items:
            name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            price = item.find_element(By.CLASS_NAME, "inventory_item_price").text
            assert len(name) > 0, "Product name is empty."
            assert price.startswith("$"), f"Price '{price}' does not start with '$'"

    def test_product_sorting_az(self, logged_in_driver):
        """
        TC_PROD_007: Verify sorting products alphabetically from A to Z.
        """
        driver = logged_in_driver
        sort_dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
        sort_dropdown.select_by_value("az")

        item_names = [
            el.text for el in driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        ]
        assert item_names == sorted(item_names), "Products are not sorted alphabetically A-Z."

    def test_product_sorting_za(self, logged_in_driver):
        """
        TC_PROD_008: Verify sorting products alphabetically in reverse order from Z to A.
        """
        driver = logged_in_driver
        sort_dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
        sort_dropdown.select_by_value("za")

        item_names = [
            el.text for el in driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        ]
        assert item_names == sorted(item_names, reverse=True), "Products are not sorted Z-A."

    def test_product_sorting_price_low_to_high(self, logged_in_driver):
        """
        TC_PROD_009: Verify sorting products by price from low to high.
        """
        driver = logged_in_driver
        sort_dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
        sort_dropdown.select_by_value("lohi")

        price_elements = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        prices = [float(el.text.replace("$", "")) for el in price_elements]

        assert prices == sorted(prices), f"Prices not sorted low to high: {prices}"

    def test_product_sorting_price_high_to_low(self, logged_in_driver):
        """
        TC_PROD_010: Verify sorting products by price from high to low.
        """
        driver = logged_in_driver
        sort_dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
        sort_dropdown.select_by_value("hilo")

        price_elements = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        prices = [float(el.text.replace("$", "")) for el in price_elements]

        assert prices == sorted(prices, reverse=True), f"Prices not sorted high to low: {prices}"

    def test_product_details_navigation(self, logged_in_driver):
        """
        TC_PROD_004 & TC_PROD_006: Verify clicking product title opens item details and back navigation works.
        """
        driver = logged_in_driver
        first_product_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "inventory_item_name"))
        )
        product_name = first_product_link.text
        first_product_link.click()

        WebDriverWait(driver, 10).until(EC.url_contains("/inventory-item.html"))
        detail_name = driver.find_element(By.CLASS_NAME, "inventory_details_name").text
        assert detail_name == product_name, f"Expected '{product_name}', got '{detail_name}'"

        # Back to products button
        back_btn = driver.find_element(By.ID, "back-to-products")
        back_btn.click()
        WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))
        assert "/inventory.html" in driver.current_url

    def test_add_and_remove_product_from_catalog(self, logged_in_driver):
        """
        TC_PROD_011 & TC_PROD_012: Verify adding product updates button to 'Remove' and badge count,
        and clicking 'Remove' reverts state.
        """
        driver = logged_in_driver
        add_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
        )
        add_btn.click()

        # Check button changed to Remove
        remove_btn = driver.find_element(By.ID, "remove-sauce-labs-backpack")
        assert remove_btn.is_displayed(), "Remove button not displayed after adding product."

        # Check cart badge displays 1
        badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert badge.text == "1", f"Expected cart badge '1', got '{badge.text}'"

        # Click Remove button
        remove_btn.click()

        # Check button reverted to Add to cart
        reverted_add_btn = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        assert reverted_add_btn.is_displayed(), "Add button not restored after removal."

        # Check cart badge is gone
        badges = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        assert len(badges) == 0, "Cart badge still present after removing all items."
