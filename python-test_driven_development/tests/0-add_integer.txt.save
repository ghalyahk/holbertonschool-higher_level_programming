#!/usr/bin/python3
"""
Module that contains the function add_integer.
This function adds two integers after validating their types.
"""


def add_integer(a, b=98):
    """Adds two integers after validating types.

    Args:
        a (int/float): First number.
        b (int/float, optional): Second number. Defaults to 98.

    Raises:
        TypeError: If a or b is not an int or float.

    Returns:
        int: Sum of a and b as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
