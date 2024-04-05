"""
Module: dto_sim.py

Module for building team data to be used by Monte Carlo sim.

This module provides a class, `TeamBuilder`, for constructing team rosters by retrieving and processing game
data from a MySQL database. It utilizes individual game data to calculate player statistics and populate
roster positions accordingly.

Classes:
    - TeamBuilder: Class for building team data to be used by Monte Carlo sim.
    - Roster: Represents a team's roster.
    - Player: Represents a basketball player with stats built from the last 365 days of games.

Attributes:
    - pd: pandas library for data manipulation.
    - MySQLHandler: Custom module for handling MySQL database operations.
    - Teams: Enum representing basketball teams.

Usage:
    Example usage of `TeamBuilder` class:
    ```
    from datetime import datetime
    from model.db_handler import MySQLHandler
    import pandas as pd
    from model.teams import Teams

    # Initialize a TeamBuilder instance
    builder = TeamBuilder(db_host=None, season="1991-1992", team=Teams.from_short_name('CHI'),
                          game_date="1993-04-30", game_type="regular", h_or_a="home")
"""

from datetime import datetime
from typing import Optional
import pandas as pd
from model.db_handler import MySQLHandler
from model.teams import Teams


class TeamBuilder:
    """
    Class for building team data to be used by Monte Carlo sim.
    Contains dfs for team, individual, and player tables from db.

    This class is responsible for constructing team rosters by retrieving and processing game data
    from a MySQL database. It utilizes individual game data to calculate player statistics and populate
    roster positions accordingly.

        Args:
        db_host (Optional[str]): The host address of the MySQL database.
        season (str): The season for which to build the team roster (e.g., '1991-1992').
        team (Teams): The team for which to build the roster.
        game_date (str): The date of the game in 'YYYY-MM-DD' format.
        game_type (str): The type of game, either 'regular' or 'playoff'.
        h_or_a (str): Specifies whether the game is home ('home') or away ('away').

    Attributes:
        conn (MySQLHandler): Connection to the MySQL database.
        team_df (pd.DataFrame): DataFrame containing team data for the specified season and game type.
        player_df (pd.DataFrame): DataFrame containing player data for the specified team, season, and game
        type.
        individual_df (pd.DataFrame): DataFrame containing individual game data modified to account for
        recent games.
        h_or_a (str): Indicates whether the game is home or away.
        roster (Roster): Instance of the Roster class to hold player positions.

    Methods:
        disconnect(self): Disconnects from the MySQL database.
        build_roster(self, df: pd.DataFrame): Populates the roster instance's position lists based on player
        data.
        date_w_individual(self, team: Teams, game_date: str, game_type: str,
                          high_thresh: float = 0.985, mid_thresh: float = 0.8) -> pd.DataFrame:
            Modifies individual game data to account for recent games and returns the modified DataFrame.
        get_individual_data(self, team_short: str, game_date: str, game_type: str) -> pd.DataFrame:
            Retrieves individual game data for the specified team, game date, and game type.
        get_team_data(self, season: str, team: Teams, game_type: str) -> pd.DataFrame:
            Retrieves team data for the specified season and game type.
        get_player_data(self, team_short: str, season: str, game_type: str, h_or_a: str) -> pd.DataFrame:
            Retrieves player data for the specified team, season, game type, and home/away status.
        get_data(self, condition: str, table_name: str) -> pd.DataFrame:
            Reads data from the specified table in the MySQL database and returns it as a DataFrame.
        validate_game_date(self, season: str, game_date: str) -> None:
            Validates that the game date falls within the chosen season.
    """
    def __init__(self, db_host: Optional[str], season: str, team: Teams, game_date: str, game_type: str,
                 h_or_a: str):
        self.validate_game_date(season, game_date)
        self.conn = MySQLHandler(db_host)
        self.team_df = self.get_team_data(season, team, game_type)
        self.player_df = self.get_player_data(team.short_name, season, game_type, h_or_a)
        self.individual_df = self.date_w_individual(team, game_date, game_type)
        self.h_or_a = h_or_a
        self.roster = Roster()
        self.build_roster(self.player_df)
        self.disconnect()
        self.validate_roster()

    def __del__(self):
        if self.conn.connection.is_connected:
            self.disconnect()

    def disconnect(self) -> None:
        """
        Disconnects from db.
        :return: None
        """
        self.conn.disconnect()

    def build_roster(self, pl_df: pd.DataFrame) -> None:
        """
        Populates roster instance's position lists (e.g.: Roster.SG, etc.)
        Follows player df to reconstruct roster stats from individual game data
        (from the last 365 days, where last 2-3 games have a greater weight, and
        last few weeks of season are also weighted compared to earlier games). Stats
        are loaded into Player instances, which populate the Roster position lists.
        All stats are calculated averages from individual games.
        :param pl_df: player df for team and season
        :return: None
        """
        # pd.set_option('display.max_rows', None)
        # pd.set_option('display.max_columns', None)
        # print(self.individual_df)
        # print(self.player_df)

        for _, row in pl_df.iterrows():
            test = row["position"] and row["player"] in self.individual_df['player'].unique()
            if test:
                position = getattr(self.roster, row["position"])
                position.append(Player(self.individual_df.loc[self.individual_df['player'] == row["player"], 
                                       :], row["player"], row["GP"], row["depth"], row["MPG"]))
                setattr(self.roster, row["position"], position)
            # draft picks and traded players
            if row["position"] and not test:
                # mock individual df fabricated from season data for draft picks and trades
                mock_ind_df = pd.DataFrame({
                    "id": [row["id"]],
                    "player": [row["player"]],
                    "date": [self.individual_df['date'].max()],
                    "team": [row["team"]],
                    "MIN": [row["MPG"]],
                    "PTS": [row["PPG"]],
                    "FGM": [row["FGM"]],
                    "FGA": [row["FGA"]],
                    "3PM": [row["3PM"]],
                    "3PA": [row["3PA"]],
                    "FTM": [row["FTM"]],
                    "FTA": [row["FTA"]],
                    "ORB": [row["ORB"]],
                    "DRB": [row["DRB"]],
                    "REB": [row["RPG"]],
                    "AST": [row["APG"]],
                    "STL": [0],
                    "BLK": [0],
                    "TOV": [0],
                    "PF": [0],
                    "interval_game": [0]
                })
                position = getattr(self.roster, row["position"])
                position.append(Player(mock_ind_df,
                                       row["player"], row["GP"], row["depth"], row["MPG"]))

    def date_w_individual(self, team: Teams, game_date: str, game_type: str,
                          high_thresh: float = 0.985, mid_thresh: float = 0.8) -> pd.DataFrame:
        """
        Modifies individual games df by making most recent games count for more in averages.
        Instead of using weights:
            - last 2-3 games are in df 5x
            - last few weeks of games are in df 3x
            - anything past 20% of current date in 365 day range only counts 1x
        These stats are calculated into yearly player averages by build_roster and stored in
        Player instances.
        :param team: Teams object for team in table
        :param game_date: str of game date: "1993-04-30"
        :param game_type: str for game type: 'regular' or 'playoff'
        :param high_thresh: float threshold for where to repeat games 5x from, default: 0.985
        :param mid_thresh: float threshold for where to repeat games 3x from, default: 0.8
        :return: individual games df with rows repeating where games more recent
        """
        df = self.get_individual_data(team.short_name, game_date, game_type)
        df['date'] = pd.to_datetime(df['date'])
        game_date_dt = pd.to_datetime(game_date)

        df['interval_game'] = (365 + (df['date'] - game_date_dt).dt.days) / 365
        mask_5x = df['interval_game'] > high_thresh
        mask_3x = (df['interval_game'] <= high_thresh) & (df['interval_game'] > mid_thresh)
        p_5x = df[mask_5x].copy()
        p_3x = df[mask_3x].copy()
        p_1x = df[~(mask_5x | mask_3x)].copy()
        p_5x = pd.concat([p_5x] * 5, ignore_index=True)
        p_3x = pd.concat([p_3x] * 3, ignore_index=True)

        return pd.concat([p_5x, p_3x, p_1x], ignore_index=True).sort_values(by=['date'])

    def get_individual_data(self, team_short: str, game_date: str, game_type: str) -> pd.DataFrame:
        """
        Gets individual df of game data from previous 365 days, up until game_date for game type.
        :param team_short: str short form of team, format: 'CHI'
        :param game_date: str of game date: '1993-04-30'
        :param game_type: str for game type: 'regular' or 'playoff'
        :return: individual df
        """
        condition = (f'team="{team_short}" AND date >= "{int(game_date[:4]) - 1}{game_date[4:]}" '
                     f'AND date < "{game_date}" ORDER BY date')
        table = f"individual_games_{game_type}"
        return self.get_data(condition, table)

    def get_team_data(self, season: str, team: Teams, game_type: str) -> pd.DataFrame:
        """
        Gets team df for season and game type.
        :param season: str of season, format: '1991-1992'
        :param team: str of team's city name, format: 'Chicago'
        :param game_type: str for game type: 'regular' or 'playoff'
        :return: team df for season and game type
        """
        condition = f'season="{season}" AND team="{team.city_name}"'
        table = f"team_{game_type}"
        return self.get_data(condition, table)

    def get_player_data(self, team_short: str, season: str, game_type: str, h_or_a: str) -> pd.DataFrame:
        """
        Gets player df for seasn and game type.
        :param team_short: str short form of team, format: 'CHI'
        :param season: str of season, format: '1991-1992'
        :param game_type: str for game type: 'regular' or 'playoff'
        :param h_or_a: str of 'home' or 'away'
        :return: player df for season and game type
        """
        condition = f'season="{season}" AND team="{team_short}" ORDER BY player'
        table = f"player_{game_type}_{h_or_a}"
        return self.get_data(condition, table)

    def get_data(self, condition: str, table_name: str) -> pd.DataFrame:
        """
        Reads specified table from db and converts it to df.
        :param condition: str for condition to use in SQL command after WHERE
        :param table_name: str of table to read from
        :return: df of read table's data
        """
        table = self.conn.read(table_name, "*", condition)
        result = pd.DataFrame(table[1:], columns=table[0])
        if not len(result) > 0:
            raise ValueError(f"{table_name} table is empty! dto_sim's TeamBuilder.get_data() has "
                             f"returned an empty DataFrame when attempting to read the table with "
                             f"conditions: {condition}! Please check your database for missing values.")
        return result

    def validate_game_date(self, season: str, game_date: str) -> None:
        """
        Checks to make sure the game_date is inside the chosen season. Raises ValueError if test failed.
        :param season: str of season, format: '1991-1992'
        :param game_date: str of game date: '1993-04-30'
        :return: None
        :raises: ValueError if game_date outside season
        """
        start_year, end_year = map(int, season.split('-'))
        game_date_dt = datetime.strptime(game_date, '%Y-%m-%d')
        season_start = datetime(start_year, 8, 30)
        season_end = datetime(end_year, 8, 30)

        if not season_start <= game_date_dt <= season_end:
            raise ValueError(f"Game date {game_date} is outside the scope of the {season} season!")

    def validate_roster(self) -> None:
        """
        Ensures all roster positions are filled.
        :return: None
        """
        for attrib in ["PF", "SF", "PG", "SG", "C"]:
            position = getattr(self.roster, attrib)
            if len(position) < 1:
                raise ValueError(f"Position {attrib} is empty! All roster positions must be filled for "
                                 f"{self.h_or_a} team!")


