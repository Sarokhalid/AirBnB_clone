#!/usr/bin/python3
"""
A Class Represinting a place in AirBnB
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class that inherits from BaseModel.
    Attributes:
        city_id (str): A unique City ID.
        user_id (str): A unique User ID.
        name (str): The Place name identifier.
        description (str): A string describes The Place.
        number_rooms (int): The Available Rooms in The Place.
        number_bathrooms (int): The Available Bathrooms in The Place.
        max_guest (int): The Capacity of the Place.
        price_by_night (int): The Price of one night in the Place.
        latitude (float): Place location north or south of the Equator.
        longitude (float): Place location east or west of the Equator.
        amenity_ids (list): The list of unique Available facilities.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
