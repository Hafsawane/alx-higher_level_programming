#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for row in matrix:
        for element in range(len(row)):
            print("{:d}".format(row[element]), end=" ")
        print()
