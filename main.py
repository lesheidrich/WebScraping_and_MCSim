import os
import random
import time

import pandas as pd

from controller.control_service import ScrapeControl
from controller.dto_sim import TeamBuilder
from controller.host_service import Host
from model.teams import Teams
from project_secrets import Hidden
from simulator.monte_carlo import MonteCarlo
from webscraper.utilities import WebKit

if __name__ == '__main__':
    Hidden.set_project_folder(os.getcwd())
    server = Host()
    server.run()


    # season = "1992-1993"
    # home = Teams.from_full_name('Chicago Bulls')
    # away = Teams.from_full_name('Boston Celtics')
    # game_date = "1992-12-05"
    # game_type = "regular"
    # mc = MonteCarlo(None, season, home, away, game_date, game_type, 10000)
    # result = mc.run_plt()



    # """on this one"""
    # season = "1991-1992"
    # home = Teams.from_short_name('ATL')
    # away = Teams.from_short_name('DET')
    # game_date = "1991-11-02"
    # game_type = "regular"
    # # mc = MonteCarlo(None, season, home, away, game_date, game_type, 10)
    # # result = mc.run_plt()
    #
    #
    # # season = "1991-1992"
    # # home = Teams.from_short_name('SAS')
    # # away = Teams.from_short_name('DAL')
    # # game_date = "1991-11-01"
    # # game_type = "regular"
    # mc = MonteCarlo(None, season, home, away, game_date, game_type, 10)
    # result = mc.run_plt()
    #
    # t = TeamBuilder(None, season, away, game_date, game_type, "away")
    # # t = TeamBuilder(None, season, home, game_date, game_type, "home")
    #
    # # pd.set_option('display.max_rows', None)
    # # pd.set_option('display.max_columns', None)
    #
    # # print(t.player_df)
    # # print(len(t.roster.PG))
    # # for p in t.roster.PG:
    # #     print(p.name)
    # #
    # print(len(t.roster.PF))
    # for p in t.roster.PF:
    #     print(p.name)



    # print(t.roster.get_stat_df())
    #
    # filtered_players = t.individual_df[t.individual_df["player"].isin(["Darrell Walker", "Joe Dumars", "Lance Blanks"])]
    # print(filtered_players)
    # print(t.player_df)





    """to here"""
    # print(len(t.roster.PF))
    # for p in t.roster.PF:
    #     print(p.name)
    #
    # print(len(t.roster.SF))
    # for p in t.roster.SF:
    #     print(p.name)
    #
    # print(len(t.roster.C))
    # for p in t.roster.C:
    #     print(p.name)

    # print(t.player_df[t.player_df["position"] == "SG"])

    # df.fillna(0, inplace=True)








    # sc = ScrapeControl("proxies_full.csv",
    #                                 "1991-1992",
    #                                 "Chicago-Bulls/4",
    #                                 False,
    #                                 db_host=Hidden.get_xampp_uri())



