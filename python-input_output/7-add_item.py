#!/usr/bin/python3
"""
This script adds all arguments to a Python list,
then saves them to a JSON file named add_item.json.
"""

import sys
import json
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

FILENAME = "add_item.json"

if __name__ == "__main__":
    try:
        items = load_from_json_file(FILENAME)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        items = []

    # Add all command-line arguments to the list
    items.extend(sys.argv[1:])

    # Save updated list back to the file
    save_to_json_file(items, FILENAME)
