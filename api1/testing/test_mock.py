from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestAnimal(TestBase):
    def test_dog(self):
        with patch('requests.get') as r:
            r.return_value.text = "Dog"

            response = self.client.get(url_for('get_noise'))
            self.assertIn(b'Woof', response.data)
