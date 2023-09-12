#!/usr/bin/python3
"""appending to a file"""


def append_write(filename="", text=""):
    """appends and returns chars appended"""
    with open(filename, 'a', encoding='utf-8') as f:
        no_of_chars = f.write(text)
    return no_of_chars
