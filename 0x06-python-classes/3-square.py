#!/usr/bin/python3
'''class of square'''


class Square:
    ''' Square initialized
    Args:
        __size: square, a private attribute
    '''
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''A public method for area
        Returns: computed square
        '''
        return self.__size * self.__size
