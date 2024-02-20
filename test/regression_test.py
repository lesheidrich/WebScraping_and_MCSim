import unittest

from test.unit.db_handler_test import TestMySQLHandler
from test.unit.teams_test import TestTeams
from test.unit.webscraper_test import TestScraperFacade
from test.linter.linter import TestLint
from test.unit.parse_service_test import TestRealGMParser
from test.unit.selenium_service_test import TestWebDriverFactory, TestChromeDriver, TestFirefoxDriver
from test.unit.webscraper_utilities_test import TestWebKit, TestProxyKit
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
        unittest.TestLoader().loadTestsFromTestCase(TestRealGMParser),
        # unittest.TestLoader().loadTestsFromTestCase(TestScraperFacade),
        unittest.TestLoader().loadTestsFromTestCase(TestTeams),
        unittest.TestLoader().loadTestsFromTestCase(TestMySQLHandler)
    ])
    return test_suite


def integration_test() -> unittest.TestSuite:
    """
    Compiles all integration tests into a single runnable integration test
    :return: test suite of all integration tests
    """
    integration_suite = unittest.TestSuite()

    integration_suite.addTests([
        unittest.TestLoader().loadTestsFromTestCase()
    ])
    return integration_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(regression_test())

    TestLint.run_linter(exceptions=["parse_service_html.py", "regression_test.py", "main.py"])
