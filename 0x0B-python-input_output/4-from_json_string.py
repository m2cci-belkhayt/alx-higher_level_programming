#!/usr/bin/python3
"""
    4-from_json_string: from_json_string()
"""


import json


def from_json_string(my_str):
    """
        having the JSON representation of an object.
    """
    return json.loads(my_str)
