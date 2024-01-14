#!/usr/bin/python3
"""
A Class Represinting a User Review in AirBnB

"""

from .base_model import BaseModel


class Review(BaseModel):
    """
    Review class that inherits from BaseModel.
    Attributes:
        place_id (str): The unique Place ID.
        user_id (str): The unique User ID.
        text (str): The Review body.
    """

    place_id = ""
    user_id = ""
    text = ""
