import os
import time

from controller.control_service import ScrapeControl
from controller.host_service import Host
from project_secrets import Hidden
from webscraper.utilities import WebKit

if __name__ == '__main__':
    Hidden.set_project_folder(os.getcwd())
    server = Host()
    server.run()





    # season = "1991-1992"
    # home = Teams.from_full_name('Chicago Bulls')
    # away = Teams.from_link_name('Miami-Heat/15')
    # game_date = "1992-03-24"
    # game_type = "regular"
    # mc = MonteCarlo(None, season, home, away, game_date, game_type, 100)
    # result = mc.run()


