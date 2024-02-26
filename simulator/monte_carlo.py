"""
Module: monte_carlo.py

Module for conducting Monte Carlo simulations of basketball games.

This module provides classes for simulating basketball games using Monte Carlo methods.

Classes:
    - Simulation: Class for simulating a single basketball game and tracking home and away scores.
    - MonteCarlo: Class for conducting Monte Carlo simulations to predict game outcomes based on historical
      data.

Dependencies:
    - random: Python's built-in library for generating random numbers.
    - matplotlib.pyplot: Library for creating plots and visualizations.
    - numpy: Library for numerical computing.
    - TeamBuilder: Class from controller.dto_sim module for building basketball teams.
    - Teams: Class from model.teams module representing basketball teams.
    - GameBuilder: Class from simulator.game_service module for managing game simulations.
    - GameTools: Class from simulator.tools module providing various tools for game simulations.
"""
import base64
import statistics
from io import BytesIO
from typing import Optional
import matplotlib.pyplot as plt
import numpy as np
from controller.dto_sim import TeamBuilder
from model.teams import Teams
from simulator.game_service import GameBuilder
from simulator.tools import GameTools


class Simulation:
    """
    Class builds Monte Carlo simulation for a single basketball game, and tracks home and away scores.
    Instances used by MonteCarlo class.

    Attributes:
        game (GameBuilder): An instance of GameBuilder for managing the game simulation.
        home_pts (int): The total points scored by the home team.
        away_pts (int): The total points scored by the away team.

    Methods:
        play_game(): Runs the simulation of the basketball game between the home and away teams.
        possession(has_ball: TeamBuilder): Simulates a possession during the game, determining turnovers,
            shot attempts, and scoring.
        get_pace(): Calculates and returns the pace of the game based on the statistical attributes of the
        teams.
    """
    def __init__(self, db_host: Optional[str], season: str, home_team: Teams, away_team: Teams,
                 game_date: str, game_type: str):
        self.game = GameBuilder(db_host, season, home_team, away_team, game_date, game_type)
        self.home_pts = 0
        self.away_pts = 0

    def play_game(self) -> None:
        """
        Runs game between home and away TeamBuilder instances. Uses pace from instances to define
        a pace for the game. Iterates over possessions until pace is reached. Note that not all
        possessions lead to points scored.
        :return: None
        """
        for _ in range(self.get_pace()):
            self.possession(self.game.has_ball)

    def possession(self, has_ball: TeamBuilder) -> None:
        """
        Possessions start by identifying Roster instance Players instances that are on the court for the
        current play. From these, the players are selected that are actively involved in the offensive.
        Turnover (TOV) is calculated using simulate_stat(). Here, a weighted probability based step function
        decides if the ball is turned over in order for the other team to take possession of the ball.
        If the possession continues, the Player instances involved in the offense attempt a shot. The same
        step function decides success, in which case the other team takes possession. On failure, the step
        function calculates if an offensive rebound (ORB) was successful, else the ball is turned over.
        :param has_ball: TeamBuilder instance's home or away
        :return: None
        """
        # print("home" if has_ball == self.game.home else "away" if has_ball == self.game.away else "error")
        oncourt = self.game.on_court(self.game.has_ball.roster)
        touches_ball = self.game.in_current_play(oncourt, self.game.has_ball.roster)

        # TOV
        if self.game.simulate_stat(touches_ball, "TOV"):
            # print("SWITCHING POSSESSION**************************", has_ball.team_df)
            self.game.switch_possession()
            return

        # attempt
        attempt = self.game.shot_attempt(touches_ball)
        if attempt > 0:
            if has_ball.h_or_a == "home":
                self.home_pts += attempt
            else:
                self.away_pts += attempt

            self.game.switch_possession()
        else:
            # Offensive REB
            orb = self.game.home.team_df["ORB"].iloc[0]/100
            if GameTools.step(orb):
                # print("OFFENSIVE REBOUND, player should be the same")
                self.possession(self.game.has_ball)
            else:
                self.game.switch_possession()

    def get_pace(self) -> int:
        """
        Returns pace of game based on stats from both teams.
        :return: int for pace of game
        """
        home_pace = self.game.home.team_df["Pace"].iloc[0]
        away_pace = self.game.away.team_df["Pace"].iloc[0]
        return int(home_pace + away_pace)


