import math
import random
from typing import List, Optional

from model.teams import Teams
from controller.dto_sim import TeamBuilder, Player
from simulator.tools import GameTools


class GameBuilder:
    def __init__(self, db_host: Optional[str], season: str, home_team: Teams, away_team: Teams, game_date: str,
                 game_type: str):
        self.home = TeamBuilder(db_host, season, home_team, game_date, game_type, "home")
        self.away = TeamBuilder(db_host, season, away_team, game_date, game_type, "away")
        self.has_ball = self.tip_off()

    def simulate_stat(self, players: List[Player], stat: str):
        stat_total = sum(getattr(player, stat) for player in players)
        stat_avg = stat_total / len(players)
        return GameTools.step(stat_avg)

    def shot_attempt(self, players: List[Player], shooter_w_mult: float = 2):
        # who takes shot
        w = [p.player_w + (p.FGA + p.threePA) / 200 for p in players]
        shooter = GameTools.weighted_random_sample(players, w, 1, shooter_w_mult)[0]
        # type of shot attempted
        shot_points_w = [shooter.FGA, shooter.threePA]
        points = GameTools.weighted_random_sample([2, 3], shot_points_w, 1, 1)[0]
        if points == 2:
            return GameTools.step(shooter.FGpercent/100) * points
        else:
            return GameTools.step(shooter.threePpercent/100) * points



    def switch_possession(self):
        if self.has_ball == self.home:
            self.has_ball = self.away
        else:
            self.has_ball = self.home

    def tip_off(self) -> TeamBuilder:
        home_player = max(self.home.roster, key=lambda home_players: home_players.REB)
        away_player = max(self.away.roster, key=lambda away_players: away_players.REB)
        reb_delta = abs(home_player.REB - away_player.REB)
        home_val = home_player.REB + reb_delta * 0.05
        away_val = away_player.REB - reb_delta * 0.05
        total_prob = home_val + away_val
        home_val /= total_prob
        away_val /= total_prob
        if random.uniform(0, 1) < home_val:
            return self.home
        else:
            return self.away

    def in_current_play(self, oncourt, roster, weight_multiplier: float = 1) -> List[Player]:
        # choose point guard(s) - guarantees G in play
        weights = [player.playtime_w for player in roster.PG + roster.SG]
        guards = [random.choices(roster.PG + roster.SG, weights)[0]]
        # choose other players (can choose point guards again)
        n = random.randint(1, 5)
        w = [player.player_w for player in oncourt]
        players = GameTools.weighted_random_sample(oncourt, w, n, weight_multiplier)
        # unique set of all players chosen
        return list(set(players + guards))

    def on_court(self, roster) -> List[Player]:
        playing = []
        for position in [roster.PF, roster.SF, roster.PG, roster.SG, roster.C]:
            playing.append(self.choose_player(position))
        return playing

    def choose_player(self, roster_position: List) -> Player:
        probs = [player.playtime_w for player in roster_position]
        players = [player for player in roster_position]
        return random.choices(players, weights=probs)[0]



