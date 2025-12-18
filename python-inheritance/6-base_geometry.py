#!/usr/bin/python3
"""
Defines a BaseGeometry class with an unimplemented area method.
"""


class BaseGeometry:
    """BaseGeometry class."""

    def area(self):
        """
        Raises an Exception indicating that the area method
        is not implemented.
        """
        raise Exception("area() is not implemented")
