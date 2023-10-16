#!/usr/bin/env python3
""" tests utils"""


from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)
import unittest
from parameterized import parameterized
import utils

access_nested_map = __import__('utils').access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ TestAccessNestedMap class that inherits from unittest.TestCase """
    @parameterized.expand([
        # contains dict, path and expected value
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])

    def test_access_nested_map(self, nested_map, path, expected_result):
        """ checks if the result is equal to the expected result"""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        # contains dict, path and expected value
        ({}, ("a",), ""),
        ({"a": 1}, ("a", "b",), "Error msg"),
    ])

    def test_access_nested_map_exception(self, nested_map, path, expected_msg):
        """ check assertRaises exception """
        with self.assertRaises(Exception):
            access_nested_map(nested_map, path)
        exception_msg = "Error msg"
        self.assertEqual(exception_msg, expected_msg)


if __name__ == '__main__':
    unittest.main()
