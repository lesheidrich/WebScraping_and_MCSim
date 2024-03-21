"""
Module: host_service.py

Module for hosting a Flask server for handling requests related to a Monte Carlo simulation application.

Classes:
    Host: Represents the Flask server instance.
"""

from typing import Any
import matplotlib
from flask import Flask, request
from matplotlib import pyplot as plt
from controller.control_service import ScrapeControl
from controller.dto_service import Persist
from log.logger import Logger
from model.teams import Teams
from simulator.monte_carlo import MonteCarlo
from webscraper.utilities import WebKit


class Host:
    """
    Represents a Flask server for handling requests related to a Monte Carlo simulation application.

    Attributes:
        app (Flask): The Flask application instance.
        log (Logger): The logger instance for logging application events.

    Methods:
        get_game_data(): Handles the '/monte_carlo/game_data' endpoint to retrieve game data.
        get_teams_in_db(): Handles the '/monte_carlo/team_in_db' endpoint to check teams in the database.
        get_season_data(): Handles the '/monte_carlo/season_data' endpoint to scrape missing season data.
        get_monte_carlo_sim(): Handles the '/monte_carlo/simulation' endpoint to perform Monte Carlo
        simulation.
        pack_json(message: Any, status_code: int) -> dict: Utility method to assemble JSON responses.
        run(): Method to run the Flask host until manually aborted by the user.
    """

    def __init__(self):
        matplotlib.use('Agg')  # non-interactive rendering env
        self.app = Flask(__name__)
        self.app.config['TIMEOUT'] = 100000
        self.log = Logger(log_file="application_log.log",
                          name="FLASK HOST",
                          log_level="INFO")

        @self.app.route('/monte_carlo/game_data', methods=['POST'])
        def get_game_data() -> dict:
            """
            Order: 1
            View: Get Games button (Find Games)
            Reads df of game schedule for selected params from DB and returns it as json to api.
            :return: json of game schedule
            """
            home = Teams.from_full_name(request.args.get('home'))
            away = Teams.from_full_name(request.args.get('away'))
            season = request.args.get('season')
            db = request.args.get('dbURI')

            try:
                df = Persist.get_game_data(home.full_name, away.full_name, season, db)
                df['date'] = df['date'].astype(str)
                data = df.to_json(orient='records')
                if len(df) < 1:
                    message = (f"Game data is empty for H:{home.full_name}, A:{away.full_name}, Season:"
                               f"{season}, DB:{db}!")
                    self.log.warning(message)
                    raise ValueError(message)
                return self.pack_json(data, 200)
            except TypeError as e:
                self.log.error(f"get_game_data() raised TypeError while responding to request: {e}")
                return self.pack_json(e, 404)
            # pylint: disable=W0718
            except Exception as e:
                self.log.error(f"get_game_data() raised Exception while responding to request: {e}")
                return self.pack_json(e, 400)

        @self.app.route('/monte_carlo/team_in_db')
        def get_teams_in_db() -> dict:
            """
            Order: 2
            View: Simulate button (Find Games)
            Reviews current and previous season to make sure both home and away team is in DB.
            Constructs json of missing data attrib.
            Sends json response containing comment of seasons and teams missing for viewing.
            :return: json of missing seasons and teams for client viewing
            """
            season = request.args.get('season')
            home = Teams.from_full_name(request.args.get('home'))
            away = Teams.from_full_name(request.args.get('away'))
            db = request.args.get('db')

            last_season = f"{season[:3]}{int(season[3]) - 1}{season[4:8]}{int(season[8]) - 1}"
            message = ""

            try:
                # pack missing dict
                for season in [last_season, season]:
                    for team in [home, away]:
                        if not Persist.season_in_db(season, team.short_name, db):
                            self.log.info(f"{team.short_name} for {season} season is not in DB!")
                            if team.short_name not in message:
                                message += f" {team.short_name}"

                if message:
                    self.log.info(f"Response with 204:{message} sent to client.")
                    return self.pack_json(message, 204)

                self.log.info(f"Database contains {season}: {home.short_name} and {away.short_name}!")
                return self.pack_json("", 200)
            # pylint: disable=W0718
            except Exception as e:
                self.log.error(f"get_teams_in_db() raised Exception while responding to request: {e}")
                return self.pack_json(e, 400)

        @self.app.route('/monte_carlo/season_data')
        def get_season_data() -> dict:
            """
            Order: 3
            View: Scrape button (Scrape Pop Up)
            Iterates over missing parameters from missing_seasons dictionary. Attempts to scrape, in case
            of error will re-attempt again (sc.run_all() also re-attempts all failed attempts with Firefox).
            Successful scrape attempts result in dropping of list params.
            :return: json of success, or failure
            """
            season = request.args.get('season')
            home = Teams.from_full_name(request.args.get('home'))
            away = Teams.from_full_name(request.args.get('away'))
            db = request.args.get('db')
            proxy_list = rf"{request.args.get('proxy_list')}"
            check_proxies = bool(request.args.get('check_proxies'))
            scrape_method = request.args.get('scrape_method')
            forced = bool(request.args.get('forced'))

            proxies = proxy_list if proxy_list else None
            last_season = f"{season[:3]}{int(season[3]) - 1}{season[4:8]}{int(season[8]) - 1}"

            for s in [last_season, season]:
                for t in [home, away]:

                    # not brute force scrape checks if other client updated db already
                    if not forced:
                        if Persist.season_in_db(s, t.short_name, db):
                            continue

                    # scrape
                    sc = ScrapeControl(proxies, s, t.link_name, check_proxies, db_host=db)
                    try:
                        try:
                            sc.run_all(scrape_method)
                            self.log.info(f"\nSCRAPING {t.link_name} for season {s} with "
                                          f"{scrape_method}.")
                        # pylint: disable=W0718
                        except Exception as e:
                            WebKit.random_delay()
                            sc.run_all(scrape_method)
                            self.log.warning(f"{scrape_method} ran into an error while scraping "
                                             f"{t.short_name} for season {s}. Attempting to scrape "
                                             f"again.\nDetails: {e}")
                        del sc
                    # pylint: disable=W0718
                    except Exception as e:
                        # deletes if unsuccessful so in_db returns False
                        Persist.delete_records("player_regular_home",
                                               f'season="{s}" and team="{t.short_name}"')
                        Persist.delete_records("player_regular_away",
                                               f'season="{s}" and team="{t.short_name}"')
                        self.log.error(f"get_season_data() raised Exception while responding to request. "
                                       f"Season {s} for team {t.short_name} has been rolled back.\n{e}")
                        self.pack_json(e, 400)

            self.log.info(f"get_season_data() responded with 200 on {season}:{home.short_name},"
                          f"{away.short_name}.")
            return self.pack_json("", 200)

        @self.app.route('/monte_carlo/simulation')
        def get_monte_carlo_sim() -> dict:
            """
            Order: last
            View: Simulate button (Find Games) || auto activated after Scrape button (Monte Carlo)
            Responds to client with simulation graphs and message of game data as json.
            :return: json of simulation graphs and game data
            """
            game_type = request.args.get('game_type')
            epochs = int(request.args.get('epochs'))
            season = request.args.get('season')
            home = Teams.from_full_name(request.args.get('home'))
            away = Teams.from_full_name(request.args.get('away'))
            db = request.args.get('db')
            game_date = request.args.get('game_date')

            try:
                plt.ioff()  # interactive mode
                mc = MonteCarlo(db, season, home, away, game_date, game_type, epochs)
                result = mc.run()

                return {
                    'status': 200,
                    'message': result[2],
                    'image': result[0],
                    'image2': result[1]
                }
            # pylint: disable=W0718
            except Exception as e:
                comment = f"get_monte_carlo_sim() raised Exception while responding to request: {e}"
                self.log.error(comment)
                return self.pack_json(comment, 400)

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
