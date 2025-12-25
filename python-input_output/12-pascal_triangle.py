#!/usr/bin/python3
"""
12-pascal_triangle
Returns a list of lists of integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """Return Pascal's triangle of size n as a list of lists"""
    if n <= 0:
        return []

    triangle = [[1]]  # الصف الأول

    for i in range(1, n):
        prev_row = triangle[i - 1]
        # كل صف يبدأ وينتهي ب 1
        row = [1]
        # كل عنصر داخلي هو مجموع العنصرين فوقه
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)
        triangle.append(row)

    return triangle
