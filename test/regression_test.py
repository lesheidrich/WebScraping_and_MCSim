import unittest
from test.unit.selenium_service_test import TestWebDriverFactory, TestChromeDriver, TestFirefoxDriver
from test.unit.webscraper_utilities_test import TestWebKit, TestProxyKit
from unit.proxy_handler_test import TestProxyHandler
from unit.logger_test import TestLogger
import os
from pylint import lint


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
        unittest.TestLoader().loadTestsFromTestCase(TestWebDriverFactory)
    ])

    return test_suite


def list_files_recursively(folder_path: str) -> [str]:
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        dirs[:] = [d for d in dirs if "env" not in d]
        for file in files:
            if file.endswith(".py"):
                file_list.append(os.path.join(root, file))
    return file_list


def run_linter(path: str, exceptions: list) -> None:
    files = list_files_recursively(path)

    if not os.getcwd().endswith("linter"):
        os.chdir(os.path.join(path, "test", "linter"))

    files[:] = [f for f in files if not any(module in f for module in exceptions)]

    [lint.Run([f], exit=False) for f in files]


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(regression_test())

    path = 'C:\\Users\\dblin\\PycharmProjects\\WebScraping_and_MCSim'
    exceptions = ["linter.py", "regression_test.py", "main.py"]
    run_linter(path, exceptions)
