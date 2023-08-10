#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len(sys.argv)
    args = sys.argv
    sum = 0
    if count == 1:
        print("0")
    else:
        for x in args[1:]:
            x = int(x)
            sum += x
        print(sum)
