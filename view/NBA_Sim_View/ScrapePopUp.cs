using RestSharp;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Security.AccessControl;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using static System.Windows.Forms.VisualStyles.VisualStyleElement;

namespace NBA_Sim_View
{
    public partial class ScrapePopUp : Form
    {
        private FindGame homeScreen;
        private string proxyList = null;
        private bool checkProxies = false;
        private string missingStats = string.Empty;
        private string gameDate = string.Empty;
        private string visitorTeam = string.Empty;
        private string visitorPts = string.Empty;
        private string homeTeam = string.Empty;
        private string homePts = string.Empty;
        private string attendance = string.Empty;
        private string arena = string.Empty;
        private string gameType = string.Empty;
        private string epochs = string.Empty;
        private string dbHost = string.Empty;
        private string season = string.Empty;
        private bool forced = false;

        private string scrapeMethod = "requests_scrape";
        List<RadioButton> radioButtons;

        public ScrapePopUp(FindGame window, string missingStats, string gameDate, string visitorTeam, string visitorPts, 
            string homeTeam, string homePts, string attendance, string arena, string gameType, string epochs,
            string dbHost, string season)
        {
            InitializeComponent();

            homeScreen = window;
            this.missingStats = missingStats;
            radioButtons = new List<RadioButton> { rbRequests, rbFirefox, rbChrome, rbRequestsProxy, rbFirefoxProxy, 
                rbChromeProxy };
            this.gameDate = gameDate;
            this.visitorTeam = visitorTeam;
            this.visitorPts = visitorPts;
            this.homeTeam = homeTeam;
            this.homePts = homePts;
            this.attendance = attendance;
            this.arena = arena;
            this.gameType = gameType;
            this.epochs = epochs;
            this.dbHost = dbHost;
            this.season = season;

            rbRequests.Checked = true;
            WireUpEventHandlers();
            tbMissing.Text = missingStats;
        }

        private void btnScrape_Click(object sender, EventArgs e)
        {
            if (checkProxies)
            {
                if (rbRequests.Checked || rbFirefox.Checked || rbChrome.Checked)
                {
                    lblCheckProxies_Click(sender, e);  
                }
            }

            btnScrape.Enabled = false;                 
            btnScrape.Text = "Scrape in Progress";
            btnScrape.ForeColor = Color.Goldenrod;

            if (missingStats == "FORCED")
            {
                forced = true;
            }
            Scrape();
        }

        public void Scrape()
        {
            var options = new RestClientOptions($"http://127.0.0.1:5000/monte_carlo/season_data");
            options.MaxTimeout = 500000;

            RestClient scrapeClient = new RestClient(options);
            RestRequest request = new RestRequest();

            request.AddQueryParameter("check_proxies", checkProxies);
            request.AddQueryParameter("proxy_list", proxyList);
            request.AddQueryParameter("scrape_method", scrapeMethod);
            request.AddQueryParameter("forced", forced);
            request.AddParameter("season", season);
            request.AddParameter("home", homeTeam);
            request.AddParameter("away", visitorTeam);
            request.AddParameter("db", dbHost);

            try
            {
                RestResponse response = scrapeClient.Get(request);
                if (response.IsSuccessful)
                {
                    Response res = scrapeClient.Deserialize<Response>(response).Data;

                    if (res.Status == 200 && res.Message == "")
                    {
                        MonteCarlo mc = new MonteCarlo(homeScreen, gameDate, visitorTeam, visitorPts, homeTeam, homePts, attendance,
                            arena, gameType, epochs, season, dbHost);
                        mc.Show();
                        this.Close();
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

        private void btnCancel_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void btnCustomProxyList_Click(object sender, EventArgs e)
        {
            using (OpenFileDialog file = new OpenFileDialog())
            {
                file.Filter = "CSV Files (*.csv)|*.csv";
                file.FilterIndex = 1;
                file.RestoreDirectory = true;

                DialogResult result = file.ShowDialog();
                if (result == DialogResult.OK)
                {
                    proxyList = file.FileName;
                }
            }
            btnCustomProxyList.ForeColor = Color.Goldenrod;
        }

        private void lblCheckProxies_Click(object sender, EventArgs e)
        {
            if (checkProxies)
            {
                lblCheckProxies.ForeColor = Color.Snow;
                checkProxies = false;
            }
            else
            {
                lblCheckProxies.ForeColor = Color.Goldenrod;
                checkProxies = true;
            }
        }

        // radio button change + name string change for scrape method in REST
        private void WireUpEventHandlers()
        {
            foreach (RadioButton radioButton in radioButtons)
            {
                radioButton.CheckedChanged += UpdateScrapeMethod;
            }
        }

        private void UpdateScrapeMethod(object sender, EventArgs e)
        {
            RadioButton selectedRadioButton = radioButtons.FirstOrDefault(rb => rb.Checked);
            if (selectedRadioButton != null)
            {
                scrapeMethod = selectedRadioButton.Text.Replace(' ', '_').ToLower() + "_scrape";
            }
        }


    }
}
