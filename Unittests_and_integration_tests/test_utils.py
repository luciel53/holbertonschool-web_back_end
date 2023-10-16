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
        ({}, ("a",), "Key not found"),
        ({"a": 1}, ("a", "b",), "Key not found"),
    ])

    def test_access_nested_map_exception(self, nested_map, path, expected_msg):
        """ check assertRaises exception """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
        exception_msg = "Key not found"
        self.assertEqual(exception_msg, expected_msg)


if __name__ == '__main__':
    unittest.main()
