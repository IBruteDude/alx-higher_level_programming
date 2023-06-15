#!/usr/bin/python3
def square_matrix_simple (matrix=[]):
    new_matrix = list(map(lambda column : list(map(lambda e : e ** 2, column)), matrix))
    return new_matrix
