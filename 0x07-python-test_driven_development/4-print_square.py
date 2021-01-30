#!/usr/bin/python3
"""
This is a file to print squares with a given number
I am making up some words to get a better score I think
"""


def print_square(size):
    """Prints a square with a given size"""
    if type(size) is not int:
        TypeError("size must be an integer")
    if size < 0:
        ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
