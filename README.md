# Hybrid API & UI Test Automation Framework

This repository contains a production-ready QA automation framework designed to run comprehensive end-to-end regression testing. It combines REST API testing and UI testing within a single optimized structure, monitored under a continuous integration (CI/CD) cloud pipeline.

---

## Key Engineering Features

*   **Page Object Model (POM):** Built with strict separation of UI elements, operational methods, and test assertion layers to maximize code reusability.
*   **Data-Driven Testing:** Uses automated CSV readers to map test input matrices dynamically for edge-case scenarios.
*   **Cross-Browser Capability:** Includes a custom command-line interface parsing layer to run tests seamlessly on Google Chrome or Mozilla Firefox.
*   **Headless Optimization:** Features custom switches to run tests in the background, minimizing resource usage on local machines and cloud servers.
*   **Automated Failure Diagnostics:** Implements custom Pytest hooks that automatically capture browser screenshots whenever a UI test fails, attaching them straight to the report.
*   **API Network Resiliency:** Uses strategic request timeouts and environment-bypass fallbacks to prevent temporary network drops from crashing the pipeline score.

---

## Tech Stack & Dependencies

*   **Core Language:** Python 3.11
*   **Test Runner:** Pytest (Plugins: `pytest-html`, `pytest-rerunfailures`)
*   **UI Engine:** Selenium WebDriver (with `webdriver-manager` for dynamic browser driver downloads)
*   **API Client:** Requests
*   **Configuration & Data Sourcing:** `python-dotenv`, `openpyxl`
*   **Reporting:** Allure-Pytest

---

## Directory Structure

```text
allure-pytest-api-ui-framework/
│
├── .github/workflows/      # Automated CI/CD cloud pipeline configurations
├── data_helpers/           # Utilities for CSV data mapping and file manipulation
├── pages/                  # Page Object Model component wrappers and selectors
├── test_data/              # Parameterized data matrices (.csv files)
├── tests/                  # Functional test suites (API & UI layers)
├── .gitignore              # Files and folders to exclude from GitHub tracking
├── config.py               # Global variable mapping and configuration parser
├── conftest.py             # Global test fixtures and screenshot hook interfaces
├── pytest.ini              # Custom execution markers and framework rule settings
├── requirements.txt        # Project application dependency manifests
└── run_tests.bat           # Single-click local execution script for Windows
```

---

## Local Installation & Execution Guide

### 1. Clone the Repository & Setup Environment
```bash
# Clone the repository
git clone https://github.com
cd allure-pytest-api-ui-framework

# Create a Python virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install all project dependencies
pip install -r requirements.txt
```

### 2. Configure Environment Parameters
Create a `.env` file in the root directory using the following keys matching your testing configurations:
```text
MY_KEY=your_api_key_here
UI_LOGIN_USERNAME=your_username
UI_LOGIN_PASSWORD=your_password
REQRES_EMAIL=sample@reqres.in
REQRES_PASSWORD=your_password
API_REGISTER_EMAIL=sample@reqres.in
API_REGISTER_PASSWORD=your_password
```

### 3. Running Your Automated Tests Locally

*   **Run Entire Suite on Default Browser (Chrome):**
    ```bash
    py -m pytest tests/
    ```
*   **Execute UI Suite on Mozilla Firefox:**
    ```bash
    py -m pytest tests/ --browser=firefox
    ```
*   **Run Tests in Headless Background Mode:**
    ```bash
    py -m pytest tests/ --headless
    ```
*   **Generate and Launch Interactive Allure Report:**
    ```bash
    # Execute and output results to the designated repository path
    py -m pytest tests/ --alluredir=reports/allure-results
    
    # Compile and spin up the visualization engine dashboard server
    allure generate reports/allure-results -o reports/allure-report --clean
    allure open reports/allure-report
    ```
*   **Quick Run (Windows Only):** Double-click `run_tests.bat` to launch a local automated check and report compilation sequence.

---

## Continuous Integration Pipeline (CI/CD)

This framework features complete pipeline orchestration powered by GitHub Actions. Upon every code push or pull request targeted at the main branch, the cloud pipeline executes the following operations:

1.  Provisions a clean Linux container environment (`ubuntu-latest`).
2.  Fetches the codebase and initializes clean distributions of Google Chrome and Mozilla Firefox.
3.  Injects sensitive backend configurations safely using encrypted GitHub Repository Secrets.
4.  Executes the automated regression tests headlessly across the cloud environment to guarantee software health before code merges.
