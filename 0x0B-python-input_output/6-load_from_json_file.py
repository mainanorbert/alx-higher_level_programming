#!/usr/bin/python3
"""creating object from JSON file"""
import json


def load_from_json_file(filename):
    """returns object from json file"""
    with open(filename, 'r', encoding="utf-8") as f:
        return json.loads(f)
