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



    # # """on this one"""
    # season = "1992-1993"
    # home = Teams.from_short_name('BOS')
    # away = Teams.from_short_name('DEN')
    # game_date = "1992-12-09"
    # game_type = "regular"
    # mc = MonteCarlo(None, season, home, away, game_date, game_type, 100)
    # result = mc.run_plt()


    # season = "1991-1992"
    # home = Teams.from_short_name('SAS')
    # away = Teams.from_short_name('DAL')
    # game_date = "1991-11-01"
    # game_type = "regular"
    # mc = MonteCarlo(None, season, home, away, game_date, game_type, 10)
    # result = mc.run_plt()

    # t = TeamBuilder(None, season, away, game_date, game_type, "away")
    # t = TeamBuilder(None, season, home, game_date, game_type, "home")

    # pd.set_option('display.max_rows', None)
    # pd.set_option('display.max_columns', None)

    # print(t.player_df)
    # print(len(t.roster.PG))
    # for p in t.roster.PG:
    #     print(p.name)
    #
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

    # teamlist_w_nums = [
    #     'Atlanta-Hawks/1',
    #     'Boston-Celtics/2',
    #     'Brooklyn-Nets/38',
    #     'Charlotte-Hornets/3',
    #     'Chicago-Bulls/4',
    #     'Cleveland-Cavaliers/5',
    #     'Dallas-Mavericks/6',
    #     'Denver-Nuggets/7',
    #     'Detroit-Pistons/8',
    #     'Golden-State-Warriors/9',
    #     'Houston-Rockets/10',
    #     'Indiana-Pacers/11',
    #     'Los-Angeles-Clippers/12',
    #     'Los-Angeles-Lakers/13',
    #     'Memphis-Grizzlies/14',
    #     'Miami-Heat/15',
    #     'Milwaukee-Bucks/16',
    #     'Minnesota-Timberwolves/17',
    #     'New-Orleans-Pelicans/19',
    #     'New-York-Knicks/20',
    #     'Oklahoma-City-Thunder/33',
    #     'Orlando-Magic/21',
    #     'Philadelphia-Sixers/22',
    #     'Phoenix-Suns/23',
    #     'Portland-Trail-Blazers/24',
    #     'Sacramento-Kings/25',
    #     'San-Antonio-Spurs/26',
    #     'Toronto-Raptors/28',
    #     'Utah-Jazz/29',
    #     'Washington-Wizards/30']
    #
    # for team in teamlist_w_nums:
    #
    #     sc = ScrapeControl("proxies_full.csv",
    #                                     "1994-1995",
    #                                     team,
    #                                     False,
    #                                     db_host=Hidden.get_xampp_uri())
    #
    #     try:
    #         sc.run_all("requests_scrape")
    #         WebKit.random_delay()
    #     except Exception as e:
    #         print("Exception on team " + team + " trying again w selenium.")
    #         try:
    #             sc.run_all("firefox_selenium_scrape")
    #         except Exception as e:
    #             print("Selenium failed on team " + team)


