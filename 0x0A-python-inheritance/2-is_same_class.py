#!/usr/bin/python3
"""checks for exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """returns true or false"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
