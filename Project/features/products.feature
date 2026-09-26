Feature: Product Catalog API

  Scenario: Retrieve all products successfully
    Given the API is accessible
    When I send a GET request to "/productsList"
    Then the HTTP status code should be 200
    And the response should contain a list of products