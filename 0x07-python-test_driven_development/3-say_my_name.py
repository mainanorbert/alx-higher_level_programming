#!/usr/bin/pythn3
def say_my_name(first_name, last_name=""):
    """
    Function says name

    Args:
        first_name (str): first name to print
        last_name (str): second name to print
    Raises:
        TypeError: if first_name or last_name not string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
