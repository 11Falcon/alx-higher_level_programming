#!/usr/bin/python3
"""
2-matrix_divided
divides all elements of a matrix 
takes same size lists of ints or floats, and max two decimal places
"""


def matrix_divided(matrix, div):
    """
    output:  new matrix with dividends
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    error_message = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(error_message)

    new_matrix = []
    samelen = len(matrix[0])
    for lists in matrix:
        if type(lists) is not list:
            raise TypeError(error_message)
        if len(lists) != samelen:
            raise TypeError("Each row of the matrix must have the same size")
        newlist = []
        for i in lists:
            if not isinstance(i, (int, float)):
                raise TypeError(error_message)
            newlist.append(round(i/div, 2))
        new_matrix.append(newlist)
    return new_matrix
