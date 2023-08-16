#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        sq_matrix = []
        for row in matrix:
            sq_row = []
            for x in row:
                sq_row.append(x**2)
            sq_matrix.append(sq_row)
        return sq_matrix
