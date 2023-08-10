#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    s = "name"
    print(s[:2])
    strs = dir(hidden_4)

    for str in strs:
        if str[:2] != "__":
            print(str)
