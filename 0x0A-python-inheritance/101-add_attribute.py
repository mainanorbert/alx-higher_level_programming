#!/usr/bin/python3
"""adding new attribute to object """


def add_attribute(my_obje, attr_name, att_value):
    if not hasattr(my_obje, attr_name):
        setattr(my_obje, attr_name, att_value)
    else:
        raise TypeError("can't add new attribute")
