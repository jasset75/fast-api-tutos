import unittest
import pytest
from tuto_02.main import app

from fastapi.testclient import TestClient

class TestMain(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)


    def test_welcome(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        expected_json = {"welcome": "To have here or take away?. Don't forget the cutlery!"}

        self.assertEqual(response.json(), expected_json)