"""
Module: control_service.py

Module for controlling the scraping and persistence of data from RealGM website.

This module provides a ScrapeControl class that facilitates the scraping and persistence of various data
tables from the RealGM website. It utilizes DataTransferObject and Persist classes for data handling and
persistence operations, respectively.

Classes:
    - ScrapeControl: A class for controlling the scraping and persistence of data from RealGM.

Dependencies:
    - DataTransferObject: A class for handling data transfer.
    - Persist: A class for persisting data to a database.
    - Logger: A class for logging information during scraping and persistence operations.
"""

from typing import Optional
from controller.dto_service import DataTransferObject, Persist
from log.logger import Logger


class ScrapeControl:
    """
        Class for controlling the scraping and persistence of data from RealGM website.

        Attributes:
            dto (DataTransferObject): An instance of the DataTransferObject class for handling data transfer.
            db_host (Optional[str]): The URL of the database host. Defaults to None.
            players (list): A list to store player data.
            base (str): The base URL of the RealGM website.
            season (str): The season for which data is being scraped, in the format 'YYYY-YYYY'.
            team (str): The name of the NBA team for which data is being scraped.
            year (str): The last four digits of the season, extracted from the 'season' attribute.
            urls (dict): A dictionary containing URLs for different categories of data scraping.
            in_playoffs (bool): A boolean indicating whether the specified team is in the playoffs for
            the given season.
            df_depth (DataFrame): A DataFrame to store depth chart data.
            log (Logger): An instance of the Logger class for logging information.

        Methods:
            run_all(scrape_method: str) -> None:
                Scrapes and persists all tables from RealGM for the specified season and team.
            run_single(category_type: str, scrape_method: str) -> None:
                Processes only the specified category of data scraping for the team.
            process_player(scrape_method: str, url: str, table_name: str) -> None:
                Scrapes player data from the specified RealGM URL and persists it to the specified table
                in the database.
            process_individual(scrape_method: str, url: str, table_name: str) -> None:
                Scrapes individual tables from RealGM to the specified table in the database.
            process_team(scrape_method: str, url: str, table_name: str) -> None:
                Scrapes team table from RealGM to the specified table in the database.
            set_link_tree() -> dict:
                Provides a dictionary of URLs for RealGM scraping based on initialization arguments.
        """
    def __init__(self, proxies_csv: Optional[str], season: str, team: str,
                 check_proxies: bool = False, db_host: Optional[str] = None):
        self.dto = DataTransferObject(proxies_csv, check_proxies)
        self.db_host = db_host
        self.players = []
        self.base = "https://basketball.realgm.com/nba/team"
        self.season = season
        self.team = team
        self.year = self.season.split('-')[1]
        self.urls = self.set_link_tree()
        self.in_playoffs = Persist.team_in_playoffs(self.team, self.season, db_host)
        self.df_depth = None
        self.log = Logger(log_file="app_test_log.log", name="Scrape Control", log_level="INFO")

    def run_all(self, scrape_method: str) -> None:
        """
        Method scrapes and persists all tables from RealGM for specified season and team.
        The link tree is parsed to account for the team playing in the playoffs, and
        removes playoff links otherwise. It then proceeds to scrape.
        In case of an error during scraping, the process attempts to continue on using
        Firefox WebDriver for the page that caused the error (in case website's js blocks
        scrape attempt).
        :param scrape_method: str of specified scrape method to utilize
        :return: None
        """
        url_depth = f"{self.base}s/{self.team}/Depth_Charts"
        self.df_depth = self.dto.new_depth_df(scrape_method, url_depth, self.season)

        for category, (links, tables) in self.urls.items():
            self.log.info(f"Scraping category: {category}, team: {self.team}, season: {self.season}.")
            for link, table in zip(links, tables):
                if (not self.in_playoffs and "Playoff" not in link) or self.in_playoffs:
                    try:
                        method = getattr(self, f"process_{category}")
                        method(scrape_method, link, table)
                    # pylint: disable=W0718
                    except Exception as e:
                        self.log.warning(f"Scrape method {scrape_method} failed for {link} on table {table}."
                                         f" {e}")
                        method = getattr(self, f"process_{category}")
                        method("firefox_selenium_scrape", link, table)

    def run_single(self, category_type: str, scrape_method: str) -> None:
        """
        Runs specified scrape and persist method. Use to process only the team, individual, or
        player table.
        :param category_type: category to scrape: 'team', 'individual', 'player'
        :param scrape_method: str of chosen scrape method
        :return: None
        """
        links = self.urls[category_type]
        method = getattr(self, f"process_{category_type}")

        for _ in range(len(links[0])):
            if (not self.in_playoffs and "Playoff" not in links[0][_]) or self.in_playoffs:
                method(scrape_method, links[0][_], links[1][_])

    def process_player(self, scrape_method: str, url: str, table_name: str) -> None:
        """
        Scrapes player data from specified RealGM URL to specified table in db.
        :param scrape_method: str of chosen scrape method
        :param url: str URL of website to scrape
        :param table_name: str name of table to populate with scraped data
        :return: None
        """
        if self.df_depth is None:
            url_depth = f"{self.base}s/{self.team}/Depth_Charts"
            self.df_depth = self.dto.new_depth_df(scrape_method, url_depth, self.season)

        df_player = self.dto.new_players_df(scrape_method, url)
        self.dto.player_depth_merged_df(self.df_depth, df_player)
        df_player['Season'] = self.season
        Persist.insert(df_player, table_name, "player", self.db_host)

    def process_individual(self, scrape_method: str, url: str, table_name: str) -> None:
        """
        Scrapes individual tables from RealGM to specified table in database.
        Method follows next page link from initial page to gather entire table
        for the specified team and season.
        :param scrape_method: str of chosen scrape method
        :param url: str URL of website to scrape
        :param table_name: str name of table to populate with scraped data
        :return: None
        """
        df_individual = self.dto.merged_individual_df(scrape_method, url)
        Persist.insert(df_individual, table_name, "individual", self.db_host)

    def process_team(self, scrape_method: str, url: str, table_name: str) -> None:
        """
        Scrapes team table from RealGM to specified table in database.
        :param scrape_method: str of chosen scrape method
        :param url: str URL of website to scrape
        :param table_name: str name of table to populate with scraped data
        :return: None
        """
        if not Persist.team_in_db(self.season, table_name, self.db_host):
            df_team = self.dto.new_team_df(scrape_method, url)
            df_team['Season'] = self.season
            Persist.insert(df_team, table_name, "team", self.db_host)
        else:
            self.log.info(f"Team {self.team} with season {self.season} is already in the database.")

    def set_link_tree(self) -> dict:
        """
        Provides dictionary of URLs for RealGM scraping based on initialization args.
        :return: dictionary of URLs
        """
        return {
            "player": [
                [
                    f"{self.base}s/{self.team}/Stats/{self.year}/Averages/All/points/All/desc/1/Home",
                    f"{self.base}s/{self.team}/Stats/{self.year}/Averages/All/points/All/desc/1/Away",
                    f"{self.base}s/{self.team}/Stats/{self.year}/Averages/All/points/All/desc/1/Playoff_Home",
                    f"{self.base}s/{self.team}/Stats/{self.year}/Averages/All/points/All/desc/1/Playoff_Away"
                ],
                [
                    "player_regular_home",
                    "player_regular_away",
                    "player_playoff_home",
                    "player_playoff_away"
                ]
            ],
            "team": [
                [
                    f"{self.base}-stats/{self.year}/Advanced_Stats/Team_Totals/Regular_Season",
                    f"{self.base}-stats/{self.year}/Advanced_Stats/Team_Totals/Playoffs"
                ],
                [
                    "team_regular",
                    "team_playoff"
                ]
            ],
            "individual": [
                [
                    f"{self.base}s/{self.team}/individual-games/{self.year}/points/Regular_Season/desc/",
                    f"{self.base}s/{self.team}/individual-games/{self.year}/points/Playoffs/desc/"
                ],
                [
                    "individual_games_regular",
                    "individual_games_playoff"
                ]
            ]
        }
