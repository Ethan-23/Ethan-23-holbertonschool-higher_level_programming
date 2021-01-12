#!/usr/bin/python3
"""This is an empty rectangle class"""


class Rectangle:
    """This is a class"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Sets sizes"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        """Property"""
        return self.__height

    @height.setter
    def height(self, value):
        """Checks height for errors"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """Property"""
        return self.__width

    @width.setter
    def width(self, value):
        """Checks widths for errors"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        """Area of rect"""
        return self.width * self.height

    def perimeter(self):
        """Length of sides"""
        if self.width == 0:
            return 0
        elif self.height == 0:
            return 0
        else:
            return self.width * 2 + self.height * 2

    def __str__(self):
        """string for rectangle"""
        rectangle_str = ""
        if self.width == 0:
            rectangle_str = "\n"
        elif self.height == 0:
            rectangle_str = "\n"
        else:
            for i in range(self.height):
                for j in range(self.width):
                    rectangle_str += "#"
                rectangle_str += "\n"
        return rectangle_str[:-1]

    def __repr__(self):
        """string for rect"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Delete rect"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
