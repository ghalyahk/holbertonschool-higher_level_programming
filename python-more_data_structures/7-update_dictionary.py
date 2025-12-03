#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """Update the dictionary with the key/value. Replace if exists, add if not."""
    a_dictionary[key] = value
    return a_dictionary
