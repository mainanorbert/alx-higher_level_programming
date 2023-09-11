#!/usr/bin/python3

"""checks if object is instance of class inherited"""


def inherits_from(obj, a_class):
    """chcking for inherited instance of specified class

    Args:
        obj(any-type object): object of any type
        a_class (type): the class to check against
    Returns:
        If object is of inherited class (a_class) Return True otherwise false
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
