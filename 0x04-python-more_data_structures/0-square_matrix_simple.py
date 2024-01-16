#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return None
    new_matrix = []
    for row in matrix:
        squared_row = []
        for element in row:
            squared_row.append(element ** 2)
        new_matrix.append(squared_row)
    return new_matrix
