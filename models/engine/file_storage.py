#!/usr/bin/python3
"""Defines the class FileStorage"""


class FileStorage:
    """Represents a file storage engine

    Attribute:
        __file_path (str): filename to save objects to
        __objects (dict): dictionary of objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __obects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path"""

        #to be continued...
