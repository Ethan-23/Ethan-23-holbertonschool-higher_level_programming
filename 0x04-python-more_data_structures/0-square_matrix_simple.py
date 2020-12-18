#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [x[:] for x in matrix]
    for i in new_matrix:
        for j in range(0, len(i)):
            i[j] = i[j]**2
    return new_matrix
