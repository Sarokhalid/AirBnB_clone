#!/usr/bin/python3
"""
Amenity Class Represinting Amenity in AirBnB
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class that inherits from BaseModel.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new Amenity instance.
        """
        self.name = ""
        super().__init__(*args, **kwargs)
