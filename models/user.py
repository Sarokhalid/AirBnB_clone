#!/usr/bin/python3
"""
User Class That inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class that inherits from BaseModel.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize a new User instance.
        """
        super().__init__(*args, **kwargs)
