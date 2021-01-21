#!/usr/bin/python3
"""Student Class"""


class Student:
    """Class"""
    def __init__(self, first_name, last_name, age):
        """Init"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """json"""
        if attrs is None or type(attrs) is not list:
            return self.__dict__
        else:
            new_dict = {}
            for x in attrs:
                if type(x) is str:
                    try:
                        new_dict[x] = self.__dict__[x]
                    except:
                        pass
            return new_dict

    def reload_from_json(self, json):
        """replace with json"""
        for x in json:
            try:
                self.__dict__[x] = json[x]
            except:
                pass
