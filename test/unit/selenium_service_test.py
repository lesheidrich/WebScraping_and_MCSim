"""
selenium_service_test Module:

This module contains unit tests for the Selenium service, including tests for the FirefoxDriver,
ChromeDriver, and WebDriverFactory classes.

The Selenium service provides functionality for web scraping and interaction with web browsers
using Selenium WebDriver.

Classes:
    - TestFirefoxDriver: A unittest class for testing the FirefoxDriver class.
    - TestChromeDriver: A unittest class for testing the ChromeDriver class.
    - TestWebDriverFactory: A unittest class for testing the WebDriverFactory class.

Each unittest class contains test cases to verify specific functionalities of the respective
classes, including setup of options, content retrieval, and handling of connection errors.
"""

import unittest
from unittest.mock import patch
from webscraper.selenium_service import FirefoxDriver, WebDriver, ChromeDriver, WebDriverFactory
from selenium.webdriver import FirefoxOptions, ChromeOptions


class TestFirefoxDriver(unittest.TestCase):
    """
    A unittest class for testing the FirefoxDriver class.

    This class contains test cases to verify the functionality of the FirefoxDriver class,
    including the setup of options, content retrieval, and handling of connection errors.

    Methods:
        setUp: Initializes a FirefoxDriver instance before each test case.
        tearDown: Deletes the FirefoxDriver instance after each test case.
        test_setup_options: Verifies the setup_options method of FirefoxDriver.
        test_return_content: Checks the return_content method of FirefoxDriver.
        test_return_content_connection_error: Tests the behavior of return_content
            method when encountering a ConnectionError.
    """
    def setUp(self):
        self.driver = FirefoxDriver()

    def tearDown(self):
        del self.driver

    def test_setup_options(self):
        """
        Verifies that the _setup_options method correctly initializes options
        for the WebDriver instance. It ensures that the returned options object is an
        instance of FirefoxOptions.
        :return: None
        """
        options = self.driver._setup_options()
        self.assertIsInstance(options, FirefoxOptions)

    def test_return_content(self):
        """
        Checks whether the return_content method returns the expected content
        from a mocked website. It patches the _return_and_quit method to simulate a successful
        retrieval of content from a URL and compares the returned content with the expected
        content.
        :return: None
        """
        expected_content = "<html><body><h1>Hello, World!</h1></body></html>"
        with patch.object(WebDriver, '_return_and_quit', return_value=expected_content):
            content = self.driver.return_content("https://mock_site.com")
        self.assertEqual(content, expected_content)

    def test_return_content_connection_error(self):
        """
        Verifies the behavior of the return_content method when a ConnectionError
        is raised during the attempt to retrieve content from a URL. It patches the _return_and_quit
        method to simulate a ConnectionError and ensures that the method raises a ConnectionError
        exception.
        :return: None
        """
        with patch.object(WebDriver, '_return_and_quit', side_effect=ConnectionError):
            with self.assertRaises(ConnectionError):
                self.driver.return_content("https://mock_site.com")


class TestChromeDriver(unittest.TestCase):
    """
    A unittest class for testing the ChromeDriver class.

    This class contains test cases to verify the functionality of the ChromeDriver class,
    including the setup of options, content retrieval, and handling of connection errors.

    Methods:
        setUp: Initializes a ChromeDriver instance before each test case.
        tearDown: Deletes the ChromeDriver instance after each test case.
        test_setup_options: Verifies the setup_options method of ChromeDriver.
        test_return_content: Checks the return_content method of ChromeDriver.
        test_return_content_connection_error: Tests the behavior of return_content
            method when encountering a ConnectionError.
    """
    def setUp(self):
        self.driver = ChromeDriver()

    def tearDown(self):
        del self.driver

    def test_setup_options(self):
        """
        Verifies that the _setup_options method correctly initializes options
        for the WebDriver instance. It ensures that the returned options object is an
        instance of ChromeOptions.
        :return: None
        """
        options = self.driver._setup_options()
        self.assertIsInstance(options, ChromeOptions)

    def test_return_content(self):
        """
        Checks whether the return_content method returns the expected content
        from a mocked website. It patches the _return_and_quit method to simulate a successful
        retrieval of content from a URL and compares the returned content with the expected
        content.
        :return: None
        """
        expected_content = "<html><body><h1>Hello, World!</h1></body></html>"
        with patch.object(WebDriver, '_return_and_quit', return_value=expected_content):
            content = self.driver.return_content("https://mock_site.com")
        self.assertEqual(content, expected_content)

    def test_return_content_connection_error(self):
        """
        Verifies the behavior of the return_content method when a ConnectionError
        is raised during the attempt to retrieve content from a URL. It patches the _return_and_quit
        method to simulate a ConnectionError and ensures that the method raises a ConnectionError
        exception.
        :return: None
        """
        with patch.object(WebDriver, '_return_and_quit', side_effect=ConnectionError):
            with self.assertRaises(ConnectionError):
                self.driver.return_content("https://mock_site.com")


class TestWebDriverFactory(unittest.TestCase):
    """
    Unit tests for the WebDriverFactory class.

    This test suite verifies the functionality of the WebDriverFactory class, specifically
    its ability to create instances of different WebDriver subclasses like FirefoxDriver and ChromeDriver.

    Methods:
        test_firefox_factory: Ensures that the WebDriverFactory correctly creates a FirefoxDriver instance.
        test_chrome_factory: Ensures that the WebDriverFactory correctly creates a ChromeDriver instance.
    """
    def test_firefox_factory(self):
        """
        Ensures that the WebDriverFactory correctly creates a FirefoxDriver instance
        :return: None
        """
        driver = WebDriverFactory.firefox()
        self.assertIsInstance(driver, FirefoxDriver)
        del driver

    def test_chrome_factory(self):
        """
        Ensures that the WebDriverFactory correctly creates a ChromeDriver instance
        :return: None
        """
        driver = WebDriverFactory.chrome()
        self.assertIsInstance(driver, ChromeDriver)
        del driver
