#!/usr/bin/env python3
""" tests client """


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
from client import GithubOrgClient
import requests


class TestGithubOrgClient(unittest.TestCase):
    """ Test Github Org Client Class """
    @parameterized.expand([
        ("https://api.github.com/orgs/google"),
        ("https://api.github.com/abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org, mock, expected):
        """ test org """
        client = client.GitHubOrgClient(org)
        mock.return_value = expected

        result = org()

        mock.assert_called_once_with("https://api.github.com/orgs/{org}")

        self.assertEqual(result, expected)




