#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if isinstance(a_dictionary, dict):
        for k, v in a_dictionary.items():
            a_dictionary[k] = v*2
        return a_dictionary
