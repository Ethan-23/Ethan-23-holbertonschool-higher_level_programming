#!/usr/bin/python3
"""This is a square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        super(Square,self).__init__(size, size, x, y, id)
        self.size = self.width
        self.size = self.height

    @property
    def size(self):
        """Property"""
        return self.__size

    @size.setter
    def size(self, value):
        """Checks Width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__size = value


    def __str__(self):
        square_str_print = "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)
        return square_str_print
