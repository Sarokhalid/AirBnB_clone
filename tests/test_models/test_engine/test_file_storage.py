#!/usr/bin/python3
"""
Module for testing FileStorage Engine
"""

import os
import unittest

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Test cases for the FileStorage class.
    """

    def setUp(self):
        """
        Simple set up method.
        """
        self.storage = FileStorage()

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
        obj = BaseModel()
        self.storage.new(obj)
        key = obj.__class__.__name__ + "." + obj.id
        self.assertTrue(key in self.storage.all())

    def test_save_and_reload(self):
        """
        Test the save and reload methods.
        """
        base_model_instance = BaseModel()
        self.storage.new(base_model_instance)

        self.storage.save()

        pre_reload_state = {
            key: dict(instance.to_dict())
            for key, instance in self.storage.all().items()
        }

        self.storage.reload()

        post_reload_state = {
            key: dict(instance.to_dict())
            for key, instance in self.storage.all().items()
        }

        self.assertEqual(pre_reload_state, post_reload_state)


if __name__ == "__main__":
    unittest.main()
