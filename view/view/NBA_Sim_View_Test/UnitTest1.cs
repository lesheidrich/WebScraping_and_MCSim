using Microsoft.VisualStudio.TestTools.UnitTesting;
using System;
using TestStack.White;
using TestStack.White.UIItems;
using TestStack.White.UIItems.Finders;
using TestStack.White.UIItems.ListBoxItems;
using TestStack.White.UIItems.WindowItems;
using TestStack.White.UIItems.ListViewItems;
using TestStack.White.InputDevices;
using TestStack.White.UIItems.TableItems;
using TestStack.White.Factory;
using TestStack.White.Utility;
using System.Linq;
using System.Runtime.InteropServices;
using System.IO;
using System.Reflection;
using System.Diagnostics;

namespace NBA_Sim_View_Test
{
    [TestClass]
    public class UnitTest1
    {
        private string appPath = @"C:\Users\dblin\PycharmProjects\WebScraping_and_MCSim\view\NBA_Sim_View\bin\Debug\NBA_Sim_View.exe";
        private string[] nbaTeams = new string[]
            {
                "Atlanta Hawks",
                "Boston Celtics",
                "Charlotte Hornets",
                "Chicago Bulls",
                "Cleveland Cavaliers",
                "Dallas Mavericks",
                "Denver Nuggets",
                "Detroit Pistons",
                "Golden State Warriors",
                "Houston Rockets",
                "Indiana Pacers",
                "Los Angeles Clippers",
                "Los Angeles Lakers",
                "Miami Heat",
                "Milwaukee Bucks",
                "Minnesota Timberwolves",
                "New York Knicks",
                "Orlando Magic",
                "Philadelphia Sixers",
                "Phoenix Suns",
                "Portland Trail Blazers",
                "Sacramento Kings",
                "San Antonio Spurs",
                "Utah Jazz"
            };

        private string[] seasons = new string[]
        {
            "1991-1992", "1992-1993", "1993-1994", "1994-1995", "1995-1996"
        };


        [TestMethod]
        public void TestGetGamesMissingEpochs()
        {
            // tests pop-up warning for epochs empty
            Application application = Application.Launch(appPath);
            Window window = application.GetWindow("Monte Carlo");

            ComboBox home = window.Get<ComboBox>(SearchCriteria.ByAutomationId("cbHome"));
            ComboBox away = window.Get<ComboBox>(SearchCriteria.ByAutomationId("cbAway"));
            ComboBox season = window.Get<ComboBox>(SearchCriteria.ByAutomationId("cbSeason"));

            home.Select("Chicago Bulls");
            away.Select("Boston Celtics");
            season.Select("1991-1992");

            Button games = window.Get<Button>(SearchCriteria.ByAutomationId("btnGetGames"));
            games.Click();

            Button ok = window.Get<Button>(SearchCriteria.ByText("OK"));
            ok.Click();

            application.Close();
        }

        [TestMethod]
        public void TestGetGamesEpochsNotNumeric()
        {
            // tests pop-up warning for epochs not numeric
            Application application = Application.Launch(appPath);
            Window window = application.GetWindow("Monte Carlo");

            ComboBox home = window.Get<ComboBox>(SearchCriteria.ByAutomationId("cbHome"));
            ComboBox away = window.Get<ComboBox>(SearchCriteria.ByAutomationId("cbAway"));
            ComboBox season = window.Get<ComboBox>(SearchCriteria.ByAutomationId("cbSeason"));
            TextBox epoch = window.Get<TextBox>(SearchCriteria.ByAutomationId("tbEpochs"));

            home.Select("Chicago Bulls");
            away.Select("Boston Celtics");
            season.Select("1991-1992");
            epoch.Text = "wrong answer";

            Button games = window.Get<Button>(SearchCriteria.ByAutomationId("btnGetGames"));
            games.Click();

            Button ok = window.Get<Button>(SearchCriteria.ByText("OK"));
            ok.Click();

            application.Close();
        }

        [TestMethod]
        public void TestGetGamesSeasonEmpty()
        {
            // tests pop-up warning for empty season
            Application application = Application.Launch(appPath);
            Window window = application.GetWindow("Monte Carlo");

            ComboBox home = window.Get<ComboBox>(SearchCriteria.ByAutomationId("cbHome"));
            ComboBox away = window.Get<ComboBox>(SearchCriteria.ByAutomationId("cbAway"));
            TextBox epoch = window.Get<TextBox>(SearchCriteria.ByAutomationId("tbEpochs"));

            home.Select("Chicago Bulls");
            away.Select("Boston Celtics");
            epoch.Text = "10";

            Button games = window.Get<Button>(SearchCriteria.ByAutomationId("btnGetGames"));
            games.Click();

            Button ok = window.Get<Button>(SearchCriteria.ByText("OK"));
            ok.Click();

            application.Close();
        }

        [TestMethod]
        public void TestGetGamesTeamsSame()
        {
            // tests pop-up warning for home team == away team
            Application application = Application.Launch(appPath);
            Window window = application.GetWindow("Monte Carlo");

            ComboBox home = window.Get<ComboBox>(SearchCriteria.ByAutomationId("cbHome"));
            ComboBox away = window.Get<ComboBox>(SearchCriteria.ByAutomationId("cbAway"));
            TextBox epoch = window.Get<TextBox>(SearchCriteria.ByAutomationId("tbEpochs"));
            ComboBox season = window.Get<ComboBox>(SearchCriteria.ByAutomationId("cbSeason"));

            home.Select("Chicago Bulls");
            away.Select("Chicago Bulls");
            epoch.Text = "10";
            season.Select("1991-1992");

            Button games = window.Get<Button>(SearchCriteria.ByAutomationId("btnGetGames"));
            games.Click();

            Button ok = window.Get<Button>(SearchCriteria.ByText("OK"));
            ok.Click();

            application.Close();
        }

