#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    other = []
    for x in my_list:
        if x % 2 == 0:
            other.append(True)
        else:
            other.append(False)
    return other
