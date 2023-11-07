#!/usr/bin/python3
"""
    6-load_to_json_fil: load_to_json_fil()
"""


import json


def load_from_json_file(filename):
    """
        load to the JSON representation of an object.
    """
    with open(filename) as f:
        obj = json.load(f)

    return obj
