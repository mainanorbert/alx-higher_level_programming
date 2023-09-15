#!/usr/bin/python3
"""returns dictionary description"""


class class_to_json(obj):
    """function returning dict representation of simple data structure

    Args:
        obj(any): object of any type
    Returns:
        returns dictionary of all methods and objects
    """
    return obj.__dict__
