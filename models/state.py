#!/usr/bin/python3
"""
State Class Representing a State in AirBnB
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    State class that inherits from BaseModel.
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize a new State instance.
        """
        super().__init__(*args, **kwargs)
