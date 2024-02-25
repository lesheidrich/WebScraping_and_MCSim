import base64
import os
from typing import Any

import matplotlib
from flask import Flask, render_template, jsonify, request
from matplotlib import pyplot as plt

from controller.dto_service import Persist
from log.logger import Logger
from model.teams import Teams
from project_secrets import PROJECT_FOLDER
from simulator.monte_carlo import MonteCarlo


class Host:
    def __init__(self):
        matplotlib.use('Agg')
        self.app = Flask(__name__)
        self.home = None
        self.away = None
        self.season = None
        self.game_date = None
        self.db = None
        self.log = Logger(log_file="app_test_log.log",
                          name="FLASK HOST",
                          log_level="INFO")

        @self.app.route('/monte_carlo/game_data', methods=['POST'])
        def get_game_data() -> dict:
            self.home = Teams.from_full_name(request.args.get('home'))
            self.away = Teams.from_full_name(request.args.get('away'))
            self.season = request.args.get('season')
            self.db = request.args.get('dbURI')

            try:
                df = Persist.get_game_data(self.home.full_name, self.away.full_name, self.season, self.db)
                df['date'] = df['date'].astype(str)
                data = df.to_json(orient='records')
                if len(df) < 1:
                    raise ValueError(f"Game data is empty for H:{self.home.full_name}, "
                                     f"A:{self.away.full_name}, Season:{self.season}, DB:{self.db}!")
                return self.pack_json(data, 200)
            except Exception as e:
                self.pack_json(e, 400)

        @self.app.route('/monte_carlo/team_in_db')
        def get_teams_in_db() -> dict:
            self.game_date = request.args.get('game_date')

            for team in [self.home, self.away]:
                if not Persist.season_in_db(self.season, team.short_name, self.db):
                    self.log.info(f"{team} for {self.season} season is not in DB!")
                    return self.pack_json(team.short_name, 400)
            self.log.info("Database contains all necessary data!")
            return self.pack_json("OK", 200)

        @self.app.route('/simulation')
        def get_monte_carlo_sim() -> dict:
            game_type = request.args.get('game_type')
            epochs = int(request.args.get('epochs'))

            try:
                plt.ioff()  # interactive mode
                mc = MonteCarlo(self.db, self.season, self.home, self.away, self.game_date, game_type, epochs)
                result = mc.run()

                image_base64 = base64.b64encode(result.getvalue()).decode('utf-8')
                return {
                    'status': 200,
                    'message': "none",
                    'image': image_base64
                }
            except Exception as e:
                return self.pack_json(e, 400)

    def pack_json(self, message: Any, status_code: int):
        return {
                    'message': message,
                    'status': status_code
                }

    def run(self) -> None:
        self.app.run(debug=True)