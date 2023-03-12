#!/usr/bin/python3
"""
converts dictionary representation to a JSON string
"""

import os.path
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file (path: __file_path)"""
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(obj_dict, file, ensure_ascii=False)

    def reload(self):
        """Deserialize the JSON file to __objects"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                obj_dict = json.load(file)
                for key, obj_data in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    if class_name == 'User':
                        obj = User(**obj_data)
                    elif class_name == 'Place':
                        obj = Place(**obj_data)
                    elif class_name == 'State':
                        obj = State(**obj_data)
                    elif class_name == 'City':
                        obj = City(**obj_data)
                    elif class_name == 'Amenity':
                        obj = Amenity(**obj_data)
                    elif class_name == 'Review':
                        obj = Review(**obj_data)
                    else:
                        module = __import__('models.' + class_name.lower(),
                                            fromlist=[class_name])
                        class_ = getattr(module, class_name)
                        obj = class_(**obj_data)
                    self.__objects[key] = obj
