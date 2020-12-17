#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix = [[x*x for x in matrix[y]]for y in range(len(matrix))]
    return (matrix)
