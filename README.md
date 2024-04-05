***This project serves as the practical implementation of my computer science BSc [thesis](https://github.com/lesheidrich/Thesis/blob/bf28caa3c3bd65426a2e8a63fd0e69c3d5d254b0/thesis_gwjz4t.pdf) at Eszterházy Károly Catholic University.***

# Project Description
The application utilizes web scraping services to construct a MySQL/MariaDB database of historic NBA game data from the early 1990s. Users can select any historic game in the provided range, and the Monte Carlo simulation will estimate the expected results from reconstructed data predating the match. Simulations run for a preset range of epochs. The simulation performs best between 5-10 thousand epochs.

Project documentation is available in the [thesis](https://github.com/lesheidrich/Thesis/blob/bf28caa3c3bd65426a2e8a63fd0e69c3d5d254b0/thesis_gwjz4t.pdf).

# Installation
1. Installation prerequisites:
  - Client side:
    - Operating system must be Microsoft Windows 10 or later.
    - .NET framework 4.8 or later.
  - Server side:
    - Python 3.11 or later must be installed.
    - A VPN service is suggested.
    - XAMPP 3.3.0 or later (or any other database service that works with MySQL and MariaDB).
2. From */model/data/* upload *nba.sql* and *nba_test.sql* to your database. Depending on your database provider you may need to break the *individual_games_regular* table into smaller chunks, due to row limitations.
3. Install requirements by navigating to the project folder or using the absolute path with the command: `pip install -r requirements.txt`
4. Fill out *project_secrets.py* with the necessary access data.
5. Ensure your database is running, then start the back-end service by running *main.py*.
6. The client application found in */view* should be downloaded to, and run from the client system. */view/NBA_Sim_View/bin/Debug/NBA_Sim_View.exe* will commence
the client application.

# Web Scraper
Content is sourced through either Python's Requests library, or Selenium WebDrivers (Firefox or Chrome). The application allows for the optional utilization of built in rotating proxies, with functionality to pre-check connection availability. Users can opt to upload and use their own proxy list. HTTP request headers are automatically rotated.

At default, the scraper automatically repeats failed attempts with Selenium's Firefox Webdriver, therefore the use of Requests is suggested for initial attempts.

# Simulation
The simulation process operates in conjunction with three stat table categories:
- **Individual games**: stats broken down by player for each game date
- **Player**: seasonal averages per player
- **Team**: team averages per season

Match data is constructed in team roster instances, which house player instances containing each player's stats for the past year of play leading up to the game date. This data is taken from the *individual games* table. The table is modified to make the last 2-3 games count 5x, and the last few weeks to count 3x compared to their original value. This ensures recent games have a greater effect on a player's performance. Player instances also utilize additional metrics from seasonal averages.

Each game operates based on offensive possessions, where decisions regarding the outcome of single events are made by random weighted sampling and random probability thresholds pertaining to player stats. Total possessions per game are based on each team's pace. 

Games run for the parameterized epoch count, resulting in a display similar to the below example:
- **Top right**: outcome of the original NBA game.
- **Top left**: simulated outcome, with the percentage of games won, and the mode of scores for each team.
- **Probability density graph**: x-axis represents scores, y-axis represents the volume for each score. Yellow is home, blue is away.
- **Violin graph**: y-axis represents score range, the width of each resulting cluster represents how often the score occurred.

![Monte Carlo simulation results](https://github.com/lesheidrich/Thesis/blob/main/img/user-guide/MonteCarlo.png?raw=true)
