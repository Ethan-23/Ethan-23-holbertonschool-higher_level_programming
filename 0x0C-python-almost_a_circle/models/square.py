#!/usr/bin/python3
"""This is a square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        super(Square,self).__init__(size, size, x, y, id)

    def __str__(self):
        square_str_print = "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
        return square_str_print
