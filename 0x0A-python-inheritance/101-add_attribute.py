#!/usr/bin/python3
"""adding new attribute to object """


def add_attribute(my_obje, attr_name, att_value):
    """function adding new attribute to object

    Args:
        my_obje(any): object of any type
        attr_name: name of new attribute
        att_value: value to add
    Raises:
        TypeError: if attribute exists
    """
    if not hasattr(my_obje, attr_name):
        setattr(my_obje, attr_name, att_value)
    else:
        raise TypeError("can't add new attribute")
