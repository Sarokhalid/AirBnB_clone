#!/usr/bin/python3
"""
State Class Representing a State in AirBnB
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    State class that inherits from BaseModel.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new State instance.
        """
        self.name = ""
        super().__init__(*args, **kwargs)
