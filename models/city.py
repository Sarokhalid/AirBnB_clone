#!/usr/bin/python3
"""
City Class Representing a City in AirBnB
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City class that inherits from BaseModel.
    Attributes:
        state_id (str): A unique State ID
        name (str): The name of the City.
    """

    state_id = ""
    name = ""
