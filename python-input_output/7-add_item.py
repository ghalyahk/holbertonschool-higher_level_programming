#!/usr/bin/python3
"""
7-add_item
This script adds all arguments to a Python list and saves them to a JSON file.
"""
import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

FILENAME = "add_item.json"

if __name__ == "__main__":
    # Attempt to load existing items from the JSON file
    try:
        items = load_from_json_file(FILENAME)
    except (FileNotFoundError, ValueError):
        items = []

    # Add all arguments passed to the script to the list
    items.extend(sys.argv[1:])

    # Save updated list back to the JSON file
    save_to_json_file(items, FILENAME)
