#!/usr/bin/python3
"""
task_02_csv.py
Convert CSV data to JSON format.
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts a CSV file to JSON format and writes it to data.json.

    Args:
        csv_filename (str): Path to the CSV file.

    Returns:
        bool: True if conversion is successful, False if an error occurs.
    """
    try:
        with open(csv_filename, mode='r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        with open('data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except Exception:
        return False
