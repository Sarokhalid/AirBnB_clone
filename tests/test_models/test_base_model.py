#!/usr/bin/python3
"""
Tst Module for BaseModel
"""
import unittest
from datetime import datetime

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Defines unit test for the BaseModel class.
    """

    def setUp(self):
        """
        Sets up the tests.
        """
        self.model1 = BaseModel()
        self.model2 = BaseModel(name="My_First_Model", my_number=89)

    def tearDown(self):
        """
        Tears down the tests.
        """
        pass

    def test_init(self):
        """
        Tests for correct initialization.
        """
        self.assertTrue(isinstance(self.model1, BaseModel))
        self.assertTrue(isinstance(self.model2, BaseModel))
        self.assertEqual(self.model2.name, "My_First_Model")
        self.assertEqual(self.model2.my_number, 89)

        # Test that the created_at and updated_at are datetime objects
        self.assertIsInstance(self.model1.created_at, datetime)
        self.assertIsInstance(self.model1.updated_at, datetime)

    def test_to_dict(self):
        """
        Tests the to_dict method.
        """
        model1_dict = self.model1.to_dict()
        self.assertEqual(model1_dict["__class__"], "BaseModel")
        self.assertEqual(type(model1_dict["created_at"]), str)
        self.assertEqual(type(model1_dict["updated_at"]), str)

        # Test that the to_dict method includes all attributes
        self.assertIn("id", model1_dict)
        self.assertIn("created_at", model1_dict)
        self.assertIn("updated_at", model1_dict)

    def test_str(self):
        """
        Tests the __str__ method.
        """
        model1_str = str(self.model1)
        self.assertEqual(
            model1_str,
            "[BaseModel] ({}) {}".format(self.model1.id, self.model1.__dict__),
        )

    def test_save(self):
        """
        Tests the save method.
        """
        old_updated_at = self.model1.updated_at
        self.model1.save()
        self.assertNotEqual(self.model1.updated_at, old_updated_at)


if __name__ == "__main__":
    unittest.main()