        [TestMethod]
        public void TestGetGamesHomeEmpty()
        {
            // tests pop-up warning for home unselected
            Application application = Application.Launch(appPath);
            Window window = application.GetWindow("Monte Carlo");

            ComboBox away = window.Get<ComboBox>(SearchCriteria.ByAutomationId("cbAway"));
            TextBox epoch = window.Get<TextBox>(SearchCriteria.ByAutomationId("tbEpochs"));
            ComboBox season = window.Get<ComboBox>(SearchCriteria.ByAutomationId("cbSeason"));

            away.Select("Chicago Bulls");
            epoch.Text = "10";
            season.Select("1991-1992");

            Button games = window.Get<Button>(SearchCriteria.ByAutomationId("btnGetGames"));
            games.Click();

            Button ok = window.Get<Button>(SearchCriteria.ByText("OK"));
            ok.Click();

            application.Close();
        }

        [TestMethod]
        public void TestGetGamesAwayEmpty()
        {
            // tests pop-up warning for away unselected
            Application application = Application.Launch(appPath);
            Window window = application.GetWindow("Monte Carlo");

            ComboBox home = window.Get<ComboBox>(SearchCriteria.ByAutomationId("cbHome"));
            TextBox epoch = window.Get<TextBox>(SearchCriteria.ByAutomationId("tbEpochs"));
            ComboBox season = window.Get<ComboBox>(SearchCriteria.ByAutomationId("cbSeason"));

            home.Select("Chicago Bulls");
            epoch.Text = "10";
            season.Select("1991-1992");

            Button games = window.Get<Button>(SearchCriteria.ByAutomationId("btnGetGames"));
            games.Click();

            Button ok = window.Get<Button>(SearchCriteria.ByText("OK"));
            ok.Click();

            application.Close();
        }

        [TestMethod]
        public void TestTeamsMC()
        {
            string filePath = @"..\..\test_log.txt";
            if (!File.Exists(filePath))
            {
                File.Create(filePath).Close();
            }

            // iteratively check Monte Carlo params
            foreach (var season in seasons)
            {
                for (int i = 0; i < nbaTeams.Length; i++)
                {
                    for (int j = 0; j < nbaTeams.Length; j++)
                    {
                        if (!nbaTeams[i].Equals(nbaTeams[j]))
                        {
                            try
                            {
                                RunMCTest(nbaTeams[i], nbaTeams[j], season);
                            }
                            catch (Exception e)
                            {
                                using (StreamWriter sw = new StreamWriter(filePath, true))
                                {
                                    sw.WriteLine($"{DateTime.Now} - UI LOG - MC Test - Error on {nbaTeams[i]} " +
                                        $"VS {nbaTeams[j]}: {e}\n");
                                }
                            }
                        }
                    }
                }
            }

            //var season = "1991-1992";
            //for (int i = 0; i < nbaTeams.Length; i++)
            //{
            //    for (int j = 0; j < nbaTeams.Length; j++)
            //    {
            //        if (!nbaTeams[i].Equals(nbaTeams[j]))
            //        {
            //            try
            //            {
            //                RunMCTest(nbaTeams[i], nbaTeams[j], season);
            //            }
            //            catch (Exception e)
            //            {
            //                using (StreamWriter sw = new StreamWriter(filePath, true))
            //                {
            //                    sw.WriteLine($"{DateTime.Now} - UI LOG - MC Test - Error on {nbaTeams[i]} " +
            //                        $"VS {nbaTeams[j]}: {e}\n");
            //                }
            //            }
            //        }
            //    }
            //}

            // open the log
            try
            {
                Process.Start(filePath);
            }
            catch (Exception ex)
            {
                Console.WriteLine("Error while attempting to open file: " + ex.Message);
            }

        }

        public void RunMCTest(string home_team, string away_team, string yrs)
        {

            Application application = Application.Launch(appPath);
            Window window = application.GetWindow("Monte Carlo");

            // UI elements
            TextBox epoch = window.Get<TextBox>(SearchCriteria.ByAutomationId("tbEpochs"));
            ComboBox home = window.Get<ComboBox>(SearchCriteria.ByAutomationId("cbHome"));
            ComboBox away = window.Get<ComboBox>(SearchCriteria.ByAutomationId("cbAway"));
            ComboBox season = window.Get<ComboBox>(SearchCriteria.ByAutomationId("cbSeason"));
            Button games = window.Get<Button>(SearchCriteria.ByAutomationId("btnGetGames"));

            // simulation params
            epoch.Text = "10";
            home.Select(home_team);
            away.Select(away_team);
            season.Select(yrs);

            games.Click();

            Button sel = window.Get<Button>(SearchCriteria.ByAutomationId("btnSelect"));
            sel.Click();

            // second window
            Window mc = application.GetWindow("Simulation");

            // test home score mode result is int
            TextBox mode = mc.Get<TextBox>(SearchCriteria.ByAutomationId("tbModeHome"));
            bool isValidValue = int.TryParse(mode.Text, out _);

            application.Close();
        }
    }
}
