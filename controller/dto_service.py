"""
Module: dto_service.py

Module for handling data transfer and persistence operations.

This module provides classes and methods for scraping data from RealGM website and persisting/retrieving data
to/from a MySQL database.

Classes:
    DataTransferObject: A class representing a data transfer object for scraping data from RealGM website.

Methods:
    Persist:
        insert: Static method to insert DataFrame into a specified table in the database.
        get_game_data: Static method to retrieve game data between two teams for a specified season.
        team_in_playoffs: Static method to check if a team is in the playoffs for a specified season.
        season_in_db: Static method to check if a season is already in the database.
        team_in_db: Static method to check if a team is in the database for a specified season.

Dependencies:
    - datetime from datetime: For handling date and time objects.
    - typing.Optional: For specifying optional parameters.
    - typing.Literal: For specifying literal types.
    - pandas as pd: For handling data manipulation and analysis.
    - BeautifulSoup from bs4: For parsing HTML and XML documents.
    - MySQLHandler from model.db_handler: For handling MySQL database operations.
    - RealGMParser from webscraper.parse_service: For parsing data scraped from RealGM.
    - ScraperFacade from webscraper.webscraper: For handling the scraping process.
"""

from datetime import datetime
from typing import Optional, Literal
import pandas as pd
from bs4 import BeautifulSoup
from model.db_handler import MySQLHandler
from webscraper.parse_service import RealGMParser
from webscraper.webscraper import ScraperFacade


