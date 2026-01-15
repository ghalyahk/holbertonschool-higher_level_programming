#!/usr/bin/python3
"""Defines a class Square with size validation."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """
        Initialize a new square.

        Args:
            size (int): size of the square (default 0).

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size < 0.
        """
        self.size = size  # يستخدم الـ setter للتحقق من القيمة

    @property
    def size(self):
        """Retrieve the private size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the private size attribute with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
