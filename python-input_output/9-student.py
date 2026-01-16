#!/usr/bin/python3
"""Module that defines a Student class"""


class Student:
    """Student class with first_name, last_name, and age"""

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance

        Args:
            first_name (str): first name of the student
            last_name (str): last name of the student
            age (int): age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of the Student instance

        Returns:
            dict: dictionary with all attributes of the student
        """
        return self.__dict__.copy()
