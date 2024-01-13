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
        self.assertTrue(hasattr(Place, "city_id"))
        self.assertTrue(hasattr(Place, "user_id"))
        self.assertTrue(hasattr(Place, "name"))
        self.assertTrue(hasattr(Place, "description"))
        self.assertTrue(hasattr(Place, "number_rooms"))
        self.assertTrue(hasattr(Place, "number_bathrooms"))
        self.assertTrue(hasattr(Place, "max_guest"))
        self.assertTrue(hasattr(Place, "price_by_night"))
        self.assertTrue(hasattr(Place, "latitude"))
        self.assertTrue(hasattr(Place, "longitude"))
        self.assertTrue(hasattr(Place, "amenity_ids"))

    def test_attribute_initialization(self):
        """
        Test if the attributes are initialized with the correct values.
        """
        self.assertEqual(self.place1.city_id, "")
        self.assertEqual(self.place1.user_id, "")
        self.assertEqual(self.place1.name, "")
        self.assertEqual(self.place1.description, "")
        self.assertEqual(self.place1.number_rooms, 0)
        self.assertEqual(self.place1.number_bathrooms, 0)
        self.assertEqual(self.place1.max_guest, 0)
        self.assertEqual(self.place1.price_by_night, 0)
        self.assertEqual(self.place1.latitude, 0.0)
        self.assertEqual(self.place1.longitude, 0.0)
        self.assertEqual(self.place1.amenity_ids, [])

    def test_attribute_assignment(self):
        """
        Test if the attributes can be assigned values.
        """
        self.place1.city_id = "1234"
        self.place1.user_id = "5678"
        self.place1.name = "Test Place"
        self.place1.description = "A beautiful place."
        self.place1.number_rooms = 3
        self.place1.number_bathrooms = 2
        self.place1.max_guest = 4
        self.place1.price_by_night = 100
        self.place1.latitude = 12.34
        self.place1.longitude = 56.78
        self.place1.amenity_ids = ["9", "10"]
        self.assertEqual(self.place1.city_id, "1234")
        self.assertEqual(self.place1.user_id, "5678")
        self.assertEqual(self.place1.name, "Test Place")
        self.assertEqual(self.place1.description, "A beautiful place.")
        self.assertEqual(self.place1.number_rooms, 3)
        self.assertEqual(self.place1.number_bathrooms, 2)
        self.assertEqual(self.place1.max_guest, 4)
        self.assertEqual(self.place1.price_by_night, 100)
        self.assertEqual(self.place1.latitude, 12.34)
        self.assertEqual(self.place1.longitude, 56.78)
        self.assertEqual(self.place1.amenity_ids, ["9", "10"])

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
        self.assertTrue(isinstance(self.place1.updated_at, datetime))

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
