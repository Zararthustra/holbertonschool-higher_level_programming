#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
    for line in matrix:
        for i in range(len(line)):
            if i == len(line) - 1:
                print("{:d}".format(line[i]))
            else:
                print("{:d}".format(line[i]), end=" ")
