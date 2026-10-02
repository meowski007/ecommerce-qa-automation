# QA Test Execution Report: E-Commerce Web Application

## 1. Executive Summary
This document provides the formal Test Execution Report for the **E-Commerce Web Application (SauceDemo)** quality assurance cycle. Testing encompassed comprehensive manual test design and verification alongside an automated end-to-end regression test suite built with Python, Selenium WebDriver, and PyTest.

| Metric | Result |
| :--- | :--- |
| **Execution Date** | October 3, 2026 |
| **Operating System** | Windows 11 64-bit |
| **Test Browser** | Google Chrome (Version 154.0.8037.93) |
| **Test Framework** | PyTest 9.1.1 + Selenium WebDriver 4.50.0 |
| **Total Manual Test Cases Designed** | 54 |
| **Total Automated Test Cases Executed** | 26 |
| **Automated Tests Passed** | 26 (100%) |
| **Automated Tests Failed** | 0 (0%) |
| **Automated Tests Blocked** | 0 (0%) |
| **Suite Execution Duration** | 114.98 seconds (~1 min 55 sec) |
| **Confirmed Functional Defects** | 3 (documented in `Bug_Report.md`) |
| **Exploratory / Usability Findings** | 3 (documented in `Bug_Report.md`) |
| **Final Test Verdict** | **PASSED – READY FOR RELEASE** (Standard User Flow) |

---

## 2. Test Execution Breakdown by Module

| Module | Automated Tests | Passed | Failed | Blocked | Pass Rate |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Authentication & Login** (`test_login.py`) | 6 | 6 | 0 | 0 | 100% |
| **Product Catalog & Details** (`test_products.py`) | 7 | 7 | 0 | 0 | 100% |
| **Shopping Cart Operations** (`test_cart.py`) | 5 | 5 | 0 | 0 | 100% |
| **Checkout & Calculations** (`test_checkout.py`) | 5 | 5 | 0 | 0 | 100% |
| **Session & Navigation** (`test_logout.py`) | 3 | 3 | 0 | 0 | 100% |
| **TOTAL** | **26** | **26** | **0** | **0** | **100%** |

---

## 3. Automation Suite Test Inventory & Outcomes

### 3.1 Authentication Module (`test_login.py`)
- `test_valid_login`: Verified standard authentication redirects to `/inventory.html` and renders product header. `[PASSED]`
- `test_invalid_username`: Verified validation banner on non-existent account submission. `[PASSED]`
- `test_invalid_password`: Verified rejection of incorrect password with exact banner text. `[PASSED]`
- `test_empty_username_field`: Verified required field validation when username is omitted. `[PASSED]`
- `test_empty_password_field`: Verified required field validation when password is omitted. `[PASSED]`
- `test_locked_out_user`: Verified locked-out persona generates explicit account lock warning. `[PASSED]`

### 3.2 Product Catalog Module (`test_products.py`)
- `test_product_catalog_displays_six_items`: Confirmed catalog displays exactly 6 products with non-empty titles and valid price strings. `[PASSED]`
- `test_product_sorting_az`: Verified inventory sorts alphabetically A-Z. `[PASSED]`
- `test_product_sorting_za`: Verified inventory sorts in reverse alphabetical Z-A. `[PASSED]`
- `test_product_sorting_price_low_to_high`: Verified ascending numeric price order ($7.99 to $49.99). `[PASSED]`
- `test_product_sorting_price_high_to_low`: Verified descending numeric price order ($49.99 to $7.99). `[PASSED]`
- `test_product_details_navigation`: Confirmed clicking item title navigates to item details and back-button returns to inventory. `[PASSED]`
- `test_add_and_remove_product_from_catalog`: Verified button toggling between "Add to cart" and "Remove", and badge counter increment/reset. `[PASSED]`

### 3.3 Shopping Cart Module (`test_cart.py`)
- `test_cart_opens_and_displays_added_item`: Confirmed cart page navigation and verified item name, price, and default qty `1`. `[PASSED]`
- `test_add_multiple_items_to_cart`: Verified 3 distinct items added consecutively update badge counter to `3` and populate cart. `[PASSED]`
- `test_remove_item_from_cart_page`: Confirmed removing item inside cart updates cart list and decrements badge to `1`. `[PASSED]`
- `test_continue_shopping_navigation`: Verified returning to catalog preserves active cart selections. `[PASSED]`
- `test_cart_persistence_on_page_refresh`: Confirmed cart contents remain persistent following browser reload (F5). `[PASSED]`

### 3.4 Checkout Workflow Module (`test_checkout.py`)
- `test_checkout_with_valid_data`: End-to-end happy path: submitted customer details, verified item total ($39.98) + tax ($3.20) == order total ($43.18), completed order, verified confirmation header, and verified cart badge cleared. `[PASSED]`
- `test_checkout_missing_first_name`: Confirmed required validation error when First Name is omitted. `[PASSED]`
- `test_checkout_missing_last_name`: Confirmed required validation error when Last Name is omitted. `[PASSED]`
- `test_checkout_missing_postal_code`: Confirmed required validation error when Postal Code is omitted. `[PASSED]`
- `test_checkout_cancel_button_returns_to_cart`: Verified step-one Cancel button safely returns to cart without modifying state. `[PASSED]`

### 3.5 Session & Menu Module (`test_logout.py`)
- `test_successful_logout`: Verified hamburger menu logout redirects to login page with login button visible. `[PASSED]`
- `test_prevent_access_to_inventory_after_logout`: Verified direct URL navigation to `/inventory.html` after session termination is denied with security banner. `[PASSED]`
- `test_sidebar_menu_open_and_close`: Verified menu opens and transitions closed cleanly upon clicking close icon. `[PASSED]`

---

## 4. Defect & Observational Summary

Testing confirmed the primary production path (`standard_user`) is stable, performant, and reliable. Defects were isolated to specific test personas designed for failure testing:

1. **BUG-AUT-001 (Medium)**: Broken image placeholders on all inventory items for `problem_user`.
2. **BUG-AUT-002 (Critical)**: Non-editable "Last Name" field in checkout step one for `problem_user`.
3. **BUG-AUT-003 (Critical)**: Order placement failure when clicking "Finish" on overview for `error_user`.
4. **OBS-EXP-001 (Usability Observation)**: Empty cart allows proceeding through checkout and placing $0.00 order.
5. **OBS-EXP-002 (Enhancement Opportunity)**: Cart item quantity is static and cannot be modified inline.
6. **OBS-EXP-003 (Accessibility Observation)**: Missing show/hide password toggle on login portal.

---

## 5. Test Coverage & Quality Assessment
- **Functional Coverage**: 100% of specified core user flows are automated and verified.
- **Negative Testing Coverage**: Form validations across authentication and checkout are fully covered with explicit assertion of error messages.
- **Test Automation Stability**: Zero test flakiness observed. Tests utilize explicit `WebDriverWait` with expected conditions instead of arbitrary delays.
- **Maintainability**: Automated tests leverage modular fixtures (`driver`, `logged_in_driver`) and hook-based failure screenshot capture.

---

## 6. Recommendations
1. **Empty Cart Restriction**: Add validation to `/cart.html` disabling the "Checkout" button when no items are present.
2. **Inline Quantity Adjustments**: Enhance the cart component to allow users to increase or decrease quantities without having to re-add items from the catalog.
3. **CI/CD Integration**: Connect the PyTest suite to GitHub Actions to execute automatically on pull requests and commits.

---

## 7. Sign-off Verdict
**Sign-off Status**: **APPROVED**  
The core e-commerce workflow meets all functional acceptance criteria under normal operating conditions.
