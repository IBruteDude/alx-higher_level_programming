#!/usr/bin/python3
"""Module for defining and testing the matrix_divided function
    Examples:
        >>> matrix = [[1, 2, 3], [4, 5, 6]]
        >>> matrix_divided(matrix, 3)
        [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
"""


def matrix_divided(matrix, div):
    """a function that divides all elements of a matrix

    Args:
        matrix (list[list[float | int]]): input numeric matrix
        div (float): the matrix divisor
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if float(div) == 0.0:
        raise ZeroDivisionError("division by zero")
    if not (isinstance(matrix, list) and isinstance(matrix[0], list)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    row_len = len(matrix[0])
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists)" +
                    " of integers/floats"
                )
    return [[round(element / div, 2) for element in row] for row in matrix]

if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print(matrix_divided(matrix, 3))
    print(matrix)
