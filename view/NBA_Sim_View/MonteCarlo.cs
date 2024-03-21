using RestSharp;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Security.AccessControl;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace NBA_Sim_View
{
    public partial class MonteCarlo : Form
    {
        FindGame homeScreen;
        private string gameDate = string.Empty;
        private string visitorTeam = string.Empty;
        private string visitorPts = string.Empty;
        private string homeTeam = string.Empty;     
        private string homePts = string.Empty;
        private string attendance = string.Empty;
        private string arena = string.Empty;
        private string gameType = string.Empty;
        private string epochs = string.Empty;
        private string season = string.Empty;
        private string dbHost = string.Empty;

        public MonteCarlo(FindGame window, string gameDate, string visitorTeam, string visitorPts, string homeTeam, 
            string homePts, string attendance, string arena, string gameType, string epochs, string season,
            string dbHost)
        {
            InitializeComponent();

            this.homeScreen = window;
            this.gameDate = gameDate;
            this.visitorTeam = visitorTeam;
            this.visitorPts = visitorPts;
            this.homeTeam = homeTeam;
            this.homePts = homePts;
            this.attendance = attendance;
            this.arena = arena;
            this.gameType = gameType;
            this.epochs = epochs;
            this.season = season;
            this.dbHost = dbHost;

            PopulateScoreboard();
            GraphSimulationData();         
        }

        public void GraphSimulationData()
        {
            //RestClient client = new RestClient("http://127.0.0.1:5000/monte_carlo/simulation");

            var options = new RestClientOptions($"http://127.0.0.1:5000/monte_carlo/simulation");
            options.MaxTimeout = 100000000;

            RestClient client = new RestClient(options);
            RestRequest request = new RestRequest();

            request.AddParameter("epochs", epochs);
            request.AddParameter("game_type", gameType);
            request.AddParameter("season", season);
            request.AddParameter("home", homeTeam);
            request.AddParameter("away", visitorTeam);
            request.AddParameter("db", dbHost);
            request.AddParameter("game_date", gameDate);

            try
            {
                RestResponse response = client.Get(request);

                if (response.IsSuccessful)
                {
                    Response res = client.Deserialize<Response>(response).Data;

                    if (res.Status == 200)
                    {
                        Image probDist = ConvertBase64ToImage(res.Image);
                        Image violinPlt = ConvertBase64ToImage(res.Image2);

                        pbHist.Image = probDist;
                        pbHist.Show();

                        pbViolin.Image = violinPlt;
                        pbViolin.Show();

                        SetStatValues(res.Message);
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

        private void SetStatValues(string message)
        {
            string[] stats = message.Split(',');
            tbWonHome.Text = stats[0] + "%";
            tbWonAway.Text = stats[1] + "%";
            tbModeHome.Text = stats[2];
            tbModeAway.Text = stats[3];
            tbWonHome.ReadOnly = true;
            tbWonAway.ReadOnly = true;
            tbModeHome.ReadOnly = true;
            tbModeAway.ReadOnly = true;
        }

        private Image ConvertBase64ToImage(string imageBase64)
        {
            byte[] imageData = Convert.FromBase64String(imageBase64);

            Image image;
            using (MemoryStream ms = new MemoryStream(imageData))
            {
                image = Image.FromStream(ms);
            }
            return image;
        }

        private void btnSelectGame_Click(object sender, EventArgs e)
        {
            this.Close();
            homeScreen.Show();
        }

        private void btnExit_Click(object sender, EventArgs e)
        {
            this.Close();
            homeScreen.Close();
        }
        
        private void PopulateScoreboard()
        {
            tbGameDate.Text = gameDate;
            tbHome.Text = homeTeam;
            tbHomePts.Text = homePts;
            tbAway.Text = visitorTeam;
            tbAwayPts.Text = visitorPts;
            lblAttendance.Text = attendance;
            lblArena.Text = arena;

            tbGameDate.ReadOnly = true;
            tbHome.ReadOnly = true;
            tbHomePts.ReadOnly = true;
            tbAway.ReadOnly = true;
            tbAwayPts.ReadOnly = true;
        }

    }
}
