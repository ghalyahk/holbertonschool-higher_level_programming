#!/usr/bin/python3
"""
7-add_item.py
Adds all command-line arguments to a Python list and saves them to a JSON file.
"""

import sys
import json
from pathlib import Path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

FILENAME = "add_item.json"

# Try loading existing list, or start with empty list if file doesn't exist or is empty
try:
    items = load_from_json_file(FILENAME)
except (FileNotFoundError, json.JSONDecodeError):
    items = []

# Add command-line arguments to the list
items.extend(sys.argv[1:])

# Save updated list back to file
save_to_json_file(items, FILENAME)
