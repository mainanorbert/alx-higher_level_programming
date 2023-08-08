#!/usr/bin/python3

for x in range(0, 100):
    if x < 10:
        print("0{0}".format(x), end="")
    else:
        print("{0}".format(x), end="")
    if x != 99:
        print(", ", end="")
print("")
