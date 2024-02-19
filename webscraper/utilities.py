"""
This module provides utility classes for web scraping and proxy management.

Classes:
    WebKit: A utility class with methods for generating user agent headers, introducing random delays,
            and moving the mouse cursor.
    ProxyKit: A class for managing proxies used in web scraping, including initialization, random selection,
              validation, conversion, and rotating proxies.

Dependencies:
    - random: Module for generating random numbers and performing random selections.
    - re: Module for working with regular expressions for string pattern matching.
    - time: Module for time-related functions, including sleeping.
    - Logger: Custom logger class for logging events and errors.
    - ProxyHandler: Class for handling proxy-related operations such as loading from CSV files and processing.
    - requests: Module for making HTTP requests.
    - RequestException: Exception class for representing exceptions that occur during HTTP requests.
    - UserAgent: Class for generating random user agent strings.
    - ActionChains: Class for performing browser actions such as moving the mouse cursor.
    - webdriver: Module for controlling web browsers.
    - By: Class for locating elements by various strategies.
    - NoSuchElementException: Exception class for representing exceptions that occur when an element is not
      found.

Usage Example:
    # Import the WebKit and ProxyKit classes
    from module_name import WebKit, ProxyKit

    # Generate a random user agent header
    header = WebKit.new_header()

    # Introduce a random delay
    WebKit.random_delay(3, 7)

    # Move the mouse cursor to a specified HTML element
    WebKit.move_mouse_to_element(driver, '//div[@class="example"]')

    # Manage proxies for web scraping
    proxy_kit = ProxyKit(proxies_csv='proxy_list.csv', check_proxies=True)
    proxy = proxy_kit.pop_random_proxy()
    response = proxy_kit.apply_rotating_proxy(requests.get, 'https://example.com')

"""

import random
import re
import time
from typing import Optional, Callable, List
from log.logger import Logger
from webscraper.proxy.proxy_handler import ProxyHandler
import requests
from requests.exceptions import RequestException
from fake_useragent import UserAgent
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException


class WebKit:
    """
    Utility class providing various functions for web scraping and browser automation.

    Methods:
        new_header(): Generates a random user agent header string for HTTP requests.
        random_delay(min_sec: float = 2.8, max_sec: float = 5.6): Introduces a random delay in the scraping
        process.
        move_mouse_to_element(driver: webdriver, element_xpath: str): Moves the mouse cursor to a specified
        HTML element.
        move_mouse(driver): Attempts to move the mouse cursor to the first div element inside the body of a
        webpage.

    Attributes:
        None

    Usage Example:
        header = WebKit.new_header()
        WebKit.random_delay(3, 7)
        WebKit.move_mouse_to_element(driver, '//div[@class="example"]')
        WebKit.move_mouse(driver)
    """
    @staticmethod
    def new_header() -> str:
        """
        Provides a random header for callable function performing http request, in format:
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)
        Chrome/115.0.0.0 Safari/537.36'
        :return: random header string
        """
        ua = UserAgent()
        return ua.random

    @staticmethod
    def random_delay(min_sec: float = 2.8, max_sec: float = 5.6) -> None:
        """
        Introduces a random delay to the scrape process based on provided timeframe.
        :param min_sec: float for min seconds to way
        :param max_sec: float for max seconds to wait
        :return: None
        """
        delay = random.uniform(min_sec, max_sec)
        time.sleep(delay)

    @staticmethod
    def move_mouse_to_element(driver: webdriver, element_xpath: str) -> None:
        """
        Driver moves mouse to provided xpath element.
        :param driver: browser's webdriver instance
        :param element_xpath: xpath string for html element to move mouse to
        :return: None
        """
        first_div = driver.find_element(By.XPATH, element_xpath)
        action_chains = ActionChains(driver)
        action_chains.move_to_element(first_div).perform()

    @staticmethod
    def move_mouse(driver) -> None:
        """
        Driver attempts to move mouse to the first div inside the body. Should the div not exist,
        the driver opts for moving the mouse to the body tag fo the website's html.
        :param driver: browser's webdriver instance
        :return: None
        """
        try:
            WebKit.move_mouse_to_element(driver, '//body//div[1]')
        except NoSuchElementException:
            WebKit.move_mouse_to_element(driver, '//body')
        # pylint: disable=W0718
        except Exception as e:
            raise ValueError(f"WebKit.move_mouse encountered an error running driver {driver}: {e}") from e


