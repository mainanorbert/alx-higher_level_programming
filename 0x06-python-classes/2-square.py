#!/usr/bin/python3
'''Defining square class'''


class Square:

    '''representing a square class'''

    def __init__(self, size=0):
        '''initializing a square'''

        '''size (int): size of the square'''
        if not isinstance(size, int):
            raise TypeError("the size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
