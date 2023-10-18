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
from unittest.mock import MagicMock, patch, Mock, PropertyMock
from client import GithubOrgClient
import requests


class TestGithubOrgClient(unittest.TestCase):
    """ Test Github Org Client Class """
    @parameterized.expand([
        ("google", {"google": True}),
        ("abc", {"abc": True}),
    ])
    @patch('client.get_json')
    def test_org(self, org, expected, mock):
        # set mock
        """ Test the org of the client """
        mock.return_value = expected
        # GithubOrgClient instance
        client = GithubOrgClient(org)
        # check
        self.assertEqual(client.org, expected)
        # check that the function is called once
        mock.assert_called_once_with("https://api.github.com/orgs/" + org)

    @parameterized.expand([
        ("www.test1.com",),
        ("www.test2.com",),
    ])
    def test_public_repos_url(self, expected):
        # Create a dict with the expected values
        payload = {"repos_url": expected}

        # replace org property by mocked value
        with patch('client.GithubOrgClient.org',
                    new_callable=PropertyMock, return_value=payload):
            client = GithubOrgClient("test")

            # check _public_repos_url returns expected value
            self.assertEqual(client._public_repos_url, expected)


if __name__ == '__main__':
    unittest.main()



