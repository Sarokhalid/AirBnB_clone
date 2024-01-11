#!/usr/bin/python3
"""
City Class Representing a City in AirBnB
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City class that inherits from BaseModel.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new City instance.
        """
        self.state_id = ""
        self.name = ""
        super().__init__(*args, **kwargs)
