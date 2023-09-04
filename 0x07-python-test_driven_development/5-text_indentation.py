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
    i = 0
    while i < len(text) and text[i] == " ":
        i += 1

    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:" or text[i] == "\n":
            if text[i] == "." or text[i] == "?" or text[i] == ":":
                print("\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
