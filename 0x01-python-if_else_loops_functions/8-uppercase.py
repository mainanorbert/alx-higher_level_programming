#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if ord(letter) >= 97 and ord(letter) <= 122:
            upper_l = chr(ord(letter) - 32)
            print("{}".format(upper_l), end="")
        else:
            print("{}".format(letter), end="")
    print()
