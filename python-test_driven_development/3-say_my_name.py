#!/usr/bin/python3
"""
Module to print a full name.
"""


def say_my_name(first_name, last_name):
    """
    Prints "My name is <first_name> <last_name>".

    Args:
        first_name (str): First name, must be a string.
        last_name (str): Last name, must be a string.

    Raises:
        TypeError: If either first_name or last_name is not a string.

    Example:
    >>> say_my_name("John", "Doe")
    My name is John Doe
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
