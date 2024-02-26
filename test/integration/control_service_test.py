"""
Module: control_service_test.py

Module for unit testing the ScrapeControl class.

This module contains unit tests for the ScrapeControl class, which is responsible for orchestrating
the scraping of data from RealGM and persisting it into a MySQL database.

WARNING: Test class contains test methods that employ live scrapers. For your privacy and protection,
please turn on your VPN!

While there is an option to use built-in proxies, they may not always provide the desired level
of anonymity. Proxies in the built-in table have not been individually tested.

Tested Methods:
    - setUp(self): Set up the test environment by initializing a ScrapeControl instance.
    - tearDown(self): Clean up the test environment by deleting the ScrapeControl instance.
    - truncate_all(self): Utility method to truncate all working tables in the nba_test database.
    - test_run_all(self): Test the run_all method of the ScrapeControl class.
    - run_single_base(self, category: Literal['team', 'individual', 'player'], table_name: str,
                      season: str = "1991-1992", team: str = "CHI", scrape_method: str = "requests_scrape")
                      -> None: Utility method for run_single test cases.
    - test_run_singe_team(self): Test the run_single method for 'team' argument.
    - test_run_singe_individual(self): Test the run_single method for 'individual' argument.
    - test_run_singe_player(self): Test the run_single method for 'player' argument.
"""
import os.path
import unittest
from typing import Literal

import pandas as pd

from controller.control_service import ScrapeControl
from controller.dto_service import Persist
from model.db_handler import MySQLHandler
from project_secrets import XAMPP_TEST, PROJECT_FOLDER
from webscraper.parse_service import RealGMParser


