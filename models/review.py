#!/usr/bin/python3
"""Defines the Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents review

    Attributes:
        place_id (str): the Place id
        user_id (str): the User id
        text (str): review of the place
    """

    place_id = ""
    user_id = ""
    text = ""
