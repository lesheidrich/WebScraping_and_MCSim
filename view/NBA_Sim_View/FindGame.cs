using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Configuration;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Net.NetworkInformation;
using System.Runtime.Serialization;
using System.Text;
using System.Text.Json;
using System.Text.Json.Serialization;
using System.Threading.Tasks;
using System.Windows.Forms;
using RestSharp;

namespace NBA_Sim_View
{
    public partial class FindGame : Form
    {
        private string dbHost = string.Empty;
        private string season = string.Empty;         // e.g.: '1991-1992'
        private string gameDate = string.Empty;
        private string visitorTeam = string.Empty;
        private string visitorPts = string.Empty;    
        private string homeTeam = string.Empty;       // e.g.: 'Chicago Bulls'
        private string homePts = string.Empty;
        private string attendance = string.Empty;
        private string arena = string.Empty;
        private string gameType = string.Empty;
        private string epochs = string.Empty;

        public FindGame()
        {
            InitializeComponent();

            InitializedgvGetGames();
            InitialFormSettings();
            rbDefault.Checked = true;
            dgvGetGames.Visible = false;
        }


        // gets game info for dgv
        private void btnGetGames_Click(object sender, EventArgs e)
        {
            // input check
            if (cbHome.Text == "-- Home Team --" || cbAway.Text == "-- Away Team --" || cbSeason.Text == "-- Season --" ||
                (rbCustom.Checked && tbDB.Text == ""))
            {
                string content = "Please complete selection process!";
                MessageBox.Show(content, "SETUP ERROR!", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            if (cbHome.Text == cbAway.Text)
            {
                string content = $"Teams cannot play themselves!\nHome = Away ({cbHome.Text})";
                MessageBox.Show(content, "SETUP ERROR!", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            epochs = tbEpochs.Text;
            if (epochs == "" || epochs is null || !double.TryParse(epochs, out _))
            {
                string content = "Epoch number must be a numeric value!";
                MessageBox.Show(content, "EPOCH ERROR!", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            // vals assgn to class attribs
            dgvGetGames.Rows.Clear();
            PopulateAttributes();

            RestClient gamesClient = new RestClient("http://127.0.0.1:5000/monte_carlo/game_data");
            RestRequest request = new RestRequest();
            request.AddQueryParameter("home", homeTeam);
            request.AddQueryParameter("away", visitorTeam);
            request.AddQueryParameter("season", season);
            request.AddQueryParameter("dbURI", dbHost);

            try
            {
                RestResponse response = gamesClient.Post(request);

                if (response.IsSuccessful)
                {
                    Response res = gamesClient.Deserialize<Response>(response).Data;

                    try
                    {
                        List<GameData> gamesList = JsonSerializer.Deserialize<List<GameData>>(res.Message);

                        if (gamesList.Count == 0)
                        {
                            MessageBox.Show("Teams did not play each other in season!", "DATA WARNING",
                                MessageBoxButtons.OK, MessageBoxIcon.Warning);
                        }

                        dgvGetGames.Visible = true;
                        btnSelect.Visible = true;
                        btnForceScrape.Visible = true;
                        foreach (var game in gamesList)
                        {
                            dgvGetGames.Rows.Add(
                                game.id,
                                game.date,
                                game.home_team,
                                game.home_pts,
                                game.visitor_team,
                                game.visitor_pts,
                                game.attendance,
                                game.arena,
                                game.game_type
                            );
                        }
                    }
                    catch (Exception ex)
                    {
                        MessageBox.Show($"Failed to deserealize games list!\n{ex.Message}", "JSON ERROR",
                            MessageBoxButtons.OK, MessageBoxIcon.Error);
                    }
                }
                else
                {
                    MessageBox.Show("Failed to make request! Status code: " + response.StatusCode, "REQUEST ERROR",
                        MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }

            // save content from selected first row
            SaveGameContentsFromRows(0);
        }

        private void btnInitialize_Click(object sender, EventArgs e)
        {
            // gets ok to proceed if in db, else str team name (e.g.: 'CHI') that is missing
            RestClient cl = new RestClient("http://127.0.0.1:5000/monte_carlo/team_in_db");
            RestRequest request = new RestRequest();

            request.AddParameter("season", season);
            request.AddParameter("home", homeTeam);
            request.AddParameter("away", visitorTeam);
            request.AddParameter("db", dbHost);

            try
            {
                RestResponse response = cl.Get(request);

                if (response.IsSuccessful)
                {
                    Response res = cl.Deserialize<Response>(response).Data;

                    if (res.Status == 200 && res.Message == "")
                    {
                        MonteCarlo mc = new MonteCarlo(this, gameDate, visitorTeam, visitorPts, homeTeam, homePts, attendance,
                         arena, gameType, epochs, season, dbHost);
                        mc.Show();
                        this.Hide();
                    }
                    else if (res.Status == 204 && res.Message.Length > 1)
                    {
                        ScrapePopUp sp = new ScrapePopUp(this, res.Message, gameDate, visitorTeam, visitorPts, homeTeam, homePts, attendance,
                         arena, gameType, epochs, dbHost, season);
                        sp.Show();
                    }
                    else
                    {
                        MessageBox.Show("Response returned error! Status code: " + res.Status, "RESPONSE ERROR",
                            MessageBoxButtons.OK, MessageBoxIcon.Error);
                    }
                }
                else
                {
                    MessageBox.Show("Failed to make request! Status code: " + response.StatusCode, "REQUEST ERROR",
                        MessageBoxButtons.OK, MessageBoxIcon.Error);
                }

            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void btnExit_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void rbDefault_CheckedChanged(object sender, EventArgs e)
        {
            tbDB.Enabled = false;
            dbHost = string.Empty;
            tbDB.Text = "URL connection str";
        }

        private void rbCustom_CheckedChanged(object sender, EventArgs e)
        {
            tbDB.Enabled = true;
            tbDB.Text = "URL connection str";
        }

        private void tbDB_MouseClick(object sender, MouseEventArgs e)
        {
            tbDB.Text = string.Empty;
        }

        private void tbEpochs_MouseClick(object sender, MouseEventArgs e)
        {
            tbEpochs.Text = string.Empty;
        }

        private void btnSelectGame_Click(object sender, EventArgs e)
        {
            InitialFormSettings();
        }

        private void InitialFormSettings() 
        {
            rbDefault.Checked = true;
            tbDB.Text = "URL connection str";
            cbHome.Text = "-- Home Team --";
            cbAway.Text = "-- Away Team --";
            cbSeason.Text = "-- Season --";
            dgvGetGames.Visible = false;
            btnSelect.Visible = false;
            btnForceScrape.Visible = false;
        }

        private void InitializedgvGetGames()
        {
            dgvGetGames.AutoSizeColumnsMode = DataGridViewAutoSizeColumnsMode.AllCells;
            dgvGetGames.Columns.Add("id", "ID");
            dgvGetGames.Columns.Add("date", "Date");

            dgvGetGames.Columns.Add("home_team", "Home Team");
            dgvGetGames.Columns.Add("home_pts", "Home Points");
            dgvGetGames.Columns.Add("visitor_team", "Visitor Team");
            dgvGetGames.Columns.Add("visitor_pts", "Visitor Points");
            dgvGetGames.Columns.Add("attendance", "Attendance");
            dgvGetGames.Columns.Add("arena", "Arena");
            dgvGetGames.Columns.Add("game_type", "Game Type");
        }

        private void dgvGetGames_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {
            // gets content from cell click
            SaveGameContentsFromRows(e.RowIndex);
            //if (e.RowIndex >= 0 && e.RowIndex < dgvGetGames.Rows.Count)
            //{
            //    dgvGetGames.Rows[e.RowIndex].Selected = true;
            //    DataGridViewRow row = dgvGetGames.Rows[e.RowIndex];

            //    gameDate = row.Cells["date"].Value.ToString();
            //    visitorTeam = row.Cells["visitor_team"].Value.ToString();
            //    visitorPts = row.Cells["visitor_pts"].Value.ToString();
            //    homeTeam = row.Cells["home_team"].Value.ToString();
            //    homePts = row.Cells["home_pts"].Value.ToString();
            //    attendance = row.Cells["attendance"].Value.ToString();
            //    arena = row.Cells["arena"].Value.ToString();
            //    gameType = row.Cells["game_type"].Value.ToString();
            //}
        }

        private void SaveGameContentsFromRows(int index)
        {
            // gets content from cell click
            if (index >= 0 && index < dgvGetGames.Rows.Count)
            {
                //dgvGetGames.Rows[index].Selected = true;
                DataGridViewRow row = dgvGetGames.Rows[index];

                gameDate = row.Cells["date"].Value.ToString();
                visitorTeam = row.Cells["visitor_team"].Value.ToString();
                visitorPts = row.Cells["visitor_pts"].Value.ToString();
                homeTeam = row.Cells["home_team"].Value.ToString();
                homePts = row.Cells["home_pts"].Value.ToString();
                attendance = row.Cells["attendance"].Value.ToString();
                arena = row.Cells["arena"].Value.ToString();
                gameType = row.Cells["game_type"].Value.ToString();
            }
        }

        private void PopulateAttributes()
        {
            homeTeam = cbHome.Text;
            visitorTeam = cbAway.Text;
            season = cbSeason.Text;
            dbHost = tbDB.Text;

            if (rbDefault.Checked)
            {
                dbHost = ProjectSecrets.DEFAULT_URI;
            }
        }

        private void btnForceScrape_Click(object sender, EventArgs e)
        {
            ScrapePopUp sp = new ScrapePopUp(this, "FORCED", gameDate, visitorTeam, visitorPts, homeTeam, homePts, attendance,
                arena, gameType, epochs, dbHost, season);
            sp.Show();
        }
    }
}
