import unittest

from test.integration.control_service_test import TestScrapeControl
from test.unit.db_handler_test import TestMySQLHandler
from test.unit.dto_service_test import TestPersist
from test.unit.teams_test import TestTeams
from test.unit.webscraper_test import TestScraperFacade
from test.linter.linter import TestLint
from test.unit.parse_service_test import TestRealGMParser
from test.unit.selenium_service_test import TestWebDriverFactory, TestChromeDriver, TestFirefoxDriver
from test.unit.webscraper_utilities_test import TestWebKit, TestProxyKit
from unit.logger_test import TestLogger


def unittests() -> unittest.TestSuite:
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
        unittest.TestLoader().loadTestsFromTestCase(TestMySQLHandler),
        unittest.TestLoader().loadTestsFromTestCase(TestPersist)
    ])
    return test_suite


def integration_tests() -> unittest.TestSuite:
    """
    Compiles all integration tests into a single runnable integration test
    :return: test suite of all integration tests
    """
    integration_suite = unittest.TestSuite()

    integration_suite.addTests([
        unittest.TestLoader().loadTestsFromTestCase(TestScrapeControl)
    ])
    return integration_suite


if __name__ == '__main__':
    unit = unittest.TextTestRunner()
    integration = unittest.TextTestRunner()

    unit.run(unittests())
    # integration.run(integration_tests)

    TestLint.run_linter(exceptions=["parse_service_html.py", "regression_test.py", "main.py"])
