"""
MySQLHandler Module

Houses class for interacting with a MySQL database, including methods for connecting to
the database, executing queries, and performing CRUD operations.

Usage:
    Instantiate MySQLHandler class with appropriate credentials.
    Call methods to perform database operations.

Example:
    handler = MySQLHandler(host='localhost',
                           username='root',
                           password='password',
                           database='mydb')
    handler.connect()
    handler.insert_record('my_table', {'name': 'John', 'age': 30})
    handler.disconnect()

Attributes:
    host (str): The host address of the MySQL database server.
    username (str): The username for authenticating with the database.
    password (str): The password for authenticating with the database.
    database (str): The name of the database to connect to.

Methods:
    connect(): Establishes a connection to the MySQL database.
    disconnect(): Closes the connection to the MySQL database.
    commit_and_close_cur(cur): Commits changes and closes the cursor.
    execute_query(query, params=None): Executes a SQL query with optional parameters.
    execute_and_commit(query, params=None): Executes a query and commits changes.
    insert_record(table, data, columns=None): Inserts a record into the specified table.
    read(table, conditions=None): Reads records from the specified table with optional conditions.
    update_record(table, data, conditions): Updates records in the specified table based on conditions.
    delete_record(table, conditions): Deletes records from the specified table based on conditions.
    season_in_db(season: str, team: str): Returns boolean for presence of specified team and season in DB.
"""

from typing import List, Optional
from urllib.parse import urlparse
from project_secrets import XAMPP_URI
import mysql.connector


