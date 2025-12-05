#!/usr/bin/python3
"""
This module contains the function text_indentation.
"""

def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: '.', '?', ':'

    Args:
        text (str): The text to print.

    Raises:
        TypeError: if text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ".?:"
    i = 0
    start = 0
    while i < len(text):
        if text[i] in separators:
            # Print up to current character, strip spaces
            print(text[start:i + 1].strip())
            print()  # first newline
            print()  # second newline
            start = i + 1  # next start after separator
        i += 1

    # Print remaining text after last separator if any
    remaining = text[start:].strip()
    if remaining:
        print(remaining)
