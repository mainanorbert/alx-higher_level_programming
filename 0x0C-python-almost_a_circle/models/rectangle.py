#!/usr/bin/python3
from models.base import Base
"""Rectangle class for rectangle"""


class Rectangle(Base):
    """defining a class rectangle"""

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
        """setter for y value"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def update(self, *args, **kwargs):
        """updating with args and kwargs"""
        if args and len(args) > 0:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.__width = args[1]
            if len(args) > 2:
                self.__height = args[2]
            if len(args) > 3:
                self.__x = args[3]
            if len(args) > 4:
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def area(self):
        """returning area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """printing rectangle with #"""
        for y in range(self.__height):
            if y == 0:
                for _ in range(self.__y):
                    print()
            for x in range(self.__width):
                if x == 0:
                    for x in range(self.__x):
                        print(" ", end="")
                print("#", end="")
            print()

    def __str__(self):
        """returning str representation of a string"""
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - " +
                f"{self.__width}/{self.__height}")

    def to_dictionary(self):
        """converts an object to dictionary"""
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
