#!/usr/bin/python3
"""
Defines a BaseGeometry class with area and integer validation methods.
"""


class BaseGeometry:
    """BaseGeometry class."""

    def area(self):
        """
        Raises an Exception indicating that the area method
        is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is an integer greater than 0.

        Args:
            name (str): The name of the value.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
