#!/usr/bin/python3
"""Defines the class FileStorage"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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
        obj_dict = {}
        for key, val in FileStorage.__objects.items():
            obj_dict[key] = val.to_dict()

        with open(FileStorage.__file_path, mode='w', encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects if it exists"""
        try:
            with open(FileStorage.__file_path, mode='r') as f:
                obj_dict = json.load(f)
                for o in obj_dict.values():
                    inst_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(inst_name)(**o))
        except FileNotFoundError:
            return
