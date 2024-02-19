"""
Module: tests_webscraper_utilities.py

This module contains unit tests for the webscraper.utilities module.
"""

import random
import unittest
from unittest.mock import patch
from webscraper.utilities import WebKit, ProxyKit


class TestWebKit(unittest.TestCase):
    """
    Test case for the WebKit class in the webscraper.utilities module.
    """
    def test_new_header_not_empty_string(self):
        """
        Ensures header is a string that is not empty.
        :return: None
        """
        header = WebKit.new_header()
        self.assertIsInstance(header, str)
        self.assertTrue(header.strip())

    def test_new_header_browser(self):
        """
        Checks to make sure one of the browser types is in the header string.
        :return: None
        """
        header = WebKit.new_header()
        browsers = ['Mozilla', 'Chrome', 'Safari', 'Opera', 'Edge']
        found_browser = False
        for browser in browsers:
            if browser in header:
                found_browser = True
                break
        self.assertTrue(found_browser, f"At least one of {browsers} should be in the header")

    @patch('webscraper.utilities.time')
    def test_random_delay(self, mock_time):
        """
        Ensures function provides expected time delay.
        :param mock_time: mock time to simulate time.sleep
        :return: None
        """
        random.uniform = lambda a, b: 1.0
        WebKit.random_delay()
        mock_time.sleep.assert_called_once_with(1.0)


class TestProxyKit(unittest.TestCase):
    """
    Test case for the ProxyKit class in the webscraper.utilities module.
    """
    def test_initialize_proxy_list(self):
        """
        Tests proxy kit instantiation with mock data.
        :return: None
        """
        with unittest.mock.patch('webscraper.utilities.ProxyHandler') as mock_proxy_handler:
            mock_proxy_handler.return_value.load_proxies.return_value = ['proxy1', 'proxy2', 'proxy3']
            proxy_kit = ProxyKit(proxies_csv='mock_file.csv', check_proxies=False)
            self.assertEqual(proxy_kit.proxy_list, ['proxy1', 'proxy2', 'proxy3'])

    def test_pop_random_proxy(self):
        """
        Tests proxy list random popping of proxy.
        :return: None
        """
        proxy_kit = ProxyKit(proxies_csv='proxies_test.csv', check_proxies=False)
        proxy_kit.proxy_list = ['proxy1', 'proxy2', 'proxy3']
        random_proxy = proxy_kit.pop_random_proxy()
        self.assertIn(random_proxy, ['proxy1', 'proxy2', 'proxy3'])
        self.assertNotIn(random_proxy, proxy_kit.proxy_list)

    def test_load_proxy_str_to_dict(self):
        """
        Asserts proper encoding of proxy string to dictionary for requests use.
        :return: None
        """
        proxy_str = "127.0.0.1:8080"
        actual = ProxyKit._load_proxy_str_to_dict(proxy_str)
        expected = {
            'http': f"{proxy_str}",
            'https': f"{proxy_str}"
        }
        self.assertEqual(actual, expected)

    def test_is_valid_proxy_proper(self):
        """
        Ensures proper functionality of proxy string validation function.
        :return: None
        """
        proper = "127.0.0.1:8080"
        actual = ProxyKit.is_valid_proxy(proper)
        self.assertTrue(actual)

    def test_is_valid_proxy_improper(self):
        """
        Ensures proper functionality of proxy string validation through improper proxy test.
        :return: None
        """
        improper = "127.0.0.1"
        actual = ProxyKit.is_valid_proxy(improper)
        self.assertFalse(actual)

    def test_is_valid_ip_proper(self):
        """
        Ensures proper functionality of ip string validation function.
        :return: None
        """
        proper = "127.0.0.1"
        actual = ProxyKit.is_valid_ip(proper)
        self.assertTrue(actual)

    def test_is_valid_ip_improper(self):
        """
        Ensures proper functionality of ip string validation through improper proxy test.
        :return: None
        """
        improper = "127.0.0"
        actual = ProxyKit.is_valid_ip(improper)
        self.assertFalse(actual)

    def test_proxy_to_dict_proper(self):
        """
        Tests proxy conversion after proxy testing with correct parameters.
        :return: None
        """
        proper = "127.0.0.1:8080"
        actual = ProxyKit.proxy_to_dict(proper)
        expected = {
            'http': f"{proper}",
            'https': f"{proper}"
        }
        self.assertEqual(actual, expected)

    def test_proxy_to_dict_improper(self):
        """
        Tests proxy conversion after proxy testing with incorrect parameters.
        :return: None
        """
        improper = "127.0.0.1"
        actual = ProxyKit.proxy_to_dict(improper)
        self.assertEqual(actual, None)

    def test_proxy_to_dict_empty(self):
        """
        Tests proxy conversion after proxy testing with null parameters.
        :return: None
        """
        actual = ProxyKit.proxy_to_dict(None)
        self.assertEqual(actual, None)
