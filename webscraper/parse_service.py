import re
from io import StringIO
import pandas as pd
import bs4


class RealGMParser:
    @staticmethod
    def parse_footnote_unavailable(html_content):
        soup = bs4.BeautifulSoup(html_content, 'html.parser')
        footnote_paragraphs = soup.find_all('p', class_='footnote')

        for p in footnote_paragraphs:
            if p.get_text() == "Stats are not currently available for this season.":
                return True
        return False

    @staticmethod
    def full_name_populate_depth_position(player_name, player_df, r, depth_df, ind, col):
        if player_name in player_df["Player"].values:
            # depth = r[depth_df.columns[0]] if r[depth_df.columns[0]] in ["Starters", "Lim PT"] else str(ind + 1)
            depth = 1 if r[depth_df.columns[0]] == "Starters" else (
                r[depth_df.columns[0]] if r[depth_df.columns[0]] == "Lim PT" else str(ind + 1))
            player_index = player_df.index[player_df["Player"] == player_name]
            player_df.at[player_index[0], "Depth"] = depth
            player_df.at[player_index[0], "Position"] = col
            return True

    @staticmethod
    def initial_name_populate_depth_position(player_df, player_name, r, depth_df, ind, col):
        if player_df['Player'].apply(lambda x: bool(re.search(player_name, x))).any():
            # depth = r[depth_df.columns[0]] if r[depth_df.columns[0]] in ["Starters", "Lim PT"] else str(ind + 1)
            depth = 1 if r[depth_df.columns[0]] == "Starters" else (
                r[depth_df.columns[0]] if r[depth_df.columns[0]] == "Lim PT" else str(ind + 1))
            player_index = player_df.index[player_df['Player'].apply(lambda x: bool(re.search(player_name, x)))]
            player_df.at[player_index[0], "Depth"] = depth
            player_df.at[player_index[0], "Position"] = col
            return True

    @staticmethod
    def parse_depth_2_players(df_depth, df_player):
        for i, row in df_depth.iterrows():
            for column, value in row.items():
                if column == df_depth.columns[0]:
                    continue
                if pd.notna(value):
                    name = re.split(r'(?=\d)', value, 1)[0].strip()
                    pattern = re.escape(name[0]) + r'.*' + re.escape(name.split()[-1])

                    if not (RealGMParser.full_name_populate_depth_position(name, df_player, row, df_depth, i, column) or
                            RealGMParser.initial_name_populate_depth_position(df_player, pattern, row, df_depth, i,
                                                                              column)):
                        print(f"Player {name} is missing from the Players table!")
                    # if name in df_player["Player"].values:
                    #     depth = row[df_depth.columns[0]] if row[df_depth.columns[0]] in ["Starters", "Lim PT"] else i+1
                    #     player_index = df_player.index[df_player["Player"] == name]
                    #     df_player.at[player_index[0], "Depth"] = depth
                    #     df_player.at[player_index[0], "Position"] = column
                    # elif df_player['Player'].apply(lambda x: bool(re.search(pattern, x))).any():
                    #     depth = row[df_depth.columns[0]] if row[df_depth.columns[0]] in ["Starters", "Lim PT"] else i+1
                    #     player_index = df_player.index[df_player['Player'].apply(lambda x: bool(re.search(pattern, x)))]
                    #     df_player.at[player_index[0], "Depth"] = depth
                    #     df_player.at[player_index[0], "Position"] = column
                    # else:
                    #     print(f"Player {name} is missing from the Players table!")

    @staticmethod
    def players_df_add_columns(df):
        df["Position"] = ""
        df["Depth"] = ""
        df.insert(df.columns.get_loc("Player") + 1, "Season", "")

    @staticmethod
    def depth_table_2_df(sauce, years: str):
        soup = bs4.BeautifulSoup(sauce, 'html.parser')
        h2_element = soup.find('h2', string=lambda text: text and years in text)
        div_with_table = h2_element.find_next_sibling('div')
        table_html = div_with_table.find('table', class_='basketball')
        table_str = str(table_html)
        mock_html = StringIO(table_str)
        return pd.read_html(mock_html)[0]

    @staticmethod
    def html_table_append_df(sauce, df_base):
        df_extension = RealGMParser.html_table_2_df(sauce)
        df_base = pd.concat([df_base, df_extension], ignore_index=True)
        return df_base

    @staticmethod
    def html_table_2_df(sauce):
        soup = bs4.BeautifulSoup(sauce, 'html.parser')
        table_html = soup.find('table', class_='tablesaw')
        table_str = str(table_html)
        mock_html = StringIO(table_str)

        return pd.read_html(mock_html)[0]
