#!/usr/bin/python3
"""
task_03_xml.py
Serialize and deserialize Python dictionaries to/from XML.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The XML file to write to.
    """
    root = ET.Element('data')  # Create root element

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)  # Convert value to string

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize an XML file into a Python dictionary.

    Args:
        filename (str): The XML file to read from.

    Returns:
        dict: The reconstructed Python dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}
        for child in root:
            result[child.tag] = child.text  # All values are strings

        return result
    except Exception:
        return {}
