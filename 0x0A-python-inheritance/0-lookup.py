#!/usr/bin/python3
"""Module 0-lookup
List of available attributes & methods of an object
"""

def lookup(obj):
"""Returns a list of attributes and methods
Args:
- obj: object to look into
"""

    return dir(obj)
