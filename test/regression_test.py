import unittest
from test.linter.linter import TestLint
from test.unit.parse_service_test import TestRealGMParser
from test.unit.selenium_service_test import TestWebDriverFactory, TestChromeDriver, TestFirefoxDriver
from test.unit.webscraper_utilities_test import TestWebKit, TestProxyKit
from unit.proxy_handler_test import TestProxyHandler
from unit.logger_test import TestLogger


def regression_test() -> unittest.TestSuite:
    """
    Compiles all unit tests into a single runnable regression test
    :return: test suite of all unit tests
    """
    test_suite = unittest.TestSuite()

    test_suite.addTests([
        unittest.TestLoader().loadTestsFromTestCase(TestLogger),
        # unittest.TestLoader().loadTestsFromTestCase(TestProxyHandler),
        unittest.TestLoader().loadTestsFromTestCase(TestWebKit),
        unittest.TestLoader().loadTestsFromTestCase(TestProxyKit),
        unittest.TestLoader().loadTestsFromTestCase(TestFirefoxDriver),
        unittest.TestLoader().loadTestsFromTestCase(TestChromeDriver),
        unittest.TestLoader().loadTestsFromTestCase(TestWebDriverFactory),
        unittest.TestLoader().loadTestsFromTestCase(TestRealGMParser)
    ])

    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(regression_test())

    TestLint.run_linter(exceptions=["parse_service_html.py", "regression_test.py", "main.py"])
