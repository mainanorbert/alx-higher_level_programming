#!/usr/bin/python3

def is_same_class(obj, a_class):

    """checks if object is an instance of class
    Args:
        obj (any type): the objects to be checked
        a_class (type of object): type against which to check
    Return: return True otherwise False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
