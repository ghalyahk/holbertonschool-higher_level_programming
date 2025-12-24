#!/usr/bin/python3
"""Script that adds all arguments to a Python list and saves them to a JSON file"""

import sys
from python_input_output.save_to_json_file import save_to_json_file
from python_input_output.load_from_json_file import load_from_json_file

filename = "add_item.json"

# Load existing list from file if it exists
try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

# Add all arguments to the list (excluding script name)
items.extend(sys.argv[1:])

# Save updated list to the JSON file
save_to_json_file(items, filename)
