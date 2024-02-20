"""
Module: selenium_service.py:

A module containing WebDriver classes for interacting with web browsers using Selenium.

This module defines abstract base class `WebDriver`, along with its concrete subclasses `FirefoxDriver`
and `ChromeDriver`,
for configuring and interacting with Firefox and Chrome web drivers respectively.
It also provides a `WebDriverFactory` class for creating instances of WebDriver subclasses.

Classes:
    WebDriver: An abstract base class representing a WebDriver.
    FirefoxDriver: A class representing a Firefox web driver.
    ChromeDriver: A class representing a Chrome web driver.
    WebDriverFactory: A factory class for creating instances of WebDriver subclasses.
"""

from abc import ABC, abstractmethod
from typing import Optional, Any
from selenium.webdriver import Firefox, FirefoxProfile, FirefoxOptions, ChromeOptions, Chrome
from selenium.webdriver.common.by import By
# import undetected_chromedriver as uc
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webscraper.utilities import WebKit


class WebDriver(ABC):
    """
    An abstract base class representing a WebDriver.

    This class defines abstract methods and helper methods common to all WebDriver subclasses,
    such as setting up options, setting up a proxy, and returning content from a URL.

    Methods:
        _setup_options: Abstract method to set up options for the WebDriver instance.
        _setup_proxy: Abstract method to set up a proxy for the WebDriver instance.
        return_content: Abstract method to return content from a URL.
        _scrape_page_source: Helper method to scrape page source from a URL using the WebDriver instance.
        _return_and_quit: Helper method to return page source and quit the WebDriver instance.
    """
    @abstractmethod
    def _setup_options(self) -> Options:
        """
        Abstract method to set up options for the WebDriver instance.
        :return: options configured for the WebDriver
        """

    @abstractmethod
    def _setup_proxy(self, options: Any, proxy_address: Optional[str] = None) -> None:
        """
        Abstract method to set up a proxy for the WebDriver instance.
        :param options: options object to configure with the proxy settings
        :param proxy_address: proxy str address, formatted: '127.0.0.1:8080'. Defaults to None
        :return: None
        """

    @abstractmethod
    def return_content(self, url: str, proxy_address: Optional[str] = None) -> str:
        """
        Abstract method to return content from a URL using the WebDriver instance.
        :param url: URL string to retrieve content from, format: 'https://www.icanhazip.com'
        :param proxy_address: proxy str address, formatted: '127.0.0.1:8080', defaults to None
        :return: html content string
        """

    def _scrape_page_source(self, driver: Any, url) -> str:
        """
        Helper method to scrape page source from a URL using the WebDriver instance.
        :param driver: WebDriver instance
        :param url: URL string to retrieve content from, format: 'https://www.icanhazip.com'
        :return: page source of the URL
        """
        driver.get(url)
        wait = WebDriverWait(driver, 90)  # max wait time
        wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        WebKit.move_mouse(driver)
        return driver.page_source

    def _return_and_quit(self, driver: Any, url: str) -> str:
        """
        Helper method to return page source and quit the WebDriver instance.
        :param driver: WebDriver instance
        :param url: URL string to retrieve content from, format: 'https://www.icanhazip.com'
        :return: html content string
        """
        try:
            return self._scrape_page_source(driver, url)
        except Exception as e:
            raise ConnectionError(f"WebDriver._scrape_page_source encountered an error while "
                                  f"attempting to scrape {url} with {driver}: {e}") from e
        finally:
            if driver:
                driver.quit()


class FirefoxDriver(WebDriver):
    """
    A class representing a Firefox web driver.

    This class extends the abstract base class WebDriver and implements methods
    specific to configuring and interacting with a Firefox web driver.

    Methods:
        _setup_options: Sets up the options for the Firefox web driver.
        _setup_proxy: Configures proxy settings for the Firefox web driver.
        return_content: Retrieves the content of a web page using the Firefox web driver.
    """
    def _setup_options(self) -> FirefoxOptions:
        """
        Sets up the options for the Firefox web driver.
        :return: Firefox driver setup config
        """
        firefox_options = FirefoxOptions()
        firefox_options.set_preference("general.useragent.override", WebKit.new_header())
        firefox_options.set_preference("dom.webdriver.enabled", False)
        firefox_options.set_preference('useAutomationExtension', False)
        firefox_options.add_argument("--headless")
        return firefox_options

    def _setup_proxy(self, options, proxy_address: Optional[str] = None) -> None:
        """
        Configures proxy settings for the Firefox web driver.
        :param options: FirefoxOptions instance to set up proxy settings for
        :param proxy_address: proxy str address, formatted: '127.0.0.1:8080'. Defaults to None.
        :return: None
        """
        firefox_profile = FirefoxProfile()
        firefox_profile.set_preference("network.proxy.type", 1)
        firefox_profile.set_preference("network.proxy.http", proxy_address.split(":")[0])
        firefox_profile.set_preference("network.proxy.http_port", int(proxy_address.split(":")[1]))
        firefox_profile.set_preference("network.proxy.ssl", proxy_address.split(":")[0])
        firefox_profile.set_preference("network.proxy.ssl_port", int(proxy_address.split(":")[1]))
        options.profile = firefox_profile

    def return_content(self, url: str, proxy_address: Optional[str] = None) -> str:
        """
        Retrieves the content of a web page using the Firefox web driver.
        :param url: URL string to retrieve content from, format: 'https://www.icanhazip.com'
        :param proxy_address: proxy str address, formatted: '127.0.0.1:8080'
        :return: html content string
        """
        firefox_options = self._setup_options()
        if proxy_address:
            self._setup_proxy(firefox_options, proxy_address)

        firefox_driver = Firefox(options=firefox_options)
        try:
            return self._return_and_quit(firefox_driver, url)
        finally:
            firefox_driver.quit()


