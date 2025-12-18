#!/usr/bin/python3
"""
This module defines a function `add_attribute` that adds a new attribute to an object
if the object allows it. Raises TypeError if the attribute cannot be added.
"""

def add_attribute(obj, name, value):
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
