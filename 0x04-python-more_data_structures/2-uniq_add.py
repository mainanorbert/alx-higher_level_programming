#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_set = set()
    sum = 0
    for x in my_list:
        if x not in unique_set:
            unique_set.add(x)
            sum += x
    return sum
