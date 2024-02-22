"""
Module: game_service_test.py

Unit tests for the simulator.game_service module.

This module contains unit tests for the functionality provided by the GameBuilder class
in the simulator.game_service module.

Classes:
    TestGameBuilder: A TestCase class for testing the GameBuilder class.
"""

import unittest
from controller.dto_sim import Player
from model.teams import Teams
from simulator.game_service import GameBuilder


class TestGameBuilder(unittest.TestCase):
    """
    Unit tests for the GameBuilder class.

    Attributes:
        g (GameBuilder): An instance of GameBuilder for testing.

    Methods:
        setUp(): Initializes a GameBuilder instance for testing purposes.
        test_switch_possession(): Ensures that possession of the ball changes upon calling switch_possession.
        test_tip_off(): Asserts that both home and away teams can win the tip-off.
        test_choose_player(): Checks if the player choice is successful.
        test_on_court_count(): Ensures that there are 5 players on the court.
        test_in_current_play(): Ensures that the number of players in play is min but not more than 5.
    """
    def setUp(self):
        season = "1991-1992"
        home = Teams.from_full_name('Chicago Bulls')
        away = Teams.from_link_name('Miami-Heat/15')
        game_date = "1992-03-24"
        game_type = "regular"
        self.g = GameBuilder(None, season, home, away, game_date, game_type)

    def test_switch_possession(self):
        """
        Ensures team in possession of ball changes upon switch_possession.
        :return: None
        """
        original = self.g.has_ball.h_or_a
        self.g.switch_possession()
        self.assertNotEqual(original, self.g.has_ball.h_or_a)

    def test_choose_player(self):
        """
        Checks if player choice is successful.
        :return: None
        """
        player = self.g.choose_player(self.g.home.roster.SG)
        self.assertIsInstance(player, Player)
        self.assertIsInstance(player.name, str)

    def test_on_court_count(self):
        """
        Ensures 5 players are on court.
        :return: None
        """
        players = self.g.on_court(self.g.home.roster)
        self.assertEqual(len(players), 5)

    def test_in_current_play(self):
        """
        Ensures players in play are at least one but not more than 5.
        :return: None
        """
        oncourt = self.g.on_court(self.g.home.roster)
        playing = self.g.in_current_play(oncourt, self.g.home.roster, 1)
        self.assertTrue(len(playing) > 0)
        self.assertTrue(len(playing) < 6)
