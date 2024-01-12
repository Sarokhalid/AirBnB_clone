#!/usr/bin/python3
"""
A Class Represinting a User Review in AirBnB
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that inherits from BaseModel.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new Review instance.
        """
        self.place_id = ""
        self.user_id = ""
        self.text = ""
        super().__init__(*args, **kwargs)
