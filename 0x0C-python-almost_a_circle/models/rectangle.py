#!/usr/bin/python3
from models.base import Base
"""Rectangle class """


class Rectangle(Base):
    """defining a class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing rectangle

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
            x (int): x coordinate
            y (int): y coordinates
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """getting and setting rect width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getting and setting rect width"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getting and setting x coordinate for the table"""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >=   0")
        self.__x = value

    @property
    def y(self):
        """getting and setting y coordinate for the table"""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
