namespace NBA_Sim_View
{
    partial class ScrapePopUp
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
            this.lblCheckProxies = new System.Windows.Forms.Label();
            this.btnCancel = new System.Windows.Forms.Button();
            this.btnCustomProxyList = new System.Windows.Forms.Button();
            this.btnScrape = new System.Windows.Forms.Button();
            this.rbChromeProxy = new System.Windows.Forms.RadioButton();
            this.rbFirefoxProxy = new System.Windows.Forms.RadioButton();
            this.rbRequestsProxy = new System.Windows.Forms.RadioButton();
            this.rbChrome = new System.Windows.Forms.RadioButton();
            this.rbFirefox = new System.Windows.Forms.RadioButton();
            this.rbRequests = new System.Windows.Forms.RadioButton();
            this.label2 = new System.Windows.Forms.Label();
            this.lblGameSelector = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.tbMissing = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.panel1.SuspendLayout();
            this.SuspendLayout();
            // 
            // panel1
            // 
            this.panel1.BackColor = System.Drawing.Color.LightSlateGray;
            this.panel1.Controls.Add(this.label3);
            this.panel1.Controls.Add(this.tbMissing);
            this.panel1.Controls.Add(this.lblCheckProxies);
            this.panel1.Controls.Add(this.btnCancel);
            this.panel1.Controls.Add(this.btnCustomProxyList);
            this.panel1.Controls.Add(this.btnScrape);
            this.panel1.Controls.Add(this.rbChromeProxy);
            this.panel1.Controls.Add(this.rbFirefoxProxy);
            this.panel1.Controls.Add(this.rbRequestsProxy);
            this.panel1.Controls.Add(this.rbChrome);
            this.panel1.Controls.Add(this.rbFirefox);
            this.panel1.Controls.Add(this.rbRequests);
            this.panel1.Location = new System.Drawing.Point(-2, 24);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(336, 450);
            this.panel1.TabIndex = 6;
            // 
            // lblCheckProxies
            // 
            this.lblCheckProxies.AutoSize = true;
            this.lblCheckProxies.Font = new System.Drawing.Font("Calibri", 10.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblCheckProxies.ForeColor = System.Drawing.Color.Snow;
            this.lblCheckProxies.Location = new System.Drawing.Point(104, 291);
            this.lblCheckProxies.Name = "lblCheckProxies";
            this.lblCheckProxies.Size = new System.Drawing.Size(114, 22);
            this.lblCheckProxies.TabIndex = 15;
            this.lblCheckProxies.Text = "Check Proxies";
            this.lblCheckProxies.Click += new System.EventHandler(this.lblCheckProxies_Click);
            // 
            // btnCancel
            // 
            this.btnCancel.BackColor = System.Drawing.Color.Tomato;
            this.btnCancel.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Center;
            this.btnCancel.FlatAppearance.BorderSize = 0;
            this.btnCancel.FlatAppearance.MouseDownBackColor = System.Drawing.Color.IndianRed;
            this.btnCancel.FlatAppearance.MouseOverBackColor = System.Drawing.Color.IndianRed;
            this.btnCancel.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.btnCancel.Font = new System.Drawing.Font("Cascadia Code SemiBold", 9F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnCancel.ForeColor = System.Drawing.Color.Snow;
            this.btnCancel.Location = new System.Drawing.Point(48, 396);
            this.btnCancel.Name = "btnCancel";
            this.btnCancel.Size = new System.Drawing.Size(240, 34);
            this.btnCancel.TabIndex = 14;
            this.btnCancel.Text = "Cancel";
            this.btnCancel.UseVisualStyleBackColor = false;
            this.btnCancel.Click += new System.EventHandler(this.btnCancel_Click);
            // 
            // btnCustomProxyList
            // 
            this.btnCustomProxyList.BackColor = System.Drawing.SystemColors.Control;
            this.btnCustomProxyList.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Center;
            this.btnCustomProxyList.FlatAppearance.BorderSize = 0;
            this.btnCustomProxyList.FlatAppearance.MouseDownBackColor = System.Drawing.Color.IndianRed;
            this.btnCustomProxyList.FlatAppearance.MouseOverBackColor = System.Drawing.Color.IndianRed;
            this.btnCustomProxyList.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.btnCustomProxyList.Font = new System.Drawing.Font("Cascadia Code SemiBold", 9F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnCustomProxyList.ForeColor = System.Drawing.Color.LightSlateGray;
            this.btnCustomProxyList.Location = new System.Drawing.Point(48, 316);
            this.btnCustomProxyList.Name = "btnCustomProxyList";
            this.btnCustomProxyList.Size = new System.Drawing.Size(240, 34);
            this.btnCustomProxyList.TabIndex = 13;
            this.btnCustomProxyList.Text = "Custom Proxy List";
            this.btnCustomProxyList.UseVisualStyleBackColor = false;
            this.btnCustomProxyList.Click += new System.EventHandler(this.btnCustomProxyList_Click);
            // 
            // btnScrape
            // 
            this.btnScrape.BackColor = System.Drawing.Color.Tomato;
            this.btnScrape.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Center;
            this.btnScrape.FlatAppearance.BorderSize = 0;
            this.btnScrape.FlatAppearance.MouseDownBackColor = System.Drawing.Color.IndianRed;
            this.btnScrape.FlatAppearance.MouseOverBackColor = System.Drawing.Color.IndianRed;
            this.btnScrape.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.btnScrape.Font = new System.Drawing.Font("Cascadia Code SemiBold", 9F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnScrape.ForeColor = System.Drawing.Color.Snow;
            this.btnScrape.Location = new System.Drawing.Point(48, 356);
            this.btnScrape.Name = "btnScrape";
            this.btnScrape.Size = new System.Drawing.Size(240, 34);
            this.btnScrape.TabIndex = 12;
            this.btnScrape.Text = "Scrape";
            this.btnScrape.UseVisualStyleBackColor = false;
            this.btnScrape.Click += new System.EventHandler(this.btnScrape_Click);
            // 
            // rbChromeProxy
            // 
            this.rbChromeProxy.AutoSize = true;
            this.rbChromeProxy.ForeColor = System.Drawing.Color.Snow;
            this.rbChromeProxy.Location = new System.Drawing.Point(85, 231);
            this.rbChromeProxy.Name = "rbChromeProxy";
            this.rbChromeProxy.Size = new System.Drawing.Size(171, 20);
            this.rbChromeProxy.TabIndex = 6;
            this.rbChromeProxy.TabStop = true;
            this.rbChromeProxy.Text = "Chrome Selenium Proxy";
            this.rbChromeProxy.UseVisualStyleBackColor = true;
            // 
            // rbFirefoxProxy
            // 
            this.rbFirefoxProxy.AutoSize = true;
            this.rbFirefoxProxy.ForeColor = System.Drawing.Color.Snow;
            this.rbFirefoxProxy.Location = new System.Drawing.Point(85, 203);
            this.rbFirefoxProxy.Name = "rbFirefoxProxy";
            this.rbFirefoxProxy.Size = new System.Drawing.Size(164, 20);
            this.rbFirefoxProxy.TabIndex = 5;
            this.rbFirefoxProxy.TabStop = true;
            this.rbFirefoxProxy.Text = "Firefox Selenium Proxy";
            this.rbFirefoxProxy.UseVisualStyleBackColor = true;
            // 
            // rbRequestsProxy
            // 
            this.rbRequestsProxy.AutoSize = true;
            this.rbRequestsProxy.ForeColor = System.Drawing.Color.Snow;
            this.rbRequestsProxy.Location = new System.Drawing.Point(85, 175);
            this.rbRequestsProxy.Name = "rbRequestsProxy";
            this.rbRequestsProxy.Size = new System.Drawing.Size(123, 20);
            this.rbRequestsProxy.TabIndex = 4;
            this.rbRequestsProxy.TabStop = true;
            this.rbRequestsProxy.Text = "Requests Proxy";
            this.rbRequestsProxy.UseVisualStyleBackColor = true;
            // 
            // rbChrome
            // 
            this.rbChrome.AutoSize = true;
            this.rbChrome.ForeColor = System.Drawing.Color.Snow;
            this.rbChrome.Location = new System.Drawing.Point(85, 136);
            this.rbChrome.Name = "rbChrome";
            this.rbChrome.Size = new System.Drawing.Size(134, 20);
            this.rbChrome.TabIndex = 3;
            this.rbChrome.TabStop = true;
            this.rbChrome.Text = "Chrome Selenium";
            this.rbChrome.UseVisualStyleBackColor = true;
            // 
            // rbFirefox
            // 
            this.rbFirefox.AutoSize = true;
            this.rbFirefox.ForeColor = System.Drawing.Color.Snow;
            this.rbFirefox.Location = new System.Drawing.Point(85, 108);
            this.rbFirefox.Name = "rbFirefox";
            this.rbFirefox.Size = new System.Drawing.Size(127, 20);
            this.rbFirefox.TabIndex = 1;
            this.rbFirefox.TabStop = true;
            this.rbFirefox.Text = "Firefox Selenium";
            this.rbFirefox.UseVisualStyleBackColor = true;
            // 
            // rbRequests
            // 
            this.rbRequests.AutoSize = true;
            this.rbRequests.ForeColor = System.Drawing.Color.Snow;
            this.rbRequests.Location = new System.Drawing.Point(85, 80);
            this.rbRequests.Name = "rbRequests";
            this.rbRequests.Size = new System.Drawing.Size(86, 20);
            this.rbRequests.TabIndex = 0;
            this.rbRequests.TabStop = true;
            this.rbRequests.Text = "Requests";
            this.rbRequests.UseVisualStyleBackColor = true;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Impact", 13.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label2.ForeColor = System.Drawing.Color.LightSlateGray;
            this.label2.Location = new System.Drawing.Point(-1, 2);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(302, 28);
            this.label2.TabIndex = 12;
            this.label2.Text = "Remember to turn on your VPN!";
            // 
            // lblGameSelector
            // 
            this.lblGameSelector.AutoSize = true;
            this.lblGameSelector.Font = new System.Drawing.Font("Calibri", 10.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblGameSelector.ForeColor = System.Drawing.Color.LightSlateGray;
            this.lblGameSelector.Location = new System.Drawing.Point(34, 482);
            this.lblGameSelector.Name = "lblGameSelector";
            this.lblGameSelector.Size = new System.Drawing.Size(252, 22);
            this.lblGameSelector.TabIndex = 13;
            this.lblGameSelector.Text = "Default proxy list is unvalidated!";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Calibri", 10.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.ForeColor = System.Drawing.Color.LightSlateGray;
            this.label1.Location = new System.Drawing.Point(40, 502);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(243, 22);
            this.label1.TabIndex = 14;
            this.label1.Text = "Anonymity is NOT guaranteed!";
            // 
            // tbMissing
            // 
            this.tbMissing.Font = new System.Drawing.Font("HoloLens MDL2 Assets", 10.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.tbMissing.Location = new System.Drawing.Point(46, 27);
            this.tbMissing.Name = "tbMissing";
            this.tbMissing.Size = new System.Drawing.Size(239, 25);
            this.tbMissing.TabIndex = 16;
            this.tbMissing.Text = "home";
            this.tbMissing.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Font = new System.Drawing.Font("Calibri", 10.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label3.ForeColor = System.Drawing.Color.Snow;
            this.label3.Location = new System.Drawing.Point(100, 6);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(132, 21);
            this.label3.TabIndex = 15;
            this.label3.Text = "Missing from DB:";
            // 
            // ScrapePopUp
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(332, 532);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.lblGameSelector);
            this.Controls.Add(this.panel1);
            this.Controls.Add(this.label2);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.Name = "ScrapePopUp";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "ScrapePopUp";
            this.panel1.ResumeLayout(false);
            this.panel1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.Button btnScrape;
        private System.Windows.Forms.RadioButton rbChromeProxy;
        private System.Windows.Forms.RadioButton rbFirefoxProxy;
        private System.Windows.Forms.RadioButton rbRequestsProxy;
        private System.Windows.Forms.RadioButton rbChrome;
        private System.Windows.Forms.RadioButton rbFirefox;
        private System.Windows.Forms.RadioButton rbRequests;
        private System.Windows.Forms.Button btnCustomProxyList;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Button btnCancel;
        private System.Windows.Forms.Label lblGameSelector;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label lblCheckProxies;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox tbMissing;
    }
}