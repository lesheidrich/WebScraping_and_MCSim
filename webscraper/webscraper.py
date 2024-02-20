"""
Module: scraper_facade.py

This module provides a facade class for scraping web pages using various methods including
Selenium with Firefox or Chrome, and Requests library with or without proxies.

"""

from typing import Optional
import requests
from webscraper.selenium_service import WebDriverFactory
from webscraper.utilities import ProxyKit, WebKit


class ScraperFacade:
    """
    ScraperFacade class provides a high-level interface for scraping web pages using different methods
    including Selenium with Firefox or Chrome, and Requests library with or without proxies.

    Methods:
        - __init__(self, proxies_csv: Optional[str], check_proxies: bool = False)
        - firefox_selenium_scrape(self, url: str, proxy=None) -> str
        - firefox_selenium_proxy_scrape(self, url: str) -> str
        - chrome_selenium_scrape(self, url: str, proxy=None) -> str
        - chrome_selenium_proxy_scrape(self, url: str) -> str
        - requests_scrape(self, url: str, proxy: str = None, timeout=120) -> requests.Response
        - requests_proxy_scrape(self, url: str) -> requests.Response
    """
    def __init__(self, proxies_csv: Optional[str], check_proxies: bool = False):
        self.proxy_kit = ProxyKit(proxies_csv, check_proxies)

    def firefox_selenium_scrape(self, url: str, proxy=None) -> str:
        """
        Scrapes the given URL using Selenium with Firefox.
        :param url: str URL of website to scrape
        :param proxy: str of proxy to use (optional)
        :return: html content str
        """
        firefox = WebDriverFactory().firefox()
        WebKit.random_delay()
        result = firefox.return_content(url, proxy)
        del firefox
        return result

    def firefox_selenium_proxy_scrape(self, url: str) -> str:
        """
        Scrapes the given URL using Selenium with Firefox and a rotating proxy.
        :param url: str URL of website to scrape
        :return: html content str
        """
        return self.proxy_kit.apply_rotating_proxy(self.firefox_selenium_scrape, url)

    def chrome_selenium_scrape(self, url: str, proxy=None) -> str:
        """
        Scrapes the given URL using Selenium with Chrome.
        :param url: str URL of website to scrape
        :param proxy: str of proxy to use (optional)
        :return: html content str
        """
        chrome = WebDriverFactory().chrome()
        WebKit.random_delay()
        result = chrome.return_content(url, proxy)
        del chrome
        return result

    def chrome_selenium_proxy_scrape(self, url: str) -> str:
        """
        Scrapes the given URL using Selenium with Chrome and a rotating proxy.
        :param url: str URL of website to scrape
        :return: html content str
        """
        return self.proxy_kit.apply_rotating_proxy(self.chrome_selenium_scrape, url)

    def requests_scrape(self, url: str, proxy: str = None, timeout=120) -> requests.Response:
        """
        Scrapes the given URL using the Requests library.
        :param url: str URL of website to scrape
        :param proxy: str of proxy to use (optional)
        :param timeout: int of seconds for request timeout, default: 120 sec
        :return: Response obj, containing html content str
        """
        header = {'User-Agent': WebKit.new_header()}
        proxy_dict = ProxyKit.proxy_to_dict(proxy)
        WebKit.random_delay()
        return requests.get(url, headers=header, proxies=proxy_dict, timeout=timeout)

    def requests_proxy_scrape(self, url: str, timeout: int = 120) -> requests.Response:
        """
        Scrapes the given URL using the Requests library with a rotating proxy.
        :param timeout: int of seconds for request timeout, default: 120 sec
        :param url: str URL of website to scrape
        :return: Response obj, containing html content str
        """
        return self.proxy_kit.apply_rotating_proxy(self.requests_scrape, url, timeout=timeout)

    # def undetected_chrome_selenium_scrape(self, url: str, proxy=None):
    #     """
    #     Method intentionally left here for further testing. undetected_chrome has issues with
    #     deleting Chrome instances, it is therefore not used in the final version of this code
    #     currently. However, it will continue to be tested for possible solutions.
    #     :param url: str URL of website to scrape
    #     :param proxy: str of proxy to use (optional)
    #     :return: html content str
    #     """
    #     uc = WebDriverFactory().undetected_chrome()
    #     WebKit.random_delay()
    #     return uc.return_content(url, proxy)
    #
    # def undetected_chrome_selenium_scrape_proxy(self, url: str):
    #     """
    #     Method intentionally left here for further testing. undetected_chrome has issues with
    #     deleting Chrome instances, it is therefore not used in the final version of this code
    #     currently. However, it will continue to be tested for possible solutions.
    #     :param url: str URL of website to scrape
    #     :return: html content str
    #     """
    #     return self.proxy_kit.apply_rotating_proxy(self.undetected_chrome_selenium_scrape, url)
