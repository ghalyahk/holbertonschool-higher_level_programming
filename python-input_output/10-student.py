#!/usr/bin/python3
"""Module that defines a Student class with to_json method supporting attrs"""


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

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance

        Args:
            attrs (list, optional): list of attribute names to retrieve.
                                    If None, all attributes are retrieved.

        Returns:
            dict: dictionary containing the requested attributes
        """
        if attrs is None:
            return self.__dict__.copy()
        else:
            return {key: value for key, value in self.__dict__.items() if key in attrs}
