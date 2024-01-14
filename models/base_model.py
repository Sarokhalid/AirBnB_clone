#!/usr/bin/python3
"""
This module defines the BaseModel class,
which serves as the foundation for all other classes
in the AirBnB clone project.
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    The BaseModel class is a superclass that defines common
    attributes and methods for other classes.

    Attributes:
        id (str): A unique identifier for each instance, generated using uuid.
        created_at (datetime): The time the instance was created.
        updated_at (datetime): The time the instance was last updated.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel instance. If kwargs are provided,
        it sets the instance attributes to the values provided.
        Otherwise, it generates a unique id and sets the created_at and
        updated_at attributes to the current datetime.

        Args:
            *args: Variable length argument list. Not used in this method.
            **kwargs (dict): Key-value pairs of instance attributes.

        Raises:
            ValueError: If the value associated with the 'created_at' or
            'updated_at' key is not in the correct format.
        """
        from models import storage

        time_form = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key in ("created_at", "updated_at"):
                    self.__dict__[key] = datetime.strptime(value, time_form)
                elif key != "__class__":
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """
        Updates the 'updated_at' attribute to the current datetime
        and saves the instance to the storage.
        """
        from models import storage

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of the
        instance's __dict__, including the class name.

        Returns:
            dict: A dictionary representation of the instance.
        """
        instance_attributes = self.__dict__.copy()

        for key, value in instance_attributes.items():
            if isinstance(value, datetime):
                instance_attributes[key] = value.isoformat()

        instance_attributes["__class__"] = self.__class__.__name__

        return instance_attributes

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance,
        including the class name, id, and dictionary of attributes.

        Returns:
            str: A string representation of the instance.
        """
        return "[{}] ({}) {}".format(
                                    self.__class__.__name__,
                                    self.id,
                                    self.__dict__
                                    )
