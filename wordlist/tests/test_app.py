import unittest
from flask import  Flask
from wordlist.app import create_app


class AppTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.app = create_app()
        self.client = self.app.test_client()

    def test_app(self):
        self.assertIsInstance(self.app, Flask)

    def test_status_code_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_status_not_found(self):
        response = self.client.get('/dinheiro')
        self.assertEqual(response.status_code, 404)
