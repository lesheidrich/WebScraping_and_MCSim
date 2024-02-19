"""
Module: secrets.py

This module is designed to store sensitive information, such as passwords.

Important:
    - Keep this module secure and do not expose it to the public.
    - Ensure that only authorized personnel have access to this file.

Example:
    import secrets
    db_password = secrets.get_db_password()

Functions:
    - get_api_key(): Retrieves the API key securely.
    - get_database_password(): Retrieves the database password securely.

Note:
    Make sure to add this file to your '.gitignore' or equivalent configuration
    to prevent accidental exposure of sensitive information in version control systems.
"""

PROJECT_FOLDER = 'C:\\users\\dblin\\PycharmProjects\\WebScraping_and_MCSim'


def get_project_folder() -> str:
    """
    Retrieves str of project's absolute path securely
    used in:
        - logger.py
        - proxy_handler.py
        - logger_test.py
        - proxy_handler_test.py
    :return: str absolute path of project folder
    """
    return PROJECT_FOLDER


# HOST = 'localhost'
# USER = 'model'
# PWD = '6jNa4GZibviELPZ'
# DB = 'nba'

# HOST = 'bsrujusf4amctsza7yp5-mysql.services.clever-cloud.com'
# USER = 'uyppr7dkk0zjc6uy'
# PWD = 'R8XxQDx7W8lOeRNpXMfl'
# DB = 'bsrujusf4amctsza7yp5'
# PORT = "3306"

# MYSQL_CLI = "mysql -h bsrujusf4amctsza7yp5-mysql.services.clever-cloud.com
# -P 3306 -u uyppr7dkk0zjc6uy -p bsrujusf4amctsza7yp5"


CLEVERCLOUD_CLI = ("mysql://uyppr7dkk0zjc6uy:R8XxQDx7W8lOeRNpXMfl@bsrujusf4amctsza7yp5-mysql."
                   "services.clever-cloud.com:3306/bsrujusf4amctsza7yp5")

XAMPP_URI = "mysql://model:6jNa4GZibviELPZ@localhost:3306/nba"
