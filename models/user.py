#!/usr/bin/python3
"""
User Class That inherits from BaseModel
"""
from .base_model import BaseModel


class User(BaseModel):
    """
    User class that inherits from BaseModel.
    Attributes:
        email (str): The E-mail of The Regestered User.
        password (str): The User Password.
        first_name (str): User First Name.
        last_name (str): User Last Name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
