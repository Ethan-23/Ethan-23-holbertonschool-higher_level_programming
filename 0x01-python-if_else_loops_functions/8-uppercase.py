#!/usr/bin/python3
def uppercase(str):
    letter = 0
    for i in str:
        letter = ord(i)
        if ord(i) >= 97 and ord(i) <= 122:
            letter = letter - 32
        print("{}".format(chr(letter)), end="")
    print()
