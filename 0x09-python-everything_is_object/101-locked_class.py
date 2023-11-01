#!/usr/bin/python3
""" This class prevents user from dynamic attributes """


class LockedClass:
    """This is a locked class"""
    __slots__ = ['first_name']
