#!/usr/bin/python3
"""
Module that contains the function add_integer.
This function adds two integers after validating their types.
"""


def add_integer(a, b=98):
    """Adds two integers after validating types."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
