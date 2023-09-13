#!/usr/bin/python3
"""returns dictionary description"""


class class_to_json(obj):
    """function returning dict representation of simple data structure"""
    attr_dict = {}
    for atr in dir(obj):
        atr_v = getattr(obj, atr)
        if isinstance(atr_v, (list, dict, str, int, bool)):
            atrr_dict[atr] = atr_v
    return atrr_dict
