from controller.dto_service import Persist
from controller.host_service import Host
from model.db_handler import MySQLHandler
from model.teams import Teams
from project_secrets import XAMPP_TEST
from simulator.monte_carlo import MonteCarlo

if __name__ == '__main__':
    server = Host()
    server.run()

    # season = "1991-1992"
    # home = Teams.from_full_name('Chicago Bulls')
    # away = Teams.from_link_name('Miami-Heat/15')
    # game_date = "1992-03-24"
    # game_type = "regular"
    # mc = MonteCarlo(None, season, home, away, game_date, game_type, 100)
    # result = mc.run()


