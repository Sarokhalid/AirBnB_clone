#!/usr/bin/python3
"""
Unittest for Place Class
"""
import unittest

from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Defines unit test for the Place class.
    """

    def setUp(self):
        """
        Sets up the tests.
        """
        self.place = Place()

    def test_attributes(self):
        """
        Tests the attributes of the Place class.
        """
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_inheritance(self):
        """
        Tests if Place class inherits from BaseModel.
        """
        self.assertIsInstance(self.place, Place)


if __name__ == "__main__":
    unittest.main()
