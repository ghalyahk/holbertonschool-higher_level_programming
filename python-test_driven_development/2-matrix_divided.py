#!/usr/bin/python3
"""
Module that contains the function matrix_divided.
This function divides all elements of a matrix by a given number.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div, rounded to 2 decimals."""
    # التحقق من div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # التحقق من matrix
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(all(isinstance(elem, (int, float)) for elem in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # التحقق من حجم الصفوف
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # إنشاء مصفوفة جديدة بعد القسمة
    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]

    return new_matrix
