#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv) - 1
    argss = "argument"
    if length != 1:
        argss += "s"
    if length != 0:
        argss += ":"
    else:
        argss += "."
    print("{} {}".format(length, argss))
    for i in range(1, length + 1):
        print("{}: {}".format(i, argv[i]))
