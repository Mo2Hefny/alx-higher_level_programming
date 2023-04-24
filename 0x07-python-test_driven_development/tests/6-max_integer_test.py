#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
  """Suite test for max_integer function"""
  def test_empty_list(self):
      self.assertEqual(max_integer([]), None)
  def test_max_integer(self):
      self.assertEqual(max_integer([5, -2, 100, 3]), 100)
  def test_repeated_integer(self):
     self.assertEqual(max_integer([5, 100, 100, 3]), 100)
  def test_float_numbers(self):
      self.assertEqual(max_integer([4.8, 5.9, 5.1, 5]), 5.9)
  def test_negative_numbers(self):
      self.assertEqual(max_integer([-10, -9, -8, -7]), -7)
  def test_big_list(self):
        self.assertEqual(max_integer([
            901, 902, 903, 904, 905, 906, 907, 908, 909, 910,
            911, 912, 913, 914, 915, 916, 917, 918, 919, 920,
            919, 918, 917, 1000, 915, 914, 913, 912, 911, 910,
            909, 908, 907, 906, 905, 904, 903, 902, 901]), 1000)
  def test_one_number_in_a_list(self):
      self.assertEqual(max_integer([1]), 1)
  def test_not_a_list(self):
      with self.assertRaises(TypeError):
          max_integer(5)
  def test_not_all_numbers(self):
      with self.assertRaises(TypeError):
          max_integer([1, "2", (3, 4)])
  def test_dictionary(self):
      with self.assertRaises(KeyError):
          max_integer({'key1': 1, 'key2': 2})