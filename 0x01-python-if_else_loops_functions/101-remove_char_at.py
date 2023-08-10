#!/usr/bin/python3
def remove_char_at(str, n):
    add = ''
    i = 0
    for c in str:
        if i != n:
            add += str[i]
            i += 1
    return add
