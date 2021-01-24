#!/usr/bin/python3
"""This is a rectangle class"""
from models.base import Base


class Rectangle(Base):
    """rectangle class"""
    print_symbol = "#"

    def __init__(self, width, height, x=0, y=0, id=None):
        super(Rectangle,self).__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Property"""
        return self.__width

    @width.setter
    def width(self, value):
        """Checks Width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """property"""
        return self.__height

    @height.setter
    def height(self, value):
        """Checks Height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """property"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """property"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """AREA"""
        return self.__width * self.__height

    def display(self):
        """Display"""
        rectangle_str = ""
        if self.width == 0:
            rectangle_str = "\n"
        elif self.height == 0:
            rectangle_str = "\n"
        else:
            for i in range(self.height):
                for j in range(self.width):
                    rectangle_str += str(self.print_symbol)
                rectangle_str += "\n"
        print (rectangle_str, end='')
