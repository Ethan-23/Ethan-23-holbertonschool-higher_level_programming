#!/usr/bin/python3
"""
This is the Square Class made as a parent of the base class
This has all the base functions for the square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        '''init'''
        super(Square, self).__init__(size, size, x, y, id)
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
        '''str'''
        square = "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                   self.size)
        return square

    def update(self, *args, **kwargs):
        '''update'''
        if len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''dictionary'''
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
