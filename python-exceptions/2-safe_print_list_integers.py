#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Print first x elements that are integers and return count."""
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError, IndexError):
            if isinstance(IndexError(), type(IndexError)):
                break
            continue
    print()
    return count
