#!/usr/bin/python3
def fizzbuzz():
    for x in range(0, 100):
        if x % 3 is 0 and x % 5 is 0:
            print("FizzBuzz ", end="")
        elif x % 3 is 0:
            print("Fizz ", end="")
        elif x % 5 is 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(x), end="")
    print()
