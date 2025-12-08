#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Return the sum of all unique integers in the list."""
    unique_numbers = set(my_list)
    return sum(unique_numbers)
