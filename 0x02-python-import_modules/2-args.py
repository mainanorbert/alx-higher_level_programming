#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    count = 1
    if len(args) == 1:
        print("0 arguments.")
    elif len(args) == 2:
        print("1 argument:\n1: {}".format(args[1]))
    else:
        print("{} arguments".format(len(args) - 1))
        for x in args[1:]:
            print("{}: {}".format(count, x))
            count += 1
