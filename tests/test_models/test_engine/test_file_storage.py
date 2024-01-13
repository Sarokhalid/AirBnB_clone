#!/usr/bin/python3
"""
Module for testing FileStorage Engine
"""

import os
import unittest

from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class TestFileStorage(unittest.TestCase):
    """
    Test cases for the FileStorage class.
    """

    def setUp(self):
        """
        Simple set up method.
        """
        self.storage = storage

    def tearDown(self):
        """
        Simple tear down method.
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all(self):
        """
        Test the all method.
        """
        self.assertEqual(type(self.storage.all()), dict)

    def test_new(self):
        """
        Test the new method.
        """
        for class_name in [
                            BaseModel,
                            User, State,
                            City,
                            Amenity,
                            Place,
                            Review
                            ]:
            instance = class_name()
            self.storage.new(instance)
            key = instance.__class__.__name__ + "." + instance.id
            self.assertTrue(key in self.storage.all())

    def test_save_and_reload(self):
        """
        Test the save and reload methods.
        """
        for class_name in [
                            BaseModel,
                            User,
                            State,
                            City,
                            Amenity,
                            Place,
                            Review
                            ]:
            instance = class_name()
            self.storage.new(instance)
            self.storage.save()
            self.storage.reload()
            key = instance.__class__.__name__ + "." + instance.id
            self.assertTrue(key in self.storage.all())


if __name__ == "__main__":
    unittest.main()
