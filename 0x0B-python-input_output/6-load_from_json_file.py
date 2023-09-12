#!/usr/bin/python3
"""creating object from JSON file"""
import json


def load_from_json_file(filename):
    """returns object from json file"""
        return json.loads(filename)
