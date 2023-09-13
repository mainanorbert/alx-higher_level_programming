#!/usr/bin/python3
"""Defining MyList inherited class"""


class MyList(list):
    """implementing inherited list  class"""

    def print_sorted(self):
        """printing list in sorted order"""
        print(sorted(self))
