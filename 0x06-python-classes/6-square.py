#!/usr/bin/python3
'''square class'''


class Square:
    '''class inialization
    Args:
        __size: private square size
    '''
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of positive integers")
        if not all(isinstance(x, int) and x > 0 for x in value):
            raise TypeError("position must be a tuple of positive integers")
        self.__position = value

    @property
    def size(self):
        '''gets size of square'''
        return self.__size

    @size.setter
    def size(self, value):
        '''sets size of square'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):

        ''' calculates area of square
        Returns: returns area
        '''
        return self.__size**2

    def my_print(self):
        if self.__size == 0:
            print("")
            return
        [print("") for i in range(self.__position[1])]
        for x in range(0, self.__size):
            [print(" ", end="") for y in range(self.__position[0])]
            [print(" ", end="") for z in range(self.__size)]
            print()
