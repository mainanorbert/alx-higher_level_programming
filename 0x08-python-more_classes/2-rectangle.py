#!/usr/bin/python3
""" Function that defines a rectangle"""


class Rectangle:
    """
    Defining a class
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

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
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """returning perimeter of a rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return ((2 * self.width) + (2 * self.height))