class ChromeDriver(WebDriver):
    """
    A class representing a Chrome web driver.

    This class extends the abstract base class WebDriver and implements methods
    specific to configuring and interacting with a Chrome web driver.

    Methods:
        _setup_options: Sets up the options for the Chrome web driver.
        _setup_proxy: Configures proxy settings for the Chrome web driver.
        return_content: Retrieves the content of a web page using the Chrome web driver.
    """
    def _setup_options(self) -> ChromeOptions:
        """
        Sets up the options for the Chrome webdriver.
        :return: setup config for Chrome webdriver
        """
        chrome_options = ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument(f"--user-agent={WebKit.new_header()}")
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--disable-notifications')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--mute-audio')
        chrome_options.add_argument('--ignore-certificate-errors')
        return chrome_options

    def _setup_proxy(self, options, proxy_address: Optional[str] = None) -> None:
        """
        Configures proxy settings for the Chrome web driver.
        :param options: ChromeOptions instance to set up proxy settings for
        :param proxy_address: proxy str address, formatted: '127.0.0.1:8080'. Defaults to None.
        :return: None
        """
        if proxy_address:
            options.add_argument(f"--proxy-server={proxy_address}")

    def return_content(self, url: str, proxy_address: Optional[str] = None) -> str:
        """
        Retrieves the content of a web page using the Chrome web driver.
        :param url: URL string to retrieve content from, format: 'https://www.icanhazip.com'
        :param proxy_address: proxy str address, formatted: '127.0.0.1:8080'
        :return: html content string
        """
        chrome_options = self._setup_options()
        self._setup_proxy(chrome_options, proxy_address)
        chrome_driver = Chrome(options=chrome_options)
        try:
            return self._return_and_quit(chrome_driver, url)
        finally:
            chrome_driver.quit()


# class UndetectedChromeDriver(WebDriver):
# """
#     Class is functional. It has been commented out and left here because the imported module
#     produces OS errors. Driver instances are not cleaned up, and module is not fully compatible
#     with other python modules. The source code has been left here for further testing.
# """
#     def _setup_options(self) -> ChromeOptions:
#         uc_options = uc.ChromeOptions()
#         uc_options.headless = True
#         uc_options.add_argument('--blink-settings=imagesEnabled=false')
#         return uc_options
#
#     def _setup_proxy(self, options, proxy_address: Optional[str] = None) -> dict:
#         return {'proxy': {'http': f'http://{proxy_address}',
#                           'https': f'https://{proxy_address}'}}
#
#     def return_content(self, url: str, proxy_address: Optional[str] = None) -> str:
#         uc_options = self._setup_options()
#         if proxy_address:
#             proxy_options = self._setup_proxy(uc_options, proxy_address)
#             uc_driver = uc.Chrome(options=uc_options, seleniumwire_options=proxy_options)
#         else:
#             uc_driver = uc.Chrome(options=uc_options)
#
#         return self._return_and_quit(uc_driver, url)


class WebDriverFactory:
    """
    A factory class for creating instances of WebDriver subclasses.

    This class provides static methods for creating instances of WebDriver subclasses,
    such as FirefoxDriver and ChromeDriver.

    Methods:
        firefox: Creates an instance of FirefoxDriver.
        chrome: Creates an instance of ChromeDriver.
    """
    @staticmethod
    def firefox() -> WebDriver:
        """
        Creates an instance of FirefoxDriver.
        :return: Firefox driver instance
        """
        return FirefoxDriver()

    @staticmethod
    def chrome() -> WebDriver:
        """
        Creates an instance of ChromeDriver.
        :return: Chrome driver instance
        """
        return ChromeDriver()

    # @staticmethod
    # def undetected_chrome() -> WebDriver:
    # see UndetectedChromeDriver class docstring
    #     return UndetectedChromeDriver()
