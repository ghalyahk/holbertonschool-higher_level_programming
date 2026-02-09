#!/usr/bin/python3
"""
Defines a Rectangle class that inherits from BaseGeometry,
implements area and string representation.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inheriting from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a Rectangle with validated width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the rectangle description as a string."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
