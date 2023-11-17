#!/usr/bin/python3
# base.py
"""Defines a base model class."""


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            Base.id = type(self).__nb_objects
