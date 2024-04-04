namespace NBA_Sim_View
{
    partial class FindGame
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.panel1 = new System.Windows.Forms.Panel();
            this.tbEpochs = new System.Windows.Forms.TextBox();
            this.rbCustom = new System.Windows.Forms.RadioButton();
            this.btnGetGames = new System.Windows.Forms.Button();
            this.cbSeason = new System.Windows.Forms.ComboBox();
            this.cbAway = new System.Windows.Forms.ComboBox();
            this.tbDB = new System.Windows.Forms.TextBox();
            this.rbDefault = new System.Windows.Forms.RadioButton();
            this.lblEpochs = new System.Windows.Forms.Label();
            this.cbHome = new System.Windows.Forms.ComboBox();
            this.btnExit = new System.Windows.Forms.Button();
            this.lblGameSelector = new System.Windows.Forms.Label();
            this.dgvGetGames = new System.Windows.Forms.DataGridView();
            this.btnSelect = new System.Windows.Forms.Button();
            this.btnSelectGame = new System.Windows.Forms.Button();
            this.btnForceScrape = new System.Windows.Forms.Button();
            this.panel1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.dgvGetGames)).BeginInit();
            this.SuspendLayout();
            // 
            // panel1
            // 
            this.panel1.BackColor = System.Drawing.Color.LightSlateGray;
            this.panel1.Controls.Add(this.tbEpochs);
            this.panel1.Controls.Add(this.rbCustom);
            this.panel1.Controls.Add(this.btnGetGames);
            this.panel1.Controls.Add(this.cbSeason);
            this.panel1.Controls.Add(this.cbAway);
            this.panel1.Controls.Add(this.tbDB);
            this.panel1.Controls.Add(this.rbDefault);
            this.panel1.Controls.Add(this.lblEpochs);
            this.panel1.Controls.Add(this.cbHome);
            this.panel1.Location = new System.Drawing.Point(60, 109);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(902, 182);
            this.panel1.TabIndex = 0;
            // 
            // tbEpochs
            // 
            this.tbEpochs.ForeColor = System.Drawing.Color.DimGray;
            this.tbEpochs.Location = new System.Drawing.Point(597, 45);
            this.tbEpochs.Name = "tbEpochs";
            this.tbEpochs.Size = new System.Drawing.Size(125, 22);
            this.tbEpochs.TabIndex = 7;
            this.tbEpochs.Text = "10 000 simulations";
            this.tbEpochs.MouseClick += new System.Windows.Forms.MouseEventHandler(this.tbEpochs_MouseClick);
            // 
            // rbCustom
            // 
            this.rbCustom.AutoSize = true;
            this.rbCustom.ForeColor = System.Drawing.Color.Snow;
            this.rbCustom.Location = new System.Drawing.Point(379, 18);
            this.rbCustom.Name = "rbCustom";
            this.rbCustom.Size = new System.Drawing.Size(121, 20);
            this.rbCustom.TabIndex = 6;
            this.rbCustom.TabStop = true;
            this.rbCustom.Text = "Custom DB URI";
            this.rbCustom.UseVisualStyleBackColor = true;
            this.rbCustom.CheckedChanged += new System.EventHandler(this.rbCustom_CheckedChanged);
            // 
            // btnGetGames
            // 
            this.btnGetGames.BackColor = System.Drawing.Color.Tomato;
            this.btnGetGames.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Center;
            this.btnGetGames.FlatAppearance.BorderSize = 0;
            this.btnGetGames.FlatAppearance.MouseDownBackColor = System.Drawing.Color.IndianRed;
            this.btnGetGames.FlatAppearance.MouseOverBackColor = System.Drawing.Color.IndianRed;
            this.btnGetGames.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.btnGetGames.Font = new System.Drawing.Font("Cascadia Code SemiBold", 9F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnGetGames.ForeColor = System.Drawing.Color.Snow;
            this.btnGetGames.Location = new System.Drawing.Point(327, 129);
            this.btnGetGames.Name = "btnGetGames";
            this.btnGetGames.Size = new System.Drawing.Size(240, 34);
            this.btnGetGames.TabIndex = 3;
            this.btnGetGames.Text = "Get Games";
            this.btnGetGames.UseVisualStyleBackColor = false;
            this.btnGetGames.Click += new System.EventHandler(this.btnGetGames_Click);
            // 
            // cbSeason
            // 
            this.cbSeason.ForeColor = System.Drawing.Color.DimGray;
            this.cbSeason.FormattingEnabled = true;
            this.cbSeason.Items.AddRange(new object[] {
            "1995-1996",
            "1994-1995",
            "1993-1994",
            "1992-1993",
            "1991-1992"});
            this.cbSeason.Location = new System.Drawing.Point(561, 86);
            this.cbSeason.Name = "cbSeason";
            this.cbSeason.Size = new System.Drawing.Size(190, 24);
            this.cbSeason.TabIndex = 5;
            this.cbSeason.Text = "-- Season --";
            // 
            // cbAway
            // 
            this.cbAway.ForeColor = System.Drawing.Color.DimGray;
            this.cbAway.FormattingEnabled = true;
            this.cbAway.Items.AddRange(new object[] {
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
            "Utah Jazz"});
            this.cbAway.Location = new System.Drawing.Point(353, 86);
            this.cbAway.Name = "cbAway";
            this.cbAway.Size = new System.Drawing.Size(190, 24);
            this.cbAway.TabIndex = 4;
            this.cbAway.Text = "-- Away Team --";
            // 
            // tbDB
            // 
            this.tbDB.ForeColor = System.Drawing.Color.DimGray;
            this.tbDB.Location = new System.Drawing.Point(145, 45);
            this.tbDB.Name = "tbDB";
            this.tbDB.Size = new System.Drawing.Size(398, 22);
            this.tbDB.TabIndex = 3;
            this.tbDB.Text = "URL connection str";
            this.tbDB.MouseClick += new System.Windows.Forms.MouseEventHandler(this.tbDB_MouseClick);
            // 
            // rbDefault
            // 
            this.rbDefault.AutoSize = true;
            this.rbDefault.ForeColor = System.Drawing.Color.Snow;
            this.rbDefault.Location = new System.Drawing.Point(184, 19);
            this.rbDefault.Name = "rbDefault";
            this.rbDefault.Size = new System.Drawing.Size(120, 20);
            this.rbDefault.TabIndex = 1;
            this.rbDefault.TabStop = true;
            this.rbDefault.Text = "Use Default DB";
            this.rbDefault.UseVisualStyleBackColor = true;
            this.rbDefault.CheckedChanged += new System.EventHandler(this.rbDefault_CheckedChanged);
            // 
            // lblEpochs
            // 
            this.lblEpochs.AutoSize = true;
            this.lblEpochs.ForeColor = System.Drawing.Color.Snow;
            this.lblEpochs.Location = new System.Drawing.Point(594, 19);
            this.lblEpochs.Name = "lblEpochs";
            this.lblEpochs.Size = new System.Drawing.Size(128, 16);
            this.lblEpochs.TabIndex = 2;
            this.lblEpochs.Text = "Monte Carlo Epochs";
            // 
            // cbHome
            // 
            this.cbHome.ForeColor = System.Drawing.Color.DimGray;
            this.cbHome.FormattingEnabled = true;
            this.cbHome.Items.AddRange(new object[] {
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
            "Utah Jazz"});
            this.cbHome.Location = new System.Drawing.Point(145, 86);
            this.cbHome.Name = "cbHome";
            this.cbHome.Size = new System.Drawing.Size(190, 24);
            this.cbHome.TabIndex = 0;
            this.cbHome.Text = "-- Home Team --";
            // 
            // btnExit
            // 
            this.btnExit.BackColor = System.Drawing.Color.Tomato;
            this.btnExit.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Center;
            this.btnExit.FlatAppearance.BorderSize = 0;
            this.btnExit.FlatAppearance.MouseDownBackColor = System.Drawing.Color.IndianRed;
            this.btnExit.FlatAppearance.MouseOverBackColor = System.Drawing.Color.IndianRed;
            this.btnExit.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.btnExit.Font = new System.Drawing.Font("Cascadia Code", 10.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnExit.ForeColor = System.Drawing.Color.Black;
            this.btnExit.Location = new System.Drawing.Point(968, 12);
            this.btnExit.Name = "btnExit";
            this.btnExit.Size = new System.Drawing.Size(42, 34);
            this.btnExit.TabIndex = 0;
            this.btnExit.Text = "X";
            this.btnExit.UseVisualStyleBackColor = false;
            this.btnExit.Click += new System.EventHandler(this.btnExit_Click);
            // 
            // lblGameSelector
            // 
            this.lblGameSelector.AutoSize = true;
            this.lblGameSelector.Font = new System.Drawing.Font("Microsoft Tai Le", 19.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblGameSelector.ForeColor = System.Drawing.Color.LightSlateGray;
            this.lblGameSelector.Location = new System.Drawing.Point(386, 80);
            this.lblGameSelector.Name = "lblGameSelector";
            this.lblGameSelector.Size = new System.Drawing.Size(243, 43);
            this.lblGameSelector.TabIndex = 2;
            this.lblGameSelector.Text = "Game Selector";
            // 
            // dgvGetGames
            // 
            this.dgvGetGames.BackgroundColor = System.Drawing.SystemColors.Control;
            this.dgvGetGames.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.dgvGetGames.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dgvGetGames.Location = new System.Drawing.Point(60, 314);
            this.dgvGetGames.Name = "dgvGetGames";
            this.dgvGetGames.RowHeadersWidth = 51;
            this.dgvGetGames.RowTemplate.Height = 24;
            this.dgvGetGames.SelectionMode = System.Windows.Forms.DataGridViewSelectionMode.FullRowSelect;
            this.dgvGetGames.Size = new System.Drawing.Size(902, 180);
            this.dgvGetGames.TabIndex = 3;
            this.dgvGetGames.CellContentClick += new System.Windows.Forms.DataGridViewCellEventHandler(this.dgvGetGames_CellContentClick);
            // 
            // btnSelect
            // 
            this.btnSelect.BackColor = System.Drawing.Color.Tomato;
            this.btnSelect.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Center;
            this.btnSelect.FlatAppearance.BorderSize = 0;
            this.btnSelect.FlatAppearance.MouseDownBackColor = System.Drawing.Color.IndianRed;
            this.btnSelect.FlatAppearance.MouseOverBackColor = System.Drawing.Color.IndianRed;
            this.btnSelect.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.btnSelect.Font = new System.Drawing.Font("Cascadia Code SemiBold", 9F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnSelect.ForeColor = System.Drawing.Color.Snow;
            this.btnSelect.Location = new System.Drawing.Point(529, 519);
            this.btnSelect.Name = "btnSelect";
            this.btnSelect.Size = new System.Drawing.Size(240, 34);
            this.btnSelect.TabIndex = 7;
            this.btnSelect.Text = "Simulate";
            this.btnSelect.UseVisualStyleBackColor = false;
            this.btnSelect.Click += new System.EventHandler(this.btnInitialize_Click);
            // 
            // btnSelectGame
            // 
            this.btnSelectGame.BackColor = System.Drawing.Color.Tomato;
            this.btnSelectGame.BackgroundImage = global::NBA_Sim_View.Properties.Resources.home;
            this.btnSelectGame.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Center;
            this.btnSelectGame.FlatAppearance.BorderSize = 0;
            this.btnSelectGame.FlatAppearance.MouseDownBackColor = System.Drawing.Color.IndianRed;
            this.btnSelectGame.FlatAppearance.MouseOverBackColor = System.Drawing.Color.IndianRed;
            this.btnSelectGame.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.btnSelectGame.Font = new System.Drawing.Font("Calibri", 10.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnSelectGame.ForeColor = System.Drawing.Color.SeaShell;
            this.btnSelectGame.Location = new System.Drawing.Point(920, 12);
            this.btnSelectGame.Name = "btnSelectGame";
            this.btnSelectGame.Size = new System.Drawing.Size(42, 34);
            this.btnSelectGame.TabIndex = 1;
            this.btnSelectGame.UseVisualStyleBackColor = false;
            this.btnSelectGame.Click += new System.EventHandler(this.btnSelectGame_Click);
            // 
            // btnForceScrape
            // 
            this.btnForceScrape.BackColor = System.Drawing.SystemColors.Control;
            this.btnForceScrape.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Center;
            this.btnForceScrape.FlatAppearance.BorderSize = 0;
            this.btnForceScrape.FlatAppearance.MouseDownBackColor = System.Drawing.Color.IndianRed;
            this.btnForceScrape.FlatAppearance.MouseOverBackColor = System.Drawing.Color.IndianRed;
            this.btnForceScrape.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.btnForceScrape.Font = new System.Drawing.Font("Cascadia Code SemiBold", 9F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnForceScrape.ForeColor = System.Drawing.Color.LightSlateGray;
            this.btnForceScrape.Location = new System.Drawing.Point(257, 519);
            this.btnForceScrape.Name = "btnForceScrape";
            this.btnForceScrape.Size = new System.Drawing.Size(240, 34);
            this.btnForceScrape.TabIndex = 14;
            this.btnForceScrape.Text = "Forced Scrape";
            this.btnForceScrape.UseVisualStyleBackColor = false;
            this.btnForceScrape.Click += new System.EventHandler(this.btnForceScrape_Click);
            // 
            // FindGame
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.Control;
            this.ClientSize = new System.Drawing.Size(1022, 605);
            this.Controls.Add(this.btnForceScrape);
            this.Controls.Add(this.btnSelect);
            this.Controls.Add(this.dgvGetGames);
            this.Controls.Add(this.btnSelectGame);
            this.Controls.Add(this.panel1);
            this.Controls.Add(this.btnExit);
            this.Controls.Add(this.lblGameSelector);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.Name = "FindGame";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Monte Carlo";
            this.panel1.ResumeLayout(false);
            this.panel1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.dgvGetGames)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.Button btnExit;
        private System.Windows.Forms.Button btnSelectGame;
        private System.Windows.Forms.Label lblEpochs;
        private System.Windows.Forms.RadioButton rbDefault;
        private System.Windows.Forms.ComboBox cbHome;
        private System.Windows.Forms.TextBox tbDB;
        private System.Windows.Forms.ComboBox cbAway;
        private System.Windows.Forms.ComboBox cbSeason;
        private System.Windows.Forms.Label lblGameSelector;
        private System.Windows.Forms.Button btnGetGames;
        private System.Windows.Forms.RadioButton rbCustom;
        private System.Windows.Forms.DataGridView dgvGetGames;
        private System.Windows.Forms.Button btnSelect;
        private System.Windows.Forms.TextBox tbEpochs;
        private System.Windows.Forms.Button btnForceScrape;
    }
}

