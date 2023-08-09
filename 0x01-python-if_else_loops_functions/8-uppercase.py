#!/usr/bin/python3
def uppercase(str):
    result = ""
    for c in str:
        if 'a' <= c <= 'z':
            char = chr(ord(c) - ord('a') + ord('A'))
        else:
            char = c
            result += char
        return result
