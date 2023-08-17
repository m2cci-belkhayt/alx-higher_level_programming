#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    max_val = 0
    max_key = None
    for k in a_dictionary:
        if max_val < a_dictionary[k]:
            max_val = a_dictionary[k]
            max_key = k
    return max_key
