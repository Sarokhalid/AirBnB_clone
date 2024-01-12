#!/usr/bin/python3
"""
Unittest for City Calss
"""

import unittest
from datetime import datetime

from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """
    Test cases for the City class.
    """

    def setUp(self):
        """
        Simple set up method.
        """
        self.city1 = City()
        self.city2 = City()

    def tearDown(self):
        """
        Simple tear down method.
        """
        del self.city1
        del self.city2

    def test_inheritance(self):
        """
        Test if City class inherits from BaseModel.
        """
        self.assertIsInstance(self.city1, BaseModel)

    def test_attributes(self):
        """
        Test if City class contains the attribute state_id and name.
        """
        self.assertTrue("state_id" in self.city1.__dict__)
        self.assertTrue("name" in self.city1.__dict__)

    def test_type_attributes(self):
        """
        Test the type of City class attributes.
        """
        self.assertEqual(type(self.city1.state_id), str)
        self.assertEqual(type(self.city1.name), str)

    def test_str(self):
        """
        Test the str method.
        """
        self.assertEqual(
            str(self.city1),
            "[{}] ({}) {}".format(
                self.city1.__class__.__name__,
                self.city1.id,
                self.city1.__dict__
            ),
        )

    def test_save(self):
        """
        Test the save method.
        """
        old_updated_at = self.city1.updated_at
        self.city1.save()
        self.assertNotEqual(old_updated_at, self.city1.updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method.
        """
        city_dict = self.city1.to_dict()
        self.assertEqual(city_dict["__class__"], "City")
        self.assertEqual(type(city_dict["created_at"]), str)
        self.assertEqual(type(city_dict["updated_at"]), str)


if __name__ == "__main__":
    unittest.main()
