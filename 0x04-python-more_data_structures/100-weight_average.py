#!/usr/bin/python3
def weight_average(my_list=[]):
    total_w_s = 0
    total_w = 0
    if len(my_list) == 0:
        return 0
    for scr, wgt in my_list:
        total_w_s += scr*wgt
        total_w += wgt
    if total_w == 0:
        return 0
    w_average = total_w_s / total_w
    return w_average
