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
2. Retrieve the source code from https://github.com/lesheidrich/WebScraping_and_MCSim
3. From */model/data/* upload *nba.sql* and *nba_test.sql* to your database. Depending on your database provider you may need to break the *individual_games_regular* table into smaller chunks, due to row limitations.
4. Install requirements by navigating to the project folder or using the absolute path with the command: `pip install -r requirements.txt`
5. Fill out *project_secrets.py* with the necessary access data.
6. Ensure your database is running, then start the back end service by running *main.py*.
7. The client application found in */view* should be downloaded to, and run from the client system. */view/NBA_Sim_View/bin/Debug/NBA_Sim_View.exe* will commence
the client application.

![Monte Carlo simulation results](https://github.com/lesheidrich/Thesis/blob/main/img/user-guide/MonteCarlo.png?raw=true)
