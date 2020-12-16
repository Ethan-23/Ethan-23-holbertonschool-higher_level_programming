#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    extra = my_list[0:]
    if idx < 0 or idx > len(my_list):
        return extra
    extra[idx] = element
    return extra
