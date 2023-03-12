#!/usr/bin/python3
"""
converts dictionary representation to a JSON string
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    serialize instances to a JSON file and vica-verca
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects"""
        return self.__object

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id"""
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file (path: __file_path)"""
        new = {}
        for key, values in self.__objects.items():
            new[key] = values.to_dict()

        with open(self.__file_path, 'w') as f:
            json.dump(new, f)

    def reload(self):
        """Deserialize the JSON file to __objects"""
        classes = {'BaseModel': BaseModel, 'User': User, 'City': City,
                   'State': State, 'Amenity': Amenity, 'Place': Place,
                   'Review': Review}
        try:
            with open(self.__file_path, 'r') as f:
                objects = json.load(f)
                for keys, values in objects.items():
                    temp = keys.split('.')
                    new = classes[temp[0]](**values)
                    self.new(new)
        except FileNotFoundError:
            pass

