#!/usr/bin/python3
"""
Module for testing FileStorage Engine
"""

import os
import unittest

from models import storage
from models.amenity import Amenity  # Import the Amenity class
from models.base_model import BaseModel
from models.city import City  # Import the City class
from models.place import Place  # Import the Place class
from models.review import Review  # Import the Review class
from models.state import State  # Import the State class
from models.user import User


class TestFileStorage(unittest.TestCase):
    """
    Defines unit test for the FileStorage class.
    """

    def setUp(self):
        """
        Sets up the tests.
        """
        self.model1 = BaseModel()
        self.user1 = User()
        self.place1 = Place()  # Create a Place instance
        self.state1 = State()  # Create a State instance
        self.city1 = City()  # Create a City instance
        self.amenity1 = Amenity()  # Create an Amenity instance
        self.review1 = Review()  # Create a Review instance
        self.model1.save()
        self.user1.save()
        self.place1.save()  # Save the Place instance
        self.state1.save()  # Save the State instance
        self.city1.save()  # Save the City instance
        self.amenity1.save()  # Save the Amenity instance
        self.review1.save()  # Save the Review instance

    def tearDown(self):
        """
        Tears down the tests.
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all(self):
        """
        Tests the all method.
        """
        all_objs = storage.all()
        self.assertIsInstance(all_objs, dict)
        self.assertIn("BaseModel." + self.model1.id, all_objs)
        self.assertIn("User." + self.user1.id, all_objs)
        self.assertIn("Place." + self.place1.id, all_objs)  # Test the Place
        self.assertIn("State." + self.state1.id, all_objs)  # Test the State
        self.assertIn("City." + self.city1.id, all_objs)  # Test the City
        self.assertIn(
            "Amenity." + self.amenity1.id, all_objs
        )  # Test the Amenity instance
        self.assertIn("Review." + self.review1.id, all_objs)  # Test the Review

    def test_new(self):
        """
        Tests the new method.
        """
        model2 = BaseModel()
        user2 = User()
        place2 = Place()  # Create another Place instance
        state2 = State()  # Create another State instance
        city2 = City()  # Create another City instance
        amenity2 = Amenity()  # Create another Amenity instance
        review2 = Review()  # Create another Review instance
        storage.new(model2)
        storage.new(user2)
        storage.new(place2)  # Add the Place instance
        storage.new(state2)  # Add the State instance
        storage.new(city2)  # Add the City instance
        storage.new(amenity2)  # Add the Amenity instance
        storage.new(review2)  # Add the Review instance
        self.assertIn("BaseModel." + model2.id, storage.all())
        self.assertIn("User." + user2.id, storage.all())
        self.assertIn("Place." + place2.id, storage.all())  # Test the Place
        self.assertIn("State." + state2.id, storage.all())  # Test the State
        self.assertIn("City." + city2.id, storage.all())  # Test the City
        self.assertIn(
            "Amenity." + amenity2.id, storage.all()
        )  # Test the Amenity instance
        self.assertIn("Review." + review2.id, storage.all())  # Test the Review

    def test_save(self):
        """
        Tests the save method.
        """
        model2 = BaseModel()
        user2 = User()
        place2 = Place()  # Create another Place instance
        state2 = State()  # Create another State instance
        city2 = City()  # Create another City instance
        amenity2 = Amenity()  # Create another Amenity instance
        review2 = Review()  # Create another Review instance
        model2.save()
        user2.save()
        place2.save()  # Save the Place instance
        state2.save()  # Save the State instance
        city2.save()  # Save the City instance
        amenity2.save()  # Save the Amenity instance
        review2.save()  # Save the Review instance
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        """
        Tests the reload method.
        """
        all_objs = storage.all()
        storage.reload()
        self.assertDictEqual(storage.all(), all_objs)


if __name__ == "__main__":
    unittest.main()