class ProxyKit:
    """
    A class to manage proxies for web scraping.

    This class provides functionality to handle proxies, including initialization from a CSV file,
    randomly selecting and popping proxies from the list, validating proxy strings, converting proxy
    strings to dictionaries, and rotating proxies for web scraping.

    Attributes:
        proxy_list (List[str]): A list of proxy strings in the format '127.0.0.1:8080'.

    Methods:
        __init__: Initializes the ProxyKit instance by loading proxies from a CSV file.
        _initialize_proxy_list: Initializes the proxy list instance using ProxyHandler class.
        pop_random_proxy: Pops a random proxy from the proxy list.
        _load_proxy_str_to_dict: Restructures a proxy string as a dictionary usable by HTTP request callables.
        is_valid_proxy: Validates a proxy string format.
        proxy_to_dict: Checks proxy string validity and converts it to a proper dictionary format.
        apply_rotating_proxy: Iterates over the proxy list, popping potential proxies and rotating them for
        web scraping.

    """
    def __init__(self, proxies_csv: Optional[str], check_proxies: bool):
        self.proxy_list = self._initialize_proxy_list(proxies_csv, check_proxies)

    def _initialize_proxy_list(self, proxies_csv: Optional[str], check_proxies: bool) -> List[str]:
        """
        Initializes proxy list instance utilizing ProxyHandler class. The provided CSV file's
        proxies are converted into a list of strings. If check_proxies param is set to True the
        proxies are pre-checked by the ProxyHandler instance.
        :param proxies_csv: string for CSV file that contains proxies. ProxyHandler class
        handles CSVs where the first row is the header, the first column is the ip, and second
        column is the port.
        :param check_proxies: boolean indicating preference for the ProxyHandler pre-checking
        proxies before adding them to the list
        :return: list of proxy strings formatted with port: '127.0.0.1:8080'
        """
        if proxies_csv is None:
            return []
        handler = ProxyHandler(proxies_csv)
        if check_proxies and proxies_csv.endswith("csv"):
            return handler.process_proxies()

        return handler.load_proxies()

    def pop_random_proxy(self) -> str | None:
        """
        Pops a random proxy from the proxy list and returns it as str. If the list is empty
        it returns None.
        :return: roxy string | None if proxy list empty
        """
        try:
            i = random.randint(0, len(self.proxy_list) - 1)
            return self.proxy_list.pop(i)
        except (IndexError, ValueError):
            return None

    @staticmethod
    def _load_proxy_str_to_dict(proxy_str: str) -> dict:
        """
        Restructures proxy string as dict usable by http requesting callables.
        :param proxy_str: proxy string in format: '127.0.0.1:8080'
        :return: reformatted proxy string as dict
        """
        return {
            'http': f"{proxy_str}",
            'https': f"{proxy_str}"
        }

    @staticmethod
    def is_valid_proxy(proxy_address: str) -> bool:
        """
        Validates proxy string format.
        :param proxy_address: proxy string in format: '127.0.0.1:8080'
        :return: True for proper format, otherwise False
        """
        proxy_pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}:\d{1,5}$')
        if proxy_pattern.match(proxy_address):
            return True

        return False

    @staticmethod
    def proxy_to_dict(proxy: str) -> dict | None:
        """
        Function utilizes ProxyKit.is_valid_proxy to check proxy string validity, then
        ProxyKit._load_proxy_str_to_dict to convert to proper dict format.
        :param proxy: proxy string in format: '127.0.0.1:8080'
        :return: dict of proxy string | None if not proper proxy
        """
        if proxy and ProxyKit.is_valid_proxy(proxy):
            return ProxyKit._load_proxy_str_to_dict(proxy)

        return None

    def apply_rotating_proxy(self, function: Callable, url: str, *args, **kwargs) -> requests.Response | str:
        """
        Iterates over proxy list popping potential proxies. Successful proxies are placed back in the list
        for future use.
        :param function: chosen scrape function attempting to gather URL's html content.
        :param url: URL being scraped by callable
        :param args: positional args to pass to callable (scrape) function
        :param kwargs: keyword arguments to pass to callable (scrape) function
        :return: html content as str | response object containing html
        """
        log = Logger(log_file="app_test_log.log", name="PROXY KIT-ROTATION", log_level="INFO")
        while len(self.proxy_list) > 0:
            proxy = self.pop_random_proxy()

            try:
                log.info(f"apply rotating proxy: using proxy: {proxy}")

                # callable function passed as arg depending on chosen scrape strategy
                response = function(url, proxy, *args, **kwargs)
                if (isinstance(response, requests.Response) and response.status_code == 200) or \
                        (isinstance(response, str) and "<body>" in response):
                    # successful proxies are reassigned to proxy list for future use
                    self.proxy_list.append(proxy)
                    return response
            except RequestException as e:
                log.warning(f"ProxyKit.apply_rotating_proxy encountered an error while connecting to: {proxy}"
                            f" for {url}! {e}")
            # pylint: disable=W0718
            except Exception as e:
                log.warning(f"Exception during proxy rotation for request on {url}: {e}")

        raise ValueError("Connection could not be established for any proxy in the provided csv!")
