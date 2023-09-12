#!/usr/bin/python3
"""adding all arguments to list"""
import sys


if __name__ == "__main__":
    save_to_json = __import__('5-save_to_json_file').save_to_json_file
    load_from_json = __import__('6-load_from_json_file').load_from_json_file

    try:
        my_list = load_from_json("add_item.json")
    except FileNotFoundError:
        my_list = []
    for arg in sys.argv[1:]:
        my_list.append(arg)
    save_to_json(my_list, "add_item.json")
