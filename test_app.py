import unittest
from app import app
import werkzeug

if not hasattr(werkzeug, '__version__'): 
    werkzeug.__version__ = "mock-version"

class APITestCase(unittest.TestCase): 
    @classmethod 
    def setUpClass(cls):  
        cls.client = app.test_client()
    
    def test_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_itens(self):
        response = self.client.get('/items')
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.client.post('/login')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.is_json)

if __name__ == '__main__':
    unittest.main()
