import unittest
from app import app  # Assuming your flask file is named app.py

class FlaskTest(unittest.TestCase):

    def setUp(self):
        # Creates a test client to simulate requests
        self.client = app.test_client()
        self.client.testing = True

    def test_health_endpoint(self):
        """Test that the /health endpoint returns 200 and the correct text."""
        response = self.client.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Server is up and running')

    def test_index_endpoint(self):
        """Test that the root endpoint returns 200."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
