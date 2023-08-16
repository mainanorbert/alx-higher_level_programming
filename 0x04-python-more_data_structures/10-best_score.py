#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    key_0 = list(a_dictionary.keys())[0]
    val_0 = a_dictionary[key_0]
    for k, v in a_dictionary.items():
        if v > val_0:
            val_0 = v
            key_0 = k
    return key_0
