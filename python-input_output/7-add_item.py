#!/usr/bin/python3
"""
7-add_item.py
Adds all arguments to a Python list and saves them to a JSON file.
"""

import sys
from pathlib import Path

# Import helper functions
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

FILENAME = "add_item.json"

# Load existing items if file exists, else start with empty list
if Path(FILENAME).exists():
    items = load_from_json_file(FILENAME)
else:
    items = []

# Add command-line arguments to the list
items.extend(sys.argv[1:])

# Save updated list back to file
save_to_json_file(items, FILENAME)
