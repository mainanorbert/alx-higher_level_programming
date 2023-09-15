#!/usr/bin/python3

def class_to_json(obj):
    """
    Convert an object with serializable attributes

    Args:
        obj (any): An instance of a class.

    Returns:
        dict: A dictionary representation of the object.

    Note:
        This function assumes that all attributes.
    """
    return obj.__dict__
