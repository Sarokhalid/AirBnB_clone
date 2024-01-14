#!/usr/bin/python3
"""
This module defines the FileStorage class, which handles the serialization
and deserialization of instances to and from a JSON file.
"""

import json

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """
    The FileStorage class handles the serialization and
    deserialization of instances.

    Attributes:
        __file_path (str): The path to the JSON file used for storage.
        __objects (dict): A dictionary representing instantiated objects,
        with keys in the format "<class name>.<id>".
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary of instantiated objects.

        Returns:
            dict: The dictionary of instantiated objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new instance to the dictionary of objects.

        Args:
            obj (Class Instance): The instance to be added to the dictionary.
        """
        if not obj:
            return
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes the dictionary of objects to a JSON file.
        """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as json_file:
            obj_dict = {
                key: instance.to_dict()
                for key, instance in FileStorage.__objects.items()
            }
            json.dump(obj_dict, json_file)

    def reload(self):
        """
        Deserializes the JSON file to the dictionary of objects,
        if the JSON file exists.
        """
        try:
            with open(FileStorage.__file_path, "r",
                      encoding="utf-8") as json_file:
                instance_data = json.load(json_file)
            for instance in instance_data.values():
                cls_name = instance["__class__"]
                del instance["__class__"]
                cls = globals()[cls_name]
                self.new(cls(**instance))
        except FileNotFoundError:
            pass
