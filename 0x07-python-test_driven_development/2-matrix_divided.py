#!/usr/bin/python3
"""
This is the "2-matrix_divided" module.

The example module supplies one function, matrix_divided().
"""


def matrix_divided(matrix, div):
    """
        Divides all elements of a matrix.
        Args:
            matrix (list): List of lists of integers or floats.
            div (int|float): An integer or floating point number.
        Returns:  A new matrix.
    """
    if div is None or (type(div) is not int and type(div) is not float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not matrix or type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    row_size = 0
    new_mat = []
    for sublists in matrix:
        new_list = []
        if not sublists or type(sublists) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        
        if row_size != 0 and len(sublists) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
        row_size = len(sublists)
        for num in sublists:
            if type(num) is not int and type(num) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_list.append(round(num / div, 2))
        new_mat.append(new_list)
    return new_mat
