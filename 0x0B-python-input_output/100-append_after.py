#!/usr/bin/python
"""inserting line at given string"""


def append_after(filename="", search_string="", new_string=""):
    changed_lines = []
    with open(filename, 'r') as f:
        for line in f:
            changed_lines.append(line)
            if search_string in line:
                changed_lines.append(new_string + '\n')
    with open(filename, 'w') as f:
        f.writelines(changed_lines)
