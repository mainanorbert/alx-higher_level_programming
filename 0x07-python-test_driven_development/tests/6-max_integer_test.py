#!/usr/bin/python3
"""
imports module for unittest
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Defines Unit tests for max_integer([])"""

    def test_empty(self):
        """Test for empty array"""
        my_list = []
        self.assertEqual(max_integer(my_list), None)

    def test_floats(self):
        """Test for floating numbers"""
        my_list = [4.4, 3.5, 6.6, 2.5, 0.4, -2.2, 9.9]
        self.assertEqual(max_integer(my_list), 9.9)

    def test_strings(self):
        """Tests a case of strings"""
        my_list = ["Alice", "Ben", "Charles", "Nelius", "Zacheaus"]
        self.assertEqual(max_integer(my_list), "Zacheaus")

    def test_letters(self):
        """ Tests forletters arguments"""
        my_list = ["f", "e", "x"]
        self.assertEqual(max_integer(my_list), "x")

    def test_int_and_floats(self):
        """Function that tests integers and floats"""
        my_list = [4, 54.4, 5.5, 5.4, 43, 44.4, 33.32, 3]
        self.assertEqual(max_integer(my_list), 54.4)

    def test_orderd(self):
        """hecks for ordered integers"""
        my_list = [5, 4, 2]
        self.assertEqual(max_integer(my_list), 5)
    def test_unordered_numbers(self):
        """tests for unordered numbers"""
        my_list = [4, 4, 5, 62, 9]
        self.assertEqual(max_integer(my_list), 62)
    def test_zero(self):
        """tests for a zero"""
        my_list = [0]
        self.assertEqual(max_integer(my_list), 0)




if __name__ == '__main__':
    unittest.main()