class DataTransferObject:
    """
    A class representing a data transfer object for scraping data from RealGM website.

    This class provides methods to facilitate the retrieval and processing of various data tables
    from RealGM for a given team and season.

    Args:
        proxy_csv (Optional[str]): Path to the CSV file containing proxy information. Defaults to
        "proxies_full.csv".
        check_proxies (bool): A boolean indicating whether to check the proxies before using them.
        Defaults to False.

    Attributes:
        scraper: An instance of the ScraperFacade class for handling the scraping process.

    Methods:
        data_available(url: str) -> bool:
            Attempts to scrape the specified URL with requests, switches to Selenium if it encounters an
            error.
            Returns True if there is a table that can be scraped.

        merged_individual_df(scrape_method_str: str, url_base: str) -> pd.DataFrame:
            Scrapes all individual tables from RealGM for a given team and season, and concatenates them
            into a dataframe.

        has_next_page(html_string) -> bool:
            Parses individual page's HTML content to ascertain if it has a subsequent page.

        new_team_df(scrape_method_str: str, url: str) -> pd.DataFrame:
            Scrapes team table from RealGM and returns data as a dataframe.

        player_depth_merged_df(df_depth, df_player) -> None:
            Applies depth and position data to the existing player dataframe for a given season and team.

        new_depth_df(scrape_method_str: str, url: str, years: str) -> pd.DataFrame:
            Creates a dataframe of player's depth stats from RealGM pertaining to position and rotations.

        new_players_df(scrape_method_str: str, url: str) -> pd.DataFrame:
            Scrapes player table on RealGM and returns a dataframe.

        get_soup(scrape_method: str, url: str) -> str:
            Gets HTML string from the website's response content.

        scrape_method_validation(scrape_method: str) -> None:
            Checks the scrape method to ensure the name is acceptable based on available methods.
    """
    def __init__(self, proxy_csv: Optional[str] = "proxies_full.csv", check_proxies: bool = False):
        self.scraper = ScraperFacade(proxy_csv, check_proxies)

    def data_available(self, url: str) -> bool:
        """
        Attempts to scrape the specified URL with requests, switches to selenium if it encounters
        an error. Returns True if there is a table that can be scraped.
        :param url: URL string to scrape
        :return: False if there's a table that can be scraped on the page
        """
        try:
            soup = self.get_soup("requests_scrape", url)
        # pylint: disable=W0718
        except Exception:
            soup = self.get_soup("firefox_selenium_scrape", url)
        return not RealGMParser.parse_footnote_unavailable(soup)

    def merged_individual_df(self, scrape_method_str: str, url_base: str) -> pd.DataFrame:
        """
        Scrapes all individual tables from RealGM for a given team and season, and concats
        them into a df.
        :param scrape_method_str: str of selected scrape method
        :param url_base: URL of individual tables without page number
        :return: individual games df for season and team
        """
        base_df = None
        n = 1
        url = url_base + str(n)
        while True:
            try:
                html_text = self.get_soup(scrape_method_str, url)
                base_df = RealGMParser.html_table_append_df(html_text, base_df)

                if not self.has_next_page(html_text):
                    return base_df
                n += 1
                url = url_base + str(n)
            except ValueError:
                # if has next page but no content on it
                if RealGMParser.parse_footnote_unavailable(html_text):
                    return base_df

    def has_next_page(self, html_string) -> bool:
        """
        Method parses individual page's html content to ascertain if it has a subsequent page.
        :param html_string: html content string to parse
        :return: True if there is a next page
        """
        soup = BeautifulSoup(html_string, 'html.parser')
        a_tag = soup.find("a", string="Next Page »")
        return a_tag is not None

    def new_team_df(self, scrape_method_str: str, url: str) -> pd.DataFrame:
        """
        Scrapes team table from RealGM and returns data as a df.
        :param scrape_method_str: str of selected scrape method
        :param url: str URL to scrape
        :return: team df for given season
        """
        soup = self.get_soup(scrape_method_str, url)
        team_df = RealGMParser.html_table_2_df(soup)
        team_df.insert(team_df.columns.get_loc("Team") + 1, "Season", "")
        return team_df

    def player_depth_merged_df(self, df_depth, df_player) -> None:
        """
        Applies depth and position data to existing player df for given season and team.
        :param df_depth: depth df to merge stats from
        :param df_player: player df to merge stats to
        :return: player df with depth and position data
        """
        if len(df_player) < 1 or len(df_depth) < 1:
            raise ValueError("player_depth_merged_df attempted to merge empty dataframe. "
                             "Check depth and player dataframe creaiton!")
        RealGMParser.parse_depth_2_players(df_depth, df_player)
        del df_depth

    def new_depth_df(self, scrape_method_str: str, url: str, years: str) -> pd.DataFrame:
        """
        Creates df of player's depth stats from RealGM pertaining to position and rotations.
        :param scrape_method_str: str of selected scrape method
        :param url: str URL to scrape
        :param years: str of season, format: '1991-1992'
        :return: player depth df
        """
        soup = self.get_soup(scrape_method_str, url)
        return RealGMParser.depth_table_2_df(soup, years)

    def new_players_df(self, scrape_method_str: str, url: str) -> pd.DataFrame:
        """
        Scrapes player table on RealGM and returns df.
        :param scrape_method_str: str of selected scrape method
        :param url: str URL to scrape
        :return: df of player stats
        """
        soup = self.get_soup(scrape_method_str, url)
        df_player = RealGMParser.html_table_2_df(soup)
        RealGMParser.players_df_add_columns(df_player)
        return df_player

    def get_soup(self, scrape_method: str, url: str) -> str:     # rename to get_sauce
        """
        Gets html string from website's response content.
        :param scrape_method: str of selected scrape method
        :param url: str URL to scrape
        :return: str of html content
        """
        self.scrape_method_validation(scrape_method)
        scrape_function = getattr(self.scraper, scrape_method)

        if "request" in scrape_method:
            return scrape_function(url).text

        return scrape_function(url)

    def scrape_method_validation(self, scrape_method: str) -> None:
        """
        Checks scrape method to ensure name is acceptable based on available methods.
        :param scrape_method: str of scrape method name
        :return: None
        :raises: ValueError if scrape_method not in list of accepted method names
        """
        method_list = ["firefox_selenium_scrape", "firefox_selenium_proxy_scrape", "chrome_selenium_scrape",
                       "chrome_selenium_proxy_scrape", "requests_scrape", "requests_proxy_scrape"]
        if scrape_method not in method_list:
            raise ValueError(f"{scrape_method} is not an accepted scrape method.")


