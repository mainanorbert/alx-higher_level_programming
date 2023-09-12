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
    def to_json(self):
        return self.__dict__
