"""
Module: game_service.py

Module for building and managing basketball game simulations.

This module contains classes and functions for constructing and controlling the simulation of basketball
games.
It includes functionalities for simulating various aspects of basketball gameplay, such as shot attempts,
possession switches, and player selection during gameplay.

Classes:
    - GameBuilder: Constructs and manages game-related functionalities for simulating basketball games.

Dependencies:
    - random: Provides functions for generating random numbers used in simulations.
    - typing: Provides support for type hints.
    - model.teams.Teams: Represents basketball teams participating in the game.
    - controller.dto_sim.TeamBuilder: Constructs teams and retrieves game data for simulation.
    - simulator.tools.GameTools: Provides tools for simulating game events using weighted probabilities.
"""

import random
from typing import List, Optional
from model.teams import Teams
from controller.dto_sim import TeamBuilder, Player, Roster
from simulator.tools import GameTools


class GameBuilder:
    """
    Constructs and manages game-related functionalities for simulating basketball games.

    This class provides methods for simulating various aspects of basketball games, including shot attempts,
    possession switches, tip-offs, and player selection during gameplay.

    Attributes:
        db_host (Optional[str]): The database host.
        season (str): The season of the game.
        home_team (Teams): The home team participating in the game.
        away_team (Teams): The away team participating in the game.
        game_date (str): The date of the game.
        game_type (str): The type of game (e.g., regular, playoffs).

    Methods:
        __init__: Initializes a GameBuilder instance.
        simulate_stat: Simulates the success of a specified statistic for a group of players.
        shot_attempt: Simulates a shot attempt by selecting a player and determining the outcome.
        switch_possession: Switches possession from one team to the other.
        tip_off: Simulates the tip-off to determine which team starts the game with possession.
        in_current_play: Selects players involved in the offensive play of the current possession.
        on_court: Selects players currently on the court for a team.
        choose_player: Chooses a random player from a specified position in the roster.
    """
    def __init__(self, db_host: Optional[str], season: str, home_team: Teams, away_team: Teams,
                 game_date: str, game_type: str):
        self.home = TeamBuilder(db_host, season, home_team, game_date, game_type, "home")
        self.away = TeamBuilder(db_host, season, away_team, game_date, game_type, "away")
        self.has_ball = self.tip_off()

    def simulate_stat(self, players: List[Player], stat: str) -> bool:
        """
        Simulates success of param stat for param player with step function returning bool of success.
        :param players: Player instance for player to simulate stat for
        :param stat: Player instance's stat attribute to utilize for step function
        :return: True if attempt succeeded for stat type
        """
        stat_total = sum(getattr(player, stat) for player in players)
        stat_avg = stat_total / len(players)
        return GameTools.step(stat_avg)

    def shot_attempt(self, players: List[Player], shooter_w_mult: float = 2) -> bool:
        """
        Function decides which of the players involved in the attack will shoot the ball, then
        proceeds to simulate the shot.
        :param players: list of Player instances to choose from
        :param shooter_w_mult: list of weights for Player instances (probability they will take
        the shot)
        :return: True if shot attempt succeeded, else False
        """
        # who takes shot
        w = [p.player_w + (p.FGA + p.threePA) / 200 for p in players]
        shooter = GameTools.weighted_random_sample(players, w, 1, shooter_w_mult)[0]
        # type of shot attempted
        shot_points_w = [shooter.FGA, shooter.threePA]

        try:
            if sum(shot_points_w) == 0:
                shooter.FGpercent = 50
                shot_points_w[0] = 10

            points = GameTools.weighted_random_sample([2, 3], shot_points_w, 1, 1)[0]
            if points == 2:
                return GameTools.step(shooter.FGpercent/100) * points
            return GameTools.step(shooter.threePpercent/100) * points
        except Exception as e:
            raise ValueError(f"shot_attempt error for shooter: {shooter.name}, "
                             f"shot_points_w: {shot_points_w}, FGP: {shooter.FGpercent}.\n{e}") from e

    def switch_possession(self) -> None:
        """
        Effectively gives the ball to the other team, changing offense direction.
        :return: None
        """
        if self.has_ball == self.home:
            self.has_ball = self.away
        else:
            self.has_ball = self.home

    def tip_off(self) -> TeamBuilder:
        """
        Simulates tip-off to determine which team starts the game with a possession.
        :return: TeamBuilder instance's team in possession of ball
        """
        # select strongest rebounders
        home_player = max(self.home.roster, key=lambda home_players: home_players.REB)
        away_player = max(self.away.roster, key=lambda away_players: away_players.REB)

        reb_delta = abs(home_player.REB - away_player.REB)
        # home given slight advantage
        home_val = home_player.REB + reb_delta * 0.05
        away_val = away_player.REB
        # normalize
        total_prob = home_val + away_val
        home_val /= total_prob
        away_val /= total_prob
        # random step function determines home success or failure
        if random.uniform(0, 1) < home_val:
            return self.home
        return self.away

    def in_current_play(self, oncourt: List[Player], roster: Roster, weight_multiplier: float = 1
                        ) -> List[Player]:
        """
        Selects on-court players that are involved in the offensive play of the current possession.
        :param oncourt: list of Player instances currently on court
        :param roster: Roster instance for team's roster during time of game
        :param weight_multiplier: float of weight multiplier for player involvement probability,
        defaults to 1
        :return: list of Player instances involved in current possession's offensive play
        """
        # choose point guard(s) - guarantees G in play
        weights = [player.playtime_w for player in roster.PG + roster.SG]
        guards = [random.choices(roster.PG + roster.SG, weights)[0]]
        # choose other players (can choose point guards again)
        n = random.randint(1, 5)
        w = [player.player_w for player in oncourt]
        players = GameTools.weighted_random_sample(oncourt, w, n, weight_multiplier)
        # unique set of all players chosen
        return list(set(players + guards))

    def on_court(self, roster: Roster) -> List[Player]:
        """
        Selects (weighted) random Player instances from team's roster that are currently on the court.
        :param roster: Roster instance for team's roster during time of game
        :return: list of Player instances that are on court
        """
        playing = []
        for _, position in enumerate([roster.PF, roster.SF, roster.PG, roster.SG, roster.C]):
            playing.append(self.choose_player(position))
        return playing

    def choose_player(self, roster_position: List) -> Player:
        """
        Chooses a random player from the specified position in the roster. Therefore, selection is limited
        to players of a certain position at a time. Player's playtime weight is used as weight for decision.
        :param roster_position: position list in Roster instance, format: Roster.SG
        :return: Player instance
        """
        probs = [player.playtime_w for player in roster_position]
        players = list(roster_position)
        return random.choices(players, weights=probs)[0]