class Roster:
    """
    Represents a team's roster. The class is made up of lists representing each position. Each list
    is populated with Player instances containing stat averages from the previous 365 days games.

    Attributes:
        PF (list): List of Player instances in the power forward position.
        SF (list): List of Player instances in the small forward position.
        PG (list): List of Player instances in the point guard position.
        SG (list): List of Player instances in the shooting guard position.
        C (list): List of Player instances in the center position.

    Methods:
        __iter__(): Returns an iterator over all players in the roster.
    """
    def __init__(self):
        self.PF = []
        self.SF = []
        self.PG = []
        self.SG = []
        self.C = []

    def __iter__(self):
        return iter(self.PF + self.SF + self.PG + self.SG + self.C)

    def get_stat_df(self) -> pd.DataFrame:
        """
        Returns df with all columns and rows printable. Columns all pertain to player weight stats and
        the metrics they are based on.
        :return: df of player stats with rows and columns fully printable
        """
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)

        cols = ["name", "playtime_w", "adjusted_points", "player_w", "totalPpercent", "AST", "ORB", "STL"]
        records = []
        for p in iter(self):
            records.append([p.name, p.playtime_w, p.adjusted_points, p.playtime_w, p.totalPpercent, p.AST, 
                            p.ORB, p.STL])
        return pd.DataFrame(records, columns=cols)


