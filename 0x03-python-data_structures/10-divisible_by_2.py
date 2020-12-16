#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    other = my_list[0:]
    for x in other:
        if x % 2 == 0:
            other[x] = True
        else:
            other[x] = False
    return other
