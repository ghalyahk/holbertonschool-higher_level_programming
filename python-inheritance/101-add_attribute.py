#!/usr/bin/python3
"""
This module defines a function `add_attribute` that adds a new attribute to an object
if the object allows it. Raises TypeError if the attribute cannot be added.
"""

def add_attribute(obj, name, value):
    """
    Adds a new attribute to an object if possible.

    Args:
        obj (any): The object to which the attribute will be added.
        name (str): The name of the attribute.
        value (any): The value to assign to the attribute.

    Raises:
        TypeError: If the object does not allow adding new attributes.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
