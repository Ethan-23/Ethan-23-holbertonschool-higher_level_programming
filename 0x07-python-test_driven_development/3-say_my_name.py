#!/usr/bin/python3
"""
This is some random words that came to my head because
it is late and I wanted to get some projects done
"""


def say_my_name(first_name, last_name=""):
    """
    Used for printing first and last name
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    elif first_name is None:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
