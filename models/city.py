#!/usr/bin/python3
"""
City Class Representing a City in AirBnB
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City class that inherits from BaseModel.
    """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize a new City instance.
        """
        super().__init__(*args, **kwargs)
