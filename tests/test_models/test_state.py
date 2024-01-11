#!/usr/bin/python3
"""
Unittest For State Class
"""

import unittest

from models.state import State


class TestState(unittest.TestCase):
    """
    Defines unit test for the State class.
    """

    def setUp(self):
        """
        Sets up the tests.
        """
        self.state = State()

    def test_attributes(self):
        """
        Tests the attributes of the State class.
        """
        self.assertEqual(self.state.name, "")

    def test_inheritance(self):
        """
        Tests if State class inherits from BaseModel.
        """
        self.assertIsInstance(self.state, State)


if __name__ == "__main__":
    unittest.main()
