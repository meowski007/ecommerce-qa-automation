# Test Plan: E-Commerce Web Application (SauceDemo)

## 1. Document Control
| Item | Details |
| :--- | :--- |
| **Project** | E-Commerce Web Application – QA Automation & Testing Suite |
| **Author** | QA Automation Engineer |
| **Document Version** | 1.0.0 |
| **Application Under Test** | Swag Labs / SauceDemo |
| **Application URL** | [https://www.saucedemo.com/](https://www.saucedemo.com/) |
| **Status** | Approved & Active |

---

## 2. Objective
The primary objective of this project is to implement a comprehensive, industry-standard Quality Assurance (QA) testing strategy for an e-commerce web application. This includes:
- Establishing a structured manual testing process with rigorous test planning and granular test case design.
- Implementing an automated testing framework using Python, Selenium WebDriver, and PyTest to validate core end-to-end user journeys.
- Identifying, documenting, and reporting software defects, behavioral edge cases, and user experience observations.
- Demonstrating production-ready test architecture, continuous maintainability, clean code standards, and transparent reporting.

---

## 3. Application Under Test (AUT)
The target application is **SauceDemo** ([https://www.saucedemo.com/](https://www.saucedemo.com/)), a standard, publicly accessible demo e-commerce web application maintained by Sauce Labs specifically for testing, test automation development, and QA practice.

The application simulates a complete consumer purchasing flow:
1. User Authentication (Login / Logout / Role handling)
2. Product Catalog (Inventory listing, product details, image rendering, item price display)
3. Inventory Sorting (A-to-Z, Z-to-A, Price low-to-high, Price high-to-low)
4. Shopping Cart (Add/Remove items, dynamic badge counter, quantity, price validation, persistence)
5. Checkout Flow (Customer information input, validation, order overview, tax and total calculations, order completion)

---

## 4. Scope of Testing

### 4.1 In-Scope
- **Authentication & Authorization**:
  - Positive login with `standard_user`
  - Negative login flows (empty username, empty password, invalid credentials, locked-out user)
  - Session termination via sidebar logout
- **Product Catalog & Details**:
  - Catalog rendering, product name, description, price, and image verification
  - Single and multi-criteria product sorting
  - Product details page navigation and return navigation
- **Shopping Cart**:
  - Adding single and multiple products from catalog
  - Item removal from catalog and directly from cart
  - Badge counter accuracy and state synchronization
  - Session and navigation persistence of cart state
- **Checkout Process**:
  - Step 1: Customer info form validation (First Name, Last Name, Postal Code required fields)
  - Step 2: Overview validation (item list, pricing math, tax calculation, subtotal, and total)
  - Step 3: Order confirmation and return home reset
- **UI / Usability & Cross-Browser Stability**:
  - Sidebar menu functionality (Open, Close, All Items, Reset App State)
  - Error message banners and dismissal
  - Basic responsiveness and navigation flow

### 4.2 Out-of-Scope
- Backend database schema and direct SQL verification (no direct DB access provided).
- Real financial transactions or third-party payment gateway integrations (e.g., Stripe, PayPal).
- API backend performance testing (e.g., load testing with JMeter/Locust exceeding 1,000 concurrent users).
- Native mobile application testing (iOS `.ipa` / Android `.apk`).
- Third-party OAuth authentication (Google, Apple, Facebook SSO).

---

## 5. Testing Types & Methodologies

| Testing Type | Description & Purpose |
| :--- | :--- |
| **Functional Testing** | Validate that application features work strictly according to specified e-commerce business requirements (cart math, ordering, validation). |
| **UI Testing** | Verify presence, layout, visibility, and states of UI components (buttons, inputs, error badges, icons). |
| **Smoke Testing** | Fast preliminary execution of critical sanity paths (valid login, load inventory, logout) to verify build stability. |
| **Regression Testing** | Automated repeatable suite to ensure recent code or test updates do not break existing verified workflows. |
| **Positive Testing** | Valid inputs and expected happy paths (e.g., correct login credentials, complete checkout forms). |
| **Negative Testing** | Invalid inputs, boundary omissions, and unauthorized states (e.g., blank fields, invalid users, locked account). |
| **Boundary Value Analysis** | Testing field length, special characters, and numeric validation in zip code and input fields. |
| **Compatibility Testing** | Browser compatibility on Google Chrome running across modern desktop resolutions. |
| **Basic Usability Testing** | Assessing user experience: clear error messages, intuitive navigation, button affordance, and legible pricing. |

---

## 6. Test Environment

| Component | Specification |
| :--- | :--- |
| **Operating System** | Windows 11 64-bit |
| **Web Browser** | Google Chrome (Latest Stable) |
| **Automation Language** | Python 3.12+ |
| **Automation Tool** | Selenium WebDriver (with native Selenium Manager driver resolution) |
| **Test Runner & Framework** | PyTest 8.x |
| **Design Pattern** | Lightweight Page Object Model (POM) / Reusable Component Helper |
| **Execution Mode** | Headless and Headed (UI interactive) support |
| **Repository & VCS** | Git / GitHub |

---

## 7. Test Data Management

The application provides preset user personas for test scenarios:

| Persona / User | Username | Password | Purpose / Expected Behavior |
| :--- | :--- | :--- | :--- |
| **Standard User** | `standard_user` | `secret_sauce` | Happy path; standard functional workflows |
| **Locked Out User** | `locked_out_user` | `secret_sauce` | Negative authentication; verifies error banner display |
| **Problem User** | `problem_user` | `secret_sauce` | Visual and functional defect detection |
| **Performance Glitch User** | `performance_glitch_user` | `secret_sauce` | Latency simulation and wait handling |
| **Error User** | `error_user` | `secret_sauce` | Checkout failure edge cases |
| **Visual User** | `visual_user` | `secret_sauce` | UI visual regression testing |

Checkout Customer Test Data:
- First Name: `John`, `QA`, `Tester`
- Last Name: `Doe`, `Automation`, `Candidate`
- Postal / Zip Code: `12345`, `90210`, `M5V2T6`

---

## 8. Entry and Exit Criteria

### 8.1 Entry Criteria
- Application URL is live, reachable, and responsive.
- Test documentation structure is created and test cases are finalized.
- Python 3 and all test dependencies (`selenium`, `pytest`) are successfully installed.
- Chrome browser and WebDriver compatibility verified.

### 8.2 Exit Criteria
- 100% of planned manual test cases documented and categorized.
- 100% of automated test scripts developed, debugged, and executed.
- Zero unexpected test failures in the primary regression suite for `standard_user`.
- All identified bugs or observations documented in `Bug_Report.md`.
- Test execution results compiled into `QA_Test_Report.md` and `Test_Execution_Summary.md`.
- All artifacts committed and pushed to the public GitHub repository.

---

## 9. Risks and Mitigations

| Identified Risk | Impact | Likelihood | Mitigation Strategy |
| :--- | :--- | :--- | :--- |
| **Public Website Latency / Downtime** | High | Low | Implement retry mechanisms and verify connection health prior to test runs. |
| **Dynamic DOM / Selector Changes** | High | Medium | Use robust CSS and ID locators in Page Objects; avoid fragile full XPath expressions. |
| **Asynchronous Rendering Flakiness** | Medium | Medium | Standardize on Selenium `WebDriverWait` with `expected_conditions`; strictly ban arbitrary `time.sleep()`. |
| **Local Machine Driver Mismatch** | High | Low | Rely on Selenium 4 Selenium Manager for automated, seamless driver provisioning. |

---

## 10. Test Deliverables
1. **Master Test Plan** (`test-plan/Test_Plan.md`)
2. **Comprehensive Test Cases** (`test-cases/Test_Cases.csv` - 40+ structured manual test cases)
3. **Automated Test Suite** (`automation/` - PyTest test scripts, fixtures, page models)
4. **Bug & Observational Defect Report** (`bug-reports/Bug_Report.md`)
5. **QA Test Execution Report** (`reports/QA_Test_Report.md`)
6. **Executive Test Execution Summary** (`docs/Test_Execution_Summary.md`)
7. **Production Portfolio Documentation** (`README.md`)
