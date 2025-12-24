#!/usr/bin/python3
"""Function that returns the dictionary description of a class 
for JSON serialization
"""


def class_to_json(obj):
    """
    Returns the dictionary representation of obj's attributes

    Args:
        obj: instance of a class

    Returns:
        dict containing all attributes of obj
    """
    return obj.__dict__.copy()
