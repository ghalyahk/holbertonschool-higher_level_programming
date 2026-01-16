#!/usr/bin/python3
"""
task_01_pickle.py
Serialization and deserialization of a custom Python object using pickle
"""

import pickle


class CustomObject:
    """A class representing a custom object with name, age, and is_student attributes."""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints the object’s attributes in the required format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the object and save it to a file using pickle.
        Returns None on error.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            # Could log the exception e if needed
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize a CustomObject instance from a file using pickle.
        Returns the object, or None if an error occurs.
        """
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
            if isinstance(obj, cls):
                return obj
            return None
        except Exception:
            return None
