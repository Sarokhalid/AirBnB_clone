#!/usr/bin/python3
"""Test file"""
from models.engine.file_storage import FileStorage
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """ Test cases for the HBNBCommand class"""

    def setUp(self):
        """Set up the test environment before each test case"""
        self.console = HBNBCommand()

    def tearDown(self):
        """tear down the test environment after each case"""
        pass

    def test_help(self):
        """ Test the help Command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help show")
            output = f.getvalue().strip()
            self.assertIn("display the string representation", output)

    def test_create(self):
        """Test The create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertTrue(output)

    def test_show(self):
        """Test the show command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.console.onecmd(f"show BaseModel {obj_id}")
            output = f.getvalue().strip()
            self.assertIn(obj_id, output)

    def test_destroy(self):
        """ Test the destroy command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.console.onecmd(f"destroy BaseMode {obj_id}")
            self.assertEqual(f.getvalue().strip(), "")

    def test_all(self):
        """ Test the all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("all BaseModel")
            output = f.getvalue().strip()
            self.assertIn("BaseModel", output)

    def test_count(self):
        """ Test the count command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create User")
            self.console.onecmd("count BaseModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "2")

    def test_update(self):
        """ Test the update command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.console.onecmd(f"update BaseModel {obj_id} name 'new name'")
            self.console.onecmd(f"shown BaseModel {obj_id}")
            output = f.getvalue().strip()
            self.assertIn("'name': 'new name'", output)


if __name__ == '__main__':
    unittest.main()