class MonteCarlo:
    """
    Monte Carlo simulation class for predicting game outcomes based on historical data.

    This class initializes a Monte Carlo simulation with the provided parameters:
    - db_host: Optional[str]: The host address of the database.
    - season: str: The season for which the simulation is being run.
    - home_team: Teams: The home team for the game.
    - away_team: Teams: The away team for the game.
    - game_date: str: The date of the game.
    - game_type: str: The type of game (e.g., regular, playoff).
    - epochs: int: The number of simulation epochs to run (default is 10,000).

    Methods:
        - run: Runs the Monte Carlo simulation for the desired number of epochs.
        - histogram: Builds a histogram from the simulated epochs.

    Attributes:
        - db_host: str: The host address of the database.
        - season: str: The season for which the simulation is being run.
        - home_team: Teams: The home team for the game.
        - away_team: Teams: The away team for the game.
        - game_date: str: The date of the game.
        - game_type: str: The type of game (e.g., regular, playoff).
        - epochs: int: The number of simulation epochs to run.
        - home_scores: numpy.array: An array to store the final scores of the home team in each simulation
          epoch.
        - away_scores: numpy.array: An array to store the final scores of the away team in each simulation
          epoch.
    """
    def __init__(self, db_host: Optional[str], season: str, home_team: Teams, away_team: Teams,
                 game_date: str, game_type: str, epochs: int = 10000):
        self.db_host = db_host
        self.season = season
        self.home_team = home_team
        self.away_team = away_team
        self.game_date = game_date
        self.game_type = game_type
        self.epochs = epochs
        self.home_scores = np.array([])
        self.away_scores = np.array([])

    def run(self) -> list[str]:
        """
        Runs the Monte Carlo simulation for the desired amount of epochs, documenting final scores per team.
        :return: (str) [prob. density plot, violin plot, 'mode and percentage stats']
        """
        for _ in range(self.epochs):
            game = Simulation(self.db_host, self.season, self.home_team, self.away_team, self.game_date,
                              self.game_type)
            game.play_game()
            self.home_scores = np.append(self.home_scores, game.home_pts)
            self.away_scores = np.append(self.away_scores, game.away_pts)

        return [self.prob_density(), self.violin_plot(), self.get_stats()]

    def prob_density(self) -> str:
        """
        Builds probability density plot as BytesIO buffer.
        :return: BytesIO buffer matplotlib prob. density figure of epoch simulations
        """
        fig, ax = plt.subplots()
        ax.hist(self.home_scores, bins=20, color='yellow', alpha=0.7,
                label=f'Home: {self.home_team.short_name}')
        ax.hist(self.away_scores, bins=20, color='blue', alpha=0.7,
                label=f'Visitor: {self.away_team.short_name}')
        ax.set_xlabel('Team Scores (PPG)')
        ax.set_ylabel('Frequency (simulations)')
        ax.set_title('Team Scores Histogram')
        ax.legend()
        ax.grid(True)

        return self.save_2_bytesIO_buffer_string(fig)

    def violin_plot(self) -> str:
        """
        Creates violin plot showing distribution of scores per epoch as BytesIO buffer.
        :return: BytesIO buffer of matplotlib figure showing the violin plot.
        """
        fig, ax = plt.subplots()
        violin_parts = ax.violinplot([self.home_scores, self.away_scores], showmeans=True)
        for pc, color in zip(violin_parts['bodies'], ['yellow', 'blue']):
            pc.set_facecolor(color)
        ax.set_ylabel('Team Scores (PPG)')
        ax.set_title('Violin Plot of Team Scores')
        ax.set_xticks([1, 2])
        ax.set_xticklabels([f'Home: {self.home_team.short_name}', f'Visitor: {self.away_team.short_name}'])
        ax.grid(True)

        return self.save_2_bytesIO_buffer_string(fig)

    def save_2_bytesIO_buffer_string(self, fig) -> str:
        """
        Converts matplotlib figure to BytesIO buffer to enable base64 conversion by Flask.
        :param fig: matplotlib figure of plotted graph
        :return: BytesIO buffer of matplotlib figure
        """
        buffer = BytesIO()
        fig.savefig(buffer, format='png')
        plt.close(fig)
        buffer.seek(0)
        return base64.b64encode(buffer.getvalue()).decode('utf-8')

    def get_stats(self) -> str:
        """
        Geneartes a str of CSV:
        [0]: home team win %
        [1]: away team win %
        [2]: mode of home scores
        [3]: mode of away scores
        :return: csv str of team win stats
        """
        home_wins = sum(1 for home_score, away_score in zip(self.home_scores, self.away_scores)
                        if home_score > away_score)
        h_wins = int(home_wins/self.epochs*100)
        a_wins = int((self.epochs - home_wins)/self.epochs*100)
        h_mode = int(statistics.mode(self.home_scores))
        a_mode = int(statistics.mode(self.away_scores))
        return f"{h_wins},{a_wins},{h_mode},{a_mode}"
