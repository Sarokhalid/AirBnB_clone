#!/usr/bin/python3
"""
Module for testing FileStorage Engine
"""
import os
import unittest

from models import storage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    Defines unit test for the FileStorage class.
    """

    def setUp(self):
        """
        Sets up the tests.
        """
        self.model1 = BaseModel()
        self.model1.save()

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

    def test_new(self):
        """
        Tests the new method.
        """
        model2 = BaseModel()
        storage.new(model2)
        self.assertIn("BaseModel." + model2.id, storage.all())

    def test_save(self):
        """
        Tests the save method.
        """
        model2 = BaseModel()
        model2.save()
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
