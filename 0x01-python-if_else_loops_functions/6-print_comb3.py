#!/usr/bin/python3
for x in range (0, 10):
    for i in range (x + 1, 10):
        print("{}{}".format(x, i), end="")
        if x != 8:
            print(", ", end="")
        else:
            print()
