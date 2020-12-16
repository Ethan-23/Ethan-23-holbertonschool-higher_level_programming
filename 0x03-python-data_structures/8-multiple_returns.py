#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        tuple_empty = (0, None)
        return tuple_empty
    tuple_1 = (len(sentence), sentence[0])
    return tuple_1
