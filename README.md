# E-Commerce Web Application – QA Automation & Testing Suite

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-4.50.0-43B02A?style=flat&logo=selenium&logoColor=white)
![PyTest](https://img.shields.io/badge/PyTest-9.1.1-0A9EDC?style=flat&logo=pytest&logoColor=white)
![Chrome](https://img.shields.io/badge/Chrome-Automated-4285F4?style=flat&logo=googlechrome&logoColor=white)
![Tests](https://img.shields.io/badge/Tests-26%20Passed-brightgreen?style=flat)
![Status](https://img.shields.io/badge/Build-Passing-brightgreen?style=flat)

A complete, production-grade Quality Assurance portfolio project demonstrating end-to-end QA practices—from strategic manual test planning and granular test case design to automated regression testing, defect reporting, and executive execution analytics.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Objectives](#objectives)
- [Application Under Test](#application-under-test)
- [Testing Approach](#testing-approach)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Test Coverage](#test-coverage)
- [Automation Coverage](#automation-coverage)
- [Test Case Summary](#test-case-summary)
- [Execution Results](#execution-results)
- [Defects / Findings](#defects--findings)
- [How to Run](#how-to-run)
- [Skills Demonstrated](#skills-demonstrated)

---

## Project Overview
This project showcases real-world Quality Assurance engineering applied to an e-commerce platform. As a QA Automation Engineer, the goal was to ensure comprehensive test coverage, robust validation of core revenue-critical workflows, resilient automated regression testing, and transparent bug tracking.

The suite combines:
1. **Manual Testing Assets**: An enterprise-grade [Test Plan](test-plan/Test_Plan.md), a 50-case [Test Case Matrix](test-cases/Test_Cases.csv) (Excel/CSV), and a structured [Bug & Exploratory Findings Report](bug-reports/Bug_Report.md).
2. **Automated Testing Suite**: A modular Python + Selenium WebDriver + PyTest framework with automated driver management via Selenium Manager, reusable fixtures, explicit wait synchronization, and automatic screenshot capture on test failure.

---

## Objectives
- Implement industry-standard manual QA documentation, including test planning, test case specification, and defect reporting.
- Build a maintainable, readable, and 100% reliable test automation suite covering all primary customer journeys.
- Validate critical e-commerce logic: catalog sorting algorithms, cart math, subtotal and tax calculation, and order dispatch.
- Ensure strict negative validation for authentication and checkout fields.
- Demonstrate modern QA best practices: explicit waits (zero brittle sleeps), automated failure screenshot hooks, and headless/headed execution toggling.

---

## Application Under Test
- **Application Name**: Swag Labs / SauceDemo
- **Live URL**: [https://www.saucedemo.com/](https://www.saucedemo.com/)
- **Description**: A stable, publicly accessible demo e-commerce web application created and maintained by Sauce Labs for QA engineering, functional verification, and test automation practice.

---

## Testing Approach

### 1. Manual Testing
- Structured requirement analysis and boundary identification.
- Designed 50 comprehensive manual test cases in CSV format covering positive paths, negative inputs, boundary conditions, and usability.
- Persona-based exploratory testing across standard, error, and edge-case account profiles.

### 2. Automated Testing
- Built with Python 3.12, Selenium WebDriver 4, and PyTest 9.
- Native driver provisioning through **Selenium Manager** (no manual ChromeDriver download required).
- Centralized fixtures in `automation/conftest.py` for browser lifecycle, authentication, and failure hooks.
- Strict use of explicit waits (`WebDriverWait` + `expected_conditions`) to prevent flaky execution.

### 3. Testing Types Applied
- **Functional Testing**: Verifying core workflows (login, inventory, cart manipulation, checkout).
- **Positive Testing**: Verifying expected system behavior under valid inputs.
- **Negative Testing**: Validating proper error messaging and route restrictions under invalid inputs.
- **Regression Testing**: Automated suite ensuring code changes do not regress existing functionality.
- **UI & Usability Testing**: Verifying layout elements, drawer menus, responsive styling, and modal dismissals.
- **Boundary Value Analysis**: Testing empty fields, missing inputs, and character boundary handling.

---

## Tech Stack

| Technology | Purpose |
| :--- | :--- |
| **Python 3.12+** | Core programming language for automation scripts |
| **Selenium WebDriver 4.50.0** | Web browser automation and DOM interaction |
| **PyTest 9.1.1** | Test runner, assertion engine, and test reporting framework |
| **Selenium Manager** | Automated, zero-config browser driver management |
| **Git & GitHub** | Version control, documentation hosting, and collaboration |
| **CSV / Excel** | Tabular manual test case repository compatible with spreadsheet tools |
| **Markdown** | Formatted documentation for plans, reports, and summaries |

---

## Project Structure

```
ecommerce-qa-automation/
│
├── README.md                          # Project documentation and portfolio overview
├── requirements.txt                   # Project dependencies (Selenium, PyTest)
├── .gitignore                         # Git exclusion rules for Python, venv, and cache
│
├── test-plan/
│   └── Test_Plan.md                   # Formal QA Test Plan (strategy, scope, criteria)
│
├── test-cases/
│   └── Test_Cases.csv                 # 54 manual test cases (Excel-compatible CSV)
│
├── bug-reports/
│   └── Bug_Report.md                  # Confirmed persona defects & exploratory findings
│
├── automation/
│   ├── __init__.py                    # Package initializer
│   ├── conftest.py                    # PyTest configuration, fixtures & failure hooks
│   ├── test_login.py                  # Automated tests: Authentication & Login
│   ├── test_products.py               # Automated tests: Catalog, Sorting & Details
│   ├── test_cart.py                   # Automated tests: Cart operations & persistence
│   ├── test_checkout.py               # Automated tests: Checkout, validations & math
│   └── test_logout.py                 # Automated tests: Session logout & route guards
│
├── screenshots/
│   ├── .gitkeep                       # Directory anchor
│   ├── evidence_bug_001_problem_user_catalog.png # Defect evidence: 404 dog images
│   ├── evidence_bug_002_problem_user_checkout.png # Defect evidence: checkout error
│   ├── sample_failure_hook_demo.png   # Auto-captured failure hook demonstration
│   ├── standard_user_catalog.png      # Standard user verified catalog view
│   └── standard_user_order_complete.png # Order completion confirmation
│
├── reports/
│   └── QA_Test_Report.md              # Detailed Test Execution Report with actual results
│
└── docs/
    └── Test_Execution_Summary.md       # Executive summary & key engineering learnings
```

---

## Test Coverage

The test suite covers the entire e-commerce customer journey:

| Module | Scope of Verification |
| :--- | :--- |
| **Authentication** | Valid login, invalid username, invalid password, empty username, empty password, locked-out user account |
| **Product Catalog** | 6-item catalog display, price & title formatting, image loading, product details page navigation, back navigation |
| **Inventory Sorting** | Name (A to Z), Name (Z to A), Price (Low to High), Price (High to Low) |
| **Shopping Cart** | Single item addition, multiple items addition, cart badge updates, item removal from cart, cart persistence on refresh |
| **Checkout Flow** | Information form validation (First Name, Last Name, Zip required), cancel navigation, overview order summary, pricing calculation (`Subtotal + Tax = Total`), purchase completion |
| **Session Security** | Sidebar logout, route guard verification (preventing unauthenticated access to `/inventory.html`), menu toggle |

---

## Automation Coverage

26 automated test methods across 5 test modules:

1. **`test_login.py`**
   - `test_valid_login` (Positive authentication happy path)
   - `test_invalid_username` (Validation banner on unknown account)
   - `test_invalid_password` (Validation banner on incorrect password)
   - `test_empty_username_field` (Required field validation)
   - `test_empty_password_field` (Required field validation)
   - `test_locked_out_user` (Account lockout handling)
2. **`test_products.py`**
   - `test_product_catalog_displays_six_items` (Catalog completeness and format)
   - `test_product_sorting_az` (Alphabetical A-Z sorting)
   - `test_product_sorting_za` (Alphabetical Z-A sorting)
   - `test_product_sorting_price_low_to_high` (Ascending price sorting)
   - `test_product_sorting_price_high_to_low` (Descending price sorting)
   - `test_product_details_navigation` (Item detail view and return)
   - `test_add_and_remove_product_from_catalog` (Catalog button state toggle)
3. **`test_cart.py`**
   - `test_cart_opens_and_displays_added_item` (Cart viewing and item accuracy)
   - `test_add_multiple_items_to_cart` (Multi-item addition and badge sync)
   - `test_remove_item_from_cart_page` (Direct removal from cart)
   - `test_continue_shopping_navigation` (Preserving cart while returning to catalog)
   - `test_cart_persistence_on_page_refresh` (Browser reload persistence)
4. **`test_checkout.py`**
   - `test_checkout_with_valid_data` (Full checkout flow + math verification)
   - `test_checkout_missing_first_name` (Missing First Name validation)
   - `test_checkout_missing_last_name` (Missing Last Name validation)
   - `test_checkout_missing_postal_code` (Missing Postal Code validation)
   - `test_checkout_cancel_button_returns_to_cart` (Cancel navigation)
5. **`test_logout.py`**
   - `test_successful_logout` (Session invalidation via sidebar)
   - `test_prevent_access_to_inventory_after_logout` (Route protection validation)
   - `test_sidebar_menu_open_and_close` (Sidebar drawer UI interaction)

---

## Test Case Summary

- **Total Manual Test Cases**: **54** (documented in [test-cases/Test_Cases.csv](test-cases/Test_Cases.csv))
- **Total Automated Tests**: **26**
- **Critical Priority**: 14 test cases
- **High Priority**: 24 test cases
- **Medium Priority**: 10 test cases
- **Low Priority**: 2 test cases

---

## Execution Results

> [!NOTE]
> All metrics reflect **actual local test execution** conducted on Windows 11 with Google Chrome.

```text
============================= test session starts =============================
platform win32 -- Python 3.12.10, pytest-9.1.1, pluggy-1.6.0
rootdir: ecommerce-qa-automation
collected 26 items

automation/test_cart.py::TestCart::test_cart_opens_and_displays_added_item PASSED [  3%]
automation/test_cart.py::TestCart::test_add_multiple_items_to_cart PASSED        [  7%]
automation/test_cart.py::TestCart::test_remove_item_from_cart_page PASSED       [ 11%]
automation/test_cart.py::TestCart::test_continue_shopping_navigation PASSED     [ 15%]
automation/test_cart.py::TestCart::test_cart_persistence_on_page_refresh PASSED [ 19%]
automation/test_checkout.py::TestCheckout::test_checkout_with_valid_data PASSED  [ 23%]
automation/test_checkout.py::TestCheckout::test_checkout_missing_first_name PASSED [ 26%]
automation/test_checkout.py::TestCheckout::test_checkout_missing_last_name PASSED  [ 30%]
automation/test_checkout.py::TestCheckout::test_checkout_missing_postal_code PASSED [ 34%]
automation/test_checkout.py::TestCheckout::test_checkout_cancel_button_returns_to_cart PASSED [ 38%]
automation/test_login.py::TestLogin::test_valid_login PASSED                    [ 42%]
automation/test_login.py::TestLogin::test_invalid_username PASSED               [ 46%]
automation/test_login.py::TestLogin::test_invalid_password PASSED               [ 50%]
automation/test_login.py::TestLogin::test_empty_username_field PASSED          [ 53%]
automation/test_login.py::TestLogin::test_empty_password_field PASSED          [ 57%]
automation/test_login.py::TestLogin::test_locked_out_user PASSED               [ 61%]
automation/test_logout.py::TestLogout::test_successful_logout PASSED           [ 65%]
automation/test_logout.py::TestLogout::test_prevent_access_to_inventory_after_logout PASSED [ 69%]
automation/test_logout.py::TestLogout::test_sidebar_menu_open_and_close PASSED [ 73%]
automation/test_products.py::TestProducts::test_product_catalog_displays_six_items PASSED [ 76%]
automation/test_products.py::TestProducts::test_product_sorting_az PASSED       [ 80%]
automation/test_products.py::TestProducts::test_product_sorting_za PASSED       [ 84%]
automation/test_products.py::TestProducts::test_product_sorting_price_low_to_high PASSED [ 88%]
automation/test_products.py::TestProducts::test_product_sorting_price_high_to_low PASSED [ 92%]
automation/test_products.py::TestProducts::test_product_details_navigation PASSED [ 96%]
automation/test_products.py::TestProducts::test_add_and_remove_product_from_catalog PASSED [100%]

======================= 26 passed in 114.98s (0:01:54) ========================
```

| Total Executed | Passed | Failed | Blocked | Pass Rate | Runtime |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **26** | **26** | **0** | **0** | **100%** | **114.98s** |

---

## Defects / Findings

Documented in detail in [bug-reports/Bug_Report.md](bug-reports/Bug_Report.md):

### Confirmed Defects (Persona Testing)
1. **BUG-AUT-001**: Broken/identical placeholder dog images rendered across all catalog items for `problem_user`.
2. **BUG-AUT-002**: "Last Name" input field is non-functional during checkout for `problem_user`, blocking order completion.
3. **BUG-AUT-003**: Clicking "Finish" button on checkout overview triggers an error banner instead of placing order for `error_user`.

### Exploratory / Usability Findings (Standard User Journey)
1. **OBS-EXP-001**: System permits placing empty orders ($0.00) when checkout is triggered with zero items in cart.
2. **OBS-EXP-002**: Cart item quantity is displayed as static text and cannot be edited inline.
3. **OBS-EXP-003**: Absence of a show/hide password visibility toggle on login form.

---

## How to Run

### Prerequisites
- Python 3.10+ installed
- Google Chrome browser installed
- Git installed

### 1. Clone the Repository
```bash
git clone https://github.com/meowski007/ecommerce-qa-automation.git
cd ecommerce-qa-automation
```

### 2. Create and Activate Virtual Environment
**On Windows (PowerShell / Command Prompt):**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**On macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Required Dependencies
```bash
pip install -r requirements.txt
```

### 4. Execute the Automated Test Suite

**Run all tests in headless mode (default, fastest):**
```bash
pytest
```

**Run all tests with verbose real-time output:**
```bash
pytest -v -s
```

**Run tests in visible browser window (headed mode):**
```bash
pytest --headed -v
```

**Run a specific test module:**
```bash
pytest automation/test_login.py -v
pytest automation/test_checkout.py -v
```

**Run a specific test method:**
```bash
pytest automation/test_checkout.py::TestCheckout::test_checkout_with_valid_data -v
```

---

## Skills Demonstrated
- **Manual Testing**: Requirement decomposition, test strategy formulation, exploratory testing.
- **Test Case Design**: Boundary value analysis, equivalence partitioning, positive and negative test cases.
- **Test Automation**: Selenium WebDriver 4, PyTest architecture, Selenium Manager, session fixtures.
- **Synchronization Best Practices**: Explicit waits (`WebDriverWait`, `expected_conditions`), zero hard-coded sleeps.
- **Defect Reporting**: Root cause investigation, reproducible step creation, severity/priority assignment.
- **Test Documentation**: Test Plans, Execution Reports, Traceability Matrices, and Executive Summaries.
- **Version Control & CI/CD Hygiene**: Git version control, branch management, clean `.gitignore`, GitHub repository management.
