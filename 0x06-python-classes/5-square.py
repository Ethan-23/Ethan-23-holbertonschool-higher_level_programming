#!/usr/bin/python3
"""This will create a empty class that will do nothing!"""


class Square:
    """This is a empty class named Square with nothing in it!"""
    def __init__(self, size=0):
        """Sets size"""
        self.size = size

    @property
    def size(self):
        """size size of the size"""
        return self.__size

    @size.setter
    def size(self, size):
        """Errors and size to self"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Prints Square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
