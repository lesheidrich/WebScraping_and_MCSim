from datetime import datetime
from typing import Optional
from model.db_handler import MySQLHandler
import pandas as pd
from model.teams import Teams
from simulator.tools import GameTools


class TeamBuilder:
    def __init__(self, db_host: Optional[str], season: str, team: Teams, game_date: str, game_type: str, h_or_a: str):
        self.validate_game_date(season, game_date)
        self.conn = MySQLHandler(db_host)
        self.team_df = self.get_team_data(season, team, game_type)
        self.player_df = self.get_player_data(team.short_name, season, game_type, h_or_a)
        self.individual_df = self.date_w_individual(team, game_date, game_type)
        self.h_or_a = h_or_a
        self.roster = Roster()
        self.build_roster(self.player_df)
        self.disconnect()

    def __del__(self):
        self.disconnect()

    def disconnect(self) -> None:
        self.conn.disconnect()

    def build_roster(self, df: pd.DataFrame) -> None:
        for i, row in df.iterrows():
            if row["position"]:
                position = getattr(self.roster, row["position"])  # eg: roster.PF
                position.append(Player(self.individual_df[self.individual_df['player'] == row["player"]],
                                       row["player"], row["GP"], row["depth"], row["MPG"]))

    def date_w_individual(self, team: Teams, game_date: str, game_type: str,
                          high_thresh: float = 0.985, mid_thresh: float = 0.8) -> pd.DataFrame:
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

    def get_individual_data(self, team_short: str, game_date: str, game_type: str):
        condition = (f'team="{team_short}" AND date >= "{int(game_date[:4]) - 1}{game_date[4:]}" '
                     f'AND date < "{game_date}" ORDER BY date')
        table = f"individual_games_{game_type}"
        return self.get_data(condition, table)

    def get_team_data(self, season: str, team: Teams, game_type: str):
        condition = f'season="{season}" AND team="{team.city_name}"'
        table = f"team_{game_type}"
        return self.get_data(condition, table)

    def get_player_data(self, team_short: str, season: str, game_type: str, h_or_a: str):
        condition = f'season="{season}" AND team="{team_short}" ORDER BY player'
        table = f"player_{game_type}_{h_or_a}"
        return self.get_data(condition, table)

    def get_data(self, condition: str, table_name: str) -> pd.DataFrame:
        table = self.conn.read(table_name, "*", condition)
        result = pd.DataFrame(table[1:], columns=table[0])
        if not len(result) > 0:
            raise ValueError(f"{table_name} table is empty! dto_sim's TeamBuilder.get_data() has "
                             f"returned an empty DataFrame when attempting to read the table with "
                             f"conditions: {condition}! Please check your database for missing values.")
        return result

    def validate_game_date(self, season, game_date) -> None:
        start_year, end_year = map(int, season.split('-'))
        game_date_dt = datetime.strptime(game_date, '%Y-%m-%d')
        season_start = datetime(start_year, 8, 30)
        season_end = datetime(end_year, 8, 30)

        if not season_start <= game_date_dt <= season_end:
            raise ValueError(f"Game date {game_date} is outside the scope of the {season} season!")


class Roster:
    def __init__(self):
        self.PF = []
        self.SF = []
        self.PG = []
        self.SG = []
        self.C = []

    def __iter__(self):
        return iter(self.PF + self.SF + self.PG + self.SG + self.C)


class Player:
    def __init__(self, df: pd.DataFrame, player: str, GP: str, depth: str, avg_min: float):
        # avg stats
        self.TOV = None
        self.BLK = None
        self.STL = None
        self.AST = None
        self.REB = None
        self.DRB = None
        self.ORB = None
        self.FTA = None
        self.FTM = None
        self.threePA = None
        self.threePM = None
        self.FGA = None
        self.FGM = None
        self.PTS = None
        self.populate_attribs(df)
        self.FGpercent = self.handle_zero_div(self.FGM, self.FGA)
        self.threePpercent = self.handle_zero_div(self.threePM, self.threePA)
        self.FTpercent = self.handle_zero_div(self.FTM, self.FTA)
        self.name = player
        self.GP = int(GP)
        self.depth = depth
        # weights
        self.playtime_w = self.calculate_playtime_w(depth, avg_min, df)
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
        return self.totalPpercent * 0.75 + 2.383 * self.AST * 0.25 + 5 * self.ORB * 0.25 + self.STL * 0.53 * 0.25

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

    def calculate_playtime_w(self, depth: str, avg_min: float, df: pd.DataFrame) -> float:
        """
        Play probability logic:
          - first string players probability is increased by sigmoid function (incremenet size
            decreases as probability increases) as long as play prob is under 0.89.
          - second string players probability are decreased.
          - third string players are severely decreased (threefold)
          - all other depths are 0
          - if a player is injured in last 2 games, 0 is passed, and play probability is also 0.
        :param depth:
        :param avg_min:
        :return: float for player's play probability per game
        """
        prob = avg_min / 48
        if not self.played_last_game(df):
            return 0

        if depth == "2":
            prob *= 0.25
        elif depth == "3":
            prob *= 0.02
        else:
            if depth != "1":
                prob = 0

        return prob if prob > 0 else 0

    def played_last_game(self, df) -> bool:
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
