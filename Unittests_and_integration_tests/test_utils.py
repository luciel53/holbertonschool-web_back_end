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
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), 2),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])

    def test_access_nested_map(self, nested_map, path):
        """ test access_nested_map """
        self.assertEqual(access_nested_map(nested_map, path))
