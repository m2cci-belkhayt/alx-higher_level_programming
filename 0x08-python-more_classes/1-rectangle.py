#!/usr/bin/python3
"""This class represents a rectangle with getters and setters for width and height.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """


class Rectangle:
    """ rectangle object with getters and setters"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value
