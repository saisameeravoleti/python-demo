import unittest

from src.packageName.HelloUser import main

class TestWelcome(unittest.TestCase):
    def test_welcome(self):
        self.assertEqual(main(), "Hello User")