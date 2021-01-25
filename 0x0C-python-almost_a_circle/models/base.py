#!/usr/bin/python3
""" Base Class"""
import json


class Base:
    """Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Init"""
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        new_dict = []
        if list_objs is None:
            with open('{}.json'.format(cls.__name__), 'w') as file:
                string = cls.to_json_string(new_dict)
                file.write(new_dict)
        else:
            for i in list_objs:
                new_dict.append(cls.to_dictionary(i))
            with open('{}.json'.format(cls.__name__), 'w') as file:
                file.write(cls.to_json_string(new_dict))

    def from_json_string(json_string):
        list = ""
        if json_string is None:
            return list
        else:
            return json.loads(json_string)
