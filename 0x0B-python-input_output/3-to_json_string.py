#!/usr/bin/python3
"""returning JSON representation"""
import json


def to_json_string(my_obj):
    """serializing an object"""
    return json.dumps(my_obj)
