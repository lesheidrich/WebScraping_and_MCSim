import unittest

from webscraper.utilities import ProxyKit
from webscraper.webscraper import ScraperFacade


class TestScraperFacade(unittest.TestCase):
    def setUp(self):
        self.sc = ScraperFacade("proxies_full.csv", False)
        self.url = "https://www.icanhazip.com"
        self.ip = self.sc.requests_scrape(self.url, None).text

    def tearDown(self):
        del self.sc

    def test_ip_valid(self):
        self.assertTrue(ProxyKit.is_valid_ip(self.ip))

    def test_firefox_selenium_proxy_scrape(self):
        proxy_ip = self.sc.firefox_selenium_proxy_scrape(self.url)
        self.assertTrue(ProxyKit.is_valid_ip(proxy_ip))
        self.assertNotEqual(proxy_ip, self.ip, "Ip addresses should not be equal.")

    def test_chrome_selenium_proxy_scrape(self):
        proxy_ip = self.sc.chrome_selenium_proxy_scrape(self.url)
        self.assertTrue(ProxyKit.is_valid_ip(proxy_ip))
        self.assertNotEqual(proxy_ip, self.ip, "Ip addresses should not be equal.")

    def test_requests_proxy_scrape(self):
        proxy_ip = self.sc.requests_proxy_scrape(self.url).text
        self.assertTrue(ProxyKit.is_valid_ip(proxy_ip))
        self.assertNotEqual(proxy_ip, self.ip, "Ip addresses should not be equal.")

