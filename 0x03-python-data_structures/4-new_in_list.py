#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    resu = my_list[:]
    if (idx < 0) or idx >= len(my_list):
        return resu
    else:
        resu[idx] = element
        return resu
