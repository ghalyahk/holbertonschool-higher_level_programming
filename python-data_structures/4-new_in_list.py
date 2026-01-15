#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Return a new list with element replaced at index idx."""
    new_list = my_list.copy()

    if 0 <= idx < len(my_list):
        new_list[idx] = element

    return new_list
