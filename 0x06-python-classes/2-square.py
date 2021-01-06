#!/usr/bin/python3
"""This will create a empty class that will do nothing!"""


class Square:
    """This is a empty class named Square with nothing in it!"""
    def __init__(self, size=0):
        """Sets size and error checking"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
