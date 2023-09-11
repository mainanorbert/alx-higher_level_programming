#!/usr/bin/python3

class MyList(list):
    """class inheriting from list"""

    def print_sorted(self):
        """prints list in a sorted order in ascending order"""
        print(sorted(self))
