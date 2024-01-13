#!/usr/bin/python3
"""
This module contains the BaseModel class which
serves as the base for all other classes in The
AirBnB Project.
"""

import uuid
from datetime import datetime

import models


class BaseModel:
    """
    BaseModel defines all common attributes/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new BaseModel instance.
        Args:
            *args (any): Not Used.
            **kwargs (dict): Key/Value Pairs of Attributes.
        """
        time_form = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key in ("created_at", "updated_at"):
                    self.__dict__[key] = datetime.strptime(value, time_form)
                elif key != "__class__":
                    self.__dict__[key] = value
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """
        Update the updated_at attribute with the
        current datetime and save the instance.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return a dictionary containing all
        keys/values of the instance's __dict__.
        """
        instance_attributes = self.__dict__.copy()

        instance_attributes["created_at"] = self.created_at.isoformat()
        instance_attributes["updated_at"] = self.updated_at.isoformat()

        instance_attributes["__class__"] = self.__class__.__name__

        return instance_attributes

    def __str__(self):
        """
        Return a string representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(
                                    self.__class__.__name__,
                                    self.id,
                                    self.__dict__
                                    )
