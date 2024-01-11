#!/usr/bin/python3
"""
Unittest for Review Class
"""

import unittest
from datetime import datetime

from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Test cases for the Review class.
    """

    def setUp(self):
        """
        Simple set up method.
        """
        self.review1 = Review()
        self.review2 = Review()

    def tearDown(self):
        """
        Simple tear down method.
        """
        del self.review1
        del self.review2

    def test_inheritance(self):
        """
        Test if Review class inherits from BaseModel.
        """
        self.assertIsInstance(self.review1, BaseModel)

    def test_attributes(self):
        """
        Test if Review class contains the attribute place_id, user_id, text.
        """
        self.assertTrue("place_id" in self.review1.__dict__)
        self.assertTrue("user_id" in self.review1.__dict__)
        self.assertTrue("text" in self.review1.__dict__)

    def test_type_attributes(self):
        """
        Test the type of Review class attributes.
        """
        self.assertEqual(type(self.review1.place_id), str)
        self.assertEqual(type(self.review1.user_id), str)
        self.assertEqual(type(self.review1.text), str)

    def test_str(self):
        """
        Test the str method.
        """
        self.assertEqual(
            str(self.review1),
            "[{}] ({}) {}".format(
                self.review1.__class__.__name__,
                self.review1.id,
                self.review1.__dict__
            ),
        )

    def test_save(self):
        """
        Test the save method.
        """
        old_updated_at = self.review1.updated_at
        self.review1.save()
        self.assertNotEqual(old_updated_at, self.review1.updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method.
        """
        review_dict = self.review1.to_dict()
        self.assertEqual(review_dict["__class__"], "Review")
        self.assertEqual(type(review_dict["created_at"]), str)
        self.assertEqual(type(review_dict["updated_at"]), str)


if __name__ == "__main__":
    unittest.main()
