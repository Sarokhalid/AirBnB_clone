#!/usr/bin/python3
"""
This module contains the FileStorage class which serializes
instances to a JSON file and deserializes JSON file to instances.
"""

import json

from models.base_model import BaseModel


class FileStorage:
    """
    FileStorage class for handling the serialization
    and deserialization of instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the instance with key <instance class name>.id.
        """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        with open(self.__file_path, "w", encoding="utf-8") as json_file:
            obj_dict = {
                key: instance.to_dict() for key, instance in self.__objects.items()
            }
            json.dump(obj_dict, json_file, indent=2)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists; otherwise, do nothing).
        """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as json_file:
                instance_data = json.load(json_file)
            for instance in instance_data.values():
                cls_name = instance["__class__"]
                del instance["__class__"]
                cls = globals()[cls_name]
                self.new(cls(**instance))
        except FileNotFoundError:
            pass
