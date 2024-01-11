#!/usr/bin/python3
"""
User Class That inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class that inherits from BaseModel.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new User instance.
        """
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        super().__init__(*args, **kwargs)
