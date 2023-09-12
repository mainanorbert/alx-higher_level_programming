#!/usr/bin/python3
"""writing to a file with json"""
import json


def save_to_json_file(my_obj, filename):
    """opens file and writes"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
