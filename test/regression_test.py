"""
Module: regression_test.py

Module is a regression test containing unit-test test cases and integration-test test cases as runnable
suites, as well as a full program lint.

NOTICE:
    * Scrape testing with proxies can run for extended time periods, depending on proxy availability.
    * Selenium-based proxy scrapers have even longer runtimes, and are therefore commented out when not in
      use. Average test times are around 2 hours when enabled.

WARNING:
    * Integration tests contain live scraper functions. Please make sure your VPN is turned on!
    * Built in proxies applied during testing have not been vetted or validated to ensure anonymity!
"""

import os
import unittest
from test.integration.control_service_test import TestScrapeControl
from test.integration.monte_carlo_test import TestMonteCarlo
from test.unit.db_handler_test import TestMySQLHandler
from test.unit.dto_service_test import TestPersist
from test.unit.dto_sim_test import TestTeamBuilder
from test.unit.game_service_test import TestGameBuilder
from test.unit.proxy_handler_test import TestProxyHandler
from test.unit.teams_test import TestTeams
from test.unit.webscraper_test import TestScraperFacade
from test.linter.linter import TestLint
from test.unit.parse_service_test import TestRealGMParser
from test.unit.selenium_service_test import TestWebDriverFactory, TestChromeDriver, TestFirefoxDriver
from test.unit.webscraper_utilities_test import TestWebKit, TestProxyKit
from unit.logger_test import TestLogger
from project_secrets import Hidden


def unittests() -> unittest.TestSuite:
    """
    Compiles all unit tests into a single runnable regression test
    :return: test suite of all unit tests
    """
    test_suite = unittest.TestSuite()

    test_suite.addTests([
        unittest.TestLoader().loadTestsFromTestCase(TestLogger),
        unittest.TestLoader().loadTestsFromTestCase(TestProxyHandler),
        unittest.TestLoader().loadTestsFromTestCase(TestWebKit),
        unittest.TestLoader().loadTestsFromTestCase(TestProxyKit),
        unittest.TestLoader().loadTestsFromTestCase(TestFirefoxDriver),
        unittest.TestLoader().loadTestsFromTestCase(TestChromeDriver),
        unittest.TestLoader().loadTestsFromTestCase(TestWebDriverFactory),
        unittest.TestLoader().loadTestsFromTestCase(TestRealGMParser),
        unittest.TestLoader().loadTestsFromTestCase(TestScraperFacade),
        unittest.TestLoader().loadTestsFromTestCase(TestTeams),
        unittest.TestLoader().loadTestsFromTestCase(TestMySQLHandler),
        unittest.TestLoader().loadTestsFromTestCase(TestPersist),
        unittest.TestLoader().loadTestsFromTestCase(TestTeamBuilder),
        unittest.TestLoader().loadTestsFromTestCase(TestGameBuilder)
    ])
    return test_suite


def integration_tests() -> unittest.TestSuite:
    """
    Compiles all integration tests into a single runnable integration test
    :return: test suite of all integration tests
    """
    integration_suite = unittest.TestSuite()

    integration_suite.addTests([
        unittest.TestLoader().loadTestsFromTestCase(TestScrapeControl),
        unittest.TestLoader().loadTestsFromTestCase(TestMonteCarlo)
    ])
    return integration_suite


if __name__ == '__main__':
    Hidden.set_project_folder(os.path.dirname(os.getcwd()))

    unit = unittest.TextTestRunner()
    integration = unittest.TextTestRunner()

    unit.run(unittests())
    integration.run(integration_tests())

    TestLint.run_linter(exceptions=["parse_service_html.py"], path=Hidden.get_project_folder())
