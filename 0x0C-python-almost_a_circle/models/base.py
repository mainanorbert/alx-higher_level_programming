#!/usr/bin/python3
import json
"""Defining a class called base"""


class Base:
    """class base for my project"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returning json representation of dictionary"""
        if len(list_dictionaries) == 0 or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """used to save json representation of list to file"""
        file_name = cls.__name__ + ".json"
        list_of_objects = []
        if list_objs is not None:
            list_of_objects = [obj.to_dictionary() for obj in list_objs]
        with open(file_name, mode='w') as f:
            f.write(cls.to_json_string(list_of_objects))
