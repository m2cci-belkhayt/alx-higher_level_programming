#!/usr/bin/python3
"""This class represents a rectangle with getters and setters.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """


class Rectangle:
    """ rectangle object with getters and setters"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    def area(self):
        if (self.height == 0 or self.width == 0):
            return 0
        else:
            return (self.height * self.width)

    def perimeter(self):
        if (self.height == 0 or self.width == 0):
            return 0
        else:
            return 2 * (self.height + self.width)

    def __str__(self):
        if (self.height == 0 or self.width == 0):
            return ""
        else:
            rect_str = ""
            for _ in range(self.__height):
                rect_str += str(self.print_symbol) * self.__width + "\n"
            return rect_str[:-1]

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the Rectangle with the greater area.

        Args:
            rect_1 (Rectangle): The first Rectangle.
            rect_2 (Rectangle): The second Rectangle.
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)
    
    @classmethod
    def square(cls, size=0):
        return cls(size, size)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
