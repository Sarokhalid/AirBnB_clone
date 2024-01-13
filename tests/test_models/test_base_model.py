#!/usr/bin/python3
"""
Test Module for BaseModel
"""
import unittest
from datetime import datetime

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def setUp(self):
        """
        Simple set up method.
        """
        self.base1 = BaseModel()
        self.base2 = BaseModel()

    def tearDown(self):
        """
        Simple tear down method.
        """
        del self.base1
        del self.base2

    def test_init(self):
        """
        Test the __init__ method.
        """
        self.assertTrue(isinstance(self.base1, BaseModel))

    def test_attributes(self):
        """
        Test if BaseModel class contains the attribute id,
        created_at, updated_at.
        """
        self.assertTrue("id" in self.base1.__dict__)
        self.assertTrue("created_at" in self.base1.__dict__)
        self.assertTrue("updated_at" in self.base1.__dict__)

    def test_type_attributes(self):
        """
        Test the type of BaseModel class attributes.
        """
        self.assertEqual(type(self.base1.id), str)
        self.assertEqual(type(self.base1.created_at), datetime)
        self.assertEqual(type(self.base1.updated_at), datetime)

    def test_str(self):
        """
        Test the str method.
        """
        self.assertEqual(
            str(self.base1),
            "[{}] ({}) {}".format(
                                self.base1.__class__.__name__,
                                self.base1.id,
                                self.base1.__dict__
                                ),
            )

    def test_save(self):
        """
        Test the save method.
        """
        old_updated_at = self.base1.updated_at
        self.base1.save()
        self.assertNotEqual(old_updated_at, self.base1.updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method.
        """
        base_dict = self.base1.to_dict()
        self.assertEqual(type(base_dict), dict)
        self.assertEqual(base_dict["__class__"], "BaseModel")
        self.assertEqual(type(base_dict["created_at"]), str)
        self.assertEqual(type(base_dict["updated_at"]), str)
        self.assertEqual(base_dict["id"], self.base1.id)

    def test_unique_id(self):
        """
        Test if each BaseModel instance is assigned a unique id.
        """
        self.assertNotEqual(self.base1.id, self.base2.id)


if __name__ == "__main__":
    unittest.main()
