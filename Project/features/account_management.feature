Feature: Account Management and Authentication API

  Background:
    Given the API is accessible

  Scenario Outline: Verify Login with various credential combinations
    When I send a POST request to "/verifyLogin" with email "<email>" and password "<password>"
    Then the API response code should be <expected_code>
    And the response message should be "<expected_message>"

    Examples:
      | email                   | password | expected_code | expected_message      |
      | validuser@example.com   | pass123  | 200           | User exists!          |
      | validuser@example.com   | wrongpwd | 404           | User not found!       |
      | unknown@example.com     | pass123  | 404           | User not found!       |
      |                         |          | 400           | Bad request, email or password parameter is missing in POST request. |

  Scenario: Create, Update, and Delete an Account (E2E CRUD)
    When I send a POST request to "/createAccount" with new user details
    Then the API response code should be 201
    And the response message should be "User created!"
    
    When I send a PUT request to "/updateAccount" to update the user name
    Then the API response code should be 200
    And the response message should be "User updated!"

    When I send a DELETE request to "/deleteAccount" for the current user
    Then the API response code should be 200
    And the response message should be "Account deleted!"