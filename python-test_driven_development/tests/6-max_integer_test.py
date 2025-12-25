#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_ordered_list(self):
        """Test an ordered list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test an unordered list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test when max is at the beginning"""
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)

    def test_max_at_end(self):
        """Test when max is at the end"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_one_element(self):
        """Test a list with one element"""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test an empty list"""
        self.assertIsNone(max_integer([]))

    def test_floats(self):
        """Test a list with floats"""
        self.assertEqual(max_integer([1.5, 2.3, 0.7]), 2.3)

    def test_mixed_int_float(self):
        """Test a list with ints and floats"""
        self.assertEqual(max_integer([1, 2.5, 3, 0.5]), 3)

    def test_negative_numbers(self):
        """Test a list with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_all_same(self):
        """Test a list where all numbers are the same"""
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

    def test_large_list(self):
        """Test a large list"""
        self.assertEqual(max_integer(list(range(1000))), 999)

if __name__ == "__main__":
    unittest.main()
