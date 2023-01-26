#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    if len(matrix) == 0:
        return new_matrix

    new_matrix = [[i*i for i in col] for row in matrix]
    return new_matrix
