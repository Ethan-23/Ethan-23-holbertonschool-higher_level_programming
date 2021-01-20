#!/usr/bin/python3
"""Creates a class named BaseGeometry"""


class BaseGeometry:
    """Geometry Class"""
    def area(self):
        """area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """check"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
