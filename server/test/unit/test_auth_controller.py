import unittest
from flask import json
from ...src.app import app 
from ...src.service.auth_service import AuthService  

class AuthControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_login(self):
        # Mock data for login
        login_data = {
            "email": "test@example.com",
            "password": "password123"
        }

        # Send a POST request to the login endpoint
        response = self.app.post('/login', json=login_data)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the response contains the expected keys
        data = json.loads(response.get_data(as_text=True))
        self.assertIn("access_token", data)
        self.assertIn("refresh_token", data)

if __name__ == '__main__':
    unittest.main()
