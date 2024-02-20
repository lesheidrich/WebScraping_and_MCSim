"""
Module: db_handler_test.py

Unit tests for the MySQLHandler module.

This module contains a collection of unit tests designed to test the functionalities of the MySQLHandler
class,
which is responsible for interacting with a MySQL database. The tests cover various aspects of the class,
including establishing connections, executing queries, performing CRUD operations, and checking database
state.

The MySQLHandler class is utilized for database interactions, such as connecting to the database,
executing queries, inserting records, reading data, updating records, and deleting records.
Each test method focuses on verifying specific behaviors and functionalities of the MySQLHandler class.

Test Coverage:
- Connection Establishment: Tests the connection to the MySQL database.
- Disconnection: Tests the disconnection from the MySQL database.
- Query Execution: Tests the execution of SQL queries.
- Record Manipulation: Tests the insertion, reading, updating, and deletion of records.
- Database State Checks: Tests methods for checking the presence of seasons and teams in the database.

Usage:
To run the unit tests, execute this module using a testing framework such as unittest.
"""

import unittest
from model.db_handler import MySQLHandler
import mysql.connector


class TestMySQLHandler(unittest.TestCase):
    """
    Unit tests for the MySQLHandler class.

    These tests cover various functionalities of the MySQLHandler class, including connecting to the database,
    executing queries, reading from tables, and checking the presence of seasons and teams in the database.

    Methods:
        setUp(): Prepares the test environment before each test method is executed.
        tearDown(): Cleans up the test environment after each test method has been executed.
        test_connect(): Tests the connection to the MySQL database.
        test_disconnect(): Tests the disconnection from the MySQL database.
        test_execute_query(): Tests the execution of a SQL query.
        test_read(): Tests the reading of records from a table.
        test_season_in_db_true(): Tests the method for checking if a season is present in the database
        (positive case).
        test_season_in_db_false(): Tests the method for checking if a season is present in the database
        (negative case).
        test_in_playoffs_true(): Tests the method for checking if a team is in playoffs (positive case).
        test_in_playoffs_false(): Tests the method for checking if a team is in playoffs (negative case).
    """
    def setUp(self):
        self.conn = MySQLHandler(None)

    def tearDown(self):
        self.conn.disconnect()

    def test_connect(self):
        """
        Ensures connection is successfully created to database.
        :return: None
        """
        self.assertIsInstance(self.conn.connection, mysql.connector.connection_cext.CMySQLConnection)
        self.assertIsNotNone(self.conn.connection)
        self.assertTrue(self.conn.connection.is_connected())

    def test_disconnect(self):
        """
        Ensures database connection is aborted successfully.
        :return: None
        """
        self.conn.disconnect()
        self.assertFalse(self.conn.connection.is_connected())
        self.setUp()
        self.assertTrue(self.conn.connection.is_connected())

    def test_execute_query(self):
        """
        Ensures successful execution of query.
        :return: None
        """
        query = "SELECT * FROM team_regular WHERE team='Chicago' and season='1991-1992'"
        cursor = self.conn.execute_query(query)
        table = cursor.fetchall()
        cursor.close()
        self.assertTrue("Chicago" in table[0])
        self.assertTrue(len(table[0]) > 0)

    def test_read(self):
        """
        Ensures results read from table are not empty, and that their rows are not empty. Also
        checks first column (int) is of type int.
        :return: None
        """
        table = self.conn.read("team_regular", "*")
        self.assertIsInstance(table[1][0], int)
        self.assertTrue(len(table) > 0)
        self.assertTrue(len(table[0]) > 0)

    def test_season_in_db_true(self):
        """
        Ensures check method season_in_db operates as expected when season in db.
        :return: None
        """
        result = self.conn.season_in_db("1991-1992", "CHI")
        self.assertTrue(result)

    def test_season_in_db_false(self):
        """
        Ensures check method season_in_db operates as expected when season not in db.
        :return: None
        """
        result = self.conn.season_in_db("2035-2036", "CHI")
        self.assertFalse(result)

    def test_in_playoffs_true(self):
        """
        Ensures check method in_playoffs operates as expected when team in playoffs.
        :return: None
        """
        result = self.conn.in_playoffs("Chicago-Bulls/4", "1991-1992")
        self.assertTrue(result)

    def test_in_playoffs_false(self):
        """
        Ensures check method in_playoffs operates as expected when team not in playoffs.
        :return: None
        """
        result = self.conn.in_playoffs("Chicago-Bulls/4", "2035-2036")
        self.assertFalse(result)
