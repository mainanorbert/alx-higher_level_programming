#!/usr/bin/python3

def is_same_class(obj, a_class):
    """checks if object is an instance of class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
