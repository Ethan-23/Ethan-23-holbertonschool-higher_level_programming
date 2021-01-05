#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    h = 0
    for y in my_list:
        h += 1
    if x > h:
        x = h
    for z in my_list:
        if z <= x:
            try:
                print(z, end="")
            except:
                print("An exception occurred")
    print()
    return x
