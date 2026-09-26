# API Automation Framework Capstone

**Objective:** To build a complete API Automation Framework using Behavior-Driven Development (BDD) principles, designed to be highly reusable, scalable, and ready for integration into cloud-based CI/CD pipelines.

**Technologies used:**
*   **Python 3:** Core programming language.
*   **Python Requests Library:** HTTP client engine for API interactions.
*   **Behave:** Python BDD framework for mapping Gherkin syntax to executable code.
*   **Allure Reporting:** Advanced framework for generating graphical execution and traffic reports.
*   **Faker:** Library for generating dynamic, unique test data during runtime.
*   **Pytest:** Supporting testing utility library.

**API Used:** [Automation Exercise API](https://automationexercise.com/api_list)

---

## Folder Structure

```text
Project/
├── config/
│   └── settings.py
├── core/
│   └── api_client.py
├── features/
│   ├── steps/
│   │   ├── common_steps.py
│   │   └── account_steps.py
│   ├── account_management.feature
│   ├── products.feature
│   └── environment.py
├── requirements.txt
└── behave.ini
```

---

## File Descriptions

*   **`config/settings.py`**
    Serves as the central configuration hub. It stores global environment variables, such as the `BASE_URL` and timeout limits, ensuring no hardcoded URLs exist in the test logic.

*   **`core/api_client.py`**
    Contains the `APIClient` class, which operates as the Service Object Model engine. It wraps the standard Python `requests` library to handle HTTP methods (GET, POST, PUT, DELETE), automatically attach headers, manage form-data payloads, and seamlessly log all API traffic (endpoints, payloads, status codes, and responses) directly to Allure.

*   **`features/account_management.feature`**
    A Gherkin file containing the business-level scenarios for the User Management domain. It utilizes `Scenario Outline` for data-driven authentication testing and maps out the end-to-end CRUD (Create, Read, Update, Delete) lifecycle for user accounts.

*   **`features/products.feature`**
    A separate Gherkin domain file covering the Product Catalog endpoints, ensuring tests remain modular and categorized by business function.

*   **`features/steps/common_steps.py`**
    Contains shared Python step definitions that can be utilized across any feature file. This includes reusable assertions for validating HTTP status codes, parsing specific API JSON response codes, and validating response messages.

*   **`features/steps/account_steps.py`**
    Houses domain-specific logic mapped to the `account_management.feature` steps. It handles test data injection, dynamically generates unique user emails to avoid database collisions, and executes the authentication POST payloads.

*   **`features/environment.py`**
    The central framework hooks file for Behave. It executes `before_all` to instantiate the `APIClient` and establish a persistent `requests.Session()` across the test suite, allowing data state (`context.test_data`) to be shared between independent test steps.

*   **`behave.ini`**
    The configuration file for the Behave runner. It registers custom formatters, specifically telling Behave to generate raw test data outputs formatted for the Allure Commandline tool.

*   **`requirements.txt`**
    Locks the exact versions of all dependencies (Behave, Requests, Allure-Behave, Faker) required to build the virtual environment and execute the framework consistently.

---

## Execution Instructions

Follow these steps to set up the environment, run the API test suite, and view the generated graphical reports.

### 1. Prerequisites
Ensure you have the following installed on your system:
*   **Python 3.x** (and `pip`)
*   **Allure Commandline:** Requires Node.js or Java. The easiest installation method on Windows is via NPM:
    ```bash
    npm install -g allure-commandline
    ```

### 2. Environment Setup
Navigate to the root directory of the project (`Project/`) and install all required Python libraries. It is highly recommended to use a virtual environment.

```bash
# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/Scripts/activate  # For Windows

# Install project dependencies
pip install -r requirements.txt
```

### 3. Running the Tests
To execute the BDD scenarios and simultaneously capture the traffic data for Allure reporting, run the following command from the root directory:

```bash
behave -f allure -o allure-results ./features
```
*   `-f allure`: Invokes the Allure formatter defined in `behave.ini`.
*   `-o allure-results`: Directs the raw JSON output files into the `allure-results` folder.
*   `./features`: Points to the directory containing the Gherkin feature files.

### 4. Generating the Report
Once the test execution finishes, generate and view the interactive HTML dashboard by serving the results folder:

```bash
allure serve allure-results
```
This command will compile the JSON data, spin up a local web server, and automatically launch your default browser to display the Allure dashboard. You can click into individual test suites to view the exact API Request/Response logs attached by the `APIClient`.