class Player:
    """
    Class instances represent basketball players with stats built from the last 365 days of games which
    the player participated in. All stats represent averages of their performance in this timeframe, with
    the last 2-3 games counting five-fold, and the last 20% of the year (representing last few weeks)
    counting three-fold compared to earlier game stats. These weigh the most recent performance of the player
    at a greater value than their earlier performance in the timeframe.

    Attributes:
        TOV (float): Turnovers per game.
        BLK (float): Blocks per game.
        STL (float): Steals per game.
        AST (float): Assists per game.
        REB (float): Total rebounds per game.
        DRB (float): Defensive rebounds per game.
        ORB (float): Offensive rebounds per game.
        FTA (float): Free throw attempts per game.
        FTM (float): Free throws made per game.
        threePA (float): Three-point attempts per game.
        threePM (float): Three-pointers made per game.
        FGA (float): Field goal attempts per game.
        FGM (float): Field goals made per game.
        PTS (float): Points per game.
        FGpercent (float): Field goal percentage.
        threePpercent (float): Three-point percentage.
        FTpercent (float): Free throw percentage.
        name (str): Name of the player.
        GP (int): Games played.
        depth (str): Player's depth in the team roster.
        playtime_w (float): Player's playtime weight.
        totalPpercent (float): Total points percentage.
        adjusted_points (float): Adjusted points per game.
        player_w (float): Player's overall weight.

    Methods:
        populate_attribs(df: pd.DataFrame) -> None: Populates player attributes from filtered individual
        games df and player df.
        calculate_adjusted_points() -> float: Calculates adjusted points per game.
        calulate_totalPpercent() -> float: Calculates total points percentage.
        handle_zero_div(num, den) -> float: Handles percentage stat attribute creation in case of n/0.
        calculate_playtime_w(depth: str, avg_min: float, df: pd.DataFrame) -> float: Calculates player's
        playtime weight.
        played_last_game(df) -> bool: Checks if the player played the last game.
    """
    def __init__(self, df: pd.DataFrame, player: str, GP: str, depth: str, avg_min: float):
        # avg stats
        self.TOV = 0
        self.BLK = 0
        self.STL = 0
        self.AST = 0
        self.REB = 0
        self.DRB = 0
        self.ORB = 0
        self.FTA = 0
        self.FTM = 0
        self.threePA = 0
        self.threePM = 0
        self.FGA = 0
        self.FGM = 0
        self.PTS = 0
        self.populate_attribs(df)
        self.FGpercent = self.handle_zero_div(self.FGM, self.FGA)
        self.threePpercent = self.handle_zero_div(self.threePM, self.threePA)
        self.FTpercent = self.handle_zero_div(self.FTM, self.FTA)
        self.name = player
        self.GP = int(GP)
        self.depth = depth
        # weights
        self.playtime_w = self.calculate_playtime_w(depth, avg_min)
        self.totalPpercent = self.calulate_totalPpercent()
        self.adjusted_points = self.calculate_adjusted_points()
        self.player_w = (self.adjusted_points/100 + self.playtime_w)/2

    def populate_attribs(self, df: pd.DataFrame) -> None:
        """
        Populates player attributes from filtered individual games df and player df.
        :param df: filtered self.individual_df (individual games filtered to player from last 365 days)
        :return: None
        """
        self.PTS = df['PTS'].mean() / 100
        self.FGM = df['FGM'].mean() / 100
        self.FGA = df['FGA'].mean() / 100
        self.threePM = df['3PM'].mean() / 100
        self.threePA = df['3PA'].mean() / 100
        self.FTM = df['FTM'].mean() / 100
        self.FTA = df['FTA'].mean() / 100
        self.ORB = df['ORB'].mean() / 100
        self.DRB = df['DRB'].mean() / 100
        self.REB = df['REB'].mean() / 100
        self.AST = df['AST'].mean() / 100
        self.STL = df['STL'].mean() / 100
        self.BLK = df['BLK'].mean() / 100
        self.TOV = df['TOV'].mean() / 100

    def calculate_adjusted_points(self) -> float:
        """
        San Diego State University's formulate for calculating adjust points per game applied to
        personal averages:
        points*(.75) + 2.383*(assists)*(.25) + offensive rebounds*(0.588)*(.25) + steals*(.530)*(.25)
        :return: float of average adjusted points
        """
        return (self.totalPpercent * 0.75 + 2.383 * self.AST * 0.25 + 5 * self.ORB * 0.25 + self.STL * 0.53
                * 0.25)

    def calulate_totalPpercent(self) -> float:
        """
        Calculates total points average per player from last 365 days.
        :return: float of total points percentage
        """
        return (self.FGpercent + self.threePpercent + self.FTpercent) / 3

    def handle_zero_div(self, num, den) -> float:
        """
        Handles percentage stat attribute creation in case of n/0.
        :param num: numerator for measured stat success (e.g.: FTM)
        :param den: denominator for measured stat attempts (e.g.: FTA)
        :return: float for stat probability
        """
        if den > 0:
            return num/den * 100
        return 0

    def calculate_playtime_w(self, depth: str, avg_min: float) -> float:
        """
        Play probability logic:
          - first string players probability is left unchanged
          - second string players probability are decreased to ensure they play as 'bench' players
          - third string players are severely decreased (2%) as they don't play regularly
          - all other depths are 0
          - if a player didn't play int heir previous game, they are presumed to be injured and receive
            a playtime weight of 0
        :param df: individual games df filtered for player
        :param depth: str of player depth
        :param avg_min: float value for average min played per game
        :return: float for player's play probability per game
        """
        prob = avg_min / 48

        if depth == "2":
            prob *= 0.25
        elif depth == "3":
            prob *= 0.02
        else:
            if depth != "1":
                prob = 0

        return prob if prob > 0 else 0

    def played_last_game(self, df: pd.DataFrame) -> bool:
        """
        Checks last game for player to ensure playtime not 0 (presume injured).
        :param df: players individual games DataFrame
        :return: True if player played last game.
        """
        if not len(df) > 0:
            return False

        min_td = df.iloc[-1]['MIN']
        value = min_td.components.hours
        return value > 0
