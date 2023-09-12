#!/usr/bin/python3
"""converts JSON to python object"""
import json


def from_json_string(my_str):
    """from returns an object from JSON"""
    return json.loads(my_str)
