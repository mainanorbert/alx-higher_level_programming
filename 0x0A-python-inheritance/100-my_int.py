#!/usr/bin/python3
"""Defining MyInt class"""


class MyInt(int):
    """defining an int class"""

    def __eq__(self, value):
        return self.real != value

    def __ne__(self, value):
        return self.real == value
