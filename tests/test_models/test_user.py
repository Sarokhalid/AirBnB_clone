#!/usr/bin/python3
"""
Unittest for User Class
"""
import unittest
from datetime import datetime

from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """
    Test cases for the User class.
    """

    def setUp(self):
        """
        Simple set up method.
        """
        self.user1 = User()
        self.user2 = User()

    def tearDown(self):
        """
        Simple tear down method.
        """
        del self.user1
        del self.user2

    def test_inheritance(self):
        """
        Test if User class inherits from BaseModel.
        """
        self.assertIsInstance(self.user1, BaseModel)

    def test_attributes(self):
        """
        Test if User class contains the attribute email,
        password, first_name, last_name.
        """
        self.assertTrue("email" in self.user1.__dict__)
        self.assertTrue("password" in self.user1.__dict__)
        self.assertTrue("first_name" in self.user1.__dict__)
        self.assertTrue("last_name" in self.user1.__dict__)

    def test_type_attributes(self):
        """
        Test the type of User class attributes.
        """
        self.assertEqual(type(self.user1.email), str)
        self.assertEqual(type(self.user1.password), str)
        self.assertEqual(type(self.user1.first_name), str)
        self.assertEqual(type(self.user1.last_name), str)

    def test_str(self):
        """
        Test the str method.
        """
        self.assertEqual(
            str(self.user1),
            "[{}] ({}) {}".format(
                self.user1.__class__.__name__,
                self.user1.id,
                self.user1.__dict__
            ),
        )

    def test_save(self):
        """
        Test the save method.
        """
        old_updated_at = self.user1.updated_at
        self.user1.save()
        self.assertNotEqual(old_updated_at, self.user1.updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method.
        """
        user_dict = self.user1.to_dict()
        self.assertEqual(user_dict["__class__"], "User")
        self.assertEqual(type(user_dict["created_at"]), str)
        self.assertEqual(type(user_dict["updated_at"]), str)


if __name__ == "__main__":
    unittest.main()