class TestScrapeControl(unittest.TestCase):
    """
    Unit tests for the ScrapeControl class.

    WARNING: Test class contains test methods that employ live scrapers. For your privacy and protection,
    please turn on your VPN!

    While there is an option to use built in proxies, they may not always provide the desired level
    of anonymity. Proxies in the built-in table have not been individually tested.

    This test suite covers the functionality of the ScrapeControl class, which is responsible for
    orchestrating the scraping of data from RealGM and persisting it into a MySQL database.

    Methods:
        setUp(self): Set up the test environment by initializing a ScrapeControl instance.
        tearDown(self): Clean up the test environment by deleting the ScrapeControl instance.
        truncate_all(self): Utility method to truncate all working tables in the nba_test database.
        test_run_all(self): Test the run_all method of the ScrapeControl class.
        run_single_base(self, category: Literal['team', 'individual', 'player'], table_name: str,
                        season: str = "1991-1992", team: str = "CHI",
                        scrape_method: str = "requests_scrape") -> None: Utility method for run_single
                        test cases.
        test_run_singe_team(self): Test the run_single method for 'team' argument.
        test_run_singe_individual(self): Test the run_single method for 'individual' argument.
        test_run_singe_player(self): Test the run_single method for 'player' argument.
    """
    def setUp(self):
        self.sc = ScrapeControl("proxies_full.csv",
                                "1991-1992",
                                "Chicago-Bulls/4",
                                False,
                                db_host=XAMPP_TEST)

    def tearDown(self):
        del self.sc

    def truncate_all(self):
        """
        Utility method to truncate all working tables in nba_test db.
        :return: None
        """
        conn = MySQLHandler(XAMPP_TEST)
        tables = ["individual_games_playoff", "individual_games_regular", "player_playoff_away",
                  "player_playoff_home", "player_regular_away", "player_regular_home",
                  "team_playoff", "team_regular"]
        [conn.truncate_table(table) for table in tables]
        conn.disconnect()

    def test_run_all(self):
        """
        WARNING: Test method employs live scrapers. For your privacy and protection, please turn
        on your VPN!

        Tests ScrapeControl.run_all method. Scrapes RealGM's individual, team, and players tables
        for the Chicago Bulls' 1991-1992 season.
        Method asserts tables are empty in db, then proceeds to scrape and persist table data. Once
        populated data has been confirmed, it truncates all working tables once again.
        :return: None
        """
        # ensure test tables are empty to begin with
        conn = MySQLHandler(XAMPP_TEST)
        self.assertFalse(conn.season_in_db("1991-1992", "CHI"))
        conn.disconnect()

        # scrape and persist
        self.sc.run_all("requests_scrape")

        # test and clean-up
        conn = MySQLHandler(XAMPP_TEST)
        self.assertTrue(conn.season_in_db("1991-1992", "CHI"))

        individual = conn.read("individual_games_regular", "*")
        player_home = conn.read("player_regular_home", "*")
        player_away = conn.read("player_regular_away", "*")
        team = conn.read("team_regular", "*")
        conn.disconnect()

        self.assertIsNotNone(individual)
        self.assertIsNotNone(player_home)
        self.assertIsNotNone(player_away)
        self.assertIsNotNone(team)

        self.assertIsNotNone(individual[0])
        self.assertIsNotNone(player_home[0])
        self.assertIsNotNone(player_away[0])
        self.assertIsNotNone(team[0])

        self.truncate_all()

    def run_single_base(self, category: Literal['team', 'individual', 'player'], table_name: str,
                        season: str = "1991-1992", team: str = "CHI",
                        scrape_method: str = "requests_scrape") -> None:
        """
        Utility method for run_singe test cases. Scrapes populates specified tables, then checks
        and truncates them.
        :param category: process to run, Literal['team', 'individual', 'player']
        :param table_name: str of table to check after persisting
        :param season: str of season to test for, default: '1991-1992'
        :param team: str of team to test for db empty at start, format: 'CHI',
        default: 'CHI' for Chicago
        :param scrape_method: str of scrape method to use, default: "requests_scrape"
        :return: None
        """
        conn = MySQLHandler(XAMPP_TEST)
        self.assertFalse(conn.season_in_db(season, team))
        conn.disconnect()

        self.sc.run_single(category, scrape_method)

        conn = MySQLHandler(XAMPP_TEST)
        table = conn.read(table_name, "*")
        conn.disconnect()

        self.assertIsNotNone(table)
        self.assertIsNotNone(table[0])

        self.truncate_all()

    def test_run_singe_team(self):
        """
        WARNING: Test method employs live scrapers. For your privacy and protection, please turn
        on your VPN!

        Ensures run_single's operation for 'team' arg.
        Scrapes populates specified tables, then checks and truncates them.
        :return: None
        """
        self.run_single_base("team", "team_regular")

    def test_run_singe_individual(self):
        """
        WARNING: Test method employs live scrapers. For your privacy and protection, please turn
        on your VPN!

        Ensures run_single's operation for 'individual' arg.
        Scrapes populates specified tables, then checks and truncates them.
        :return: None
        """
        self.run_single_base("individual", "individual_games_regular")

    def test_run_singe_player(self):
        """
        WARNING: Test method employs live scrapers. For your privacy and protection, please turn
        on your VPN!

        Ensures run_single's operation for 'player' arg.
        Scrapes populates specified tables, then checks and truncates them.
        :return: None
        """
        self.run_single_base("player", "player_regular_home")

    def test_individual_no_scrape(self):
        """
        No-scrape test method that ensures unique parameter functions correctly in individual table.
        :return: None
        """
        # assert empty
        tbl_len = self.get_table_length("individual_games_regular")
        self.assertEqual(tbl_len, 1)

        # read to df and persist
        individual_path = os.path.join(PROJECT_FOLDER, "test", "content", "html_test_content", "individual6.html")
        with open(individual_path, "r") as file:
            content = file.readlines()
        html_str = "\n".join(content)
        df = RealGMParser.html_table_2_df(html_str)
        Persist.insert(df, "individual_games_regular", "individual", XAMPP_TEST)

        # check insert succeeded
        tbl_len = self.get_table_length("individual_games_regular")
        self.assertTrue(tbl_len > 1)

        # duplicate persist
        Persist.insert(df, "individual_games_regular", "individual", XAMPP_TEST)

        # check duplicate
        conn = MySQLHandler(XAMPP_TEST)
        res = conn.read("individual_games_regular", "count(id)",
                        'player="Raef LaFrentz" and date="2006-01-04"')
        raef_count = res[1][0]
        self.assertEqual(raef_count, 1)

        self.truncate_all()

    def get_table_length(self, table_name: str) -> int:
        """
        Returns row count (including header) as length of table.
        :param table_name: str table to check length for
        :return: int for length of table
        """
        conn = MySQLHandler(XAMPP_TEST)
        res = conn.read(table_name, "*")
        conn.disconnect()
        return len(res)

