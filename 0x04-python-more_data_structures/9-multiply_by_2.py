#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    result = 1
    for key in a_dictionary:
        a_dictionary[key] *= 2
    return a_dictionary
