#!/usr/bin/python3
'''square class'''


class Square:
    '''class inialization
    Args:
        __size: private square size
    '''
    def __init__(self, size=0):
        self.__size = size

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
