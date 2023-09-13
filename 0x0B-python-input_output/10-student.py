#!/usr/bin/python3
"""defining a class"""


class Student:
    """initializing class

    Args:
        first_name(str): string for first name
        last_name(str): for last name
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        attributes = {}
        for attr_name in attrs:
            if hasattr(self, attr_name):
                attributes[attr_name] = getattr(self, attr_name)
        return attributes
