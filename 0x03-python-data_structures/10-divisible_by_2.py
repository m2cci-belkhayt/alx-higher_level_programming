#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return None
    result = []
    for element in my_list:
        result.append(element % 2)
    return result
