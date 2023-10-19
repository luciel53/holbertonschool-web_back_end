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

    @parameterized.expand([
        ("www.test1.com", {"name": "repo1", "content": "my contain"}),
        ("www.test2.com", {"name": "repo2", "content": "another content"}),
    ])
    @patch('client.get_json')
    def test_public_repos(self, public_repos_url, payload, json_mock):
        """ Test public repositories method """
        # Set the return value for the mocked property
        json_mock.return_value = payload

        # Set the return value for the mocked _public_repos_url
        mock_public_repos_url = PropertyMock(return_value=public_repos_url)

        # Patch the _public_repos_url property with the mocked value
        with patch('client.GithubOrgClient._public_repos_url', mock_public_repos_url):
            client = GithubOrgClient("test_org")
            result = client.public_repos()

            # Verify that the result matches the payload
            self.assertEqual(result, payload)

            # Verify that the mocked property and get_json were called once
            mock_public_repos_url.assert_called_once()
            json_mock.assert_called_once()


if __name__ == '__main__':
    unittest.main()



