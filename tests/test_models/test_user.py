#!/usr/bin/python3
"""
Unittest for User Class
"""
import unittest

from models.user import User


class TestUser(unittest.TestCase):
    """
    Defines unit test for the User class.
    """

    def setUp(self):
        """
        Sets up the tests.
        """
        self.user1 = User()
        self.user1.email = "test@example.com"
        self.user1.password = "password"
        self.user1.first_name = "First"
        self.user1.last_name = "Last"

    def test_attributes(self):
        """
        Tests the attributes of the User class.
        """
        self.assertEqual(self.user1.email, "test@example.com")
        self.assertEqual(self.user1.password, "password")
        self.assertEqual(self.user1.first_name, "First")
        self.assertEqual(self.user1.last_name, "Last")

    def test_inheritance(self):
        """
        Tests if User class inherits from BaseModel.
        """
        self.assertIsInstance(self.user1, User)


if __name__ == "__main__":
    unittest.main()
