#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if 97 <= ord(letter) <= 122:
            upper_l = ord(letter) - 32
            print("{}".format(chr(upper_l)), end="")
        else:
            print("{}".format(letter), end="")
    print()
