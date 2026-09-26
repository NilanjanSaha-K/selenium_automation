from behave import when
import time

@when('I send a POST request to "{endpoint}" with email "{email}" and password "{password}"')
def step_post_login(context, endpoint, email, password):
    """
    Handles authentication. Includes logic to translate the 'BLANK' keyword 
    from the Gherkin feature file into actual empty strings for negative testing.
    """
    if email == "BLANK":
        email = ""
    if password == "BLANK":
        password = ""
        
    payload = {
        "email": email,
        "password": password
    }
    context.response = context.api.post(endpoint, data=payload)

@when('I send a POST request to "{endpoint}" with new user details')
def step_post_create_account(context, endpoint):
    """Creates a new user with a dynamically generated email to prevent duplication errors."""
    
    unique_email = f"qa_test_{int(time.time())}@example.com"
    
    context.test_data['current_email'] = unique_email
    context.test_data['current_password'] = "SecurePass123!"
    
    payload = {
        "name": "Automation Tester",
        "email": context.test_data['current_email'],
        "password": context.test_data['current_password'],
        "title": "Mr",
        "birth_date": "15",
        "birth_month": "August",
        "birth_year": "1995",
        "firstname": "John",
        "lastname": "Doe",
        "company": "QA Solutions Inc",
        "address1": "123 Automation Blvd",
        "country": "United States",
        "zipcode": "90210",
        "state": "California",
        "city": "Los Angeles",
        "mobile_number": "5559876543"
    }
    context.response = context.api.post(endpoint, data=payload)

@when('I send a PUT request to "{endpoint}" to update the user name')
def step_put_update_account(context, endpoint):
    """Updates the user account created in the previous step."""
    
    payload = {
        "email": context.test_data['current_email'],
        "password": context.test_data['current_password'],
        "name": "Updated Automation Tester", 
        "firstname": "John",
        "lastname": "Doe",
        "address1": "123 Automation Blvd",
        "country": "United States",
        "zipcode": "90210",
        "state": "California",
        "city": "Los Angeles",
        "mobile_number": "5559876543"
    }
    context.response = context.api.put(endpoint, data=payload)

@when('I send a DELETE request to "{endpoint}" for the current user')
def step_delete_account(context, endpoint):
    """Cleans up the test data by deleting the user account."""
    
    payload = {
        "email": context.test_data['current_email'],
        "password": context.test_data['current_password']
    }
    context.response = context.api.delete(endpoint, data=payload)