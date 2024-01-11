#!/usr/bin/python3
"""
Unittest for Amenity Class
"""

import unittest
from datetime import datetime

from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """
    Test cases for the Amenity class.
    """

    def setUp(self):
        """
        Simple set up method.
        """
        self.amenity1 = Amenity()
        self.amenity2 = Amenity()

    def tearDown(self):
        """
        Simple tear down method.
        """
        del self.amenity1
        del self.amenity2

    def test_inheritance(self):
        """
        Test if Amenity class inherits from BaseModel.
        """
        self.assertIsInstance(self.amenity1, BaseModel)

    def test_attributes(self):
        """
        Test if Amenity class contains the attribute name.
        """
        self.assertTrue("name" in self.amenity1.__dict__)

    def test_type_attributes(self):
        """
        Test the type of Amenity class attributes.
        """
        self.assertEqual(type(self.amenity1.name), str)

    def test_str(self):
        """
        Test the str method.
        """
        self.assertEqual(
            str(self.amenity1),
            "[{}] ({}) {}".format(
                self.amenity1.__class__.__name__,
                self.amenity1.id,
                self.amenity1.__dict__,
            ),
        )

    def test_save(self):
        """
        Test the save method.
        """
        old_updated_at = self.amenity1.updated_at
        self.amenity1.save()
        self.assertNotEqual(old_updated_at, self.amenity1.updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method.
        """
        amenity_dict = self.amenity1.to_dict()
        self.assertEqual(amenity_dict["__class__"], "Amenity")
        self.assertEqual(type(amenity_dict["created_at"]), str)
        self.assertEqual(type(amenity_dict["updated_at"]), str)


if __name__ == "__main__":
    unittest.main()
