#!/usr/bin/python3
"""defining geometry class"""


class BaseGeometry:
    """a class for base geometry"""

    def area(self):
        raise Exception("area() is not implemented")
