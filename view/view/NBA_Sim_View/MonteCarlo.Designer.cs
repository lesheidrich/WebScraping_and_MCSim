namespace NBA_Sim_View
{
    partial class MonteCarlo
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
            this.pbHist = new System.Windows.Forms.PictureBox();
            this.btnSelectGame = new System.Windows.Forms.Button();
            this.btnExit = new System.Windows.Forms.Button();
            this.panel1 = new System.Windows.Forms.Panel();
            this.lblArena = new System.Windows.Forms.Label();
            this.lblAttendance = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.tbAwayPts = new System.Windows.Forms.TextBox();
            this.tbHomePts = new System.Windows.Forms.TextBox();
            this.tbGameDate = new System.Windows.Forms.TextBox();
            this.tbAway = new System.Windows.Forms.TextBox();
            this.tbHome = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.lblDatabase = new System.Windows.Forms.Label();
            this.pbViolin = new System.Windows.Forms.PictureBox();
            this.tbWonAway = new System.Windows.Forms.TextBox();
            this.tbWonHome = new System.Windows.Forms.TextBox();
            this.tbModeAway = new System.Windows.Forms.TextBox();
            this.tbModeHome = new System.Windows.Forms.TextBox();
            this.label4 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.label6 = new System.Windows.Forms.Label();
            this.label7 = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.pbHist)).BeginInit();
            this.panel1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pbViolin)).BeginInit();
            this.SuspendLayout();
            // 
            // pbHist
            // 
            this.pbHist.Location = new System.Drawing.Point(12, 178);
            this.pbHist.Name = "pbHist";
            this.pbHist.Size = new System.Drawing.Size(550, 399);
            this.pbHist.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pbHist.TabIndex = 0;
            this.pbHist.TabStop = false;
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
            this.btnSelectGame.TabIndex = 3;
            this.btnSelectGame.UseVisualStyleBackColor = false;
            this.btnSelectGame.Click += new System.EventHandler(this.btnSelectGame_Click);
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
            this.btnExit.TabIndex = 2;
            this.btnExit.Text = "X";
            this.btnExit.UseVisualStyleBackColor = false;
            this.btnExit.Click += new System.EventHandler(this.btnExit_Click);
            // 
            // panel1
            // 
            this.panel1.BackColor = System.Drawing.Color.LightSlateGray;
            this.panel1.Controls.Add(this.lblArena);
            this.panel1.Controls.Add(this.lblAttendance);
            this.panel1.Controls.Add(this.label3);
            this.panel1.Controls.Add(this.label2);
            this.panel1.Controls.Add(this.tbAwayPts);
            this.panel1.Controls.Add(this.tbHomePts);
            this.panel1.Controls.Add(this.tbGameDate);
            this.panel1.Controls.Add(this.tbAway);
            this.panel1.Controls.Add(this.tbHome);
            this.panel1.Controls.Add(this.label1);
            this.panel1.Controls.Add(this.lblDatabase);
            this.panel1.Location = new System.Drawing.Point(568, 55);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(442, 182);
            this.panel1.TabIndex = 4;
            // 
            // lblArena
            // 
            this.lblArena.AutoSize = true;
            this.lblArena.ForeColor = System.Drawing.Color.Snow;
            this.lblArena.Location = new System.Drawing.Point(102, 157);
            this.lblArena.Name = "lblArena";
            this.lblArena.Size = new System.Drawing.Size(40, 16);
            this.lblArena.TabIndex = 13;
            this.lblArena.Text = "None";
            // 
            // lblAttendance
            // 
            this.lblAttendance.AutoSize = true;
            this.lblAttendance.ForeColor = System.Drawing.Color.Snow;
            this.lblAttendance.Location = new System.Drawing.Point(102, 138);
            this.lblAttendance.Name = "lblAttendance";
            this.lblAttendance.Size = new System.Drawing.Size(14, 16);
            this.lblAttendance.TabIndex = 12;
            this.lblAttendance.Text = "0";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.ForeColor = System.Drawing.Color.Snow;
            this.label3.Location = new System.Drawing.Point(13, 157);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(46, 16);
            this.label3.TabIndex = 11;
            this.label3.Text = "Arena:";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.ForeColor = System.Drawing.Color.Snow;
            this.label2.Location = new System.Drawing.Point(13, 138);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(78, 16);
            this.label2.TabIndex = 10;
            this.label2.Text = "Attendance:";
            // 
            // tbAwayPts
            // 
            this.tbAwayPts.Font = new System.Drawing.Font("Impact", 16.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.tbAwayPts.Location = new System.Drawing.Point(224, 93);
            this.tbAwayPts.Name = "tbAwayPts";
            this.tbAwayPts.Size = new System.Drawing.Size(202, 40);
            this.tbAwayPts.TabIndex = 9;
            this.tbAwayPts.Text = "100";
            this.tbAwayPts.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // tbHomePts
            // 
            this.tbHomePts.Font = new System.Drawing.Font("Impact", 16.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.tbHomePts.Location = new System.Drawing.Point(16, 93);
            this.tbHomePts.Name = "tbHomePts";
            this.tbHomePts.Size = new System.Drawing.Size(202, 40);
            this.tbHomePts.TabIndex = 8;
            this.tbHomePts.Text = "100";
            this.tbHomePts.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // tbGameDate
            // 
            this.tbGameDate.BackColor = System.Drawing.Color.LightSlateGray;
            this.tbGameDate.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.tbGameDate.Font = new System.Drawing.Font("Lucida Console", 7F);
            this.tbGameDate.Location = new System.Drawing.Point(165, 3);
            this.tbGameDate.Name = "tbGameDate";
            this.tbGameDate.Size = new System.Drawing.Size(106, 12);
            this.tbGameDate.TabIndex = 7;
            this.tbGameDate.Text = "1991-04-15";
            this.tbGameDate.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // tbAway
            // 
            this.tbAway.Font = new System.Drawing.Font("HoloLens MDL2 Assets", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.tbAway.Location = new System.Drawing.Point(224, 57);
            this.tbAway.Name = "tbAway";
            this.tbAway.Size = new System.Drawing.Size(202, 27);
            this.tbAway.TabIndex = 6;
            this.tbAway.Text = "awaay";
            this.tbAway.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // tbHome
            // 
            this.tbHome.Font = new System.Drawing.Font("HoloLens MDL2 Assets", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.tbHome.Location = new System.Drawing.Point(16, 57);
            this.tbHome.Name = "tbHome";
            this.tbHome.Size = new System.Drawing.Size(202, 27);
            this.tbHome.TabIndex = 5;
            this.tbHome.Text = "home";
            this.tbHome.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Impact", 16.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.ForeColor = System.Drawing.Color.Snow;
            this.label1.Location = new System.Drawing.Point(288, 19);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(75, 35);
            this.label1.TabIndex = 4;
            this.label1.Text = "AWAY";
            // 
            // lblDatabase
            // 
            this.lblDatabase.AutoSize = true;
            this.lblDatabase.Font = new System.Drawing.Font("Impact", 16.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblDatabase.ForeColor = System.Drawing.Color.Snow;
            this.lblDatabase.Location = new System.Drawing.Point(79, 19);
            this.lblDatabase.Name = "lblDatabase";
            this.lblDatabase.Size = new System.Drawing.Size(78, 35);
            this.lblDatabase.TabIndex = 3;
            this.lblDatabase.Text = "HOME";
            // 
            // pbViolin
            // 
            this.pbViolin.Location = new System.Drawing.Point(568, 243);
            this.pbViolin.Name = "pbViolin";
            this.pbViolin.Size = new System.Drawing.Size(442, 334);
            this.pbViolin.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pbViolin.TabIndex = 5;
            this.pbViolin.TabStop = false;
            // 
            // tbWonAway
            // 
            this.tbWonAway.BackColor = System.Drawing.Color.LightSlateGray;
            this.tbWonAway.Font = new System.Drawing.Font("Impact", 16.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.tbWonAway.ForeColor = System.Drawing.Color.Snow;
            this.tbWonAway.Location = new System.Drawing.Point(287, 132);
            this.tbWonAway.Name = "tbWonAway";
            this.tbWonAway.Size = new System.Drawing.Size(202, 40);
            this.tbWonAway.TabIndex = 15;
            this.tbWonAway.Text = "35%";
            this.tbWonAway.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // tbWonHome
            // 
            this.tbWonHome.BackColor = System.Drawing.Color.LightSlateGray;
            this.tbWonHome.Font = new System.Drawing.Font("Impact", 16.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.tbWonHome.ForeColor = System.Drawing.Color.Snow;
            this.tbWonHome.Location = new System.Drawing.Point(79, 132);
            this.tbWonHome.Name = "tbWonHome";
            this.tbWonHome.Size = new System.Drawing.Size(202, 40);
            this.tbWonHome.TabIndex = 14;
            this.tbWonHome.Text = "65%";
            this.tbWonHome.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // tbModeAway
            // 
            this.tbModeAway.BackColor = System.Drawing.Color.LightSlateGray;
            this.tbModeAway.Font = new System.Drawing.Font("HoloLens MDL2 Assets", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.tbModeAway.ForeColor = System.Drawing.Color.Snow;
            this.tbModeAway.Location = new System.Drawing.Point(287, 96);
            this.tbModeAway.Name = "tbModeAway";
            this.tbModeAway.Size = new System.Drawing.Size(202, 27);
            this.tbModeAway.TabIndex = 13;
            this.tbModeAway.Text = "100";
            this.tbModeAway.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // tbModeHome
            // 
            this.tbModeHome.BackColor = System.Drawing.Color.LightSlateGray;
            this.tbModeHome.Font = new System.Drawing.Font("HoloLens MDL2 Assets", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.tbModeHome.ForeColor = System.Drawing.Color.Snow;
            this.tbModeHome.Location = new System.Drawing.Point(79, 96);
            this.tbModeHome.Name = "tbModeHome";
            this.tbModeHome.Size = new System.Drawing.Size(202, 27);
            this.tbModeHome.TabIndex = 12;
            this.tbModeHome.Text = "110";
            this.tbModeHome.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Font = new System.Drawing.Font("Impact", 16.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label4.ForeColor = System.Drawing.Color.LightSlateGray;
            this.label4.Location = new System.Drawing.Point(351, 58);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(75, 35);
            this.label4.TabIndex = 11;
            this.label4.Text = "AWAY";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Font = new System.Drawing.Font("Impact", 16.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label5.ForeColor = System.Drawing.Color.LightSlateGray;
            this.label5.Location = new System.Drawing.Point(142, 58);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(78, 35);
            this.label5.TabIndex = 10;
            this.label5.Text = "HOME";
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Font = new System.Drawing.Font("HoloLens MDL2 Assets", 10.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label6.ForeColor = System.Drawing.Color.LightSlateGray;
            this.label6.Location = new System.Drawing.Point(12, 99);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(49, 17);
            this.label6.TabIndex = 14;
            this.label6.Text = "MODE";
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Font = new System.Drawing.Font("HoloLens MDL2 Assets", 10.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label7.ForeColor = System.Drawing.Color.LightSlateGray;
            this.label7.Location = new System.Drawing.Point(13, 141);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(40, 17);
            this.label7.TabIndex = 16;
            this.label7.Text = "WON";
            // 
            // MonteCarlo
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1022, 605);
            this.Controls.Add(this.label7);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.tbWonAway);
            this.Controls.Add(this.tbWonHome);
            this.Controls.Add(this.tbModeAway);
            this.Controls.Add(this.tbModeHome);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.pbViolin);
            this.Controls.Add(this.panel1);
            this.Controls.Add(this.btnSelectGame);
            this.Controls.Add(this.btnExit);
            this.Controls.Add(this.pbHist);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.Name = "MonteCarlo";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Simulation";
            ((System.ComponentModel.ISupportInitialize)(this.pbHist)).EndInit();
            this.panel1.ResumeLayout(false);
            this.panel1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pbViolin)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox pbHist;
        private System.Windows.Forms.Button btnSelectGame;
        private System.Windows.Forms.Button btnExit;
        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.Label lblDatabase;
        private System.Windows.Forms.TextBox tbHome;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox tbAway;
        private System.Windows.Forms.TextBox tbAwayPts;
        private System.Windows.Forms.TextBox tbHomePts;
        private System.Windows.Forms.TextBox tbGameDate;
        private System.Windows.Forms.Label lblArena;
        private System.Windows.Forms.Label lblAttendance;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.PictureBox pbViolin;
        private System.Windows.Forms.TextBox tbWonAway;
        private System.Windows.Forms.TextBox tbWonHome;
        private System.Windows.Forms.TextBox tbModeAway;
        private System.Windows.Forms.TextBox tbModeHome;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.Label label7;
    }
}