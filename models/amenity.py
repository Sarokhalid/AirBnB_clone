#!/usr/bin/python3
"""
Amenity Class Represinting Amenity in AirBnB
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class that inherits from BaseModel.
    Attributes:
        name (str): The Name of the available Amenity
    """

    name = ""
