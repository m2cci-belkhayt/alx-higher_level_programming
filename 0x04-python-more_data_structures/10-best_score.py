#!/usr/bin/python3
def best_score(a_dictionary):
    max_val = 0
    for k in a_dictionary:
        if max_val < a_dictionary[k]:
            max_val = a_dictionary[k]
    return max_val
