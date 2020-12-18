#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    for i in range(0, len(my_list)):
        if my_list[i] not in my_list[:i]:
            total = total + my_list[i]
    return total
