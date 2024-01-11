#!/usr/bin/python3
"""
Unittest for City Calss
"""

import unittest

from models.city import City


class TestCity(unittest.TestCase):
    """
    Defines unit test for the City class.
    """

    def setUp(self):
        """
        Sets up the tests.
        """
        self.city = City()

    def test_attributes(self):
        """
        Tests the attributes of the City class.
        """
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_inheritance(self):
        """
        Tests if City class inherits from BaseModel.
        """
        self.assertIsInstance(self.city, City)


if __name__ == "__main__":
    unittest.main()
