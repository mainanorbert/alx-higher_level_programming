#!/usr/bin/python3
"""defining function to check typee of object"""


def is_same_class(obj, a_class):

    """checks if object is an instance of class

    Args:
        obj (any type): the objects to be checked
        a_class (type of object): type against which to check
    Returns:
        return True otherwise False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
