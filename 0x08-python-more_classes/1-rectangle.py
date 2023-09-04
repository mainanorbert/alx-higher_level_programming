#!/usr/bin/python3
""" Function that defines a rectangle"""


class Rectangle:
    """Defining a class """

    def __init__(self, width=0, height=0):
        """ Initializing objects
        Args:
            __width (int): the width of rectangle
            __height (int): the height of a rectangle
        """

        self.__width = wid  th
        self.__height = height

    @property
    def width(self):
        """get or set width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get or set the height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value
