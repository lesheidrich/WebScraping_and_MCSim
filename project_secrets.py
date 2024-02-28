"""
Module: secrets.py

This module is designed to store sensitive information. The Hidden class contains static methods
for returning variables such as DB connection URIs and the main project dir.

Example:
    from project_secrets import Hidden
    db_uri = Hidden.get_xampp_uri()

Attributes:
- _path (str): The path of the main project directory.

Static Methods:
- get_project_folder(): Retrieves the path of the main project directory.
- set_project_folder(new_path: str): Sets the path of the main project directory.
- get_xampp_uri(): Retrieves the connection URI for the default database.
- get_xampp_test_uri(): Retrieves the connection URI for the testing database.
- get_clevercloud_uri(): Retrieves the connection URI for the CleverCloud database.

Note:
    Make sure to prevent accidental exposure of sensitive information in this file to version control
    systems.
"""


class Hidden:
    """
    Class houses private information pertaining to project:
    - project path
    - default DB URI
    - testing DB URI

    Attributes:
    - _path (str): The path of the main project directory.

    Static Methods:
    - get_project_folder(): Retrieves the path of the main project directory.
    - set_project_folder(new_path: str): Sets the path of the main project directory.
    - get_xampp_uri(): Retrieves the connection URI for the default database.
    - get_xampp_test_uri(): Retrieves the connection URI for the testing database.
    - get_clevercloud_uri(): Retrieves the connection URI for the CleverCloud database.
    """

    _path = ""

    @staticmethod
    def get_project_folder() -> str:
        """
        :return: Path string of main project dir
        """
        return Hidden._path

    @staticmethod
    def set_project_folder(new_path: str) -> None:
        """
        Sets main project dir from str input.
        :param new_path: str of new main project dir path
        :return: None
        """
        Hidden._path = new_path

    @staticmethod
    def get_xampp_uri() -> str:
        """
        URI for working DB.
        :return: str connection URI for default DB
        """
        return "mysql://model:6jNa4GZibviELPZ@localhost:3306/nba"

    @staticmethod
    def get_xampp_test_uri() -> str:
        """
        URI for testing DB.
        :return: str connection URI for testing DB
        """
        return "mysql://testing:X3YB8p99su)iqFy9@localhost:3306/nba_test"

    @staticmethod
    def get_clevercloud_uri() -> str:
        """
        :return: str connection URI for CleverCloud DB
        """
        return ("mysql://uyppr7dkk0zjc6uy:R8XxQDx7W8lOeRNpXMfl@bsrujusf4amctsza7yp5-mysql."
                "services.clever-cloud.com:3306/bsrujusf4amctsza7yp5")
