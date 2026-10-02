# Test Execution Summary: E-Commerce QA Automation Project

## 1. Executive Summary
This project represents a complete, professional Quality Assurance evaluation of an e-commerce web application ([SauceDemo](https://www.saucedemo.com/)). The objective was to combine structured manual test planning and case design with a clean, reliable, and maintainable automated regression suite using **Python**, **Selenium WebDriver**, and **PyTest**.

---

## 2. What Was Tested
The testing scope encompassed the full end-to-end user lifecycle of an online retail platform:
1. **User Authentication & Session Security**:
   - Valid user login and landing page verification.
   - Negative authentication paths: incorrect passwords, invalid usernames, empty input fields, and locked-out user handling.
   - Session termination (logout) and route guard verification (preventing unauthorized access to `/inventory.html`).
2. **Product Catalog & Inventory Management**:
   - Product list rendering and verification of title, image, and price formatting.
   - Multi-criteria inventory sorting: Alphabetical (A to Z and Z to A) and Numerical Price (Low to High and High to Low).
   - Navigation between catalog and item detail views.
   - Add to Cart / Remove button state toggling.
3. **Shopping Cart Functionality**:
   - Cart navigation, badge count updates, and item detail fidelity.
   - Multiple item additions and cart list synchronization.
   - Item removal directly from the cart view.
   - Cart state persistence across page refresh and site navigation.
4. **Checkout & Financial Calculations**:
   - Customer information form validation (First Name, Last Name, Postal Code required field checks).
   - Order summary item review and pricing mathematics validation (`Item Total + Tax = Total`).
   - Order placement completion and receipt confirmation.
5. **UI & Usability**:
   - Sidebar drawer menu open/close transitions.
   - Error banner appearance and dismissibility.
   - Responsive layout stability.

---

## 3. How It Was Tested

### 3.1 Manual Testing Process
- Formulated an enterprise-grade **Test Plan** specifying testing methodologies (functional, smoke, regression, negative, UI, usability, boundary value analysis).
- Designed **54 granular manual test cases** stored in Excel-compatible CSV format (`test-cases/Test_Cases.csv`), covering preconditions, numbered steps, test data, expected outcomes, priority levels, and test types.
- Executed exploratory testing across multiple user personas (`standard_user`, `problem_user`, `error_user`, `locked_out_user`).

### 3.2 Automated Testing Architecture
- Developed modular, readable PyTest scripts located in `automation/`.
- Employed **Selenium WebDriver 4** with native **Selenium Manager**, eliminating the need for manual driver binaries.
- Configured reusable fixtures in `automation/conftest.py` for headless/headed browser lifecycle management and pre-authenticated sessions (`logged_in_driver`).
- Implemented PyTest hook-based screenshot capture on test failure, automatically logging PNG captures to `screenshots/` without polluting the test code.
- Enforced strict reliance on explicit waits (`WebDriverWait` + `expected_conditions`), completely eliminating brittle `time.sleep()` statements.

---

## 4. Test Coverage & Execution Metrics

| Category | Metric |
| :--- | :--- |
| **Manual Test Cases Designed** | 54 test cases |
| **Automated Test Scripts Implemented** | 26 test methods |
| **Automated Tests Executed** | 26 tests |
| **Automated Pass Rate** | **100% (26 Passed / 0 Failed)** |
| **Total Automation Runtime** | 114.98 seconds (~1 min 55 sec) |
| **Core End-to-End Scenarios Covered** | 100% (Login, Sort, Cart, Checkout, Logout) |

---

## 5. Defects & Findings Summary
- **3 Confirmed Functional Defects Logged**:
  - `BUG-AUT-001`: Broken image URLs on inventory listing for `problem_user`.
  - `BUG-AUT-002`: Defective "Last Name" input field blocking checkout for `problem_user`.
  - `BUG-AUT-003`: System error upon order finalization for `error_user`.
- **3 Usability / UX Observations Logged**:
  - `OBS-EXP-001`: System permits placing empty orders ($0.00) when checkout is triggered with zero items.
  - `OBS-EXP-002`: Cart item quantities are static text and cannot be edited directly within the cart.
  - `OBS-EXP-003`: Login password field lacks a visibility toggle (show/hide password).

All findings are formally documented in `bug-reports/Bug_Report.md`.

---

## 6. What I Learned & Key Takeaways
1. **Synchronization Over Hard Sleep**: Relying on explicit waits (`EC.visibility_of_element_located`, `EC.element_to_be_clickable`, `EC.url_contains`) produces fast, deterministic, non-flaky test runs, whereas hard-coded delays slow down test suites and fail unpredictably.
2. **PyTest Fixtures for Scalability**: Factoring out browser setup, teardown, and login state into fixtures in `conftest.py` dramatically reduces boilerplate, keeps individual test functions focused on their single assertion purpose, and ensures proper teardown even when tests fail.
3. **Automated Diagnostic Artifacts**: Hooking into PyTest's report generation (`pytest_runtest_makereport`) to automatically capture screenshots upon assertion failure provides immediate visual root-cause evidence for QA and engineering teams.
4. **Balancing Manual & Automated Testing**: Automation excels at rapid, repetitive regression passes and mathematical calculations, but exploratory manual testing remains indispensable for identifying subtle UX flaws, business logic gaps, and edge-case persona anomalies.
