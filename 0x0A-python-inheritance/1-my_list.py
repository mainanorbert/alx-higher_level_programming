#!/usr/bin/python3
"""Class that defines MyList class"""


class MyList(list):
    """inheriting list"""

    def print_sorted(self):
        """printing list in sorted order"""
        print(sorted(self))
