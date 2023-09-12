#!/usr/bin/python3
"""writing to a text file"""


def write_file(filename="", text=""):
    """function that writes text to file"""
    with open(filename, 'w', encoding='utf-8') as f:
        no_of_chars = f.write(text)
    return no_of_chars
