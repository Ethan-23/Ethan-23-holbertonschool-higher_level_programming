#!/usr/bin/python3
"""This will create a empty class that will do nothing!"""


class Square:
    """This is a empty class named Square with nothing in it!"""
    def __init__(self, size=0, position=(0, 0)):
        """Sets size"""
        self.size = size
        self.position = position

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

    @property
    def position(self, position):
        """Position finder"""
        return self.__position

    @position.setter
    def position(self, position):
        """position checks"""
        if type(position) is not tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[0]) is not int or type(position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        """area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Prints Square"""
        if self.__size == 0:
            print()
        else:
            for i in range (self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
