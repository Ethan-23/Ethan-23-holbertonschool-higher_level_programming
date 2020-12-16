#!/usr/bin/python3
def no_c(my_string):
    other = my_string
    x = 0
    for i in other:
        if i == 'c' or i == 'C':
            other = other[:x] + other[x + 1:]
            x -= 1
        x = x + 1
    my_string = other
    return my_string
