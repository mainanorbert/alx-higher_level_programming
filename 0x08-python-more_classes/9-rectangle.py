#!/usr/bin/python3
""" Function that defines a rectangle"""


class Rectangle:
    """
    Defining a class
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        type(self).number_of_instances += 1
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
        return self.__width * self.__height

    def perimeter(self):
        """returning perimeter of a rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return ((2 * self.width) + (2 * self.height))

    def __str__(self):
        """returns printable representation of rectangle
        Represents recangle with #
        """
        str_rep = ""
        if self.height == 0 or self.width == 0:
            return str_rep
        else:
            for i in range(self.height):
                for x in range(self.width):
                    str_rep += self.print_symbol
                if i is not self.height - 1:
                    str_rep += '\n'
        return str_rep

    def __repr__(self):
        """returns string representation of the rectangle"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """prints message when rectangle object is destroyed"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
