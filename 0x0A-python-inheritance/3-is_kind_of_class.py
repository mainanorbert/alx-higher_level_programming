#!/usr/bin/python3

def is_kind_of_class(obj, a_class):
    """returns true if object is instance of

    Args:
        obj (any type): can be of any typw
        a_class: class of the object
    Returns:
        True if is instance otherwise false
    """
    if isinstance(obj, a_class):
        return True
    return False
