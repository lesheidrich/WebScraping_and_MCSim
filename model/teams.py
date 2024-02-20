"""
Module: teams.py

Represents NBA teams in RealGM tables.

This module defines an enumeration class `Teams` that represents NBA teams.
Each team is associated with its full name, short name, link name (used in URLs),
and city name.

Attributes:
    full_name (str): Full name of the NBA team.
    short_name (str): Short abbreviation of the NBA team.
    link_name (str): Name used in URLs for the NBA team.
    city_name (str): City associated with the NBA team.
"""

from enum import Enum


class Teams(Enum):
    """
    Enumeration class representing NBA teams in RealGM tables.

    Attributes:
        full_name (str): Full name of the NBA team.
        short_name (str): Short abbreviation of the NBA team.
        link_name (str): Name used in URLs for the NBA team.
        city_name (str): City associated with the NBA team.
    """
    ATLANTA_HAWKS = ('Atlanta Hawks', 'ATL', 'Atlanta-Hawks/1', "Atlanta")
    BOSTON_CELTICS = ('Boston Celtics', 'BOS', 'Boston-Celtics/2', "Boston")
    BROOKLYN_NETS = ('Brooklyn Nets', 'BKN', 'Brooklyn-Nets/38', "Brooklyn")
    CHARLOTTE_HORNETS = ('Charlotte Hornets', 'CHA', 'Charlotte-Hornets/3', "Charlotte")
    CHARLOTTE_BOBCATS = ('Charlotte Bobcats', 'CHA', 'Charlotte-Hornets/3', "Charlotte")
    CHICAGO_BULLS = ('Chicago Bulls', 'CHI', 'Chicago-Bulls/4', "Chicago")
    CLEVELAND_CAVALIERS = ('Cleveland Cavaliers', 'CLE', 'Cleveland-Cavaliers/5', "Cleveland")
    DALLAS_MAVERICKS = ('Dallas Mavericks', 'DAL', 'Dallas-Mavericks/6', "Dallas")
    DENVER_NUGGETS = ('Denver Nuggets', 'DEN', 'Denver-Nuggets/7', "Denver")
    DETROIT_PISTONS = ('Detroit Pistons', 'DET', 'Detroit-Pistons/8', "Detroit")
    GOLDEN_STATE_WARRIORS = ('Golden State Warriors', 'GSW', 'Golden-State-Warriors/9', "Golden State")
    HOUSTON_ROCKETS = ('Houston Rockets', 'HOU', 'Houston-Rockets/10', "Houston")
    INDIANA_PACERS = ('Indiana Pacers', 'IND', 'Indiana-Pacers/11', "Indiana")
    LOS_ANGELES_CLIPPERS = ('Los Angeles Clippers', 'LAC', 'Los-Angeles-Clippers/12', "L.A. Clippers")
    LOS_ANGELES_LAKERS = ('Los Angeles Lakers', 'LAL', 'Los-Angeles-Lakers/13', "L.A. Lakers")
    MEMPHIS_GRIZZLIES = ('Memphis Grizzlies', 'MEM', 'Memphis-Grizzlies/14', "Memphis")
    MIAMI_HEAT = ('Miami Heat', 'MIA', 'Miami-Heat/15', "Miami")
    MILWAUKEE_BUCKS = ('Milwaukee Bucks', 'MIL', 'Milwaukee-Bucks/16', "Milwaukee")
    MINNESOTA_TIMBERWOLVES = ('Minnesota Timberwolves', 'MIN', 'Minnesota-Timberwolves/17', "Minnesota")
    NEW_ORLEANS_PELICANS = ('New Orleans Pelicans', 'NOP', 'New-Orleans-Pelicans/19', "New Orleans")
    NEW_ORLEANS_HORNETS = ('New Orleans Hornets', 'NOH', 'New-Orleans-Pelicans/19', "New Orleans")
    NEW_YORK_KNICKS = ('New York Knicks', 'NYK', 'New-York-Knicks/20', "New York")
    OKLAHOMA_CITY_THUNDER = ('Oklahoma City Thunder', 'OKC', 'Oklahoma-City-Thunder/33', "Oklahoma City")
    ORLANDO_MAGIC = ('Orlando Magic', 'ORL', 'Orlando-Magic/21', "Orlando")
    PHILADELPHIA_SIXERS = ('Philadelphia Sixers', 'PHI', 'Philadelphia-Sixers/22', "Philadelphia")
    PHOENIX_SUNS = ('Phoenix Suns', 'PHX', 'Phoenix-Suns/23', "Phoenix")
    PORTLAND_TRAIL_BLAZERS = ('Portland Trail Blazers', 'POR', 'Portland-Trail-Blazers/24', "Portland")
    SACRAMENTO_KINGS = ('Sacramento Kings', 'SAC', 'Sacramento-Kings/25', "Sacramento")
    SAN_ANTONIO_SPURS = ('San Antonio Spurs', 'SAS', 'San-Antonio-Spurs/26', "San Antonio")
    TORONTO_RAPTORS = ('Toronto Raptors', 'TOR', 'Toronto-Raptors/28', "Toronto")
    UTAH_JAZZ = ('Utah Jazz', 'UTA', 'Utah-Jazz/29', "Utah")
    WASHINGTON_WIZARDS = ('Washington Wizards', 'WAS', 'Washington-Wizards/30', "Washington")

    def __init__(self, full_name, short_name, link_name, city_name):
        self.full_name = full_name
        self.short_name = short_name
        self.link_name = link_name
        self.city_name = city_name

    @classmethod
    def from_full_name(cls, full_name: str):
        """
        Get a team instance based on its full name.
        :param full_name: str of team full name, format: 'Chicago Bulls'
        :return: Teams instance for nba team str param
        """
        for team in cls:
            if team.full_name == full_name:
                return team
        raise ValueError(f"No team found with full name: {full_name}")

    @classmethod
    def from_short_name(cls, short_name: str):
        """
        Get a team instance based on its short name.
        :param short_name: str of team full name, format: 'CHI'
        :return: Teams instance for nba team str param
        """
        for team in cls:
            if team.short_name == short_name:
                return team
        raise ValueError(f"No team found with short name: {short_name}")

    @classmethod
    def from_link_name(cls, link_name: str):
        """
        Get a team instance based on its link name, as used in RealGM URLs.
        :param link_name: str of team full name, format: 'Chicago-Bulls/4'
        :return: Teams instance for nba team str param
        """
        for team in cls:
            if team.link_name == link_name:
                return team
        raise ValueError(f"No team found with link name: {link_name}")

    @classmethod
    def from_city_name(cls, city_name: str):
        """
        Get a team instance based on its city name.
        :param city_name: str of team full name, format: 'Chicago'
        :return: Teams instance for nba team str param
        """
        for team in cls:
            if team.city_name == city_name:
                return team
        raise ValueError(f"No team found with city name: {city_name}")
