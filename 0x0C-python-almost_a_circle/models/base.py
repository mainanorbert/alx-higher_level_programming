#!/usr/bin/python3
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
