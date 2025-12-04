#!/usr/bin/python3
"""
Module for add_integer function.
Contains a function that adds two integers.
"""


def add_integer(a, b=98):
    """Adds two integers after validating types."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
