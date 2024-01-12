#!/usr/bin/python3
"""
Unittest for Place Class
"""

import unittest
from datetime import datetime

from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Test cases for the Place class.
    """

    def setUp(self):
        """
        Simple set up method.
        """
        self.place1 = Place()
        self.place2 = Place()

    def tearDown(self):
        """
        Simple tear down method.
        """
        del self.place1
        del self.place2

    def test_inheritance(self):
        """
        Test if Place class inherits from BaseModel.
        """
        self.assertIsInstance(self.place1, BaseModel)

    def test_attributes(self):
        """
        Test if Place class contains the attribute city_id, user_id, name,
        description, number_rooms, number_bathrooms, max_guest, price_by_night,
        latitude, longitude, amenity_ids.
        """
        self.assertTrue("city_id" in self.place1.__dict__)
        self.assertTrue("user_id" in self.place1.__dict__)
        self.assertTrue("name" in self.place1.__dict__)
        self.assertTrue("description" in self.place1.__dict__)
        self.assertTrue("number_rooms" in self.place1.__dict__)
        self.assertTrue("number_bathrooms" in self.place1.__dict__)
        self.assertTrue("max_guest" in self.place1.__dict__)
        self.assertTrue("price_by_night" in self.place1.__dict__)
        self.assertTrue("latitude" in self.place1.__dict__)
        self.assertTrue("longitude" in self.place1.__dict__)
        self.assertTrue("amenity_ids" in self.place1.__dict__)

    def test_type_attributes(self):
        """
        Test the type of Place class attributes.
        """
        self.assertEqual(type(self.place1.city_id), str)
        self.assertEqual(type(self.place1.user_id), str)
        self.assertEqual(type(self.place1.name), str)
        self.assertEqual(type(self.place1.description), str)
        self.assertEqual(type(self.place1.number_rooms), int)
        self.assertEqual(type(self.place1.number_bathrooms), int)
        self.assertEqual(type(self.place1.max_guest), int)
        self.assertEqual(type(self.place1.price_by_night), int)
        self.assertEqual(type(self.place1.latitude), float)
        self.assertEqual(type(self.place1.longitude), float)
        self.assertEqual(type(self.place1.amenity_ids), list)

    def test_str(self):
        """
        Test the str method.
        """
        self.assertEqual(
            str(self.place1),
            "[{}] ({}) {}".format(
                self.place1.__class__.__name__,
                self.place1.id,
                self.place1.__dict__
            ),
        )

    def test_save(self):
        """
        Test the save method.
        """
        old_updated_at = self.place1.updated_at
        self.place1.save()
        self.assertNotEqual(old_updated_at, self.place1.updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method.
        """
        place_dict = self.place1.to_dict()
        self.assertEqual(place_dict["__class__"], "Place")
        self.assertEqual(type(place_dict["created_at"]), str)
        self.assertEqual(type(place_dict["updated_at"]), str)


if __name__ == "__main__":
    unittest.main()
