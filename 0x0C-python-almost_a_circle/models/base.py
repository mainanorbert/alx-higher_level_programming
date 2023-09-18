#!/usr/bin/python3
"""Defining a class called base"""
import json


class Base:
    """class base for my project

    The base class for all other rectangles

    Attributes:
        __nb_objects (int): number of instances
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """initialization of base class

        Args:
            id (int): the id of instances
        """
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
        """used to save json representation of list of instances to file"""
        file_name = cls.__name__ + ".json"
        list_of_objects = []
        if list_objs is not None:
            list_of_objects = [obj.to_dictionary() for obj in list_objs]
        with open(file_name, mode='w') as f:
            f.write(cls.to_json_string(list_of_objects))

    @staticmethod
    def from_json_string(json_string):
        """returning list of json string representation"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returning an instance with set attributes

        Args:
            dictionary(dict): key-value of ttributes
        """
        if dictionary != {} and dictionary:
            if cls.__name__ == "Rectangle":
                dummy_obj = cls(1, 1)
            else:
                dummy_obj = cls(1)
            dummy_obj.update(**dictionary)
            return dummy_obj

    @classmethod
    def load_from_file(cls):
        """function returning a list of instances"""

        obj_list = []
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, "r") as f:
                obj_list = cls.from_json_string(f.read())
                return [cls.create(**obj) for obj in obj_list]
        except FileNotFoundError:
            return []
