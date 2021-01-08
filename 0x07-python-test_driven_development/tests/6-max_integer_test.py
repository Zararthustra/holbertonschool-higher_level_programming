#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittest class"""
    def tests_ok(self):
        """tests that have to work"""
        self.assertAlmostEqual(max_integer([0, 1, 2, 3]), 3)
        self.assertAlmostEqual(max_integer([0, 1, 3, 2]), 3)
        self.assertAlmostEqual(max_integer([3]), 3)
        self.assertAlmostEqual(max_integer([]), None)

    def tests_fail(self):
        """tests that have to fail"""
        self.assertRaises(TypeError, max_integer, [0, 1, "string", 3])
        self.assertRaises(TypeError, max_integer, None)