class Persist:
    """
    Class providing methods for persisting and retrieving data from a MySQL database.

    Methods:
        insert: Static method to insert DataFrame into a specified table in the database.
        get_game_data: Static method to retrieve game data between two teams for a specified season.
        team_in_playoffs: Static method to check if a team is in the playoffs for a specified season.
        season_in_db: Static method to check if a season is already in the database.
        team_in_db: Static method to check if a team is in the database for a specified season.
    """
    @staticmethod
    def insert(df, table_name: str, preset_headers: Literal["team", "individual", "player"],
               db_host: Optional[str] = None) -> None:
        """
        Persists df into specified table in db.
        :param df: df to persist
        :param table_name: str of destination table
        :param preset_headers: preset headers to use: "team", "individual", "player"
        :param db_host: str of db host URL for MySQLHandler instance to connect. Defaults
        to None (for xampp's nba db)
        :return: None
        """
        conn = MySQLHandler(db_host)
        for _, row in df.iterrows():
            data = row.to_dict()
            del data['#']
            if preset_headers == "individual":
                data["Date"] = datetime.strptime(data["Date"], '%b %d, %Y').strftime('%Y-%m-%d')
            try:
                conn.insert_record(table_name, data, preset_headers)
            except ConnectionError as e:
                print(f"ConnectionError while attempting Persist.insert into {table_name}: "
                      f"{row.iloc[0]}-{row.iloc[1]}-{row.iloc[2]}-{row.iloc[3]}...\n{e}")
        conn.disconnect()

    @staticmethod
    def get_game_data(home: str, away: str, season: str, db_host: Optional[str] = None) -> pd.DataFrame:
        """
        Gets df of game dates for specified nba teams in season.
        :param home: str of nba city, format: "Chicago"
        :param away: str of nba city, format: "Chicago"
        :param season: str of season to check, format: '1991-1992'
        :param db_host: str of db host URL for MySQLHandler instance to connect. Defaults
        to None (for xampp's nba db)
        :return: df of game dates for teams in season
        """
        conn = MySQLHandler(db_host)
        season_start, season_end = season.split("-")[0], season.split("-")[1]

        start = f'date BETWEEN "{season_start}-01-01" AND "{season_start}-12-31" AND game_type = "playoff"'
        end = f'date BETWEEN "{season_end}-01-01" AND "{season_end}-12-31" AND game_type = "playoff"'

        condition = (f'home_team="{home}" AND visitor_team="{away}" '
                     f'AND date > "{str(conn.read("schedule", "MAX(date)", start)[1][0])}" '
                     f'AND date <= "{str(conn.read("schedule", "MAX(date)", end)[1][0])}" '
                     f'ORDER BY date;')

        table = conn.read("schedule", "*", condition)
        conn.disconnect()
        return pd.DataFrame(table[1:], columns=table[0])

    @staticmethod
    def team_in_playoffs(team: str, season: str, db_host: Optional[str] = None) -> bool:
        """
        Checks if arg team is in the playoffs for the arg season.
        :param team: str of nba team, format: Boston-Celtics/2
        :param season: str of season to check, format: '1991-1992'
        :param db_host: str of db host URL for MySQLHandler instance to connect. Defaults
        to None (for xampp's nba db)
        :return: True if arg team is in playoffs
        """
        conn = MySQLHandler(db_host)
        result = conn.in_playoffs(team, season)
        conn.disconnect()
        return result

    @staticmethod
    def season_in_db(season: str, team: str, db_host: Optional[str] = None) -> bool:
        """
        Checks if arg season is in the db already.
        :param season: str of season to check, format: '1991-1992'
        :param team: str of team to check, format: "BOS"
        :param db_host: str of db host URL for MySQLHandler instance to connect. Defaults
        to None (for xampp's nba db)
        :return: True if season in db
        """
        conn = MySQLHandler(db_host)
        result = conn.season_in_db(season, team)
        conn.disconnect()
        return result

    @staticmethod
    def team_in_db(season: str, table_name: str, db_host: Optional[str] = None) -> bool:
        """
        Checks if arg team is in the database already.
        :param season: str of season to check, format: '1991-1992'
        :param table_name: str of table to check
        :param db_host: str of db host URL for MySQLHandler instance to connect. Defaults
        to None (for xampp's nba db)
        :return: True if team in database for season
        """
        conn = MySQLHandler(db_host)
        result = conn.read(table_name, "*", f'season="{season}"')
        conn.disconnect()
        return len(result) > 1
