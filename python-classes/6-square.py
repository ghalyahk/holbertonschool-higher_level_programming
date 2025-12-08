#!/usr/bin/python3
"""Defines a class Square with size, position, area and print methods"""

class Square:
    """Represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square with optional size and position"""
        self.size = size        # يستخدم setter للتحقق
        self.position = position  # يستخدم setter للتحقق

    @property
    def size(self):
        """Retrieve the private size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the private size attribute with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the private position attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the private position attribute with validation"""
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Print the square using # characters respecting position"""
        if self.__size == 0:
            print("")
            return

        # Print blank lines for position[1]
        for _ in range(self.__position[1]):
            print("")

        # Print each row of the square
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
