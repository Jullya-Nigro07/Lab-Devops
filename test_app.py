import unittest
from app import app
import werkzeug

if not hasattr(werkzeug, '__version__'): 
    werkzeug.__version__ = "mock-version"

class APITestCase(unittest.TestCase): 
    @classmethod 
    def setUpClass(cls): 
        # Criação do cliente de teste 
        cls.client = app.test_client()

    def test_get_items(self):
        response = self.client.get('/items')
        self.assertEqual(response.status_code, 200)
        self.assertIn("items", response.json)
        self.assertEqual(len(response.json["items"]), 3)

    def test_swagger_route_exists(self):
        response = self.client.get('/swagger/')
        self.assertNotEqual(response.status_code, 404)

    def test_home(self): 
        response = self.client.get('/') 
        self.assertEqual(response.status_code, 405)


if __name__ == '__main__':
    unittest.main()
