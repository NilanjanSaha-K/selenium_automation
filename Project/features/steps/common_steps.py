from behave import given, when, then
import json

@given('the API is accessible')
def step_api_accessible(context):
    #this case is already being handled from environemnt.py.
    pass

@when('I send a GET request to "{endpoint}"')
def step_send_get_request(context, endpoint):
    """Handles all generic GET requests."""
    context.response = context.api.get(endpoint)

@then('the HTTP status code should be {status_code:d}')
def step_check_http_status(context, status_code):
    """Checks the actual network-level HTTP status code."""
    assert context.response.status_code == status_code, \
        f"Expected HTTP {status_code}, got {context.response.status_code}"

@then('the API response code should be {expected_code:d}')
def step_check_api_response_code(context, expected_code):
    """
    Checks the embedded JSON 'responseCode' specific to the Automation Exercise API.
    Automation Exercise often returns an HTTP 200 status, but puts the actual 
    business logic code (400, 404, 201) inside the JSON payload.
    """
    try:
        response_data = context.response.json()
    except ValueError:
        raise AssertionError(f"Expected JSON response, but got text: {context.response.text}")
        
    actual_code = response_data.get("responseCode")
    assert actual_code == expected_code, \
        f"Expected API code {expected_code}, got {actual_code}"

@then('the response message should be "{expected_message}"')
def step_check_message(context, expected_message):
    """Validates the specific success or error message returned by the API."""
    response_data = context.response.json()
    actual_message = response_data.get("message")
    assert actual_message == expected_message, \
        f"Expected message '{expected_message}', got '{actual_message}'"

@then('the response should contain a list of products')
def step_check_product_list(context):
    """Validates the schema of the productsList endpoint response."""
    response_data = context.response.json()
    
    assert "products" in response_data, "Response JSON does not contain a 'products' key."
    assert isinstance(response_data["products"], list), "'products' is not a list structure."
    assert len(response_data["products"]) > 0, "The product list is empty."