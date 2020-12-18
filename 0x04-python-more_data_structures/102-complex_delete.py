#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    dupe = dict(a_dictionary)
    for key in dupe:
        if dupe[key] == value:
            a_dictionary.pop(key, None)
    return a_dictionary
