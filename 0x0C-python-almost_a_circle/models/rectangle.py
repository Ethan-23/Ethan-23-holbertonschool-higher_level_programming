#!/usr/bin/python3
"""This is a rectangle class"""
from models.base import Base


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        super(Rectangle,self).__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def set_width(self, width):
        self.__width = width

    def get_width(self, width):
        return self.__width

    def set_height(self, height):
        self.__height = height

    def get_height(self, height):
        return self.__height

    def set_x(self, x):
        self.__x = x

    def get_x(self, x):
        return self.__x

    def set_width(self, y):
        self.__y = y

    def get_width(self, y):
        return self.__y
