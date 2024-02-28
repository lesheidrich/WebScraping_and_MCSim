"""
Module: linter.py

This module contains utility functions and classes for linting Python files in a project directory.
It provides a TestLint class with methods to recursively list Python files and run the pylint linter
on those files, excluding specified exceptions.

Classes:
    TestLint: A utility class for linting Python files in a project directory.
"""

import os
from typing import List
from pylint import lint


class TestLint:
    """
    A utility class for linting Python files in a project directory.

    This class provides methods to recursively list Python files in a project directory and
    run the pylint linter on those files, excluding specified exceptions.

    Methods:
        list_files_recursively: Recursively compiles a list of Python modules to lint from a project
        directory.
        run_linter: Lints all modules in the project directory, excluding specified exceptions.
    """
    @staticmethod
    def list_files_recursively(folder_path: str) -> List[str]:
        """
        Compiles list of modules to lint from project dir.
        :param folder_path: str of project root dir
        :return: str list of filepaths
        """
        file_list = []
        for root, dirs, files in os.walk(folder_path):
            dirs[:] = [d for d in dirs if "env" not in d]
            for file in files:
                if file.endswith(".py"):
                    file_list.append(os.path.join(root, file))
        return file_list

    @staticmethod
    def run_linter(exceptions: list, path: str) -> None:
        """
        Lints all modules in project directory, excluding param exceptions.
        :param exceptions: list of str filenames to exclude from lint
        :param path: path str to project dir
        :return: None
        """
        files = TestLint.list_files_recursively(path)

        if not os.getcwd().endswith("linter"):
            os.chdir(os.path.join(path, "test", "linter"))
        # filter out exceptions
        files[:] = [f for f in files if not any(module in f for module in exceptions)]

        [lint.Run([f], exit=False) for f in files]
