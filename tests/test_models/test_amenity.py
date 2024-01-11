#!/usr/bin/python3
"""
Unittest for Amenity Class
"""


import unittest

from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Defines unit test for the Amenity class.
    """

    def setUp(self):
        """
        Sets up the tests.
        """
        self.amenity = Amenity()

    def test_attributes(self):
        """
        Tests the attributes of the Amenity class.
        """
        self.assertEqual(self.amenity.name, "")

    def test_inheritance(self):
        """
        Tests if Amenity class inherits from BaseModel.
        """
        self.assertIsInstance(self.amenity, Amenity)


if __name__ == "__main__":
    unittest.main()
