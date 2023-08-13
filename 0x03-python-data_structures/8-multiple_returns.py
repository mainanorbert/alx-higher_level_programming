#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        a = "None"
        length = len(sentence)
        tup = length, a
        return tup
    a = sentence[0]
    length = len(sentence)
    tup = length, a
    return tup
