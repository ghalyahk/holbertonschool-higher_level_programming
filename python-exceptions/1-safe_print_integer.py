#!/usr/bin/python3
def safe_print_integer(value):
    """Print an integer safely using '{:d}'.format() and return True/False."""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
