#!/usr/bin/python3
def text_indentation(text):
    """
    prints a text and with 2 lines after every(.,?, :)

    Args:
        text (str): s strings text
    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in text:
        if char == "." or char == "?" or char == ":":
            print(char)
            print()
        else:
            print(char, end="")
    print()
