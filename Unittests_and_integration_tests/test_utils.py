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
from unittest.mock import MagicMock, patch, Mock
import utils
import requests

access_nested_map = __import__('utils').access_nested_map
memoize = __import__('utils').memoize


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


class TestGetJson(unittest.TestCase):
    """ Tests get json class """
    @parameterized.expand([
        # contains dict, path and expected value
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """returns Mock object with json meth that returns test_payload  """
        # create a mock object
        mock_object_expected = Mock()
        # configure the json method of the mock object
        mock_object_expected.json.return_value = test_payload

        # replace the requests get by a temp mock object
        with patch('utils.requests.get') as mock_request:
            mock_request.return_value = mock_object_expected
            # call get_json function
            result = utils.get_json(test_url)

            # check it
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """ test memoize class """
    def test_memoize(self):
        """ test memoize method """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        instance = TestClass()
        # replace the a_method by a temp mock object
        with patch.object(instance, 'a_method') as mock_object:
            # call a_property twice
            instance.a_property()
            instance.a_property()
            # call a_method once
            mock_object.assert_called_once()


if __name__ == '__main__':
    unittest.main()
