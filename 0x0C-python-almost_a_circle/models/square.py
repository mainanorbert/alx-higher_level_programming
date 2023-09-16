#!/usr/bin/python3
from models.rectangle import Rectangle
"""class square"""


class Square(Rectangle):
    """defining a class square"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializing square class

        Args:
            size (int): size of square
            x (int): x the coordinate of the square
            y (int): y coordinate of square
            id (int): identity of square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation of square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """setter and getter for width"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height - value

    def update(self, *args, **kwargs):
        """assigning attributes"""
        if args and len(args) != 0:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
                self.height = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