class MySQLHandler:
    """
    MySQLHandler Class

    Provides methods for interacting with a MySQL database,
    including connecting, executing queries, and performing CRUD operations.

    Example usage:
    connector = MySQLConnector(
        host='localhost',
        username='your_username',
        password='your_password',
        database='your_database'
    )

    Create a record:
        data = {'player': 'John Doe', 'team': 'Team A', 'PPG': 20.5}
        connector.create_record('basketball_stats', data)

    Read records:
        records = connector.read('basketball_stats')
        for record in records:
            print(record)

    Update a record:
        data = {'team': 'Team B', 'PPG': 22.3}
        connector.update_record('basketball_stats', data, 'player = "John Doe"')

    Delete a record:
        connector.delete_record('basketball_stats', 'player = "John Doe"')

    Disconnect from the database:
        connector.disconnect()
    """

    def __init__(self, uri: Optional[str]):
        if uri is None:
            uri = XAMPP_URI
        parsed = urlparse(uri)
        self.host = parsed.hostname
        self.username = parsed.username
        self.password = parsed.password
        self.port = parsed.port
        self.database = parsed.path[1:]
        self.connection = None
        self.connect()

    def connect(self) -> None:
        """
        Establishes MySQL connection utilizing class attributes.
        :return: None
        """
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.username,
            port=self.port,
            password=self.password,
            database=self.database
        )

    def disconnect(self) -> None:
        """
        Terminates existing connection to MySQL db.
        :return: None
        """
        if self.connection.is_connected():
            self.connection.close()

    def commit_and_close_cur(self, cur) -> None:
        """
        Commits changes to table for the query relating to the cursor arg, then closes cursor.
        :param cur: cursor for existing query.
        :return: None
        :raises: ConnectinError if unsuccessful.
        """
        try:
            self.connection.commit()
            cur.close()
        except mysql.connector.Error as e:
            raise ConnectionError(f"Error executing MySQLHandler.commit_and_close_cur! "
                                  f"Ensure cursor population was successful.\n{e}") from e

    def execute_query(self, query: str, params=None) -> mysql.connector.connection.MySQLCursor:
        """
        Cursor executes query string pertaining to CRUD operation. Rolls back changes if unsuccessful.
        :param query: SQL command string, utilizes placeholders for params (in case of sql injection attack).
        :param params: Parameters of SQL command to replace placeholders.
        :return: cursor for existing query.
        :raises: ConnectionError in case of mysql.connector.Error
        """
        cursor = self.connection.cursor()
        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return cursor
        except mysql.connector.Error as e:
            self.connection.rollback()
            raise ConnectionError(f"Error executing query: {e}") from e

    def execute_and_commit(self, query: str, params=None) -> None:
        """
        Wrapper function for execute_query() and commit_and_close_cur().
        Executes and commits query string, then closes the cursor.
        :param query: query string for SQL command utilizing placeholders for parameters.
        :param params: SQL command parameters (passed separate in case of injection attack).
        :return: None
        """
        cursor = self.execute_query(query, params)
        self.commit_and_close_cur(cursor)

    def insert_record(self, table: str, data: dict, columns: str = None) -> None:
        """
        Inserts a single record (row) to the arg table.
        :param table: str for table to update.
        :param data: dictionary containing values to persist.
        :param columns: str of column heads that values are provided for in data dict.
                        Use "player", "team", "individual" arg to set columns for existing tables.
                        Can also indicate custom columns with syntax: columns="(foo, bar)"
        :return: None
        """
        if columns == "player":
            columns = ("(player, season, team, GP, MPG, PPG, FGM, FGA, FGpercent, 3PM, 3PA, 3Ppercent, FTM, "
                       "FTA, FTpercent, ORB, DRB, RPG, APG, SPG, BPG, TOV, PF, position, depth)")
        elif columns == "team":
            columns = ("(team, season, TS, eFG, TotalS, ORB, DRB, TRB, AST, TOV, STL, BLK, PPS, FIC40, "
                       "ORtg, DRtg, eDiff, Poss, Pace)")
        elif columns == "individual":
            columns = ("(player, date, team, MIN, PTS, FGM, FGA, 3PM, 3PA, FTM, FTA, ORB, DRB, REB, AST, "
                       "STL, BLK, TOV, PF)")
        placeholders = ', '.join(['%s'] * (len(data)))
        query = f"INSERT INTO {table} {columns} VALUES ({placeholders})"
        self.execute_and_commit(query, tuple(data.values()))

    def read(self, table: str, selection: Optional[str] = "*", conditions: Optional[str] = None) -> List:
        """
        Reads contents of selected table, filtered by conditions param.
        :param selection: str of column to search for, default: *
        :param table: str of table name to query.
        :param conditions: str of condition to append to WHERE part of command: WHERE {conditions}.
        :return: list of tuples for each row, including header
        """
        query = f"SELECT {selection} FROM {table}"
        if conditions:
            query += f" WHERE {conditions}"
        cursor = self.execute_query(query)
        table = [tuple(col[0] for col in cursor.description)]
        for row in cursor.fetchall():
            table.append(row)
        self.connection.commit()
        cursor.close()
        return table

    def update_record(self, table: str, data: dict, conditions: str) -> None:
        """
        Updates specified record per params.
        :param table: str of table to update.
        :param data: dict of new cell values to update to.
        :param conditions: str of condition to append to WHERE part of command: WHERE {conditions}.
        :return: None
        """
        setters = ', '.join([f"{key}=%s" for key in data.keys()])
        query = f"UPDATE {table} SET {setters} WHERE {conditions}"
        self.execute_and_commit(query, tuple(data.values()))

    def delete_record(self, table: str, conditions: str) -> None:
        """
        Deletes records from the specified table based on the given conditions.
        :param table: str for table from which records will be deleted.
        :param conditions: str of condition to append to WHERE part of command: WHERE {conditions}.
        :return: None
        """
        query = f"DELETE FROM {table} WHERE {conditions}"
        self.execute_and_commit(query)

    def season_in_db(self, season: str, team: str) -> bool:
        """
        Returns boolean for presence of specified team and season in DB. Used to initalize scraper on False.
        :param season: str: "2005-2006"
        :param team: team name format: "BOS"
        :return: bool for season and team presence in DB.
        """
        query = f"""SELECT
            IF(SUM(has_data) = 4, 'true', 'false') AS all_tables_have_data
        FROM (
            SELECT IF(COUNT(id) > 0, 1, 0) AS has_data
            FROM team_regular WHERE season = '{season}'
            UNION ALL  
            SELECT IF(COUNT(id) > 0, 1, 0) AS has_data
            FROM player_regular_home WHERE season = '{season}' AND team = '{team}'
            UNION ALL
            SELECT IF(COUNT(id) > 0, 1, 0) AS has_data
            FROM player_regular_away WHERE season = '{season}' AND team = '{team}'
            UNION ALL
            SELECT IF(COUNT(id) > 0, 1, 0) AS has_data
            FROM individual_games_regular WHERE date LIKE '{season.split("-")[1]}-01-__' AND team = '{team}'
        ) AS all_tables;
        """
        cursor = self.execute_query(query)
        result = cursor.fetchall()
        cursor.close()
        return result[0][0] == 'true'

    def in_playoffs(self, team: str, season: str) -> bool:
        """
        Boolean check for arg team if they are in the playoffs for arg season.
        Method is later used to check if playoff data needs to be scraped.
        :param team: str of nba team: Boston-Celtics/2
        :param season: str of season: 1991-1992
        :return: true if arg team played in playoffs for specified season
        """
        query = f'select `{team.split("/")[0]}` from in_playoffs where Season="{season}";'
        cursor = self.execute_query(query)
        try:
            result = cursor.fetchall()[0][0]
            cursor.close()
            return result == 1
        except IndexError:
            return False

    def truncate_table(self, table_name: str) -> None:
        """
        Truncates specified table.
        :param table_name: str of table name to truncate
        :return: None
        """
        query = f'TRUNCATE {table_name};'
        self.execute_and_commit(query)
