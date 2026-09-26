import requests
import allure
import json

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def _log_to_allure(self, method, endpoint, payload, response):
        """Automatically attaches API traffic to Allure reports."""
        allure.attach(f"{method} {self.base_url}{endpoint}", name="Request URL", attachment_type=allure.attachment_type.TEXT)
        if payload:
            allure.attach(json.dumps(payload, indent=2), name="Request Payload", attachment_type=allure.attachment_type.JSON)
        allure.attach(str(response.status_code), name="Response Status Code", attachment_type=allure.attachment_type.TEXT)
        try:
            allure.attach(json.dumps(response.json(), indent=2), name="Response Body", attachment_type=allure.attachment_type.JSON)
        except ValueError:
            allure.attach(response.text, name="Response Body (Text)", attachment_type=allure.attachment_type.TEXT)

    def get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        response = self.session.get(url, params=params)
        self._log_to_allure("GET", endpoint, params, response)
        return response

    def post(self, endpoint, data=None):
        url = f"{self.base_url}{endpoint}"
        # Automation Exercise expects application/x-www-form-urlencoded
        response = self.session.post(url, data=data) 
        self._log_to_allure("POST", endpoint, data, response)
        return response

    def put(self, endpoint, data=None):
        url = f"{self.base_url}{endpoint}"
        response = self.session.put(url, data=data)
        self._log_to_allure("PUT", endpoint, data, response)
        return response

    def delete(self, endpoint, data=None):
        url = f"{self.base_url}{endpoint}"
        response = self.session.delete(url, data=data)
        self._log_to_allure("DELETE", endpoint, data, response)
        return response