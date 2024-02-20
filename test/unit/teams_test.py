"""
Module: test_teams.py

Unit tests for the Teams enumeration class.

This module contains unit tests for the functionality of the Teams enumeration class,
specifically testing the methods for creating instances based on various attributes.

Attributes: None
"""

import unittest
from model.teams import Teams


class TestTeams(unittest.TestCase):
    """
    Test case for the Teams enumeration class.

    This class contains unit tests for the functionality of the Teams enumeration class,
    specifically testing the methods for creating instances based on various attributes.

    Attributes: None
    """
    def test_from_full_name(self):
        """
        Checks creation of Teams instance from full_name, asserts short_name works.
        :return: None
        """
        actual = Teams.from_full_name("Chicago Bulls")
        expected = "CHI"
        self.assertIsInstance(actual, Teams)
        self.assertEqual(actual.short_name, expected)

    def test_from_short_name(self):
        """
        Checks creation of Teams instance from short_name, asserts city_name works.
        :return: None
        """
        actual = Teams.from_short_name("CHI")
        expected = "Chicago"
        self.assertIsInstance(actual, Teams)
        self.assertEqual(actual.city_name, expected)

    def test_from_link_name(self):
        """
        Checks creation of Teams instance from link_name (as used in RealGM URLs), asserts
        full_name works.
        :return: None
        """
        actual = Teams.from_link_name("Chicago-Bulls/4")
        expected = "Chicago Bulls"
        self.assertIsInstance(actual, Teams)
        self.assertEqual(actual.full_name, expected)

    def test_from_city_name(self):
        """
        Checks creation of Teams instance from city_name, asserts link_name (as used in RealGM
        URLs) works.
        :return: None
        """
        actual = Teams.from_city_name("Chicago")
        expected = "Chicago-Bulls/4"
        self.assertIsInstance(actual, Teams)
        self.assertEqual(actual.link_name, expected)
