#!/usr/bin/python3
"""
task_00_basic_serialization
A simple module to serialize a Python dictionary to a JSON file
and deserialize a JSON file back to a Python dictionary.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary and save it to a JSON file.

    Args:
        data (dict): Python dictionary to serialize
        filename (str): Name of the file to save the JSON data
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load JSON data from a file and deserialize it to a Python dictionary.

    Args:
        filename (str): Name of the JSON file to load

    Returns:
        dict: Python dictionary with the deserialized data
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
