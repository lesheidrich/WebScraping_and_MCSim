from typing import Optional, Literal

from pandas import DataFrame
from controller.dto_service import DataTransferObject, Persist


class ScrapeControl:
    def __init__(self, proxies_csv: Optional[str], season: str, team: str,
                 check_proxies: bool = False, db_host: Optional[str] = None):
        # scrape_method: Literal["firefox_selenium_scrape", "firefox_selenium_proxy_scrape",
        #                        "chrome_selenium_scrape", "chrome_selenium_proxy_scrape",
        #                        "requests_scrape", "requests_proxy_scrape",
        #                        "scrapy_scrape", "scrapy_proxy_scrape"]):
        self.dto = DataTransferObject(proxies_csv, check_proxies)
        self.db_host = db_host
        self.players = []
        self.base = "https://basketball.realgm.com/nba/team"
        self.season = season
        self.team = team
        self.year = self.season.split('-')[1]
        self.urls = self.set_link_tree()
        self.in_playoffs = Persist.team_in_playoffs(self.team, self.season, db_host)
        self.df_depth = None

    def run_all(self, scrape_method: str) -> None:
        url_depth = f"{self.base}s/{self.team}/Depth_Charts"
        self.df_depth = self.dto.new_depth_df(scrape_method, url_depth, self.season)

        for category, (links, tables) in self.urls.items():
            print(f"Category: {category}")
            for link, table in zip(links, tables):
                if (not self.in_playoffs and "Playoff" not in link) or self.in_playoffs:
                    try:
                        method = getattr(self, f"process_{category}")
                        method(scrape_method, link, table)
                    except Exception as e:
                        print(f"LOG: scrape method {scrape_method} failed for {link} on table {table}. {e}")
                        method = getattr(self, f"process_{category}")
                        method("firefox_selenium_scrape", link, table)

    def run_single(self, category_type: str, scrape_method: str):
        links = self.urls[category_type]
        method = getattr(self, f"process_{category_type}")

        for _ in range(len(links[0])):
            if (not self.in_playoffs and "Playoff" not in links[0][_]) or self.in_playoffs:
                print(links[0][_], links[1][_])
                method(scrape_method, links[0][_], links[1][_])

    def process_player(self, scrape_method: str, url: str, table_name: str) -> None:
        if self.df_depth is None:
            url_depth = f"{self.base}s/{self.team}/Depth_Charts"
            self.df_depth = self.dto.new_depth_df(scrape_method, url_depth, self.season)

        df_player = self.dto.new_players_df(scrape_method, url)
        self.dto.player_depth_merged_df(self.df_depth, df_player)
        df_player['Season'] = self.season
        Persist.insert(df_player, table_name, "player", self.db_host)

    def process_individual(self, scrape_method: str, url: str, table_name: str) -> None:
        df_individual = self.dto.merged_individual_df(scrape_method, url)
        Persist.insert(df_individual, table_name, "individual", self.db_host)

    def process_team(self, scrape_method: str, url: str, table_name: str) -> None:
        if not Persist.team_in_db(self.season, table_name, self.db_host):
            print(f"Adding team {self.team} with season {self.season}")
            df_team = self.dto.new_team_df(scrape_method, url)
            df_team['Season'] = self.season
            Persist.insert(df_team, table_name, "team", self.db_host)
        else:
            print(f"Team {self.team} with season {self.season} is already in the database.")

    def set_link_tree(self) -> dict:
        return {
            "player": [
                [
                    f"{self.base}s/{self.team}/Stats/{self.year}/Averages/All/points/All/desc/1/Home",
                    f"{self.base}s/{self.team}/Stats/{self.year}/Averages/All/points/All/desc/1/Away",
                    f"{self.base}s/{self.team}/Stats/{self.year}/Averages/All/points/All/desc/1/Playoff_Home",
                    f"{self.base}s/{self.team}/Stats/{self.year}/Averages/All/points/All/desc/1/Playoff_Away"
                ],
                [
                    "player_regular_home",
                    "player_regular_away",
                    "player_playoff_home",
                    "player_playoff_away"
                ]
            ],
            "team": [
                [
                    f"{self.base}-stats/{self.year}/Advanced_Stats/Team_Totals/Regular_Season",
                    f"{self.base}-stats/{self.year}/Advanced_Stats/Team_Totals/Playoff"
                ],
                [
                    "team_regular",
                    "team_playoff"
                ]
            ],
            "individual": [
                [
                    f"{self.base}s/{self.team}/individual-games/{self.year}/points/Regular_Season/desc/",
                    f"{self.base}s/{self.team}/individual-games/{self.year}/points/Playoffs/desc/"
                ],
                [
                    "individual_games_regular",
                    "individual_games_playoff"
                ]
            ]
        }

# def begin_monte_carlo():
#     conn = MySQLHandler()
#     if not conn.season_in_db("2005-2006", "BOS"):
#         print("scrape it")
#     conn.disconnect()
#     print("perform monte carlo")
