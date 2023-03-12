#!/usr/bin/python3
"""Class User module"""
from models.base_model import BaseModel
import datetime
import uuid


class User(BaseModel):
    """
    class 'User' that inherits from parent class - BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of User.
        """
        super().__init__(*args, **kwargs)