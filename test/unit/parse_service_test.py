"""
Module: parse_service_test.py

This module contains unit tests to validate the functionality of the RealGMParser class
methods for parsing HTML content related to basketball player data from the RealGM website.
"""

import unittest
import pandas as pd
from test.content.parse_service_html import DEPTH_HTML, PLAYER_HTML, INDIVIDUAL_HTML
from webscraper.parse_service import RealGMParser


class TestRealGMParser(unittest.TestCase):
    """Test cases for the RealGMParser class.

    This class contains unit tests to validate the functionality of the methods
    in the RealGMParser class, which is responsible for parsing HTML content related
    to data from the RealGM website.

    Attributes from /test/content/parse_service_html:
        DEPTH_HTML (str): HTML content for the depth table.
        PLAYER_HTML (str): HTML content for the player table.
        INDIVIDUAL_HTML (str): HTML content for the individual player table.
    """
    def test_parse_footnote_unavailable(self):
        """
        Checks 'table not found' script success.
        :return: None
        """
        html_content = "<p class='footnote'>Stats are not currently available for this season.</p>"
        self.assertTrue(RealGMParser.parse_footnote_unavailable(html_content))

    def test_parse_footnote_unavailable_not_found(self):
        """
        Checks 'table not found' script failure.
        :return: None
        """
        html_content = "<p class='footnote'>Other text</p>"
        self.assertFalse(RealGMParser.parse_footnote_unavailable(html_content))

    def test_full_name_populate_depth_position(self):
        """
        Checks if full-form names in depth df are successfully located in players df.
        :return: None
        """
        player_df = pd.DataFrame({"Player": ["Michael Jordan", "Scottie Pippen"], "Depth": ["", ""]})
        depth_df = pd.DataFrame({"Starters": ["Michael Jordan"]})
        row = {"Starters": "Starters"}
        result = RealGMParser.full_name_populate_depth_position(
                "Michael Jordan", player_df, row, depth_df, 0, "Starters")
        self.assertTrue(result)
        self.assertEqual(player_df.loc[player_df["Player"] == "Michael Jordan", "Depth"].iloc[0], "1")

    def test_initial_name_populate_depth_position(self):
        """
        Checks if short-form names in depth df are successfully located in players df.
        :return: None
        """
        player_df = pd.DataFrame({"Player": ["Bill Cartwright", "Stephen Curry"], "Depth": ["", ""]})
        depth_df = pd.DataFrame({"Starters": ["B. Cartwright"]})
        row = {"Starters": "Starters"}
        result = RealGMParser.initial_name_populate_depth_position(
                player_df, "Bill Cartwright", row, depth_df, 0, "Starters")
        self.assertTrue(result)
        self.assertEqual(player_df.loc[player_df["Player"] == "Bill Cartwright", "Depth"].iloc[0], "1")

    def test_parse_depth_2_players(self):
        """
        Ensures depth and position is correctly parsed to players in player df.
        :return: None
        """
        player_df = RealGMParser.html_table_2_df(PLAYER_HTML)
        depth_df = RealGMParser.depth_table_2_df(DEPTH_HTML, "1992-1993")
        RealGMParser.parse_depth_2_players(depth_df, player_df)
        actual_position = player_df["Position"].iloc[1]
        actual_depth = player_df["Depth"].iloc[1]
        self.assertEqual(actual_position, "SG")
        self.assertEqual(actual_depth, "1")

    def test_players_df_add_columns(self):
        """
        Ensures position, depht and season columns are successfully added to players df.
        :return: None
        """
        df = pd.DataFrame({"Player": ["Michael Jordan", "Scottie Pippen"]})
        RealGMParser.players_df_add_columns(df)
        self.assertTrue("Position" in df.columns)
        self.assertTrue("Depth" in df.columns)
        self.assertTrue("Season" in df.columns)

    def test_depth_table_2_df(self):
        """
        Checks successful depth df creation from html content.
        :return: None
        """
        sauce = DEPTH_HTML
        df = RealGMParser.depth_table_2_df(sauce, "1991-1992")
        self.assertTrue("Michael Jordan" in df["SG"][0])

    def test_html_table_2_df(self):
        """
        Checks successful player df creation from html content.
        :return: None
        """
        sauce = PLAYER_HTML
        df = RealGMParser.html_table_2_df(sauce)
        actual = df["Player"].iloc[0]
        self.assertEqual(actual, "Scottie Pippen")

    def test_html_table_append_df(self):
        """
        Checks successful addition to existing individual df from html content.
        :return: None
        """
        base_df = None
        sauce = INDIVIDUAL_HTML
        df = RealGMParser.html_table_append_df(sauce, base_df)
        actual = df["Player"].iloc[0]
        self.assertEqual(actual, "Michael Jordan")
