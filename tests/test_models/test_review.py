#!/usr/bin/python3
"""
Unittest for Review Class
"""
import unittest

from models.review import Review


class TestReview(unittest.TestCase):
    """
    Defines unit test for the Review class.
    """

    def setUp(self):
        """
        Sets up the tests.
        """
        self.review = Review()

    def test_attributes(self):
        """
        Tests the attributes of the Review class.
        """
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_inheritance(self):
        """
        Tests if Review class inherits from BaseModel.
        """
        self.assertIsInstance(self.review, Review)


if __name__ == "__main__":
    unittest.main()
