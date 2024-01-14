#!/usr/bin/python3
"""
State Class Representing a State in AirBnB
"""

from .base_model import BaseModel


class State(BaseModel):
    """
    State class that inherits from BaseModel.
    Attributes:
        name (str): The State Name.
    """

    name = ""
