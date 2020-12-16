#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    first = tuple_a[0] + tuple_b[0]
    second = tuple_a[1] + tuple_b[1]
    tuple_c = (first, second)
    return tuple_c
