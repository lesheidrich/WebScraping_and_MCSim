"""
Module: test_scraper_facade.py

This module contains unit tests for the ScraperFacade class in the webscraper package.
"""

import unittest
from webscraper.utilities import ProxyKit
from webscraper.webscraper import ScraperFacade


class TestScraperFacade(unittest.TestCase):
    """
    Test case class for the ScraperFacade class.
    Tests utilize live scraping with https://www.icanhazip.com, a website
    that returns the requesting ip address.
    """
    def setUp(self):
        self.sc = ScraperFacade("proxies_full.csv", False)
        self.url = "https://www.icanhazip.com"
        self.ip = self.sc.requests_scrape(self.url, None).text

    def tearDown(self):
        del self.sc

    def test_ip_valid(self):
        """
        Asserts initialized ip address of pc for comparison purposes.
        :return: None
        """
        self.assertTrue(ProxyKit.is_valid_ip(self.ip))

    def test_requests_scrape(self):
        """
        Ensures requests_scrape() returns correct result.
        :return: None
        """
        ip = self.sc.requests_scrape(self.url).text
        self.assertTrue(ProxyKit.is_valid_ip(ip))

    def test_firefox_selenium_scrape(self):
        """
        Ensures firefox_selenium_scrape() returns correct result.
        :return: None
        """
        result = self.sc.firefox_selenium_scrape(self.url)
        self.assertTrue(self.ip in result)

    def test_chrome_selenium_scrape(self):
        """
        Ensures chrome_selenium_scrape() returns correct result.
        :return: None
        """
        result = self.sc.chrome_selenium_scrape(self.url)
        self.assertTrue(self.ip in result)

    def test_requests_proxy_scrape(self):
        """
        Ensures requests_proxy_scrape() returns correct result.
        Checks proxy masking based on result.
        Test method's timeout has been sped up, but it can still have a long running time.
        :return: None
        """
        proxy_ip = self.sc.requests_proxy_scrape(self.url, timeout=1).text
        self.assertTrue(ProxyKit.is_valid_ip(proxy_ip))
        self.assertNotEqual(proxy_ip, self.ip, "Ip addresses should not be equal.")

    # def test_firefox_selenium_proxy_scrape(self):
    #     """
    #     Ensures firefox_selenium_proxy_scrape() returns correct result.
    #     Checks proxy masking based on result.
    #     Test method has a very long running time. Should only be used when necessary.
    #     :return: None
    #     """
    #     result = self.sc.firefox_selenium_proxy_scrape(self.url)
    #     print(result)
    #     self.assertIn("<html>", result)
    #     self.assertTrue(self.ip not in result)
    #
    # def test_chrome_selenium_proxy_scrape(self):
    #     """
    #     Ensures chrome_selenium_proxy_scrape() returns correct result.
    #     Checks proxy masking based on result.
    #     Test method has a very long running time. Should only be used when necessary.
    #     :return: None
    #     """
    #     result = self.sc.chrome_selenium_proxy_scrape(self.url)
    #     print(result)
    #     self.assertIn("<html>", result)
    #     self.assertTrue(self.ip not in result)
