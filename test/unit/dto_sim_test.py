"""
Module: dto_sim_test.py

Test module for the TeamBuilder, Roster and Player classes.

This module contains unit tests for the TeamBuilder class, which is responsible for constructing team rosters
by retrieving and processing game data from a MySQL database. The test cases cover various aspects of the
TeamBuilder functionality to ensure its correctness and robustness.

Tested Functionality:
    - Asserting first and last date of individual dataframe.
    - Testing the repetition of dates in the individual dataframe.
    - Ensuring player dataframe has the correct length and testing specific player statistics.
    - Checking the length and season of the team dataframe.
    - Validating game date handling methods, including scenarios with dates from next and previous seasons.
    - Testing roster size based on expected players per position.
    - Validating player statistics to ensure proper population, including specific player (e.g., Michael
      Jordan).
"""

import unittest
import pandas as pd
from controller.dto_sim import TeamBuilder
from model.teams import Teams


class TestTeamBuilder(unittest.TestCase):
    """
    Unit tests for the TeamBuilder class.

    This class contains a series of test cases to validate the functionality of the TeamBuilder class,
    which is responsible for constructing team rosters by retrieving and processing game data
    from a MySQL database.

    Test Methods:
        - test_date_w_individual_first_last: Asserts the first and last date of individual dataframe.
        - test_date_w_individual_date_repetition: Tests the repetition of dates in the individual dataframe.
        - test_get_player_data: Ensures player dataframe has the correct length and tests the value for
          Michael Jordan's games played.
        - test_get_team_data: Checks the length and season of the team dataframe.
        - test_validate_game_date_next: Checks if a date from the next season raises a ValueError.
        - test_validate_game_date_previous: Checks if a date from the previous season raises a ValueError.
        - test_validate_game_date_ok: Checks if a date within the season does not raise a ValueError.
        - test_roster_len: Tests the size of the roster based on expected players per position.
        - test_roster_mj: Finds and checks Michael Jordan's stats to ensure proper population.
    """
    def setUp(self):
        season = "1992-1993"
        home = Teams.from_full_name('Chicago Bulls')
        game_date = "1993-03-24"
        game_type = "regular"
        self.chi = TeamBuilder(None, season, home, game_date, game_type, "home")

    def tearDown(self):
        del self.chi

    def test_date_w_individual_first_last(self):
        """
        Asserts first and last date of individual df.
        :return: None
        """
        first_actual = self.chi.individual_df['date'].min()
        last_actual = self.chi.individual_df['date'].max()
        first_expected = pd.Timestamp("1992-03-24 00:00:00")
        last_expected = pd.Timestamp("1993-03-23 00:00:00")
        self.assertEqual(first_actual, first_expected, "Dates should be equal")
        self.assertEqual(last_actual, last_expected, "Dates should be equal")

    def test_date_w_individual_date_repetition(self):
        """
        Tests first date in individual table 1x and last 5x.
        :return: None
        """
        start_df = self.chi.individual_df[(self.chi.individual_df["player"] == "Michael Jordan") &
                                          (self.chi.individual_df["date"] == "1992-03-24")]
        self.assertTrue(len(start_df) == 1)
        end_df = self.chi.individual_df[(self.chi.individual_df["player"] == "Michael Jordan") &
                                        (self.chi.individual_df["date"] == "1993-03-23")]
        self.assertTrue(len(end_df) == 5)

    def test_get_player_data(self):
        """
        Ensures player df is the right length, and tests value for Michael Jordan's games played.
        :return: None
        """
        self.assertEqual(len(self.chi.player_df), 17)
        filtered = self.chi.player_df[self.chi.player_df["player"] == "Michael Jordan"]["GP"].iloc[0]
        self.assertEqual(filtered, 38)

    def test_get_team_data(self):
        """
        Checks length and season of team df.
        :return: None
        """
        self.assertEqual(self.chi.team_df["season"].iloc[0], "1992-1993")
        self.assertEqual(len(self.chi.team_df), 1)

    def test_validate_game_date_next(self):
        """
        Checks if date within season param but from next season raises ValueError.
        :return: None
        """
        season = "1992-1993"
        game_date = "1993-10-24"
        self.assertRaises(ValueError, self.chi.validate_game_date, season, game_date)

    def test_validate_game_date_previous(self):
        """
        Checks if date within season param but from previous season raises ValueError.
        :return: None
        """
        season = "1992-1993"
        game_date = "1992-4-24"
        self.assertRaises(ValueError, self.chi.validate_game_date, season, game_date)

    def test_validate_game_date_ok(self):
        """
        Checks if date within season param.
        :return: None
        """
        season = "1992-1993"
        game_date = "1993-4-24"
        try:
            self.assertRaises(ValueError, self.chi.validate_game_date, season, game_date)
        except AssertionError:
            self.chi.validate_game_date(season, game_date)

    def test_roster_len(self):
        """
        Tests roster size based on expected players per position.
        Use https://basketball.realgm.com/nba/teams/Chicago-Bulls/4/Depth_Charts to validate
        :return: None
        """
        self.assertEqual(len(self.chi.roster.PG), 2)
        self.assertEqual(len(self.chi.roster.SG), 4)
        self.assertEqual(len(self.chi.roster.PF), 2)
        self.assertEqual(len(self.chi.roster.SF), 3)
        self.assertEqual(len(self.chi.roster.C), 3)

    def test_roster_mj(self):
        """
        Finds and checks Michael Jordan and validates stats to ensure proper population.
        :return: None
        """
        mj = None
        for player in self.chi.roster.SG:
            if player.name == "Michael Jordan":
                mj = player

        self.assertAlmostEqual(mj.player_w, 0.6169783383274374)
        self.assertAlmostEqual(mj.playtime_w, 0.8041666666666667)
        self.assertAlmostEqual(mj.FGA, 0.2577857142857143)
        self.assertAlmostEqual(mj.ORB, 0.01742857142857143)
