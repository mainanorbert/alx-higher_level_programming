#!/usr/bin/python3
"""inserting line at given string"""


def append_after(filename="", search_string="", new_string=""):
    """function adding lines after given string

    Args:
        filename(str): the name of file to modify
        search_string(str): the string to search for
        new_string(str): the string to add
    """
    changed_lines = []
    with open(filename, 'r') as f:
        for line in f:
            changed_lines.append(line)
            if search_string in line:
                changed_lines.append(new_string + '\n')
    with open(filename, 'w') as f:
        f.writelines(changed_lines)
