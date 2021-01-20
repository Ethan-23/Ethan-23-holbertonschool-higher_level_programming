#!/usr/bin/python3
"""object is an instance of a class that inherited (directly or indirectly)"""


def inherits_from(obj, a_class):
    """return true or false"""
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
