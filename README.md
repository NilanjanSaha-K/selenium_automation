# Final Project and Assignment Submission - Wipro Python Automation

This repository contains the complete coursework, lab assignments, and the final capstone project for the Wipro Python Automation training program. It demonstrates progression from foundational Python concepts to advanced UI and API automation framework design.

---

## 📂 Repository Structure

The repository is divided into two primary sections: progressive learning **Assignments** and the **Final Capstone Project**[cite: 5].

### 1. Assignments
Contains practical labs and exercises completed throughout the training modules[cite: 5].

*   **`Module 1/`**: Foundational Python programming assignments and Jupyter Notebooks covering core language concepts[cite: 5, 6].
*   **`Module 2/`**: Web UI automation scripts utilizing Selenium WebDriver, including data-driven testing implementations via CSV (`login_data.csv`)[cite: 5, 6].
*   **`Module 3/`** (`Module3_BDD_Lab`): Behavior-Driven Development (BDD) implementation using the Behave framework. Includes feature files, step definitions, and a Page Object Model (POM) architectural design[cite: 5, 6].
*   **`Module 4/`** (`Module4_Robot_Framework`): Keyword-driven automation using the Robot Framework. Contains `.robot` files, custom Python keywords, data-driven tests, and generated execution logs (`log.html`, `report.html`)[cite: 5, 6].

---

### 2. Final Project (API Automation Framework)
The `Project/` directory contains a fully functional, enterprise-grade REST API Automation Framework built from scratch using Python `requests`, Behave BDD, and Allure Reporting[cite: 5, 6].

**Core Framework Files:**
*   **`config/settings.py`**: Centralized configuration hub storing global environment variables, base URLs, and timeout settings[cite: 5, 6].
*   **`core/api_client.py`**: A robust, reusable wrapper for the Python `requests` library. It acts as the engine for all HTTP interactions and automatically logs request/response traffic directly to Allure[cite: 5, 6].

**BDD & Test Execution:**
*   **`features/`**: Contains the business-readable Gherkin test scenarios (e.g., `account_management.feature`, `products.feature`) and the `environment.py` file handling framework setup and teardown hooks[cite: 5, 6].
*   **`features/steps/`**: Python step definitions (`account_steps.py`, `common_steps.py`) that map the English Gherkin steps to executable backend code[cite: 5, 6].
*   **`behave.ini`**: Configuration file that registers the Allure formatter with the Behave test runner[cite: 5, 6].
*   **`requirements.txt`**: Locked dependencies required to run the framework (Behave, Requests, Allure-Behave, Faker)[cite: 5, 6].

**Reporting & Output:**
*   **`allure-results/`**: Directory where Behave generates the raw JSON test data during execution[cite: 5, 6].
*   **`Output/`**: A portfolio directory containing evidence of successful execution[cite: 5, 6]. This includes:
    *   `Allure Report.pdf`: The final compiled test report[cite: 5, 6].
    *   Screenshots documenting passing tests, intentionally failing/broken tests, and terminal execution commands (`Terminal_Output_allure_serve.png`, `Test_case3(Pass).png`, etc.)[cite: 5, 6].
*   **`project_documentation.md`**: In-depth architectural documentation explaining the framework's design pattern and objectives[cite: 5, 6].

---

## 🚀 How to Run the Final Project

**1. Setup the Environment**<br>
Ensure Python 3 is installed. Navigate to the `Project/` directory and install the required dependencies:
```bash
pip install -r requirements.txt
```

**2. Execute the Test Suite**<br>
Run the Behave tests and format the output for Allure:
```bash
behave -f allure_behave.formatter:AllureFormatter -o allure-results ./features
```

**3. Generate the Allure Report**<br>
(Requires the Allure Commandline tool installed on your system)<br>
Serve the generated JSON results to a local HTML dashboard:
```bash
allure serve allure-results
```
