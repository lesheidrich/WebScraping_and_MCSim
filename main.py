import os
import time

from controller.control_service import ScrapeControl
from controller.host_service import Host
from model.teams import Teams
from project_secrets import Hidden
from simulator.monte_carlo import MonteCarlo
from webscraper.utilities import WebKit

if __name__ == '__main__':
    Hidden.set_project_folder(os.getcwd())
    # server = Host()
    # server.run()

    # season = "1990-1991"
    # home = Teams.from_full_name('Chicago Bulls')
    # away = Teams.from_full_name('Boston Celtics')
    # game_date = "1991-02-26"
    # game_type = "regular"
    # mc = MonteCarlo(None, season, home, away, game_date, game_type, 10000)
    # result = mc.run_plt()

    season = "1991-1992"
    home = Teams.from_short_name('PHX')
    away = Teams.from_short_name('POR')
    game_date = "1992-01-19"
    game_type = "regular"
    mc = MonteCarlo(None, season, home, away, game_date, game_type, 10000)
    result = mc.run_plt()


    # sc = ScrapeControl("proxies_full.csv",
    #                                 "1991-1992",
    #                                 "Chicago-Bulls/4",
    #                                 False,
    #                                 db_host=Hidden.get_xampp_uri())



