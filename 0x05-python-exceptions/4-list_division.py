#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_new = []
    for x in range(list_length):
        try:
            math = my_list_1[x]/my_list_2[x]
        except TypeError:
            print("wrong type")
            math = 0
        except ZeroDivisionError:
            print("division by 0")
            math = 0
        except IndexError:
            print("out of range")
            math = 0
        finally:
            list_new.append(math)
    return list_new
