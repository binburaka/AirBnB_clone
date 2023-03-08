#!/usr/bin/python3
"""Defines a BaseModel class"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the BaseModel for the AirBnb project"""

    def __init__(self, *args, **kwargs):
        """Initialise a new BaseModel

        Args:
            args: any variable of unknown length
            kwargs(dict): key/value pairs

        """
        format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(val, format)
                elif key == "__class__":
                    continue
                else:
                    self.__dict__[key] = val
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        """Updates the attr updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns dictionary containing all keys/values of BaseModel
        instance which includes a  key __class___ to be represented
        containing the name"""

        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary

    def __str__(self):
        """Return print/str representation of the BaseModel"""
        className = self.__class__.__name__
        return "[{}] ({}) {}".format(className, self.id, self.__dict__)
