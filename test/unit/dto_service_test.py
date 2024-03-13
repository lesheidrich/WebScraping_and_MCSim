"""
Module: dto_service_test.py

Test module for the Persist class in the controller.dto_service module.

This module contains unit tests for the methods of the Persist class, which is responsible for interacting
with the database and performing various checks and operations related to game data, teams, and seasons.

Attributes:
    unittest (module): The unittest module for creating unit tests.
    pd (module): The pandas module for handling data in DataFrame format.
    Persist (class): The class being tested, responsible for database operations.

Classes:
    TestPersist (unittest.TestCase): A TestCase class containing unit tests for the Persist class methods.

Methods:
    test_get_game_data: Ensures get_game_data returns a DataFrame of games for the specified teams.
    test_team_in_playoffs_true: Ensures positive check for team in playoffs works as expected.
    test_team_in_playoffs_false: Ensures negative check for team in playoffs works as expected.
    test_season_in_db_true: Ensures positive check for season in database works as expected.
    test_season_in_db_false: Ensures negative check for season in database works as expected.
    test_team_in_db_true: Ensures positive check for team in database works as expected.
    test_team_in_db_false: Ensures negative check for team in database works as expected.
"""

import unittest
from test.content.parse_service_html import PLAYER_HTML
from controller.dto_service import Persist
from model.db_handler import MySQLHandler
from project_secrets import Hidden
import pandas as pd
from webscraper.parse_service import RealGMParser


class TestPersist(unittest.TestCase):
    """
    Unit tests for the Persist class methods.

    Methods:
        test_get_game_data: Ensures get_game_data returns a DataFrame of games for the specified teams.
        test_team_in_playoffs_true: Ensures positive check for team in playoffs works as expected.
        test_team_in_playoffs_false: Ensures negative check for team in playoffs works as expected.
        test_season_in_db_true: Ensures positive check for season in database works as expected.
        test_season_in_db_false: Ensures negative check for season in database works as expected.
        test_team_in_db_true: Ensures positive check for team in database works as expected.
        test_team_in_db_false: Ensures negative check for team in database works as expected.
    """
    def test_get_game_data(self):
        """
        Ensures get game data returns a df of games for the arg teams.
        :return: None
        """
        df = Persist.get_game_data("Chicago Bulls", "Miami Heat", "1992-1993", None)
        self.assertTrue(len(df) >= 1)
        self.assertTrue("Miami Heat" in df["visitor_team"].iloc[1])
        self.assertTrue("Chicago Bulls" in df["home_team"].iloc[1])
        self.assertIsInstance(df, pd.DataFrame)

    def test_team_in_playoffs_true(self):
        """
        Ensures positive check for team in playoffs works as expected.
        :return: None
        """
        result = Persist.team_in_playoffs("Chicago-Bulls/4", "1991-1992", None)
        self.assertTrue(result)

    def test_team_in_playoffs_false(self):
        """
        Ensures negative check for team in playoffs works as expected.
        :return: None
        """
        result = Persist.team_in_playoffs("Atlanta-Hawks/1", "1991-1992", None)
        self.assertFalse(result)

    def test_season_in_db_true(self):
        """
        Ensures positive check for season in db.
        :return: None
        """
        result = Persist.season_in_db("1991-1992", "CHI", None)
        self.assertTrue(result)

    def test_season_in_db_false(self):
        """
        Ensures negative check for season in db.
        :return: None
        """
        result = Persist.season_in_db("2025-2026", "CHI", None)
        self.assertFalse(result)

    def test_team_in_db_true(self):
        """
        Ensures positive check for team in db.
        :return: None
        """
        result = Persist.team_in_db("1991-1992", "team_regular", None)
        self.assertTrue(result)

    def test_team_in_db_false(self):
        """
        Ensures negative check for team in db.
        :return: None
        """
        result = Persist.team_in_db("2025-2026", "team_regular", None)
        self.assertFalse(result)

    def test_delete_records(self):
        """
        Test ensures successful persistence and deletion from table.
        :return: None
        """
        sauce = PLAYER_HTML
        df = RealGMParser.html_table_2_df(sauce)
        RealGMParser.players_df_add_columns(df)
        df["Season"] = "1991-1992"

        # db is empty to start
        self.assertEqual(self.get_player_table_len(), 0)

        # db is populated
        Persist.insert(df, "player_regular_home", "player",
                       Hidden.get_xampp_test_uri())
        self.assertTrue(self.get_player_table_len() > 0)

        # empty again
        Persist.delete_records("player_regular_home", 'season="1991-1992" and team="CHI"',
                               Hidden.get_xampp_test_uri())
        self.assertEqual(self.get_player_table_len(), 0)


    def get_player_table_len(self) -> int:
        """
        Utility method returns nba_test.player_regular_home table length.
        :return: int nba_test.player_regular_home table length
        """
        conn = MySQLHandler(Hidden.get_xampp_test_uri())
        count = conn.read("player_regular_home", "count(id)")
        conn.disconnect()
        return count[1][0]
