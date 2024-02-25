"""
Module: monte_carlo_test.py

Module containing unit tests for Monte Carlo simulations of basketball games.

This module provides a collection of test cases to verify the functionality of Monte Carlo simulations
for both regular season and playoff games.

Classes:
    - TestMonteCarlo: A TestCase class containing methods for testing Monte Carlo simulations.

Methods:
    - test_regular: Tests the successful return of plt.figure from a Monte Carlo regular game.
    - test_playoff: Tests the successful return of plt.figure from a Monte Carlo playoff game.
"""
import _io
import unittest
from model.teams import Teams
from simulator.monte_carlo import MonteCarlo


class TestMonteCarlo(unittest.TestCase):
    """
    A test case class for Monte Carlo simulations of basketball games.

    This class contains test methods for verifying the functionality of Monte Carlo simulations
    for both regular season and playoff games.

    Methods:
        - test_regular: Tests the successful return of plt.figure from a Monte Carlo regular game.
        - test_playoff: Tests the successful return of plt.figure from a Monte Carlo playoff game.
    """
    def test_regular(self):
        """
        Tests successful return of BytesIO for matplotlib figure from Monte Carlo regular game.
        :return: None
        """
        season = "1991-1992"
        home = Teams.from_full_name('Chicago Bulls')
        away = Teams.from_link_name('Miami-Heat/15')
        game_date = "1992-03-24"
        game_type = "regular"
        mc = MonteCarlo(None, season, home, away, game_date, game_type, 10)
        result = mc.run()
        self.assertTrue(isinstance(result, _io.BytesIO))
        self.assertIsNotNone(result)

    def test_playoff(self):
        """
        Tests successful return of BytesIO for matplotlib figure from Monte Carlo playoff game.
        :return: None
        """
        home = Teams.from_full_name('Phoenix Suns')
        away = Teams.from_full_name('Los Angeles Lakers')
        season = "1992-1993"
        game_date = "1993-04-30"
        game_type = "playoff"
        mc = MonteCarlo(None, season, home, away, game_date, game_type, 10)
        result = mc.run()
        self.assertTrue(isinstance(result, _io.BytesIO))
        self.assertIsNotNone(result)
