"""
Module: parse_service.py

This module provides classes and functions for parsing HTML content
from RealGM website and converting it into structured data.

Dependencies:
    - re
    - StringIO from io
    - Optional from typing
    - pandas as pd
    - bs4 from BeautifulSoup
    - Logger from log.logger
"""

import re
from io import StringIO
from typing import Optional
import pandas as pd
import bs4
from log.logger import Logger


class RealGMParser:
    """
    RealGMParser class contains static methods for parsing HTML content
    from the RealGM website and converting it into structured data.

    Methods:
        - parse_footnote_unavailable(html_content: str) -> bool
        - full_name_populate_depth_position(player_name: str, player_df: pd.DataFrame,
                                             r: pd.Series, depth_df: pd.DataFrame,
                                             ind, col) -> bool
        - initial_name_populate_depth_position(player_df: pd.DataFrame, player_name: str,
                                                r: pd.Series, depth_df: pd.DataFrame,
                                                ind, col) -> bool
        - parse_depth_2_players(df_depth: pd.DataFrame, df_player: pd.DataFrame) -> None
        - players_df_add_columns(df: pd.DataFrame) -> None
        - depth_table_2_df(sauce: str, years: str) -> pd.DataFrame
        - html_table_append_df(sauce: str, df_base: Optional[pd.DataFrame]) -> pd.DataFrame
        - html_table_2_df(sauce: str) -> pd.DataFrame
    """
    @staticmethod
    def parse_footnote_unavailable(html_content: str) -> bool:
        """
        Returns True if there is no table on the page (html content).
        The phrase 'Stats are not currently available for this season.' is present if
        the page lacks a stat table, or if the URL params are incorrect.
        :param html_content: html content of website
        :return: True if no stat table  in html
        """
        soup = bs4.BeautifulSoup(html_content, 'html.parser')
        footnote_paragraphs = soup.find_all('p', class_='footnote')

        for p in footnote_paragraphs:
            if p.get_text() == "Stats are not currently available for this season.":
                return True
        return False

    @staticmethod
    def full_name_populate_depth_position(player_name: str, player_df: pd.DataFrame, r: pd.Series,
                                          depth_df: pd.DataFrame, ind, col) -> bool:
        """
        Populates player dfs 'Depth' and 'Position' columns from depth df where
        player names math.
        This function focuses specifically on full name matches.
        RealGMParser.initial_name_populate_depth_position() populates based on first and
        middle name initials.
        :param player_name: str of player name as provided in player df, eg: 'Michael Jordan'
        :param player_df: player stat averages per season df
        :param r: row data of depth df
        :param depth_df: player position and rotation string per season
        :param ind: index of player in the player df
        :param col: column indicating player's position (e.g.: SG)
        :return: True if successful, else False
        """
        if player_name in player_df["Player"].values:
            depth = "1" if r[depth_df.columns[0]] == "Starters" else (
                r[depth_df.columns[0]] if r[depth_df.columns[0]] == "Lim PT" else str(ind + 1))
            player_index = player_df.index[player_df["Player"] == player_name]
            player_df.at[player_index[0], "Depth"] = depth
            player_df.at[player_index[0], "Position"] = col
            return True
        return False

    @staticmethod
    def initial_name_populate_depth_position(player_df: pd.DataFrame, player_name: str, r: pd.Series,
                                             depth_df: pd.DataFrame, ind, col) -> bool:
        """
        Populates player dfs 'Depth' and 'Position' columns from depth df where
        player names math.
        This function focuses specifically on initial-based name matches (e.g.: B. Cartwright)
        RealGMParser.full_name_populate_depth_position() populates based on full name.
        :param player_df: player stat averages per season df
        :param player_name: str of player name as provided in player df, eg: 'B. Cartwright'
        :param r: row data of depth df
        :param depth_df: player position and rotation string per season
        :param ind: index of player in the player df
        :param col: column indicating player's position (e.g.: SG)
        :return: True if successful, else False
        """
        if player_df['Player'].apply(lambda x: bool(re.search(player_name, x))).any():
            depth = "1" if r[depth_df.columns[0]] == "Starters" else (
                r[depth_df.columns[0]] if r[depth_df.columns[0]] == "Lim PT" else str(ind + 1))
            player_index = player_df.index[player_df['Player'].apply(lambda x: bool(
                re.search(player_name, x)))]
            player_df.at[player_index[0], "Depth"] = depth
            player_df.at[player_index[0], "Position"] = col
            return True
        return False

    @staticmethod
    def parse_depth_2_players(df_depth: pd.DataFrame, df_player: pd.DataFrame) -> None:
        """
        Wrapper function that utilizes RealGMParser.full_name_populate_depth_position() and
        RealGMParser.initial_name_populate_depth_position() to parse and map player positions
        and depth in rotation from the depth df to the player df.
        :param df_depth: player position and rotation string per season
        :param df_player: player stat averages per season df
        :return: None
        """
        for i, row in df_depth.iterrows():
            for column, value in row.items():
                if column == df_depth.columns[0]:
                    continue
                if pd.notna(value):
                    # separates stats from player name in depth df and strips it
                    name = re.split(r'(?=\d)', value, 1)[0].strip()
                    pattern = re.escape(name[0]) + r'.*' + re.escape(name.split()[-1])

                    if not (RealGMParser.full_name_populate_depth_position(
                            name, df_player, row, df_depth, i, column)
                            or
                            RealGMParser.initial_name_populate_depth_position(
                                df_player, pattern, row, df_depth, i, column)):
                        log = Logger(log_file="app_test_log.log", name="Depth Parser", log_level="INFO")
                        log.info(f"Player {name} is missing from the Players table!")

    @staticmethod
    def players_df_add_columns(df: pd.DataFrame) -> None:
        """
        Adds position, depth, and season solumns to specified player df.
        :param df: player df to append columns to
        :return: None
        """
        df["Position"] = ""
        df["Depth"] = ""
        df.insert(df.columns.get_loc("Player") + 1, "Season", "")

    @staticmethod
    def depth_table_2_df(sauce: str, years: str) -> pd.DataFrame:
        """
        Converts htmls content string's depth table to depth df for specified season.
        :param sauce: html content string
        :param years: str for season, format: '1991-1992'
        :return: depth df
        """
        soup = bs4.BeautifulSoup(sauce, 'html.parser')
        h2_element = soup.find('h2', string=lambda text: text and years in text)
        div_with_table = h2_element.find_next_sibling('div')
        table_html = div_with_table.find('table', class_='basketball')
        table_str = str(table_html)
        mock_html = StringIO(table_str)
        return pd.read_html(mock_html)[0]

    @staticmethod
    def html_table_append_df(sauce: str, df_base: Optional[pd.DataFrame]) -> pd.DataFrame:
        """
        Concatenates multiple html source codes containing individual tables from RealGM with
        param of base individual df, which can initially be None. Results in one large concatenated
        individual df for a given team in a season.
        :param sauce: html content string
        :param df_base: individual df to append (can be None)
        :return: merged individual df
        """
        df_extension = RealGMParser.html_table_2_df(sauce)
        df_base = pd.concat([df_base, df_extension], ignore_index=True)
        return df_base

    @staticmethod
    def html_table_2_df(sauce: str) -> pd.DataFrame:
        """
        Converts class="tablesaw" table in html source from RealGM to df.
        :param sauce: html content string
        :return: df of table from html content
        """
        soup = bs4.BeautifulSoup(sauce, 'html.parser')
        table_html = soup.find('table', class_='tablesaw')
        table_str = str(table_html)
        mock_html = StringIO(table_str)

        return pd.read_html(mock_html)[0]
