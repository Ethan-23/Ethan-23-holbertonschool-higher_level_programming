#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10
if number < 0:
    last = 10 - last
    last *= -1
string = "Last digit of " + str(number) + " is " + str(last)
if last > 5:
    print("{} and is greater than 5".format(string))
elif last == 0:
    print("{} and is 0".format(string))
else:
    print("{} and is less than 6 and not 0".format(string))
