#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for k in matrix:
        print(' '.join('{:d}'.format(h) for h in k))
