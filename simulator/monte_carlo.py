from typing import Optional
import matplotlib.pyplot as plt
import numpy as np

from controller.dto_sim import TeamBuilder
from log.logger import Logger
from model.teams import Teams
from simulator.game_service import GameBuilder
from simulator.tools import GameTools


class Simulation:
    def __init__(self, db_host: Optional[str], season: str, home_team: Teams, away_team: Teams, game_date: str,
                 game_type: str):
        self.game = GameBuilder(db_host, season, home_team, away_team, game_date, game_type)
        self.home_pts = 0
        self.away_pts = 0

    def play_game(self):
        for i in range(self.get_pace()):
            self.possession(self.game.has_ball)

    def possession(self, has_ball: TeamBuilder) -> None:
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
        home_pace = self.game.home.team_df["Pace"].iloc[0]
        away_pace = self.game.away.team_df["Pace"].iloc[0]
        return int(home_pace + away_pace)


class MonteCarlo:
    def __init__(self, db_host: Optional[str], season: str, home_team: Teams, away_team: Teams, game_date: str,
                 game_type: str, epochs: int = 10000):
        self.db_host = db_host
        self.season = season
        self.home_team = home_team
        self.away_team = away_team
        self.game_date = game_date
        self.game_type = game_type
        self.epochs = epochs
        self.home_scores = np.array([])
        self.away_scores = np.array([])

    def run(self) -> None:
        for epoch in range(self.epochs):

            print(epoch) if epoch % 100 == 0 else None

            game = Simulation(self.db_host, self.season, self.home_team, self.away_team, self.game_date, self.game_type)
            game.play_game()
            self.home_scores = np.append(self.home_scores, game.home_pts)
            self.away_scores = np.append(self.away_scores, game.away_pts)
        self.historgram()

    def historgram(self) -> None:
        plt.hist(self.home_scores, bins=20, color='yellow', alpha=0.7, label=f'Home: {self.home_team.short_name}')
        plt.hist(self.away_scores, bins=20, color='blue', alpha=0.7, label=f'Visitor: {self.away_team.short_name}')
        plt.xlabel('Team Scores (PPG)')
        plt.ylabel('Frequency (simulations)')
        plt.title('Team Scores Histogram')
        plt.legend()
        plt.grid(True)
        plt.show()
