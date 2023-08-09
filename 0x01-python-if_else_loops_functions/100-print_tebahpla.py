#!/usr/bin/python3
x = 0
for i in range(122, 97 - 1, -1):
    print("{}".format(chr(i - x)), end="")
    if x == 0:
        x = 32
    else:
        x = 0
