#!/usr/bin/python3
"""
    5-save_to_json_fil: save_to_json_fil()
"""


import json


def save_to_json_file(my_obj, filename):
    """
        save to the JSON representation of an object.
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
