#!/usr/bin/python3
def remove_char_at(str, n):
    if (n >= 0 and n < len(str)):
        my_str = ""
        for x in range(len(str)):
            if x != n:
                my_str += str[x]
        return my_str
    else:
        return (str)
