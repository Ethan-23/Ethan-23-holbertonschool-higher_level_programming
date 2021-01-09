#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    end = "My name is "
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    elif first_name is None:
        raise TypeError("first_name must be a string")
    else:
        end += first_name + " "
    if type(last_name) != str:
        raise TypeError("first_name must be a string")
    else:
        end += last_name
    return(end)
