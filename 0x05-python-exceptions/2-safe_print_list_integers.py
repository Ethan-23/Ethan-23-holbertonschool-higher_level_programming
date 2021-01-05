#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    for z in my_list:
            try:
                print("{:d}".format(z), end="")
            except:
                x -= 1
                pass
    print()
    return x
