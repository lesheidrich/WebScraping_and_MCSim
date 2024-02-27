
from typing import Any

import matplotlib
from flask import Flask, request
from matplotlib import pyplot as plt

from controller.control_service import ScrapeControl
from controller.dto_service import Persist
from log.logger import Logger
from model.teams import Teams
from project_secrets import PROJECT_FOLDER
from simulator.monte_carlo import MonteCarlo


class Host:
    def __init__(self):
        matplotlib.use('Agg')  # non-interactive rendering env
        self.app = Flask(__name__)
        self.home = None
        self.away = None
        self.season = None
        self.game_date = None
        self.db = None
        self.missing_seasons = {}
        self.log = Logger(log_file="app_test_log.log",
                          name="FLASK HOST",
                          log_level="INFO")

        @self.app.route('/monte_carlo/game_data', methods=['POST'])
        def get_game_data() -> dict:
            """
            Order: 1
            Takes params of home team, away team, season and DB URI from client.
            Reads df of game schedule for selected params from DB and returns it as json to api.
            :return: json of game schedule
            """
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
            except TypeError as e:
                self.pack_json(e, 404)
            except Exception as e:
                self.pack_json(e, 400)

        @self.app.route('/monte_carlo/team_in_db')
        def get_teams_in_db() -> dict:
            """
            Order: 2
            Takes param of game date from client. Initializes previous season date from it.
            Reviews current and previous season to make sure both home and away team is in DB.
            Constructs json of missing data attrib.
            Sends json response containing comment of seasons and teams missing for viewing.
            :return: json of missing seasons and teams for client viewing
            """
            self.game_date = request.args.get('game_date')
            last_season = f"{self.season[:3]}{int(self.season[3])-1}{self.season[4:8]}{int(self.season[8])-1}"

            try:
                for season in [last_season, self.season]:
                    for team in [self.home, self.away]:
                        if not Persist.season_in_db(season, team.short_name, self.db):
                            self.log.info(f"{team} for {season} season is not in DB!")
                            if season not in self.missing_seasons:
                                self.missing_seasons[season] = []
                            self.missing_seasons[season].append(team.short_name)
                if self.missing_seasons:
                    message = ""
                    for k, v in self.missing_seasons.items():
                        message += f"{k}: {', '.join(v)} "
                    return self.pack_json(message, 204)

                self.log.info("Database contains all necessary data!")
                return self.pack_json("", 200)
            except Exception as e:
                self.pack_json(e, 400)

        @self.app.route('/monte_carlo/season_data')
        def get_season_data() -> dict:

            proxy_list = rf"{request.args.get('proxy_list')}"
            check_proxies = bool(request.args.get('check_proxies'))
            scrape_method = request.args.get('scrape_method')

            print(proxy_list)

            # sc = ScrapeControl(proxy_list,
            #                    "1991-1992",
            #                    "Chicago-Bulls/4",
            #                    check_proxies,
            #                    db_host=self.db)
            return self.pack_json("", 200)

        @self.app.route('/monte_carlo/simulation')
        def get_monte_carlo_sim() -> dict:
            """
            Order: last
            Takes params of game type ('regular' || 'playoff') and epochs (for sim) from client.
            Responds to client with simulation graphs and message of game data as json.
            :return: json of simulation graphs and game data
            """
            game_type = request.args.get('game_type')
            epochs = int(request.args.get('epochs'))

            try:
                plt.ioff()  # interactive mode
                mc = MonteCarlo(self.db, self.season, self.home, self.away, self.game_date, game_type, epochs)
                result = mc.run()

                return {
                    'status': 200,
                    'message': result[2],
                    'image': result[0],
                    'image2': result[1]
                }
            except Exception as e:
                return self.pack_json(e, 400)

    def pack_json(self, message: Any, status_code: int) -> dict:
        """
        Utility method, assembles json to be returned to client.
        :param message: container takes any arg as message to client
        :param status_code: int of HTTP code
        :return: json response to client
        """
        return {
                    'message': message,
                    'status': status_code
                }

    def run(self) -> None:
        """
        Method runs Flask host until manual abort by user.
        :return: None
        """
        self.app.run(debug=True)
