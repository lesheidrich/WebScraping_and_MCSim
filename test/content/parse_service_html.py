"""
Module: parse_service_html.py

Contains html strings for unit-testing parsers.
"""

PLAYER_HTML = """
<body style="">
      <div id="site-takeover">
      
         <div id="header_wrap" class="scroll">
         
            <header class="wrapper clearfix">
            
               <div class="container">
               
                  <div class="tabs-container clearfix">
                  
                     <div class="logo-container clearfix">
                        <a href="/"><img src="/images/basketball/5.0/template/realgm-basketball-logo-175-80.png" class="logo"></a>
                     </div>
                     
                     <div class="secondary-ad-container"></div>
                     
                     <div id="social-menu" class="topmenu">
                        <ul>
                           <li class="instagram"><a href="https://www.instagram.com/realgmnba" title="RealGM on Instagram"></a></li>
                           <li class="facebook"><a href="https://www.facebook.com/RealGM" title="RealGM on Facebook"></a></li>
                           <li class="twitter"><a href="https://twitter.com/RealGM" title="RealGM on Twitter"></a></li>
                        </ul>
                     </div>
                     
                     <div id="sports-menu" class="topmenu">
                        <div id="sports-menu-container">
                           <ul>
                              <li class="top-icon navitem nbalink selected"><a href="/"><span></span><nav>Basketball</nav></a></li>
                              <li class="top-icon navitem nfllink"><a href="https://football.realgm.com/"><span></span><nav>Football</nav></a></li>
                              <li class="top-icon navitem mlblink"><a href="https://baseball.realgm.com/"><span></span><nav>Baseball</nav></a></li>
                              <li class="top-icon navitem soccerlink"><a href="https://soccer.realgm.com/"><span></span><nav>Soccer</nav></a></li>
                              <li class="top-icon navitem nhllink"><a href="https://hockey.realgm.com/"><span></span><nav>Hockey</nav></a></li>
                              <li class="top-icon navitem forumlink"><a href="https://forums.realgm.com/boards/index.php"><span></span><nav>Forums</nav></a></li>
                                                            <li class="top-icon navitem tixlink"><a href="https://www.vividseats.com/?wsUser=958" target="_blank"><span></span><nav>Tickets</nav></a></li>
                              <li class="top-icon navitem instagram"><a href="https://www.instagram.com/realgmnba" title="RealGM on Instagram"><span></span></a></li>
                              <li class="top-icon navitem facebook"><a href="https://www.facebook.com/RealGM" title="RealGM on Facebook"><span></span></a></li>
                              <li class="top-icon navitem twitter"><a href="https://twitter.com/RealGM" title="RealGM on Twitter"><span></span></a></li>
                           </ul>
                        </div>
                     </div>
                     
                     <div class="searchbar">
                        <form action="/search" method="get" class="searchbox" id="playersearch" autocomplete="off">
                           <input type="text" class="searchbox-text ui-autocomplete-input" placeholder="Search..." name="q" id="searchfield" onkeyup="searchButtonUp();" required="required" autocomplete="off"><input type="submit" class="searchbox-submit" value="Go">
                        </form>
                     </div>
                     
                  </div>
                  
               </div>
            </header>
               
            <div class="top-nav-container">
<div class="wrapper clearfix">
<div id="menu-button" class="clearfix">
<a href="/" class="home_logo"><img src="/images/basketball/5.0/template/realgm-basketball-logo-130-60.png" style="height: 30px; width: 65px;"></a>
<a href="javascript:void(0);" class="menu-link"><span></span><nav>Menu</nav></a>
<a href="javascript:void(0);" onclick="showSportsNav()"><nav id="primary-sport-menu-icon"><u>NBA</u></nav></a>
</div><nav id="top-level-nav" role="navigation" class="container has-subnav">
<ul class="primary-nav">
<li class="search-nav with-js">
<form action="/search" method="get" class="searchbox" autocomplete="off">
<input type="text" class="searchbox-text ui-autocomplete-input" placeholder="Search..." name="q" required="required" autocomplete="off"><input type="submit" class="searchbox-submit" value="Go">
</form>
</li>
<li class="mobile-menu with-js"><a href="javascript: void(0);" onclick="showSecondaryNav();"><span>« Back</span></a></li><li class="has-subnav with-js">
<a href="/nba" id="change-sports-menu">NBA</a>
<div class="primary-nav-ddl">
<ul>
<li class="with-js"><a href="/nba">NBA</a></li><li class="with-js"><a href="/ncaa">NCAA</a></li><li class="with-js"><a href="/gleague">G League</a></li><li class="with-js"><a href="/international">International</a></li><li class="with-js"><a href="/national">National</a></li><li class="with-js"><a href="/highschool">High School</a></li></ul>
</div>
</li><li class="has-subnav with-js">
<a href="https://forums.realgm.com/boards/viewforum.php?f=243">Forums</a>
<div class="primary-nav-ddl">
<ul class="primary-nav-col" style="width: 15em; float: left;">
<li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=243">Basketball Forums</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=6">The General Board</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=64">Player Comparisons</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=2">Trades &amp; Transactions</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=344">Statistical Analysis</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=39">Fantasy Basketball</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=465">Gambling</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=3">NBA Draft</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=36">NCAA Basketball</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=350">G League</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=5">International Basketball</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=346">High School Basketball</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=69">Current Affairs</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=42">Off-Topic Board</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=4">CBA &amp; Business</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=40">Feedback</a></li></ul>
<div style="float: left; border-left: 1px solid black; padding-left: 1em;">
<div style="float: left; width: 16em;">
<p style="padding-left: 15px;">Atlantic Division</p>
<ul class="primary-nav-col" style="font-weight: normal;">
<li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=8">Boston Celtics</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=23">Brooklyn Nets</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=24">New York Knicks</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=26">Philadelphia Sixers</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=32">Toronto Raptors</a></li></ul>
</div>
<div style="float: left; width: 16em;">
<p style="padding-left: 15px;">Central Division</p>
<ul class="primary-nav-col" style="font-weight: normal;">
<li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=10">Chicago Bulls</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=11">Cleveland Cavaliers</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=14">Detroit Pistons</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=17">Indiana Pacers</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=21">Milwaukee Bucks</a></li></ul>
</div>
<div style="float: left; width: 16em;">
<p style="padding-left: 15px;">Southeast Division</p>
<ul class="primary-nav-col" style="font-weight: normal;">
<li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=7">Atlanta Hawks</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=53">Charlotte Hornets</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=20">Miami Heat</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=25">Orlando Magic</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=35">Washington Wizards</a></li></ul>
</div>
<div style="clear: both; height: 1em;" class="sep"></div>
<div style="float: left; width: 16em;">
<p style="padding-left: 15px;">Northwest Division</p>
<ul class="primary-nav-col" style="font-weight: normal;">
<li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=13">Denver Nuggets</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=22">Minnesota Timberwolves</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=334">Oklahoma City Thunder</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=28">Portland Trail Blazers</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=33">Utah Jazz</a></li></ul>
</div>
<div style="float: left; width: 16em;">
<p style="padding-left: 15px;">Pacific Division</p>
<ul class="primary-nav-col" style="font-weight: normal;">
<li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=15">Golden State Warriors</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=18">Los Angeles Clippers</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=19">Los Angeles Lakers</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=27">Phoenix Suns</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=29">Sacramento Kings</a></li></ul>
</div>
<div style="float: left; width: 16em;">
<p style="padding-left: 15px;">Southwest Division</p>
<ul class="primary-nav-col" style="font-weight: normal;">
<li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=12">Dallas Mavericks</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=16">Houston Rockets</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=34">Memphis Grizzlies</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=9">New Orleans Pelicans</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=30">San Antonio Spurs</a></li></ul>
</div>
</div>
<div style="clear: both;"></div>
</div>
</li><li class="with-js">
<a href="/nba/news">News</a>
<div class="primary-nav-ddl">
<ul class="primary-nav-col" style="width: 15em; float: left;">
<li class="with-js"><a href="/news/wiretap/tags/15/NBA">All Rumors</a></li><li class="with-js"><a href="/news/wiretap/tags/16/Signing-Rumor">Free Agent Rumors</a></li><li class="with-js"><a href="/news/wiretap/tags/18/Trade Rumor">Trade Rumors</a></li><li class="with-js"><a href="/news/wiretap/tags/53/Waiver">Waivers</a></li><li class="with-js"><a href="/news/wiretap/tags/25/NBA-Draft">NBA Draft</a></li><li class="with-js"><a href="/news/wiretap/tags/52/CBA">CBA</a></li><li class="with-js"><a href="/news/wiretap/tags/24/Injury">Injuries</a></li><li class="with-js"><a href="/news/wiretap/tags/55/Award">Awards</a></li><li class="with-js"><a href="/news/wiretap/tags/63/Fines">Fines</a></li><li class="with-js"><a href="/news/wiretap/tags/23/Suspension">Suspensions</a></li><li class="with-js"><a href="/news/wiretap/tags/69/B-Ball-IQ">B-Ball IQ</a></li><li class="with-js"><a href="/news/wiretap/tags/97/Preseason">Preseason</a></li><li class="with-js"><a href="/news/wiretap/tags/98/Playoffs">Playoffs</a></li><li class="with-js"><a href="/news/wiretap/tags/95/Summer-League">Summer League</a></li><li class="with-js"><a href="/news/wiretap/tags/54/All-Star">All-Star</a></li><li class="with-js"><a href="/news/wiretap/tags/22/NBA">Rankings</a></li></ul>
<div class="portal" style="float: left; border-left: 1px solid black; padding-left: 1em; max-width: 50em;">
<div class="secondary-story-container" style="border-top: 0;"><div class="secondary-story">
<a class="article-image" href="/wiretap/274748/Nets-Fire-Jacque-Vaughn" style="background-image: url('https://basketball.realgm.com/images/nba/4.2/wiretap/photos/2006/Vaughn_Jacque_bkn_221114.jpg');"></a>
<div class="article-title"><a style="padding-left: 0;" href="/wiretap/274748/Nets-Fire-Jacque-Vaughn">Nets Fire Jacque Vaughn</a></div>
<div class="article-content" style="font-weight: normal;"></div>
</div>
<div class="secondary-story">
<a class="article-image" href="/wiretap/274747/Stephen-Curry-On-Retirement-I-Dont-Think-Im-Anywhere-Close-To-That" style="background-image: url('https://basketball.realgm.com/images/nba/4.2/wiretap/photos/2006/Curry_Stephen_gsw_230311.jpg');"></a>
<div class="article-title"><a style="padding-left: 0;" href="/wiretap/274747/Stephen-Curry-On-Retirement-I-Dont-Think-Im-Anywhere-Close-To-That">Stephen Curry On Retirement: I Don't Think I'm Anywhere Close To That</a></div>
<div class="article-content" style="font-weight: normal;"></div>
</div>
<div class="secondary-story">
<a class="article-image" href="/wiretap/274746/LeBron-James-To-Have-Treatment-On-Left-Ankle-Could-Miss-Thursdays-Game" style="background-image: url('https://basketball.realgm.com/images/nba/4.2/wiretap/photos/2006/James_LeBron_lal_240116.jpg');"></a>
<div class="article-title"><a style="padding-left: 0;" href="/wiretap/274746/LeBron-James-To-Have-Treatment-On-Left-Ankle-Could-Miss-Thursdays-Game">LeBron James To Have Treatment On Left Ankle, Could Miss Thursday's Game</a></div>
<div class="article-content" style="font-weight: normal;"></div>
</div>
<div class="secondary-story">
<a class="article-image" href="/wiretap/274745/Bradley-Beal-On-Track-To-Return-Thursday-From-Hamstring-Injury" style="background-image: url('https://basketball.realgm.com/images/nba/4.2/wiretap/photos/2006/Beal_Bradley_phx_231117.jpg');"></a>
<div class="article-title"><a style="padding-left: 0;" href="/wiretap/274745/Bradley-Beal-On-Track-To-Return-Thursday-From-Hamstring-Injury">Bradley Beal On Track To Return Thursday From Hamstring Injury</a></div>
<div class="article-content" style="font-weight: normal;"></div>
</div>
</div>
</div>
<div style="clear: both;"></div>
</div>
</li><li class="with-js">
<a href="/nba/news/analysis">Analysis</a>
<div class="primary-nav-ddl">
<ul class="primary-nav-col" style="width: 15em; float: left; padding-top: 0.5em;">
<li class="label with-js"><u>Featured Writers</u></li><li class="with-js"><a href="/news/analysis/author/217/Colin-McGowan">Colin McGowan</a></li><li class="with-js"><a href="/news/analysis/author/226/John-Wilmes">John Wilmes</a></li><li class="with-js"><a href="/news/analysis/author/245/Micah-Wimmer">Micah Wimmer</a></li><li class="label with-js">&nbsp;</li><li class="label with-js"><u>More Contributors</u></li><li class="with-js"><a href="/news/analysis/author/258/Zachary-Cohen">Zachary Cohen</a></li><li class="with-js"><a href="/news/analysis/author/257/Wes-Goldberg">Wes Goldberg</a></li><li class="with-js"><a href="/news/analysis/author/145/RealGM-Staff-Report">RealGM Staff Report</a></li><li class="with-js"><a href="/news/analysis/author/248/Jack-Tien-Dana">Jack Tien-Dana</a></li><li class="with-js"><a href="/news/analysis/author/247/Kevin-Yeung">Kevin Yeung</a></li></ul>
<div class="portal" style="float: left; border-left: 1px solid black; padding-left: 1em; max-width: 50em;">
<div class="secondary-story-container" style="border-top: 0;"><div class="secondary-story">
<a class="article-image" href="/analysis/274590/Are-The-Cavaliers-For-Real" style="background-image: url('https://basketball.realgm.com/images/nba/4.2/wiretap/photos/2006/Mitchell_Donovan_cle_240102.jpg');"></a>
<div class="article-title"><a style="padding-left: 0;" href="/analysis/274590/Are-The-Cavaliers-For-Real">Are The Cavaliers For Real?</a></div>
<p class="author-details" style="margin: 0 0 0.5em;">
by <a href="/news/analysis/author/257/Wes-Goldberg" style="text-decoration: none;">Wes Goldberg</a></p>
<div class="article-content" style="font-weight: normal;">The Cavaliers have surged since the turn of the calendar in large part due to Donovan Mitchell and Jarrett Allen establishing themselves as their top two stars and others stepping into roles that complement their strengths.</div>
</div>
<div class="secondary-story">
<a class="article-image" href="/analysis/274567/NBA-Draft-Report-Stephon-Castle-Of-UConn" style="background-image: url('https://basketball.realgm.com/images/nba/4.2/wiretap/photos/2006/Castle_Stephon_uconn_240202.jpg');"></a>
<div class="article-title"><a style="padding-left: 0;" href="/analysis/274567/NBA-Draft-Report-Stephon-Castle-Of-UConn">NBA Draft Report: Stephon Castle Of UConn</a></div>
<p class="author-details" style="margin: 0 0 0.5em;">
by <a href="/news/analysis/author/258/Zachary-Cohen" style="text-decoration: none;">Zachary Cohen</a></p>
<div class="article-content" style="font-weight: normal;">Stephon Castle's biggest strength is his point of attack defense and his ability to make plays off the dribble. If his jumper develops, Castle can become a special NBA player.</div>
</div>
<div class="secondary-story">
<a class="article-image" href="/analysis/274486/Welcome-To-Giannis-Revisionism" style="background-image: url('https://basketball.realgm.com/images/nba/4.2/wiretap/photos/2006/Antetokounmpo_Giannis_mil_231027.jpg');"></a>
<div class="article-title"><a style="padding-left: 0;" href="/analysis/274486/Welcome-To-Giannis-Revisionism">Welcome To Giannis Revisionism</a></div>
<p class="author-details" style="margin: 0 0 0.5em;">
by <a href="/news/analysis/author/226/John-Wilmes" style="text-decoration: none;">John Wilmes</a></p>
<div class="article-content" style="font-weight: normal;">Giannis Antetokounmpo was unassailable in the public realm, but he ultimately is more like other stars than previously imagined, and less the exception to their characteristic profile than assumed.</div>
</div>
<div class="secondary-story">
<a class="article-image" href="/analysis/274484/NBA-Draft-Report-JaKobe-Walter-Of-Baylor" style="background-image: url('https://basketball.realgm.com/images/nba/4.2/wiretap/photos/2006/Walter_Jakobe_bay_240126.jpg');"></a>
<div class="article-title"><a style="padding-left: 0;" href="/analysis/274484/NBA-Draft-Report-JaKobe-Walter-Of-Baylor">NBA Draft Report: Ja'Kobe Walter Of Baylor</a></div>
<p class="author-details" style="margin: 0 0 0.5em;">
by <a href="/news/analysis/author/258/Zachary-Cohen" style="text-decoration: none;">Zachary Cohen</a></p>
<div class="article-content" style="font-weight: normal;">Ja'Kobe Walter has the size, shooting and tenacity on the wing every team in the NBA is always prioritizing to make him a safe bet for a lottery pick.</div>
</div>
</div>
</div>
<div style="clear: both;"></div>
</div>
</li><li class="has-subnav with-js">
<a href="/nba/teams" class="selected">Teams</a>
<div class="primary-nav-ddl">
<div style="float: left; width: 16em;">
<p style="padding-left: 15px;">Atlantic Division</p>
<ul class="primary-nav-col" style="font-weight: normal;">
<li class="with-js"><a href="/nba/teams/Boston-Celtics/2/Home">Boston Celtics</a></li><li class="with-js"><a href="/nba/teams/Brooklyn-Nets/38/Home">Brooklyn Nets</a></li><li class="with-js"><a href="/nba/teams/New-York-Knicks/20/Home">New York Knicks</a></li><li class="with-js"><a href="/nba/teams/Philadelphia-Sixers/22/Home">Philadelphia Sixers</a></li><li class="with-js"><a href="/nba/teams/Toronto-Raptors/28/Home">Toronto Raptors</a></li></ul>
</div>
<div style="float: left; width: 16em;">
<p style="padding-left: 15px;">Central Division</p>
<ul class="primary-nav-col" style="font-weight: normal;">
<li class="with-js"><a href="/nba/teams/Chicago-Bulls/4/Home">Chicago Bulls</a></li><li class="with-js"><a href="/nba/teams/Cleveland-Cavaliers/5/Home">Cleveland Cavaliers</a></li><li class="with-js"><a href="/nba/teams/Detroit-Pistons/8/Home">Detroit Pistons</a></li><li class="with-js"><a href="/nba/teams/Indiana-Pacers/11/Home">Indiana Pacers</a></li><li class="with-js"><a href="/nba/teams/Milwaukee-Bucks/16/Home">Milwaukee Bucks</a></li></ul>
</div>
<div style="float: left; width: 16em;">
<p style="padding-left: 15px;">Southeast Division</p>
<ul class="primary-nav-col" style="font-weight: normal;">
<li class="with-js"><a href="/nba/teams/Atlanta-Hawks/1/Home">Atlanta Hawks</a></li><li class="with-js"><a href="/nba/teams/Charlotte-Hornets/3/Home">Charlotte Hornets</a></li><li class="with-js"><a href="/nba/teams/Miami-Heat/15/Home">Miami Heat</a></li><li class="with-js"><a href="/nba/teams/Orlando-Magic/21/Home">Orlando Magic</a></li><li class="with-js"><a href="/nba/teams/Washington-Wizards/30/Home">Washington Wizards</a></li></ul>
</div>
<div style="clear: both; height: 1em;" class="sep"></div>
<div style="float: left; width: 16em;">
<p style="padding-left: 15px;">Northwest Division</p>
<ul class="primary-nav-col" style="font-weight: normal;">
<li class="with-js"><a href="/nba/teams/Denver-Nuggets/7/Home">Denver Nuggets</a></li><li class="with-js"><a href="/nba/teams/Minnesota-Timberwolves/17/Home">Minnesota Timberwolves</a></li><li class="with-js"><a href="/nba/teams/Oklahoma-City-Thunder/33/Home">Oklahoma City Thunder</a></li><li class="with-js"><a href="/nba/teams/Portland-Trail-Blazers/24/Home">Portland Trail Blazers</a></li><li class="with-js"><a href="/nba/teams/Utah-Jazz/29/Home">Utah Jazz</a></li></ul>
</div>
<div style="float: left; width: 16em;">
<p style="padding-left: 15px;">Pacific Division</p>
<ul class="primary-nav-col" style="font-weight: normal;">
<li class="with-js"><a href="/nba/teams/Golden-State-Warriors/9/Home">Golden State Warriors</a></li><li class="with-js"><a href="/nba/teams/Los-Angeles-Clippers/12/Home">Los Angeles Clippers</a></li><li class="with-js"><a href="/nba/teams/Los-Angeles-Lakers/13/Home">Los Angeles Lakers</a></li><li class="with-js"><a href="/nba/teams/Phoenix-Suns/23/Home">Phoenix Suns</a></li><li class="with-js"><a href="/nba/teams/Sacramento-Kings/25/Home">Sacramento Kings</a></li></ul>
</div>
<div style="float: left; width: 16em;">
<p style="padding-left: 15px;">Southwest Division</p>
<ul class="primary-nav-col" style="font-weight: normal;">
<li class="with-js"><a href="/nba/teams/Dallas-Mavericks/6/Home">Dallas Mavericks</a></li><li class="with-js"><a href="/nba/teams/Houston-Rockets/10/Home">Houston Rockets</a></li><li class="with-js"><a href="/nba/teams/Memphis-Grizzlies/14/Home">Memphis Grizzlies</a></li><li class="with-js"><a href="/nba/teams/New-Orleans-Pelicans/19/Home">New Orleans Pelicans</a></li><li class="with-js"><a href="/nba/teams/San-Antonio-Spurs/26/Home">San Antonio Spurs</a></li></ul>
</div>
<div style="clear: both;"></div>
</div>
</li><li class="has-subnav with-js">
<a href="#">GM Laboratory</a>
<div class="primary-nav-ddl">
<p style="margin-bottom: 0; color: #F36E21; text-align: center; font-style: italic; font-size: 1.5em;">Tools and Resources Used by Real General Managers.</p>
<div style="float: left; width: 15em;">
<p style="text-decoration: underline; padding: 0.3em 0.8em; margin-bottom: 0;"><a href="/nba/players">Players</a></p>
<ul class="primary-nav-col" style="font-weight: normal;">
<li class="with-js"><a href="/nba/players">Current Players</a></li><li class="with-js"><a href="/nba/depth-charts">Depth Charts</a></li><li class="with-js"><a href="/nba/birth-cities">Birth Cities</a></li><li class="with-js"><a href="/nba/birth-countries">Birth Countries</a></li><li class="with-js"><a href="/nba/birth-dates">Birth Dates</a></li><li class="with-js"><a href="/nba/players-abroad">NBA Players Abroad</a></li></ul>
<p style="text-decoration: underline; padding: 0.3em 0.8em; margin-bottom: 0;"><a href="/nba/awards">Awards</a></p>
<ul class="primary-nav-col" style="font-weight: normal;">
<li class="with-js"><a href="/nba/awards/by_season">By Season</a></li><li class="with-js"><a href="/nba/awards/by_type">By Type</a></li><li class="with-js"><a href="/nba/awards/by_player">By Player</a></li><li class="with-js"><a href="/nba/awards/top_75">NBA's Top 75</a></li><li class="with-js"><a href="/nba/hall-of-fame">Hall of Fame</a></li><li class="with-js"><a href="/nba/retired-numbers">Retired Jerseys</a></li></ul>
<p style="text-decoration: underline; padding: 0.3em 0.8em; margin-bottom: 0;"><a href="/nba/staff-members">Staff Members</a></p>
<ul class="primary-nav-col" style="font-weight: normal;">
<li class="with-js"><a href="/nba/staff-members/20/Head-Coach/Current">Head Coaches</a></li><li class="with-js"><a href="/nba/staff-members/16/General-Manager/Current">General Managers</a></li></ul>
</div>
<div style="float: left; width: 15em;">
<p style="text-decoration: underline; padding: 0.3em 0.8em; margin-bottom: 0;"><a href="/nba/transactions">Transactions</a></p>
<ul class="primary-nav-col" style="font-weight: normal;">
<li class="with-js"><a href="/nba/transactions/league">Transactions History</a></li><li class="with-js"><a href="/nba/transactions/composition">Roster Compositions</a></li><li class="with-js"><a href="/nba/transactions/composition_search">Compositions Search</a></li><li class="with-js"><a href="/nba/transactions/trade-deadline">Trade Deadline</a></li><li class="with-js"><a href="/nba/player_tracker/trade">Trade Tracker</a></li><li class="with-js"><a href="/nba/current_free_agents">Current Free Agents</a></li><li class="with-js"><a href="/nba/future_free_agents">Future Free Agents</a></li><li class="with-js"><a href="/nba/free_agent_options">Contract Options</a></li><li class="with-js"><a href="/nba/player_tracker/free_agent">Free Agent Tracker</a></li><li class="with-js"><a href="/nba/offseason">Offseason Recap</a></li><li class="with-js"><a href="/nba/roster-turnover">Roster Turnover</a></li></ul>
<p style="text-decoration: underline; padding: 0.3em 0.8em; margin-bottom: 0;"><a href="/nba/agent-client-list">Agents</a></p>
<ul class="primary-nav-col" style="font-weight: normal;">
<li class="with-js"><a href="/nba/agent-client-list">Agent Client Lists</a></li><li class="with-js"><a href="/nba/agent-relationships">Agent Relationships</a></li></ul>
</div>
<div style="float: left; width: 15em;">
<p style="text-decoration: underline; padding: 0.3em 0.8em; margin-bottom: 0;"><a href="/nba/draft/future_drafts/team">Future Draft Picks</a></p>
<ul class="primary-nav-col" style="font-weight: normal;">
<li class="with-js"><a href="/nba/draft/future_drafts/team">Team Summary</a></li><li class="with-js"><a href="/nba/draft/future_drafts/yearly">Yearly Summary</a></li><li class="with-js"><a href="/nba/draft/future_drafts/detailed">Pick Details</a></li></ul>
<p style="text-decoration: underline; padding: 0.3em 0.8em; margin-bottom: 0;">NBA Draft Tools</p>
<ul class="primary-nav-col" style="font-weight: normal;">
<li class="with-js"><a href="/nba/draft/draft_simulator">Mock Draft Simulator</a></li><li class="with-js"><a href="/nba/draft/lottery_simulator">Lottery Simulator</a></li><li class="with-js"><a href="/nba/draft/prospects/stats">Prospect Stats</a></li></ul>
<p style="text-decoration: underline; padding: 0.3em 0.8em; margin-bottom: 0;"><a href="/nba/draft">NBA Draft History</a></p>
<ul class="primary-nav-col" style="font-weight: normal;">
<li class="with-js"><a href="/nba/draft/past-drafts">Past Drafts</a></li><li class="with-js"><a href="/nba/teams/Atlanta-Hawks/1/Draft_History/Historical">Team Draft History</a></li><li class="with-js"><a href="/nba/draft/draft-rights">Draft Rights</a></li><li class="with-js"><a href="/nba/draft/lottery_winners">Lottery Winners</a></li><li class="with-js"><a href="/nba/draft/lottery_results">Lottery History</a></li><li class="with-js"><a href="/nba/draft/lottery_results/by_team">Team Lottery History</a></li><li class="with-js"><a href="/nba/draft/search">NBA Draft Search</a></li><li class="with-js"><a href="/nba/draft/early_entry/by_year">Early Entrants</a></li><li class="with-js"><a href="/nba/draft/special_events">Special Events</a></li></ul>
</div>
<div style="float: left; width: 15em;">
<p style="text-decoration: underline; padding: 0.3em 0.8em; margin-bottom: 0;"><a href="/nba/scores">Games</a></p>
<ul class="primary-nav-col" style="font-weight: normal;">
<li class="with-js"><a href="/nba/scores">Scores</a></li><li class="with-js"><a href="/nba/schedules">Schedules</a></li><li class="with-js"><a href="/nba/standings">Standings</a></li><li class="with-js"><a href="/nba/venues">Venues</a></li></ul>
<p style="text-decoration: underline; padding: 0.3em 0.8em; margin-bottom: 0;">Events</p>
<ul class="primary-nav-col" style="font-weight: normal;">
<li class="with-js"><a href="/nba/preseason">Preseason</a></li><li class="with-js"><a href="/nba/summer">Summer League</a></li><li class="with-js"><a href="/nba/regular_season/history">Regular Season</a></li><li class="with-js"><a href="/nba/nba-cup">NBA Cup</a></li><li class="with-js"><a href="/nba/allstar">All-Star Weekend</a></li><li class="with-js"><a href="/nba/playoffs">Playoffs</a></li><li class="with-js"><a href="/nba/draft">NBA Draft</a></li></ul>
<p style="text-decoration: underline; padding: 0.3em 0.8em; margin-bottom: 0;"><a href="/nba/info/salary_cap">Salary Cap</a></p>
<ul class="primary-nav-col" style="font-weight: normal;">
<li class="with-js"><a href="/nba/info/salary_cap">Salary Cap History</a></li><li class="with-js"><a href="/nba/info/minimum_scale">Minimum Scale</a></li><li class="with-js"><a href="/nba/info/rookie_scale">Rookie Scale</a></li><li class="with-js"><a href="http://www.cbafaq.com/salarycap.htm" target="_blank">NBA Salary Cap FAQ</a></li></ul>
</div>
<div style="clear: both;"></div>
</div>
</li><li class="has-subnav with-js">
<a href="/nba/stats">Stats</a>
<div class="primary-nav-ddl">
<ul class="primary-nav-col" style="width: 15em; float: left;">
<li class="with-js"><a href="/nba/stats">Player Stats</a></li><li class="with-js"><a href="/nba/team-stats">Team Stats</a></li><li class="with-js"><a href="/nba/individual-games">Individual Games</a></li><li class="with-js"><a href="/nba/individual-seasons">Individual Seasons</a></li><li class="with-js"><a href="/nba/daily-leaders">Daily Leaders</a></li></ul>
<ul class="primary-nav-col" style="width: 15em; float: left;">
<li class="with-js"><a href="/nba/stats/2024/Averages/Qualified/points/All/desc/1/Playoffs">Playoff Stats</a></li><li class="with-js"><a href="/nba/stats/2024/Averages/Qualified/points/All/desc/1/Preseason">Preseason Stats</a></li><li class="with-js"><a href="/nba/stats/2024/Averages/Qualified/points/All/desc/1/Summer_League">Summer League Stats</a></li></ul>
<ul class="primary-nav-col" style="width: 15em; float: left;">
<li class="with-js"><a href="/nba/stats/2024/Advanced_Stats/Qualified/points/All/desc/1/Regular_Season">Advanced Stats</a></li><li class="with-js"><a href="/nba/stats/2024/Misc_Stats/Qualified/per/All/desc/1/Regular_Season">Misc. Stats</a></li></ul>
<ul class="primary-nav-col" style="width: 15em; float: left;">
<li class="with-js"><a href="/nba/team-stats/2024/Advanced_Stats/Team_Totals/Regular_Season/ediff/desc">Team Net Rating</a></li><li class="with-js"><a href="/nba/team-stats/2024/Advanced_Stats/Team_Totals/Regular_Season/ortg/desc">Offensive Efficiency</a></li><li class="with-js"><a href="/nba/team-stats/2024/Advanced_Stats/Team_Totals/Regular_Season/drtg/desc">Defensive Efficiency</a></li></ul>
<div style="clear: both;"></div>
</div>
</li><li class="with-js"><a href="/nba/scores">Scores</a></li><li class="with-js">
<a href="/tradechecker">Trade Checker</a>
<div class="primary-nav-ddl">
<div id="tcwrapper">
<h2 style="font-weight: bold;">RealGM Trade Checker™</h2>
<ul id="checkerNav" class="threeStep" style="margin: 1em 0;">
<li class="current with-js"><em>Step 1: Select the Teams</em><span>Choose at least two teams from the menus below to start your trade.</span></li><li class="with-js"><em>Step 2: Choose the Players</em><span>Select the players you wish to trade from the rosters below.</span></li><li class="mainNavNoBg with-js"><em>Step 3: Verify the Trade</em><span>Confirm that your trade proposal is valid according to the NBA collective bargaining agreement.</span></li></ul><form method="post" action="/tradechecker/select_player">
<div class="selectwrap">
<div class="bluehead" style="font-weight: bold;">Team One *</div>
<div class="bluebody" style="font-weight: normal;">Select the first team from the drop down menu.<br><br>
<select name="team1">
<option></option>
<option value="1" selected="">Atlanta</option>
<option value="2">Boston</option>
<option value="38">Brooklyn</option>
<option value="3">Charlotte</option>
<option value="4">Chicago</option>
<option value="5">Cleveland</option>
<option value="6">Dallas</option>
<option value="7">Denver</option>
<option value="8">Detroit</option>
<option value="9">Golden State</option>
<option value="10">Houston</option>
<option value="11">Indiana</option>
<option value="12">L.A. Clippers</option>
<option value="13">L.A. Lakers</option>
<option value="14">Memphis</option>
<option value="15">Miami</option>
<option value="16">Milwaukee</option>
<option value="17">Minnesota</option>
<option value="19">New Orleans</option>
<option value="20">New York</option>
<option value="33">Oklahoma City</option>
<option value="21">Orlando</option>
<option value="22">Philadelphia</option>
<option value="23">Phoenix</option>
<option value="24">Portland</option>
<option value="25">Sacramento</option>
<option value="26">San Antonio</option>
<option value="28">Toronto</option>
<option value="29">Utah</option>
<option value="30">Washington</option>
</select>
</div>
</div>
<div class="selectwrap">
<div class="bluehead">Team Two *</div>
<div class="bluebody">Select the second team from the drop down menu.<br><br>
<select name="team2">
<option></option>
<option value="1">Atlanta</option>
<option value="2" selected="">Boston</option>
<option value="38">Brooklyn</option>
<option value="3">Charlotte</option>
<option value="4">Chicago</option>
<option value="5">Cleveland</option>
<option value="6">Dallas</option>
<option value="7">Denver</option>
<option value="8">Detroit</option>
<option value="9">Golden State</option>
<option value="10">Houston</option>
<option value="11">Indiana</option>
<option value="12">L.A. Clippers</option>
<option value="13">L.A. Lakers</option>
<option value="14">Memphis</option>
<option value="15">Miami</option>
<option value="16">Milwaukee</option>
<option value="17">Minnesota</option>
<option value="19">New Orleans</option>
<option value="20">New York</option>
<option value="33">Oklahoma City</option>
<option value="21">Orlando</option>
<option value="22">Philadelphia</option>
<option value="23">Phoenix</option>
<option value="24">Portland</option>
<option value="25">Sacramento</option>
<option value="26">San Antonio</option>
<option value="28">Toronto</option>
<option value="29">Utah</option>
<option value="30">Washington</option>
</select>
</div>
</div>
<div class="selectwrap">
<div class="bluehead">Team Three</div>
<div class="bluebody">Select the third team from the drop down menu.<br><br>
<select name="team3">
<option></option>
<option value="1">Atlanta</option>
<option value="2">Boston</option>
<option value="38">Brooklyn</option>
<option value="3">Charlotte</option>
<option value="4">Chicago</option>
<option value="5">Cleveland</option>
<option value="6">Dallas</option>
<option value="7">Denver</option>
<option value="8">Detroit</option>
<option value="9">Golden State</option>
<option value="10">Houston</option>
<option value="11">Indiana</option>
<option value="12">L.A. Clippers</option>
<option value="13">L.A. Lakers</option>
<option value="14">Memphis</option>
<option value="15">Miami</option>
<option value="16">Milwaukee</option>
<option value="17">Minnesota</option>
<option value="19">New Orleans</option>
<option value="20">New York</option>
<option value="33">Oklahoma City</option>
<option value="21">Orlando</option>
<option value="22">Philadelphia</option>
<option value="23">Phoenix</option>
<option value="24">Portland</option>
<option value="25">Sacramento</option>
<option value="26">San Antonio</option>
<option value="28">Toronto</option>
<option value="29">Utah</option>
<option value="30">Washington</option>
</select>
</div>
</div>
<div class="selectwrap">
<div class="bluehead">Team Four</div>
<div class="bluebody">Select the fourth team from the drop down menu.<br><br>
<select name="team4">
<option></option>
<option value="1">Atlanta</option>
<option value="2">Boston</option>
<option value="38">Brooklyn</option>
<option value="3">Charlotte</option>
<option value="4">Chicago</option>
<option value="5">Cleveland</option>
<option value="6">Dallas</option>
<option value="7">Denver</option>
<option value="8">Detroit</option>
<option value="9">Golden State</option>
<option value="10">Houston</option>
<option value="11">Indiana</option>
<option value="12">L.A. Clippers</option>
<option value="13">L.A. Lakers</option>
<option value="14">Memphis</option>
<option value="15">Miami</option>
<option value="16">Milwaukee</option>
<option value="17">Minnesota</option>
<option value="19">New Orleans</option>
<option value="20">New York</option>
<option value="33">Oklahoma City</option>
<option value="21">Orlando</option>
<option value="22">Philadelphia</option>
<option value="23">Phoenix</option>
<option value="24">Portland</option>
<option value="25">Sacramento</option>
<option value="26">San Antonio</option>
<option value="28">Toronto</option>
<option value="29">Utah</option>
<option value="30">Washington</option>
</select>
</div>
</div>
<div class="buttons"><input type="submit" value="Continue" class="pushbutton"></div>
</form>
<div class="clearfloat">&nbsp;</div>
</div>
</div>
</li><li class="with-js"><a href="https://www.vividseats.com/nba-basketball/?wsUser=958" target="_blank">Tickets</a></li>
<li class="has-subnav with-js">
<a href="/nba/odds">Odds</a>
<div class="primary-nav-ddl">
<ul class="primary-nav-col" style="width: 15em; float: left;">
<li class="with-js"><a href="/nba/odds">Betting Preview</a></li><li class="with-js"><a href="/nba/how-to-watch">How To Watch</a></li><li class="with-js"><a href="/nba/injuries">Injury Report</a></li><li class="with-js"><a href="/nba/stat-leaders">Stat Leaders</a></li><li class="with-js"><a href="/nba/day-preview-best-best">Best Bets</a></li><li class="with-js"><a href="/nba/player-props">Player Props</a></li><li class="with-js"><a href="/nba/award-futures">Awards</a></li><li class="with-js"><a href="/nba/team-futures">Team Futures</a></li></ul>
<div class="portal" style="float: left; border-left: 1px solid black; padding-left: 1em; max-width: 50em;">
<div class="secondary-story-container" style="border-top: 0;"><div class="secondary-story">
<a class="article-image" href="https://basketball.realgm.com/nba/odds/6789/nba-injury-news-2-15-2024" style="background-image: url('https://cdn.dataskrive.com/api/asset/rJSC7Fj.jpg');"></a>
<div class="article-title"><a style="padding-left: 0;" href="https://basketball.realgm.com/nba/odds/6789/nba-injury-news-2-15-2024">NBA Injury Report Today: Thursday, February 15</a></div>
<div class="article-content" style="font-weight: normal;">Stay in the loop with our daily NBA injury report for Thursday, February 15, with active/inactive lists for every game.</div>
</div>
<div class="secondary-story">
<a class="article-image" href="https://basketball.realgm.com/nba/odds/6684/rebounds-leaders" style="background-image: url('https://cdn.dataskrive.com/api/asset/c56iRFB.jpg');"></a>
<div class="article-title"><a style="padding-left: 0;" href="https://basketball.realgm.com/nba/odds/6684/rebounds-leaders">Who Led the NBA in Rebounds Yesterday?</a></div>
<div class="article-content" style="font-weight: normal;">See who filled up the stat sheet on Wednesday, with NBA rebounds leaders for February 14.</div>
</div>
<div class="secondary-story">
<a class="article-image" href="https://basketball.realgm.com/nba/odds/6683/blocks-leaders" style="background-image: url('https://cdn.dataskrive.com/api/asset/ToW061R.jpg');"></a>
<div class="article-title"><a style="padding-left: 0;" href="https://basketball.realgm.com/nba/odds/6683/blocks-leaders">Who Led the NBA in Blocks Yesterday?</a></div>
<div class="article-content" style="font-weight: normal;">See who filled up the stat sheet on Wednesday, with NBA blocks leaders for February 14.</div>
</div>
<div class="secondary-story">
<a class="article-image" href="https://basketball.realgm.com/nba/odds/6682/assists-leaders" style="background-image: url('https://cdn.dataskrive.com/api/asset/rlMwJvW.jpg');"></a>
<div class="article-title"><a style="padding-left: 0;" href="https://basketball.realgm.com/nba/odds/6682/assists-leaders">Who Led the NBA in Assists Yesterday?</a></div>
<div class="article-content" style="font-weight: normal;">See who filled up the stat sheet on Wednesday, with NBA assists leaders for February 14.</div>
</div>
</div>
</div>
<div style="clear: both;"></div>
</div>
</li></ul>
</nav>
<div class="second-level-nav-container">
<nav id="second-level-nav" role="navigation" class="container">
<ul class="level-1">
<li class="search-nav">
<form action="/search" method="get" class="searchbox" autocomplete="off">
<input type="text" class="searchbox-text ui-autocomplete-input" placeholder="Search..." name="q" required="required" autocomplete="off"><input type="submit" class="searchbox-submit" value="Go">
</form>
</li>
<li class="mobile-menu"><a href="javascript: void(0);" onclick="showPrimaryNav();"><span>« NBA Menu</span></a></li><li><a href="/nba/teams/Chicago-Bulls/4/Home"><span>Bulls</span></a></li><li><a href="https://forums.realgm.com/boards/viewforum.php?f=10"><span>Forum</span></a></li><li><a href="/nba/teams/Chicago-Bulls/4/news/wiretap"><span>News</span></a></li><li class="has-subnav with-js">
<a href="/nba/teams/Chicago-Bulls/4/Rosters/Regular"><span class="down">Rosters</span></a>
<ul class="level-2">
<li><a href="/nba/teams/Chicago-Bulls/4/Rosters/Regular">Regular Season</a></li><li><a href="/nba/teams/Chicago-Bulls/4/Rosters/Playoff">Playoff</a></li><li><a href="/nba/teams/Chicago-Bulls/4/Rosters/Opening_Day">Opening Day</a></li><li><a href="/nba/teams/Chicago-Bulls/4/Rosters/Training_Camp">Training Camp</a></li><li><a href="/nba/teams/Chicago-Bulls/4/Rosters/Summer_League">Summer League</a></li><li><a href="/nba/teams/Chicago-Bulls/4/Rosters/Preseason">Preseason</a></li></ul>
</li><li><a href="/nba/players/2024/Chicago-Bulls/4"><span>Players</span></a></li><li><a href="/nba/teams/Chicago-Bulls/4/Schedule"><span>Schedule</span></a></li><li class="has-subnav with-js">
<a href="/nba/teams/Chicago-Bulls/4/Stats" class="selected"><span class="down">Stats</span></a>
<ul class="level-2">
<li><a href="/nba/teams/Chicago-Bulls/4/Stats">Player Stats</a></li><li><a href="/nba/teams/Chicago-Bulls/4/individual-games">Individual Games</a></li><li><a href="/nba/teams/Chicago-Bulls/4/individual-seasons">Individual Seasons</a></li></ul>
</li><li><a href="/nba/teams/Chicago-Bulls/4/depth-charts"><span>Depth Charts</span></a></li><li class="has-subnav with-js">
<a href="/nba/teams/Chicago-Bulls/4/Awards/Season"><span class="down">Awards</span></a>
<ul class="level-2">
<li><a href="/nba/teams/Chicago-Bulls/4/Awards/Season">Awards By Season</a></li><li><a href="/nba/teams/Chicago-Bulls/4/Awards/Type">Awards By Type</a></li><li><a href="/nba/teams/Chicago-Bulls/4/Awards/All_Stars">All-Stars</a></li><li><a href="/nba/teams/Chicago-Bulls/4/Awards/Rising_Stars_Challenge">Rising Stars Challenge</a></li><li><a href="/nba/teams/Chicago-Bulls/4/Awards/Three_Point_Participants">3 Point Contest</a></li><li><a href="/nba/teams/Chicago-Bulls/4/Awards/Dunk_Comp_Participants">Dunk Contest</a></li><li><a href="/nba/teams/Chicago-Bulls/4/Awards/Skill_Challenge_Participants">Skills Contest</a></li></ul>
</li><li class="has-subnav with-js">
<a href="/nba/teams/Chicago-Bulls/4/Free_Agency/Future"><span class="down">Free Agency</span></a>
<ul class="level-2">
<li><a href="/nba/teams/Chicago-Bulls/4/Free_Agency/Future">Future Free Agents</a></li><li><a href="/nba/teams/Chicago-Bulls/4/Free_Agency/Current">Current Free Agents</a></li><li><a href="/nba/teams/Chicago-Bulls/4/Free_Agency/Options">Contract Options</a></li><li><a href="/nba/player_tracker/free_agent/Chicago-Bulls/4">Free Agent Tracker</a></li><li><a href="/nba/player_tracker/trade/Chicago-Bulls/4">Trade Tracker</a></li></ul>
</li><li class="has-subnav with-js">
<a href="/nba/teams/Chicago-Bulls/4/Transaction-History"><span class="down">History</span></a>
<ul class="level-2">
<li><a href="/nba/teams/Chicago-Bulls/4/DLeague-Transactions">G League Transactions</a></li><li><a href="/nba/teams/Chicago-Bulls/4/Draft-History">Draft History</a></li><li><a href="/nba/teams/Chicago-Bulls/4/Hall-of-Fame">Hall of Fame</a></li><li><a href="/nba/teams/Chicago-Bulls/4/Lottery-History">Lottery History</a></li><li><a href="/nba/teams/Chicago-Bulls/4/offseason">Offseason Recap</a></li><li><a href="/nba/teams/Chicago-Bulls/4/Playoff-History">Playoff History</a></li><li><a href="/nba/teams/Chicago-Bulls/4/Regular-Season-History">Regular Season History</a></li><li><a href="/nba/teams/Chicago-Bulls/4/Retired-Numbers">Retired Jerseys</a></li><li><a href="/nba/teams/Chicago-Bulls/4/roster-turnover">Roster Turnover</a></li><li><a href="/nba/teams/Chicago-Bulls/4/staff-members">Staff &amp; Executives</a></li><li><a href="/nba/teams/Chicago-Bulls/4/Transaction-History">Transactions History</a></li><li><a href="/nba/teams/Chicago-Bulls/4/trade-deadline">Trade Deadline</a></li></ul>
</li><li><a href="https://www.vividseats.com/nba-basketball/chicago-bulls-tickets.html?wsUser=958" target="_blank"><span>Tickets</span></a></li>
</ul>
</nav>
</div>
</div>
</div>
<div id="teamnav" class="clearfix"><div class="container"><ul class="clearfix"><li>
<a href="/nba/teams/Atlanta-Hawks/1/Stats/2024/Averages/All/minutes/All/desc/1/Home">
ATL
</a>
</li>
<li>
<a href="/nba/teams/Boston-Celtics/2/Stats/2024/Averages/All/minutes/All/desc/1/Home">
BOS
</a>
</li>
<li>
<a href="/nba/teams/Brooklyn-Nets/38/Stats/2024/Averages/All/minutes/All/desc/1/Home">
BRK
</a>
</li>
<li>
<a href="/nba/teams/Charlotte-Hornets/3/Stats/2024/Averages/All/minutes/All/desc/1/Home">
CHA
</a>
</li>
<li>
<a href="/nba/teams/Chicago-Bulls/4/Stats/2024/Averages/All/minutes/All/desc/1/Home">
CHI
</a>
</li>
<li>
<a href="/nba/teams/Cleveland-Cavaliers/5/Stats/2024/Averages/All/minutes/All/desc/1/Home">
CLE
</a>
</li>
<li>
<a href="/nba/teams/Dallas-Mavericks/6/Stats/2024/Averages/All/minutes/All/desc/1/Home">
DAL
</a>
</li>
<li>
<a href="/nba/teams/Denver-Nuggets/7/Stats/2024/Averages/All/minutes/All/desc/1/Home">
DEN
</a>
</li>
<li>
<a href="/nba/teams/Detroit-Pistons/8/Stats/2024/Averages/All/minutes/All/desc/1/Home">
DET
</a>
</li>
<li>
<a href="/nba/teams/Golden-State-Warriors/9/Stats/2024/Averages/All/minutes/All/desc/1/Home">
GOS
</a>
</li>
<li>
<a href="/nba/teams/Houston-Rockets/10/Stats/2024/Averages/All/minutes/All/desc/1/Home">
HOU
</a>
</li>
<li>
<a href="/nba/teams/Indiana-Pacers/11/Stats/2024/Averages/All/minutes/All/desc/1/Home">
IND
</a>
</li>
<li>
<a href="/nba/teams/Los-Angeles-Clippers/12/Stats/2024/Averages/All/minutes/All/desc/1/Home">
LAC
</a>
</li>
<li>
<a href="/nba/teams/Los-Angeles-Lakers/13/Stats/2024/Averages/All/minutes/All/desc/1/Home">
LAL
</a>
</li>
<li>
<a href="/nba/teams/Memphis-Grizzlies/14/Stats/2024/Averages/All/minutes/All/desc/1/Home">
MEM
</a>
</li>
<li>
<a href="/nba/teams/Miami-Heat/15/Stats/2024/Averages/All/minutes/All/desc/1/Home">
MIA
</a>
</li>
<li>
<a href="/nba/teams/Milwaukee-Bucks/16/Stats/2024/Averages/All/minutes/All/desc/1/Home">
MIL
</a>
</li>
<li>
<a href="/nba/teams/Minnesota-Timberwolves/17/Stats/2024/Averages/All/minutes/All/desc/1/Home">
MIN
</a>
</li>
<li>
<a href="/nba/teams/New-Orleans-Pelicans/19/Stats/2024/Averages/All/minutes/All/desc/1/Home">
NOP
</a>
</li>
<li>
<a href="/nba/teams/New-York-Knicks/20/Stats/2024/Averages/All/minutes/All/desc/1/Home">
NYK
</a>
</li>
<li>
<a href="/nba/teams/Oklahoma-City-Thunder/33/Stats/2024/Averages/All/minutes/All/desc/1/Home">
OKC
</a>
</li>
<li>
<a href="/nba/teams/Orlando-Magic/21/Stats/2024/Averages/All/minutes/All/desc/1/Home">
ORL
</a>
</li>
<li>
<a href="/nba/teams/Philadelphia-Sixers/22/Stats/2024/Averages/All/minutes/All/desc/1/Home">
PHL
</a>
</li>
<li>
<a href="/nba/teams/Phoenix-Suns/23/Stats/2024/Averages/All/minutes/All/desc/1/Home">
PHX
</a>
</li>
<li>
<a href="/nba/teams/Portland-Trail-Blazers/24/Stats/2024/Averages/All/minutes/All/desc/1/Home">
POR
</a>
</li>
<li>
<a href="/nba/teams/Sacramento-Kings/25/Stats/2024/Averages/All/minutes/All/desc/1/Home">
SAC
</a>
</li>
<li>
<a href="/nba/teams/San-Antonio-Spurs/26/Stats/2024/Averages/All/minutes/All/desc/1/Home">
SAN
</a>
</li>
<li>
<a href="/nba/teams/Toronto-Raptors/28/Stats/2024/Averages/All/minutes/All/desc/1/Home">
TOR
</a>
</li>
<li>
<a href="/nba/teams/Utah-Jazz/29/Stats/2024/Averages/All/minutes/All/desc/1/Home">
UTH
</a>
</li>
<li>
<a href="/nba/teams/Washington-Wizards/30/Stats/2024/Averages/All/minutes/All/desc/1/Home">
WAS
</a>
</li>
</ul></div></div>            
         </div>
         
         <div id="header_helper" class="large_header_helper" style="display: block;"></div>

         <div class="main-container">
            
            <div class="main wrapper clearfix container" style="position: relative;">
            
               <div style="text-align: center; margin: 0 1em 1em 1em;"><div data-aaad="true" data-aa-adunit="/22181265/realgm_970v_1"></div></div><div style="text-align: center; margin: 1em 0 1em 0;"><div data-aaad="true" data-aa-adunit="/22181265/realgm_mob_320v_1"></div></div><h2 class="page_title">1991-1992 Chicago Bulls Stats
</h2>
<div class="page-navigation open">
<div class="clearfix nav-title">
<a href="javascript:void(0);" onclick="togglePageNavigation();">Change settings?</a></div>
<div class="page-nav-option clearfix">
<label>Season:</label>
<select onchange="open_network(this.options[this.selectedIndex].value)" class="ddl">
<option value="/nba/teams/Chicago-Bulls/4/Stats/2024/Averages/All/minutes/All/desc/1/Home">2023-2024</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/2023/Averages/All/minutes/All/desc/1/Home">2022-2023</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/2022/Averages/All/minutes/All/desc/1/Home">2021-2022</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/2021/Averages/All/minutes/All/desc/1/Home">2020-2021</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/2020/Averages/All/minutes/All/desc/1/Home">2019-2020</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/2019/Averages/All/minutes/All/desc/1/Home">2018-2019</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/2018/Averages/All/minutes/All/desc/1/Home">2017-2018</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/2017/Averages/All/minutes/All/desc/1/Home">2016-2017</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/2016/Averages/All/minutes/All/desc/1/Home">2015-2016</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/2015/Averages/All/minutes/All/desc/1/Home">2014-2015</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/2014/Averages/All/minutes/All/desc/1/Home">2013-2014</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/2013/Averages/All/minutes/All/desc/1/Home">2012-2013</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/2012/Averages/All/minutes/All/desc/1/Home">2011-2012</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/2011/Averages/All/minutes/All/desc/1/Home">2010-2011</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/2010/Averages/All/minutes/All/desc/1/Home">2009-2010</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/2009/Averages/All/minutes/All/desc/1/Home">2008-2009</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/2008/Averages/All/minutes/All/desc/1/Home">2007-2008</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/2007/Averages/All/minutes/All/desc/1/Home">2006-2007</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/2006/Averages/All/minutes/All/desc/1/Home">2005-2006</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/2005/Averages/All/minutes/All/desc/1/Home">2004-2005</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/2004/Averages/All/minutes/All/desc/1/Home">2003-2004</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/2003/Averages/All/minutes/All/desc/1/Home">2002-2003</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/2002/Averages/All/minutes/All/desc/1/Home">2001-2002</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/2001/Averages/All/minutes/All/desc/1/Home">2000-2001</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/2000/Averages/All/minutes/All/desc/1/Home">1999-2000</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1999/Averages/All/minutes/All/desc/1/Home">1998-1999</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1998/Averages/All/minutes/All/desc/1/Home">1997-1998</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1997/Averages/All/minutes/All/desc/1/Home">1996-1997</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1996/Averages/All/minutes/All/desc/1/Home">1995-1996</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1995/Averages/All/minutes/All/desc/1/Home">1994-1995</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1994/Averages/All/minutes/All/desc/1/Home">1993-1994</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1993/Averages/All/minutes/All/desc/1/Home">1992-1993</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/minutes/All/desc/1/Home" selected="selected">1991-1992</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1991/Averages/All/minutes/All/desc/1/Home">1990-1991</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1990/Averages/All/minutes/All/desc/1/Home">1989-1990</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1989/Averages/All/minutes/All/desc/1/Home">1988-1989</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1988/Averages/All/minutes/All/desc/1/Home">1987-1988</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1987/Averages/All/minutes/All/desc/1/Home">1986-1987</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1986/Averages/All/minutes/All/desc/1/Home">1985-1986</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1985/Averages/All/minutes/All/desc/1/Home">1984-1985</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1984/Averages/All/minutes/All/desc/1/Home">1983-1984</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1983/Averages/All/minutes/All/desc/1/Home">1982-1983</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1982/Averages/All/minutes/All/desc/1/Home">1981-1982</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1981/Averages/All/minutes/All/desc/1/Home">1980-1981</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1980/Averages/All/minutes/All/desc/1/Home">1979-1980</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1979/Averages/All/minutes/All/desc/1/Home">1978-1979</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1978/Averages/All/minutes/All/desc/1/Home">1977-1978</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1977/Averages/All/minutes/All/desc/1/Home">1976-1977</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1976/Averages/All/minutes/All/desc/1/Home">1975-1976</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1975/Averages/All/minutes/All/desc/1/Home">1974-1975</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1974/Averages/All/minutes/All/desc/1/Home">1973-1974</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1973/Averages/All/minutes/All/desc/1/Home">1972-1973</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1972/Averages/All/minutes/All/desc/1/Home">1971-1972</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1971/Averages/All/minutes/All/desc/1/Home">1970-1971</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1970/Averages/All/minutes/All/desc/1/Home">1969-1970</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1969/Averages/All/minutes/All/desc/1/Home">1968-1969</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1968/Averages/All/minutes/All/desc/1/Home">1967-1968</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1967/Averages/All/minutes/All/desc/1/Home">1966-1967</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/Historical/Averages/All/minutes/All/desc/1/Home">Historical</option><option value="/nba/teams/Chicago-Bulls/4/Stats/Historical_Active/Averages/All/minutes/All/desc/1/Home">Historical Active</option></select></div>
<div class="page-nav-option clearfix">
<label>Team:</label>
<select onchange="open_network(this.options[this.selectedIndex].value)" class="ddl">
<option value="/nba/stats/1992/Averages/All/minutes/All/desc/1/Home">Entire NBA</option>
<option value="/nba/teams/Atlanta-Hawks/1/stats/1992/Averages/All/minutes/All/desc/1/Home">Atlanta Hawks</option>
<option value="/nba/teams/Boston-Celtics/2/stats/1992/Averages/All/minutes/All/desc/1/Home">Boston Celtics</option>
<option value="/nba/teams/Brooklyn-Nets/38/stats/1992/Averages/All/minutes/All/desc/1/Home">Brooklyn Nets</option>
<option value="/nba/teams/Charlotte-Hornets/3/stats/1992/Averages/All/minutes/All/desc/1/Home">Charlotte Hornets</option>
<option selected="selected" value="/nba/teams/Chicago-Bulls/4/stats/1992/Averages/All/minutes/All/desc/1/Home">Chicago Bulls</option>
<option value="/nba/teams/Cleveland-Cavaliers/5/stats/1992/Averages/All/minutes/All/desc/1/Home">Cleveland Cavaliers</option>
<option value="/nba/teams/Dallas-Mavericks/6/stats/1992/Averages/All/minutes/All/desc/1/Home">Dallas Mavericks</option>
<option value="/nba/teams/Denver-Nuggets/7/stats/1992/Averages/All/minutes/All/desc/1/Home">Denver Nuggets</option>
<option value="/nba/teams/Detroit-Pistons/8/stats/1992/Averages/All/minutes/All/desc/1/Home">Detroit Pistons</option>
<option value="/nba/teams/Golden-State-Warriors/9/stats/1992/Averages/All/minutes/All/desc/1/Home">Golden State Warriors</option>
<option value="/nba/teams/Houston-Rockets/10/stats/1992/Averages/All/minutes/All/desc/1/Home">Houston Rockets</option>
<option value="/nba/teams/Indiana-Pacers/11/stats/1992/Averages/All/minutes/All/desc/1/Home">Indiana Pacers</option>
<option value="/nba/teams/Los-Angeles-Clippers/12/stats/1992/Averages/All/minutes/All/desc/1/Home">Los Angeles Clippers</option>
<option value="/nba/teams/Los-Angeles-Lakers/13/stats/1992/Averages/All/minutes/All/desc/1/Home">Los Angeles Lakers</option>
<option value="/nba/teams/Memphis-Grizzlies/14/stats/1992/Averages/All/minutes/All/desc/1/Home">Memphis Grizzlies</option>
<option value="/nba/teams/Miami-Heat/15/stats/1992/Averages/All/minutes/All/desc/1/Home">Miami Heat</option>
<option value="/nba/teams/Milwaukee-Bucks/16/stats/1992/Averages/All/minutes/All/desc/1/Home">Milwaukee Bucks</option>
<option value="/nba/teams/Minnesota-Timberwolves/17/stats/1992/Averages/All/minutes/All/desc/1/Home">Minnesota Timberwolves</option>
<option value="/nba/teams/New-Orleans-Pelicans/19/stats/1992/Averages/All/minutes/All/desc/1/Home">New Orleans Pelicans</option>
<option value="/nba/teams/New-York-Knicks/20/stats/1992/Averages/All/minutes/All/desc/1/Home">New York Knicks</option>
<option value="/nba/teams/Oklahoma-City-Thunder/33/stats/1992/Averages/All/minutes/All/desc/1/Home">Oklahoma City Thunder</option>
<option value="/nba/teams/Orlando-Magic/21/stats/1992/Averages/All/minutes/All/desc/1/Home">Orlando Magic</option>
<option value="/nba/teams/Philadelphia-Sixers/22/stats/1992/Averages/All/minutes/All/desc/1/Home">Philadelphia Sixers</option>
<option value="/nba/teams/Phoenix-Suns/23/stats/1992/Averages/All/minutes/All/desc/1/Home">Phoenix Suns</option>
<option value="/nba/teams/Portland-Trail-Blazers/24/stats/1992/Averages/All/minutes/All/desc/1/Home">Portland Trail Blazers</option>
<option value="/nba/teams/Sacramento-Kings/25/stats/1992/Averages/All/minutes/All/desc/1/Home">Sacramento Kings</option>
<option value="/nba/teams/San-Antonio-Spurs/26/stats/1992/Averages/All/minutes/All/desc/1/Home">San Antonio Spurs</option>
<option value="/nba/teams/Toronto-Raptors/28/stats/1992/Averages/All/minutes/All/desc/1/Home">Toronto Raptors</option>
<option value="/nba/teams/Utah-Jazz/29/stats/1992/Averages/All/minutes/All/desc/1/Home">Utah Jazz</option>
<option value="/nba/teams/Washington-Wizards/30/stats/1992/Averages/All/minutes/All/desc/1/Home">Washington Wizards</option>
</select></div>
<div class="page-nav-option clearfix">
<label>Stat Type:</label>
<select onchange="open_network(this.options[this.selectedIndex].value)" class="ddl">
<option value="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/minutes/All/desc/1/Home" selected="selected">Averages</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1992/Totals/All/minutes/All/desc/1/Home">Totals</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1992/Per_48/All/minutes/All/desc/1/Home">Per 48</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1992/Per_40/All/minutes/All/desc/1/Home">Per 40</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1992/Per_36/All/minutes/All/desc/1/Home">Per 36</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1992/Per_Minute/All/minutes/All/desc/1/Home">Per Minute</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1992/Minute_Per/All/minutes/All/desc/1/Home">Minute Per</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1992/Misc_Stats/All/minutes/All/desc/1/Home">Misc. Stats</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1992/Advanced_Stats/All/minutes/All/desc/1/Home">Advanced Stats</option>
</select></div>
<div class="page-nav-option clearfix">
<label>Games:</label>
<select onchange="open_network(this.options[this.selectedIndex].value)" class="ddl">
<option value="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/minutes/All/desc/1/Regular_Season" selected="selected">Regular Season</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/minutes/All/desc/1/Playoffs">Playoffs</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/minutes/All/desc/1/Summer_League">Summer League</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/minutes/All/desc/1/Preseason">Preseason</option>
</select></div>
<div class="page-nav-option clearfix">
<label>Stat Split:</label>
<select onchange="open_network(this.options[this.selectedIndex].value)" class="ddl">
<option value="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/minutes/All/desc/1/Regular_Season">Entire Season</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/minutes/All/desc/1/Home" selected="selected">Home</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/minutes/All/desc/1/Away">Away</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/minutes/All/desc/1/Wins">Wins</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/minutes/All/desc/1/Losses">Losses</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/minutes/All/desc/1/Last_5_Games">Last 5 Games</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/minutes/All/desc/1/Last_10_Games">Last 10 Games</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/minutes/All/desc/1/Starting_Lineup">Starting Lineup</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/minutes/All/desc/1/In_Rotation">In Rotation</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/minutes/All/desc/1/Limited_Playing_Time">Limited Playing Time</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/minutes/All/desc/1/Opponent_Bottom_10_Defense">Opponent Bottom 10 Defense</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/minutes/All/desc/1/Opponent_Bottom_10_Record">Opponent Bottom 10 Record</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/minutes/All/desc/1/Opponent_Top_10_Defense">Opponent Top 10 Defense</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/minutes/All/desc/1/Opponent_Top_10_Record">Opponent Top 10 Record</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/minutes/All/desc/1/Eastern_Conference">Eastern Conference</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/minutes/All/desc/1/Western_Conference">Western Conference</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/minutes/All/desc/1/Atlantic_Division">Atlantic Division</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/minutes/All/desc/1/Central_Division">Central Division</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/minutes/All/desc/1/Northwest_Division">Northwest Division</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/minutes/All/desc/1/Pacific_Division">Pacific Division</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/minutes/All/desc/1/Southeast_Division">Southeast Division</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/minutes/All/desc/1/Southwest_Division">Southwest Division</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/minutes/All/desc/1/Post-All-Star_Game">Post-All-Star Game</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/minutes/All/desc/1/Pre-All-Star_Game">Pre-All-Star Game</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/minutes/All/desc/1/October">October</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/minutes/All/desc/1/November">November</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/minutes/All/desc/1/December">December</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/minutes/All/desc/1/January">January</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/minutes/All/desc/1/February">February</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/minutes/All/desc/1/March">March</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/minutes/All/desc/1/April">April</option>
</select></div>
<div class="page-nav-option clearfix">
<label>Position:</label>
<select onchange="open_network(this.options[this.selectedIndex].value)" class="ddl">
<option value="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/minutes/All/desc/1/Home" selected="selected">All Positions</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/minutes/PG/desc/1/Home">PG</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/minutes/SG/desc/1/Home">SG</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/minutes/SF/desc/1/Home">SF</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/minutes/PF/desc/1/Home">PF</option>
<option value="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/minutes/C/desc/1/Home">C</option>
</select></div>
<div class="page-nav-option clearfix">
<input type="checkbox" id="qualified" onclick="open_network('/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/Qualified/minutes/All/desc/1/Home')"><label for="qualified" style="float:none; width: auto; margin-left:0.5em;">Qualified</label></div>
<div class="page-nav-option clearfix">
<input type="checkbox" id="rookies" onclick="changePositions('rookies')"><label for="rookies" style="float:none; width: auto; margin-left:0.5em;">Rookies</label></div>
<div class="page-nav-option clearfix">
<input type="checkbox" id="pace_adjustment" onclick="changePositions('pace_adjustment')"><label for="pace_adjustment" style="float:none; width: auto; margin-left:0.5em;">Pace Adjusted</label></div>
<div class="page-nav-option clearfix">
<a href="/info/glossary" target="_blank">Stats Legend</a></div>
</div>
<h2>
1991-1992 Chicago Bulls Home Leaders</h2>
<div class="overall-leader">
<div class="category-name">Points</div>
<div class="category-container" style="background-image: url('/images/nba/4.2/profiles/photos/2006/Jordan_Michael_nba.jpg'); background-repeat: no-repeat;"><div class="player-container clearfix"><span class="player-name"><a href="/player/Michael-Jordan/Summary/1192">Michael Jordan</a></span><span class="team-name"></span><span class="stat">27.9</span></div><div class="player-container clearfix"><span class="player-name"><a href="/player/Scottie-Pippen/Summary/725">Scottie Pippen</a></span><span class="team-name"></span><span class="stat">20.8</span></div><div class="player-container clearfix"><span class="player-name"><a href="/player/Horace-Grant/Summary/985">Horace Grant</a></span><span class="team-name"></span><span class="stat">14.0</span></div><div class="player-container clearfix"><span class="player-name"><a href="/player/BJ-Armstrong/Summary/1373">B.J. Armstrong</a></span><span class="team-name"></span><span class="stat">10.6</span></div><div class="player-container clearfix"><span class="player-name"><a href="/player/Bill-Cartwright/Summary/42872">Bill Cartwright</a></span><span class="team-name"></span><span class="stat">7.8</span></div></div></div><div class="overall-leader">
<div class="category-name">Rebounds</div>
<div class="category-container" style="background-image: url('/images/nba/4.2/profiles/photos/2006/Grant_Horace_lal.jpg'); background-repeat: no-repeat;"><div class="player-container clearfix"><span class="player-name"><a href="/player/Horace-Grant/Summary/985">Horace Grant</a></span><span class="team-name"></span><span class="stat">10.2</span></div><div class="player-container clearfix"><span class="player-name"><a href="/player/Scottie-Pippen/Summary/725">Scottie Pippen</a></span><span class="team-name"></span><span class="stat">7.6</span></div><div class="player-container clearfix"><span class="player-name"><a href="/player/Michael-Jordan/Summary/1192">Michael Jordan</a></span><span class="team-name"></span><span class="stat">5.9</span></div><div class="player-container clearfix"><span class="player-name"><a href="/player/Scott-Williams/Summary/705">Scott Williams</a></span><span class="team-name"></span><span class="stat">4.5</span></div><div class="player-container clearfix"><span class="player-name"><a href="/player/Bill-Cartwright/Summary/42872">Bill Cartwright</a></span><span class="team-name"></span><span class="stat">4.4</span></div></div></div><div class="overall-leader">
<div class="category-name">Assists</div>
<div class="category-container" style="background-image: url('/images/nba/4.2/profiles/photos/2006/Pippen_Scottie_nba.jpg'); background-repeat: no-repeat;"><div class="player-container clearfix"><span class="player-name"><a href="/player/Scottie-Pippen/Summary/725">Scottie Pippen</a></span><span class="team-name"></span><span class="stat">7.3</span></div><div class="player-container clearfix"><span class="player-name"><a href="/player/Michael-Jordan/Summary/1192">Michael Jordan</a></span><span class="team-name"></span><span class="stat">5.9</span></div><div class="player-container clearfix"><span class="player-name"><a href="/player/John-Paxson/Summary/42871">John Paxson</a></span><span class="team-name"></span><span class="stat">3.5</span></div><div class="player-container clearfix"><span class="player-name"><a href="/player/BJ-Armstrong/Summary/1373">B.J. Armstrong</a></span><span class="team-name"></span><span class="stat">3.5</span></div><div class="player-container clearfix"><span class="player-name"><a href="/player/Horace-Grant/Summary/985">Horace Grant</a></span><span class="team-name"></span><span class="stat">2.9</span></div></div></div><div class="overall-leader">
<div class="category-name">Blocks</div>
<div class="category-container" style="background-image: url('/images/nba/4.2/profiles/photos/2006/Grant_Horace_lal.jpg'); background-repeat: no-repeat;"><div class="player-container clearfix"><span class="player-name"><a href="/player/Horace-Grant/Summary/985">Horace Grant</a></span><span class="team-name"></span><span class="stat">1.7</span></div><div class="player-container clearfix"><span class="player-name"><a href="/player/Scottie-Pippen/Summary/725">Scottie Pippen</a></span><span class="team-name"></span><span class="stat">1.0</span></div><div class="player-container clearfix"><span class="player-name"><a href="/player/Michael-Jordan/Summary/1192">Michael Jordan</a></span><span class="team-name"></span><span class="stat">1.0</span></div><div class="player-container clearfix"><span class="player-name"><a href="/player/Scott-Williams/Summary/705">Scott Williams</a></span><span class="team-name"></span><span class="stat">0.6</span></div><div class="player-container clearfix"><span class="player-name"><a href="/player/Will-Perdue/Summary/1271">Will Perdue</a></span><span class="team-name"></span><span class="stat">0.6</span></div></div></div><div class="overall-leader">
<div class="category-name">Steals</div>
<div class="category-container" style="background-image: url('/images/nba/4.2/profiles/photos/2006/Jordan_Michael_nba.jpg'); background-repeat: no-repeat;"><div class="player-container clearfix"><span class="player-name"><a href="/player/Michael-Jordan/Summary/1192">Michael Jordan</a></span><span class="team-name"></span><span class="stat">2.4</span></div><div class="player-container clearfix"><span class="player-name"><a href="/player/Scottie-Pippen/Summary/725">Scottie Pippen</a></span><span class="team-name"></span><span class="stat">2.0</span></div><div class="player-container clearfix"><span class="player-name"><a href="/player/Horace-Grant/Summary/985">Horace Grant</a></span><span class="team-name"></span><span class="stat">1.5</span></div><div class="player-container clearfix"><span class="player-name"><a href="/player/Dennis-Hopson/Summary/45364">Dennis Hopson</a></span><span class="team-name"></span><span class="stat">1.0</span></div><div class="player-container clearfix"><span class="player-name"><a href="/player/John-Paxson/Summary/42871">John Paxson</a></span><span class="team-name"></span><span class="stat">0.7</span></div></div></div><div class="overall-leader">
<div class="category-name">Minutes</div>
<div class="category-container" style="background-image: url('/images/nba/4.2/profiles/photos/2006/Pippen_Scottie_nba.jpg'); background-repeat: no-repeat;"><div class="player-container clearfix"><span class="player-name"><a href="/player/Scottie-Pippen/Summary/725">Scottie Pippen</a></span><span class="team-name"></span><span class="stat">37.6</span></div><div class="player-container clearfix"><span class="player-name"><a href="/player/Michael-Jordan/Summary/1192">Michael Jordan</a></span><span class="team-name"></span><span class="stat">36.6</span></div><div class="player-container clearfix"><span class="player-name"><a href="/player/Horace-Grant/Summary/985">Horace Grant</a></span><span class="team-name"></span><span class="stat">34.5</span></div><div class="player-container clearfix"><span class="player-name"><a href="/player/BJ-Armstrong/Summary/1373">B.J. Armstrong</a></span><span class="team-name"></span><span class="stat">23.1</span></div><div class="player-container clearfix"><span class="player-name"><a href="/player/John-Paxson/Summary/42871">John Paxson</a></span><span class="team-name"></span><span class="stat">22.7</span></div></div></div><div style="clear: both;"></div><h2 class="border" style="margin-top: 0.5em;">
1991-1992 Chicago Bulls Home Stats - Averages</h2>
<div class="tablesaw-bar mode-swipe"><div class="tablesaw-modeswitch tablesaw-toolbar"><label>Col<span class="a11y-sm">umn</span>s:<span class="btn btn-small btn-select">Swipe<select><option value="stack">Stack</option><option selected="" value="swipe">Swipe</option></select></span></label></div><div class="tablesaw-advance"><a href="#" class="tablesaw-nav-btn btn btn-micro left disabled" title="Previous Column"></a><a href="#" class="tablesaw-nav-btn btn btn-micro right disabled" title="Next Column"></a></div></div><table class="tablesaw compact tablesaw-swipe" data-tablesaw-mode="swipe" data-tablesaw-mode-switch="" data-tablesaw-mode-exclude="columntoggle" id="table-2758" style="">
<thead>
<tr>
<th data-tablesaw-priority="persist" class="tablesaw-cell-persist">#</th>
<th data-tablesaw-priority="persist" class="tablesaw-cell-persist"><a href="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/player/All/desc/1/Home">Player</a></th>
<th>Team</th>
<th><a href="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/gp/All/desc/1/Home">GP</a></th>
<th data-tablesaw-sortable-default-col="" class="tablesaw-sortable-descending tablesaw-cell-persist" data-tablesaw-priority="persist"><a href="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/minutes/All/asc/1/Home">MPG</a></th>
<th><a href="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/points/All/desc/1/Home">PPG</a></th>
<th><a href="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/fgm/All/desc/1/Home">FGM</a></th>
<th><a href="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/fga/All/desc/1/Home">FGA</a></th>
<th><a href="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/fg_pct/All/desc/1/Home">FG%</a></th>
<th><a href="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/tpfgm/All/desc/1/Home">3PM</a></th>
<th><a href="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/tpfga/All/desc/1/Home">3PA</a></th>
<th><a href="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/tpfg_pct/All/desc/1/Home">3P%</a></th>
<th><a href="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/ftm/All/desc/1/Home">FTM</a></th>
<th><a href="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/fta/All/desc/1/Home">FTA</a></th>
<th><a href="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/ft_pct/All/desc/1/Home">FT%</a></th>
<th><a href="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/orb/All/desc/1/Home">ORB</a></th>
<th><a href="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/drb/All/desc/1/Home">DRB</a></th>
<th><a href="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/trb/All/desc/1/Home">RPG</a></th>
<th><a href="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/assists/All/desc/1/Home">APG</a></th>
<th><a href="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/steals/All/desc/1/Home">SPG</a></th>
<th><a href="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/blocks/All/desc/1/Home">BPG</a></th>
<th><a href="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/turnovers/All/desc/1/Home">TOV</a></th>
<th><a href="/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/fouls/All/desc/1/Home">PF</a></th>
</tr>
</thead>
<tbody>
<tr><td class="rank tablesaw-cell-persist">1</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Scottie-Pippen/Summary/725">Scottie Pippen</a></td><td><a href="/nba/teams/Chicago-Bulls/4/Home" title="Chicago Bulls">CHI</a></td><td>41</td><td class="tablesaw-cell-persist">37.6</td><td>20.8</td><td>8.4</td><td>16.1</td><td>.521</td><td>0.2</td><td>0.8</td><td>.212</td><td>3.8</td><td>4.9</td><td>.789</td><td>2.4</td><td>5.2</td><td>7.6</td><td>7.3</td><td>2.0</td><td>1.0</td><td>2.8</td><td>2.7</td></tr>
<tr><td class="rank tablesaw-cell-persist">2</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Michael-Jordan/Summary/1192">Michael Jordan</a></td><td><a href="/nba/teams/Chicago-Bulls/4/Home" title="Chicago Bulls">CHI</a></td><td>41</td><td class="tablesaw-cell-persist">36.6</td><td>27.9</td><td>10.9</td><td>20.8</td><td>.525</td><td>0.4</td><td>1.3</td><td>.291</td><td>5.7</td><td>6.6</td><td>.857</td><td>1.0</td><td>5.0</td><td>5.9</td><td>5.9</td><td>2.4</td><td>1.0</td><td>2.5</td><td>2.3</td></tr>
<tr><td class="rank tablesaw-cell-persist">3</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Horace-Grant/Summary/985">Horace Grant</a></td><td><a href="/nba/teams/Chicago-Bulls/4/Home" title="Chicago Bulls">CHI</a></td><td>40</td><td class="tablesaw-cell-persist">34.5</td><td>14.0</td><td>5.7</td><td>9.1</td><td>.623</td><td>0.0</td><td>0.0</td><td>.000</td><td>2.7</td><td>3.8</td><td>.702</td><td>4.1</td><td>6.1</td><td>10.2</td><td>2.9</td><td>1.5</td><td>1.7</td><td>1.2</td><td>2.4</td></tr>
<tr><td class="rank tablesaw-cell-persist">4</td><td class="nowrap tablesaw-cell-persist"><a href="/player/BJ-Armstrong/Summary/1373">B.J. Armstrong</a></td><td><a href="/nba/teams/Chicago-Bulls/4/Home" title="Chicago Bulls">CHI</a></td><td>41</td><td class="tablesaw-cell-persist">23.1</td><td>10.6</td><td>4.4</td><td>9.1</td><td>.483</td><td>0.4</td><td>1.0</td><td>.425</td><td>1.4</td><td>1.8</td><td>.819</td><td>0.2</td><td>1.4</td><td>1.7</td><td>3.5</td><td>0.6</td><td>0.1</td><td>1.2</td><td>1.1</td></tr>
<tr><td class="rank tablesaw-cell-persist">5</td><td class="nowrap tablesaw-cell-persist"><a href="/player/John-Paxson/Summary/42871">John Paxson</a></td><td><a href="/nba/teams/Chicago-Bulls/4/Home" title="Chicago Bulls">CHI</a></td><td>39</td><td class="tablesaw-cell-persist">22.7</td><td>7.1</td><td>3.3</td><td>6.0</td><td>.551</td><td>0.1</td><td>0.5</td><td>.263</td><td>0.3</td><td>0.5</td><td>.722</td><td>0.3</td><td>0.9</td><td>1.2</td><td>3.5</td><td>0.7</td><td>0.2</td><td>0.6</td><td>1.8</td></tr>
<tr><td class="rank tablesaw-cell-persist">6</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Bill-Cartwright/Summary/42872">Bill Cartwright</a></td><td><a href="/nba/teams/Chicago-Bulls/4/Home" title="Chicago Bulls">CHI</a></td><td>33</td><td class="tablesaw-cell-persist">20.8</td><td>7.8</td><td>3.1</td><td>6.5</td><td>.479</td><td>0.0</td><td>0.0</td><td>.000</td><td>1.6</td><td>2.7</td><td>.596</td><td>1.1</td><td>3.2</td><td>4.4</td><td>1.7</td><td>0.4</td><td>0.3</td><td>0.9</td><td>1.8</td></tr>
<tr><td class="rank tablesaw-cell-persist">7</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Stacey-King/Summary/1407">Stacey King</a></td><td><a href="/nba/teams/Chicago-Bulls/4/Home" title="Chicago Bulls">CHI</a></td><td>41</td><td class="tablesaw-cell-persist">15.8</td><td>7.1</td><td>2.8</td><td>5.5</td><td>.509</td><td>0.0</td><td>0.1</td><td>.250</td><td>1.4</td><td>2.0</td><td>.711</td><td>1.1</td><td>1.2</td><td>2.4</td><td>1.0</td><td>0.3</td><td>0.2</td><td>0.9</td><td>1.7</td></tr>
<tr><td class="rank tablesaw-cell-persist">8</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Will-Perdue/Summary/1271">Will Perdue</a></td><td><a href="/nba/teams/Chicago-Bulls/4/Home" title="Chicago Bulls">CHI</a></td><td>39</td><td class="tablesaw-cell-persist">13.5</td><td>5.0</td><td>2.1</td><td>3.9</td><td>.536</td><td>0.0</td><td>0.1</td><td>.500</td><td>0.8</td><td>1.5</td><td>.534</td><td>1.7</td><td>2.7</td><td>4.4</td><td>1.2</td><td>0.2</td><td>0.6</td><td>1.0</td><td>1.8</td></tr>
<tr><td class="rank tablesaw-cell-persist">9</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Cliff-Levingston/Summary/42868">Cliff Levingston</a></td><td><a href="/nba/teams/Chicago-Bulls/4/Home" title="Chicago Bulls">CHI</a></td><td>41</td><td class="tablesaw-cell-persist">13.0</td><td>4.3</td><td>1.8</td><td>3.3</td><td>.526</td><td>0.0</td><td>0.1</td><td>.000</td><td>0.8</td><td>1.1</td><td>.733</td><td>1.5</td><td>1.4</td><td>2.9</td><td>1.1</td><td>0.3</td><td>0.6</td><td>0.6</td><td>1.9</td></tr>
<tr><td class="rank tablesaw-cell-persist">10</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Bobby-Hansen/Summary/4669">Bobby Hansen</a></td><td><a href="/nba/teams/Chicago-Bulls/4/Home" title="Chicago Bulls">CHI</a></td><td>34</td><td class="tablesaw-cell-persist">12.7</td><td>3.0</td><td>1.4</td><td>2.9</td><td>.485</td><td>0.1</td><td>0.4</td><td>.200</td><td>0.1</td><td>0.4</td><td>.333</td><td>0.3</td><td>0.8</td><td>1.1</td><td>1.4</td><td>0.5</td><td>0.1</td><td>0.5</td><td>2.1</td></tr>
<tr><td class="rank tablesaw-cell-persist">11</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Scott-Williams/Summary/705">Scott Williams</a></td><td><a href="/nba/teams/Chicago-Bulls/4/Home" title="Chicago Bulls">CHI</a></td><td>33</td><td class="tablesaw-cell-persist">11.3</td><td>3.7</td><td>1.5</td><td>3.0</td><td>.485</td><td>0.0</td><td>0.0</td><td>.000</td><td>0.8</td><td>1.2</td><td>.675</td><td>1.7</td><td>2.9</td><td>4.5</td><td>1.2</td><td>0.2</td><td>0.6</td><td>0.6</td><td>1.9</td></tr>
<tr><td class="rank tablesaw-cell-persist">12</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Craig-Hodges/Summary/4623">Craig Hodges</a></td><td><a href="/nba/teams/Chicago-Bulls/4/Home" title="Chicago Bulls">CHI</a></td><td>32</td><td class="tablesaw-cell-persist">9.9</td><td>4.1</td><td>1.6</td><td>4.8</td><td>.333</td><td>0.6</td><td>1.8</td><td>.310</td><td>0.3</td><td>0.4</td><td>.917</td><td>0.2</td><td>0.3</td><td>0.5</td><td>1.1</td><td>0.2</td><td>0.0</td><td>0.4</td><td>0.8</td></tr>
<tr><td class="rank tablesaw-cell-persist">13</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Chuck-Nevitt/Summary/43282">Chuck Nevitt</a></td><td><a href="/nba/teams/Chicago-Bulls/4/Home" title="Chicago Bulls">CHI</a></td><td>1</td><td class="tablesaw-cell-persist">6.0</td><td>2.0</td><td>1.0</td><td>2.0</td><td>.500</td><td>0.0</td><td>0.0</td><td>.000</td><td>0.0</td><td>0.0</td><td>.000</td><td>0.0</td><td>1.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>3.0</td><td>2.0</td></tr>
<tr><td class="rank tablesaw-cell-persist">14</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Mark-Randall/Summary/1442">Mark Randall</a></td><td><a href="/nba/teams/Chicago-Bulls/4/Home" title="Chicago Bulls">CHI</a></td><td>8</td><td class="tablesaw-cell-persist">5.9</td><td>1.0</td><td>0.4</td><td>1.6</td><td>.231</td><td>0.0</td><td>0.3</td><td>.000</td><td>0.3</td><td>0.5</td><td>.500</td><td>0.5</td><td>0.5</td><td>1.0</td><td>0.8</td><td>0.0</td><td>0.0</td><td>0.8</td><td>0.9</td></tr>
<tr><td class="rank tablesaw-cell-persist">15</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Dennis-Hopson/Summary/45364">Dennis Hopson</a></td><td><a href="/nba/teams/Chicago-Bulls/4/Home" title="Chicago Bulls">CHI</a></td><td>1</td><td class="tablesaw-cell-persist">5.0</td><td>2.0</td><td>1.0</td><td>2.0</td><td>.500</td><td>0.0</td><td>0.0</td><td>.000</td><td>0.0</td><td>0.0</td><td>.000</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>1.0</td></tr>
<tr><td class="rank tablesaw-cell-persist">16</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Rory-Sparrow/Summary/45365">Rory Sparrow</a></td><td><a href="/nba/teams/Chicago-Bulls/4/Home" title="Chicago Bulls">CHI</a></td><td>3</td><td class="tablesaw-cell-persist">4.3</td><td>1.0</td><td>0.3</td><td>2.0</td><td>.167</td><td>0.3</td><td>0.7</td><td>.500</td><td>0.0</td><td>0.0</td><td>.000</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>0.0</td><td>0.0</td><td>0.7</td><td>0.3</td></tr>
</tbody>
</table>
<p style="text-align: center;"></p><script type="text/javascript">
function changePositions(pos) {
var url = "/nba/teams/Chicago-Bulls/4/Stats/1992/Averages/All/minutes/All/desc/1/Home";
console.log(url);
if (url.indexOf(pos) >= 0) {
console.log("index is "+url.indexOf(pos));
url = url.replace("?"+pos+"=&","?");
url = url.replace("&"+pos+"=&","&");
url = url.replace("?"+pos+"=","");
url = url.replace("&"+pos+"=","");
url = url.replace("&"+pos,"");
} else {
console.log("index is not found");
if (url.indexOf("?") >= 0) {
url = url+"&"+pos+"=";
} else {
url = url+"?"+pos+"=";
}
}
console.log("url is now: "+url);
open_network(url);
}
</script>
               <div style="clear: both;"></div>
               
               <input type="hidden" name="pageid" value="nba_teams_stats">
            
            </div> <!-- #main -->
         
                     
         </div> <!-- #main-container -->

         <footer class="container wrapper">
            <div class="footer-logo-container wrapper clearfix">
               <a href="/" class="footer-logo mobile-only"></a>
               <a href="#" class="backtotop">↑</a>
            </div>
            
            <div class="link-lists-container">
               <div class="link-lists">
   <div class="list-column">
      <h3><a href="/nba">NBA</a></h3>
      <div class="links">
         <a href="https://forums.realgm.com/boards/viewforum.php?f=6">Forums</a>
         <a href="/nba/news">News</a>
         <a href="/nba/news/analysis">Analysis</a>
         <a href="/tradechecker">Trade Checker</a>
         <a href="/nba/teams">Teams</a>
         <a href="/nba/players">Players</a>
         <a href="/nba/scores">Scores</a>
         <a href="/nba/standings">Standings</a>
         <a href="/nba/stats">Stats</a>
         <a href="/nba/depth-charts">Depth Charts</a>
         <a href="/nba/awards">Awards</a>
         <a href="https://www.vividseats.com/?wsUser=958" target="_blank">Tickets</a>
      </div>
   </div>

   <div class="list-column">
      <h3><a href="/ncaa">NCAA</a></h3>
      <div class="links">
         <a href="https://forums.realgm.com/boards/viewforum.php?f=36">Forums</a>
         <a href="/ncaa/news">News</a>
         <a href="/ncaa/news/analysis">Analysis</a>
         <a href="/ncaa/teams">Teams</a>
         <a href="/ncaa/tournaments">Tournaments</a>
         <a href="/ncaa/players">Players</a>
         <a href="/ncaa/scores">Scores</a>
         <a href="/ncaa/standings">Standings</a>
         <a href="/ncaa/stats">Stats</a>
         <a href="/ncaa/conferences/America-East-Conference/18/depth-charts/2014">Depth Charts</a>
         <a href="/ncaa/awards">Awards</a>
               </div>
   </div>

   <div class="list-column">
      <h3><a href="/dleague">G League</a></h3>
      <div class="links">
         <a href="https://forums.realgm.com/boards/viewforum.php?f=350">Forums</a>
         <a href="/gleague/news">News</a>
         <a href="/gleague/news/analysis">Analysis</a>
         <a href="/gleague/teams">Teams</a>
         <a href="/gleague/players">Players</a>
         <a href="/gleague/scores">Scores</a>
         <a href="/gleague/standings">Standings</a>
         <a href="/gleague/stats">Stats</a>
         <a href="/gleague/depth-charts">Depth Charts</a>
         <a href="/gleague/awards">Awards</a>
      </div>
   </div>
</div>
<div class="link-lists">
   <div class="list-column">
      <h3><a href="/international">International</a></h3>
      <div class="links">
         <a href="https://forums.realgm.com/boards/viewforum.php?f=5">Forums</a>
         <a href="/international/news">News</a>
         <a href="/international/news/analysis">Analysis</a>
         <a href="/international/teams">Teams</a>
         <a href="/international/leagues">Leagues</a>
         <a href="/international/schedules">Schedules</a>
         <a href="/international/scores">Scores</a>
         <a href="/international/stats">Stats</a>
      </div>
   </div>
   
   <div class="list-column">
      <h3><a href="/national">National</a></h3>
      <div class="links">
         <a href="https://forums.realgm.com/boards/viewforum.php?f=347">Forums</a>
         <a href="/national/news">News</a>
         <a href="/national/news/analysis">Analysis</a>
         <a href="/national/countries">Countries</a>
         <a href="/national/tournaments">Events</a>
         <a href="/national/schedules">Schedules</a>
         <a href="/national/scores">Scores</a>
         <a href="/national/stats">Stats</a>
      </div>
   </div>
   
   <div class="list-column">
      <h3><a href="/highschool">High School</a></h3>
      <div class="links">
         <a href="https://forums.realgm.com/boards/viewforum.php?f=346">Forums</a>
         <a href="/highschool/news">News</a>
         <a href="/highschool/news/analysis">Analysis</a>
         <a href="/highschool/schools">Schools</a>
         <a href="/highschool/allstar">All-Star Games</a>
         <a href="/highschool/awards">Awards</a>
      </div>
   </div>
</div>
            </div>
            
            <div class="about-us-container">
               <div class="social clearfix">
                  <h3>Follow Us</h3>
<ul class="rrssb-buttons clearfix rrssb-1 large-format">
   <li class="email" data-initwidth="25" style="width: 25%;" data-size="76">
      <a href="https://realgm.m-pages.com/ug2pDT/sign-up" target="_blank">
         <span class="icon">
            <svg xmlns="https://www.w3.org/2000/svg" xmlns:xlink="https://www.w3.org/1999/xlink" version="1.1" x="0px" y="0px" width="28px" height="28px" viewBox="0 0 28 28" enable-background="new 0 0 28 28" xml:space="preserve">
               <g>
                  <path d="M20.111 26.147c-2.336 1.051-4.361 1.401-7.125 1.401c-6.462 0-12.146-4.633-12.146-12.265 c0-7.94 5.762-14.833 14.561-14.833c6.853
                     0 11.8 4.7 11.8 11.252c0 5.684-3.194 9.265-7.399 9.3 c-1.829 0-3.153-0.934-3.347-2.997h-0.077c-1.208 1.986-2.96 2.997-5.023 2.997c-2.532
                     0-4.361-1.868-4.361-5.062 c0-4.749 3.504-9.071 9.111-9.071c1.713 0 3.7 0.4 4.6 0.973l-1.169 7.203c-0.388 2.298-0.116 3.3 1 3.4 c1.673 0
                     3.773-2.102 3.773-6.58c0-5.061-3.27-8.994-9.303-8.994c-5.957 0-11.175 4.673-11.175 12.1 c0 6.5 4.2 10.2 10 10.201c1.986 0 4.089-0.43
                     5.646-1.245L20.111 26.147z M16.646 10.1 c-0.311-0.078-0.701-0.155-1.207-0.155c-2.571 0-4.595 2.53-4.595 5.529c0 1.5 0.7 2.4 1.9 2.4 c1.441
                     0 2.959-1.828 3.311-4.087L16.646 10.068z"></path>
               </g>
            </svg>
         </span>
         <span class="text">newsletter</span>
      </a>
   </li>
   <li class="twitter" data-initwidth="25" style="width: 25%;" data-size="49">
      <a href="https://twitter.com/RealGM" target="_blank">
         <span class="icon">
              <svg version="1.1" id="Layer_1" xmlns="https://www.w3.org/2000/svg" xmlns:xlink="https://www.w3.org/1999/xlink" x="0px" y="0px" width="28px" height="28px" viewBox="0 0 28 28" enable-background="new 0 0 28 28" xml:space="preserve">
                  <path d="M24.253,8.756C24.689,17.08,18.297,24.182,9.97,24.62c-3.122,0.162-6.219-0.646-8.861-2.32
                  c2.703,0.179,5.376-0.648,7.508-2.321c-2.072-0.247-3.818-1.661-4.489-3.638c0.801,0.128,1.62,0.076,2.399-0.155
                  C4.045,15.72,2.215,13.6,2.115,11.077c0.688,0.275,1.426,0.407,2.168,0.386c-2.135-1.65-2.729-4.621-1.394-6.965
                  C5.575,7.816,9.54,9.84,13.803,10.071c-0.842-2.739,0.694-5.64,3.434-6.482c2.018-0.623,4.212,0.044,5.546,1.683
                  c1.186-0.213,2.318-0.662,3.329-1.317c-0.385,1.256-1.247,2.312-2.399,2.942c1.048-0.106,2.069-0.394,3.019-0.851
                  C26.275,7.229,25.39,8.196,24.253,8.756z"></path>
              </svg>
         </span>
         <span class="text">twitter</span>
      </a>
   </li>
   <li class="facebook" data-initwidth="25" style="width: 25%;" data-size="62">
      <a href="https://www.facebook.com/RealGM" target="_blank">
         <span class="icon">
            <svg version="1.1" id="Layer_1" xmlns="https://www.w3.org/2000/svg" xmlns:xlink="https://www.w3.org/1999/xlink" x="0px" y="0px" width="28px" height="28px" viewBox="0 0 28 28" enable-background="new 0 0 28 28" xml:space="preserve">
               <path d="M27.825,4.783c0-2.427-2.182-4.608-4.608-4.608H4.783c-2.422,0-4.608,2.182-4.608,4.608v18.434
                  c0,2.427,2.181,4.608,4.608,4.608H14V17.379h-3.379v-4.608H14v-1.795c0-3.089,2.335-5.885,5.192-5.885h3.718v4.608h-3.726
                  c-0.408,0-0.884,0.492-0.884,1.236v1.836h4.609v4.608h-4.609v10.446h4.916c2.422,0,4.608-2.188,4.608-4.608V4.783z"></path>
            </svg>
         </span>
         <span class="text">facebook</span>
      </a>
   </li>
   <li class="instagram" data-initwidth="25" style="width: 25%;" data-size="66">
      <a href="https://www.instagram.com/realgmnba" target="_blank">
         <span class="icon">
            <svg width="48px" height="48px" viewBox="0 0 48 48" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
             <title>Instagram</title>
             <defs></defs>
             <g id="Icons" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                 <g id="Black" transform="translate(-642.000000, -295.000000)" fill="#000000">
                     <path d="M666.000048,295 C659.481991,295 658.664686,295.027628 656.104831,295.144427 C653.550311,295.260939 651.805665,295.666687 650.279088,296.260017 C648.700876,296.873258 647.362454,297.693897 646.028128,299.028128 C644.693897,300.362454 643.873258,301.700876 643.260017,303.279088 C642.666687,304.805665 642.260939,306.550311 642.144427,309.104831 C642.027628,311.664686 642,312.481991 642,319.000048 C642,325.518009 642.027628,326.335314 642.144427,328.895169 C642.260939,331.449689 642.666687,333.194335 643.260017,334.720912 C643.873258,336.299124 644.693897,337.637546 646.028128,338.971872 C647.362454,340.306103 648.700876,341.126742 650.279088,341.740079 C651.805665,342.333313 653.550311,342.739061 656.104831,342.855573 C658.664686,342.972372 659.481991,343 666.000048,343 C672.518009,343 673.335314,342.972372 675.895169,342.855573 C678.449689,342.739061 680.194335,342.333313 681.720912,341.740079 C683.299124,341.126742 684.637546,340.306103 685.971872,338.971872 C687.306103,337.637546 688.126742,336.299124 688.740079,334.720912 C689.333313,333.194335 689.739061,331.449689 689.855573,328.895169 C689.972372,326.335314 690,325.518009 690,319.000048 C690,312.481991 689.972372,311.664686 689.855573,309.104831 C689.739061,306.550311 689.333313,304.805665 688.740079,303.279088 C688.126742,301.700876 687.306103,300.362454 685.971872,299.028128 C684.637546,297.693897 683.299124,296.873258 681.720912,296.260017 C680.194335,295.666687 678.449689,295.260939 675.895169,295.144427 C673.335314,295.027628 672.518009,295 666.000048,295 Z M666.000048,299.324317 C672.40826,299.324317 673.167356,299.348801 675.69806,299.464266 C678.038036,299.570966 679.308818,299.961946 680.154513,300.290621 C681.274771,300.725997 682.074262,301.246066 682.91405,302.08595 C683.753934,302.925738 684.274003,303.725229 684.709379,304.845487 C685.038054,305.691182 685.429034,306.961964 685.535734,309.30194 C685.651199,311.832644 685.675683,312.59174 685.675683,319.000048 C685.675683,325.40826 685.651199,326.167356 685.535734,328.69806 C685.429034,331.038036 685.038054,332.308818 684.709379,333.154513 C684.274003,334.274771 683.753934,335.074262 682.91405,335.91405 C682.074262,336.753934 681.274771,337.274003 680.154513,337.709379 C679.308818,338.038054 678.038036,338.429034 675.69806,338.535734 C673.167737,338.651199 672.408736,338.675683 666.000048,338.675683 C659.591264,338.675683 658.832358,338.651199 656.30194,338.535734 C653.961964,338.429034 652.691182,338.038054 651.845487,337.709379 C650.725229,337.274003 649.925738,336.753934 649.08595,335.91405 C648.246161,335.074262 647.725997,334.274771 647.290621,333.154513 C646.961946,332.308818 646.570966,331.038036 646.464266,328.69806 C646.348801,326.167356 646.324317,325.40826 646.324317,319.000048 C646.324317,312.59174 646.348801,311.832644 646.464266,309.30194 C646.570966,306.961964 646.961946,305.691182 647.290621,304.845487 C647.725997,303.725229 648.246066,302.925738 649.08595,302.08595 C649.925738,301.246066 650.725229,300.725997 651.845487,300.290621 C652.691182,299.961946 653.961964,299.570966 656.30194,299.464266 C658.832644,299.348801 659.59174,299.324317 666.000048,299.324317 Z M666.000048,306.675683 C659.193424,306.675683 653.675683,312.193424 653.675683,319.000048 C653.675683,325.806576 659.193424,331.324317 666.000048,331.324317 C672.806576,331.324317 678.324317,325.806576 678.324317,319.000048 C678.324317,312.193424 672.806576,306.675683 666.000048,306.675683 Z M666.000048,327 C661.581701,327 658,323.418299 658,319.000048 C658,314.581701 661.581701,311 666.000048,311 C670.418299,311 674,314.581701 674,319.000048 C674,323.418299 670.418299,327 666.000048,327 Z M681.691284,306.188768 C681.691284,307.779365 680.401829,309.068724 678.811232,309.068724 C677.22073,309.068724 675.931276,307.779365 675.931276,306.188768 C675.931276,304.598171 677.22073,303.308716 678.811232,303.308716 C680.401829,303.308716 681.691284,304.598171 681.691284,306.188768 Z" id="Instagram"></path>
                 </g>
                 <g id="Credit" transform="translate(-1734.000000, -472.000000)"></g>
             </g>
         </svg>
         </span>
         <span class="text">instagram</span>
      </a>
   </li>
</ul>
<!-- Buttons end here -->               </div>
               
               <div class="list-column">
                  <h3>RealGM</h3>
                  <div class="links">
                     <a href="/info/contact-us">Contact Us</a>
                     <a href="/info/about-us">About Us</a>
                     <a href="/info/contact-us/advertising">Advertising</a>
                     <a href="/info/privacy-policy">Privacy Policy</a>
                     <a href="/info/terms-of-use">Terms of Use</a>
                  </div>
               </div>
            </div>
            
            <p class="copyright">All content © 2000-2024 RealGM, L.L.C. All rights reserved.</p>
            
            <div style="height: 7em;">&nbsp;</div>
         </footer>
      
      </div> <!-- #site-takeover -->

      <script src="/js/vendor/jquery.hoverIntent.min.js"></script>
      <script src="/js/main.js?v3"></script>
      <script src="/js/plugins.js?v3"></script>
     
      <script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
  ga('create', 'UA-1568648-1', 'auto');
  ga('send', 'pageview');
</script><div id="StickyLeft"><div data-aaad="true" data-aa-adunit="/22181265/realgm_sidewall_rail"></div></div><div style="text-align: center;"><div data-aaad="true" data-aa-adunit="/22181265/realgm_sticky_footer"></div></div><div style="text-align: center;"><div data-aaad="true" data-aa-adunit="/22181265/realgm_mob_sticky_footer"></div></div>    
<ul class="ui-autocomplete ui-front ui-menu ui-widget ui-widget-content" id="ui-id-1" tabindex="0" style="display: none;"></ul><span role="status" aria-live="assertive" aria-relevant="additions" class="ui-helper-hidden-accessible"></span><iframe name="__tcfapiLocator" style="display: none;"></iframe><iframe name="__uspapiLocator" style="display: none;"></iframe></body>
"""

DEPTH_HTML = """
        1993-1994 Chicago Bulls Depth Chart
        </h2>
        <div class="large-column-left">
        <table class="basketball">
        <thead>
        <tr>
        <th class="nosort">&nbsp;</th>
        <th class="nosort">PG</th>
        <th class="nosort">SG</th>
        <th class="nosort">SF</th>
        <th class="nosort">PF</th>
        <th class="nosort">C</th>
        </tr>
        </thead>
        <tbody>
        <tr class="depth_starters">
        <td data-th="Role"><strong>Starters</strong></td>
        <td data-th="PG" class="depth-chart-cell">
        <a href="/player/BJ-Armstrong/Summary/1373">B.J. Armstrong</a><br>
        15p 2r 3a </td>
        <td data-th="SG" class="depth-chart-cell">
        <a href="/player/Pete-Myers/Summary/1521">Pete Myers</a><br>
        7p 2r 3a </td>
        <td data-th="SF" class="depth-chart-cell">
        <a href="/player/Scottie-Pippen/Summary/725">Scottie Pippen</a><br>
        23p 8r 5a </td>
        <td data-th="PF" class="depth-chart-cell">
        <a href="/player/Horace-Grant/Summary/985">Horace Grant</a><br>
        16p 7r 3a </td>
        <td data-th="C" class="depth-chart-cell">
        <a href="/player/Bill-Cartwright/Summary/42872">B. Cartwright</a><br>
        5p 5r 1a </td>
        </tr>
        <tr class="depth_rotation">
        <td data-th="Role"><strong>Rotation</strong></td>
        <td data-th="PG" class="depth-chart-cell">
        <a href="/player/John-Paxson/Summary/42871">John Paxson</a><br>
        1p 1a </td>
        <td data-th="SG" class="depth-chart-cell">
        <a href="/player/Steve-Kerr/Summary/1303">Steve Kerr</a><br>
        4p 1r 1a </td>
        <td data-th="SF" class="depth-chart-cell">
        <a href="/player/Toni-Kukoc/Summary/1025">Toni Kukoc</a><br>
        9p 4r 4a </td>
        <td data-th="C" class="depth-chart-cell">&nbsp;</td>
        <td data-th="C" class="depth-chart-cell">
        <a href="/player/Luc-Longley/Summary/1041">Luc Longley</a><br>
        6p 5r 2a </td>
        </tr>
        <tr class="depth_rotation">
        <td data-th="Role"><strong>Rotation</strong></td>
        <td data-th="SG" class="depth-chart-cell">&nbsp;</td>
        <td data-th="SG" class="depth-chart-cell">
        <a href="/player/Jo-Jo-English/Summary/42859">Jo Jo English</a><br>
        2p </td>
        <td data-th="C" class="depth-chart-cell">&nbsp;</td>
        <td data-th="C" class="depth-chart-cell">&nbsp;</td>
        <td data-th="C" class="depth-chart-cell">
        <a href="/player/Scott-Williams/Summary/705">Scott Williams</a><br>
        6p 4r 1a </td>
        </tr>
        <tr class="depth_rotation">
        <td data-th="Role"><strong>Rotation</strong></td>
        <td data-th="C" class="depth-chart-cell">&nbsp;</td>
        <td data-th="C" class="depth-chart-cell">&nbsp;</td>
        <td data-th="C" class="depth-chart-cell">&nbsp;</td>
        <td data-th="C" class="depth-chart-cell">&nbsp;</td>
        <td data-th="C" class="depth-chart-cell">
        <a href="/player/Bill-Wennington/Summary/1366">B. Wennington</a><br>
        1p 1r 1a </td>
        </tr>
        <tr class="depth_limpt">
        <td data-th="Role"><strong>Lim PT</strong></td>
        <td data-th="SG" class="depth-chart-cell">&nbsp;</td>
        <td data-th="SG" class="depth-chart-cell">
        <a href="/player/Michael-Jordan/Summary/1192">Michael Jordan</a><br>
        </td>
        <td data-th="PF" class="depth-chart-cell">&nbsp;</td>
        <td data-th="PF" class="depth-chart-cell">
        <a href="/player/Corie-Blount/Summary/1134">Corie Blount</a><br>
        </td>
        <td data-th="C" class="depth-chart-cell">
        <a href="/player/Will-Perdue/Summary/1271">Will Perdue</a><br>
        </td>
        </tr>
        </tbody>
        </table>
        </div>
        <div class="small-column-right">
        <div class="portal widget">
        <h3 style="margin-top: 0;">1993-1994 Bulls Leaders</h3>
        <div class="content">
        <table style="width: 100%;">
        <tbody>
        <tr>
        <th style="text-align: left;">MPG</th>
        <td><a href="/player/Scottie-Pippen/Summary/725">Scottie Pippen</a></td>
        <td>38.3</td>
        </tr>
        <tr>
        <th style="text-align: left;">FG%</th>
        <td><a href="/player/Horace-Grant/Summary/985">Horace Grant</a></td>
        <td>.524</td>
        </tr>
        <tr>
        <th style="text-align: left;">3P%</th>
        <td><a href="/player/BJ-Armstrong/Summary/1373">B.J. Armstrong</a></td>
        <td>.444</td>
        </tr>
        <tr>
        <th style="text-align: left;">FT%</th>
        <td><a href="/player/Steve-Kerr/Summary/1303">Steve Kerr</a></td>
        <td>.856</td>
        </tr>
        <tr>
        <th style="text-align: left;">ORPG</th>
        <td><a href="/player/Horace-Grant/Summary/985">Horace Grant</a></td>
        <td>4.4</td>
        </tr>
        <tr>
        <th style="text-align: left;">DRPG</th>
        <td><a href="/player/Horace-Grant/Summary/985">Horace Grant</a></td>
        <td>6.6</td>
        </tr>
        <tr>
        <th style="text-align: left;">RPG</th>
        <td><a href="/player/Horace-Grant/Summary/985">Horace Grant</a></td>
        <td>11.0</td>
        </tr>
        <tr>
        <th style="text-align: left;">APG</th>
        <td><a href="/player/Scottie-Pippen/Summary/725">Scottie Pippen</a></td>
        <td>5.6</td>
        </tr>
        <tr>
        <th style="text-align: left;">BPG</th>
        <td><a href="/player/Horace-Grant/Summary/985">Horace Grant</a></td>
        <td>1.2</td>
        </tr>
        <tr>
        <th style="text-align: left;">SPG</th>
        <td><a href="/player/Scottie-Pippen/Summary/725">Scottie Pippen</a></td>
        <td>2.9</td>
        </tr>
        <tr>
        <th style="text-align: left;">PPG</th>
        <td><a href="/player/Scottie-Pippen/Summary/725">Scottie Pippen</a></td>
        <td>22.0</td>
        </tr>
        </tbody>
        </table>
        </div>
        </div>
        </div>
        <div style="clear: both;"></div>
        <h2 class="clearfix" style="line-height: 42px;">
        1992-1993 Chicago Bulls Depth Chart
        </h2>
        <div class="large-column-left">
        <table class="basketball">
        <thead>
        <tr>
        <th class="nosort">&nbsp;</th>
        <th class="nosort">PG</th>
        <th class="nosort">SG</th>
        <th class="nosort">SF</th>
        <th class="nosort">PF</th>
        <th class="nosort">C</th>
        </tr>
        </thead>
        <tbody>
        <tr class="depth_starters">
        <td data-th="Role"><strong>Starters</strong></td>
        <td data-th="PG" class="depth-chart-cell">
        <a href="/player/BJ-Armstrong/Summary/1373">B.J. Armstrong</a><br>
        11p 2r 3a </td>
        <td data-th="SG" class="depth-chart-cell">
        <a href="/player/Michael-Jordan/Summary/1192">Michael Jordan</a><br>
        35p 7r 6a </td>
        <td data-th="SF" class="depth-chart-cell">
        <a href="/player/Scottie-Pippen/Summary/725">Scottie Pippen</a><br>
        20p 7r 6a </td>
        <td data-th="PF" class="depth-chart-cell">
        <a href="/player/Horace-Grant/Summary/985">Horace Grant</a><br>
        11p 8r 2a </td>
        <td data-th="C" class="depth-chart-cell">
        <a href="/player/Bill-Cartwright/Summary/42872">B. Cartwright</a><br>
        6p 5r 2a </td>
        </tr>
        <tr class="depth_rotation">
        <td data-th="Role"><strong>Rotation</strong></td>
        <td data-th="PG" class="depth-chart-cell">
        <a href="/player/John-Paxson/Summary/42871">John Paxson</a><br>
        5p 1r 2a </td>
        <td data-th="SG" class="depth-chart-cell">
        <a href="/player/Trent-Tucker/Summary/4667">Trent Tucker</a><br>
        3p 1r 1a </td>
        <td data-th="SF" class="depth-chart-cell">
        <a href="/player/Rodney-McCray/Summary/4632">Rodney McCray</a><br>
        2r 1a </td>
        <td data-th="PF" class="depth-chart-cell">
        <a href="/player/Stacey-King/Summary/1407">Stacey King</a><br>
        4p 2r 1a </td>
        <td data-th="C" class="depth-chart-cell">
        <a href="/player/Scott-Williams/Summary/705">Scott Williams</a><br>
        6p 6r 1a </td>
        </tr>
        <tr class="depth_rotation">
        <td data-th="Role"><strong>Rotation</strong></td>
        <td data-th="SG" class="depth-chart-cell">&nbsp;</td>
        <td data-th="SG" class="depth-chart-cell">
        <a href="/player/Darrell-Walker/Summary/4642">Darrell Walker</a><br>
        1a </td>
        <td data-th="C" class="depth-chart-cell">&nbsp;</td>
        <td data-th="C" class="depth-chart-cell">&nbsp;</td>
        <td data-th="C" class="depth-chart-cell">
        <a href="/player/Will-Perdue/Summary/1271">Will Perdue</a><br>
        2p 2r </td>
        </tr>
        <tr class="depth_limpt">
        <td data-th="Role"><strong>Lim PT</strong></td>
        <td data-th="SG" class="depth-chart-cell">&nbsp;</td>
        <td data-th="SG" class="depth-chart-cell">
        <a href="/player/Corey-Williams/Summary/32202">Corey Williams</a><br>
        </td>
        <td data-th="SF" class="depth-chart-cell">
        <a href="/player/Ed-Nealy/Summary/44632">Ed Nealy</a><br>
        </td>
        <td data-th="SF" class="depth-chart-cell">&nbsp;</td>
        <td data-th="SF" class="depth-chart-cell">&nbsp;</td>
        </tr>
        </tbody>
        </table>
        </div>
        <div class="small-column-right">
        <div class="portal widget">
        <h3 style="margin-top: 0;">1992-1993 Bulls Leaders</h3>
        <div class="content">
        <table style="width: 100%;">
        <tbody>
        <tr>
        <th style="text-align: left;">MPG</th>
        <td><a href="/player/Michael-Jordan/Summary/1192">Michael Jordan</a></td>
        <td>39.3</td>
        </tr>
        <tr>
        <th style="text-align: left;">FG%</th>
        <td><a href="/player/Will-Perdue/Summary/1271">Will Perdue</a></td>
        <td>.557</td>
        </tr>
        <tr>
        <th style="text-align: left;">3P%</th>
        <td><a href="/player/John-Paxson/Summary/42871">John Paxson</a></td>
        <td>.463</td>
        </tr>
        <tr>
        <th style="text-align: left;">FT%</th>
        <td><a href="/player/BJ-Armstrong/Summary/1373">B.J. Armstrong</a></td>
        <td>.861</td>
        </tr>
        <tr>
        <th style="text-align: left;">ORPG</th>
        <td><a href="/player/Horace-Grant/Summary/985">Horace Grant</a></td>
        <td>4.4</td>
        </tr>
        <tr>
        <th style="text-align: left;">DRPG</th>
        <td><a href="/player/Scottie-Pippen/Summary/725">Scottie Pippen</a></td>
        <td>5.2</td>
        </tr>
        <tr>
        <th style="text-align: left;">RPG</th>
        <td><a href="/player/Horace-Grant/Summary/985">Horace Grant</a></td>
        <td>9.5</td>
        </tr>
        <tr>
        <th style="text-align: left;">APG</th>
        <td><a href="/player/Scottie-Pippen/Summary/725">Scottie Pippen</a></td>
        <td>6.3</td>
        </tr>
        <tr>
        <th style="text-align: left;">BPG</th>
        <td><a href="/player/Horace-Grant/Summary/985">Horace Grant</a></td>
        <td>1.2</td>
        </tr>
        <tr>
        <th style="text-align: left;">SPG</th>
        <td><a href="/player/Michael-Jordan/Summary/1192">Michael Jordan</a></td>
        <td>2.8</td>
        </tr>
        <tr>
        <th style="text-align: left;">PPG</th>
        <td><a href="/player/Michael-Jordan/Summary/1192">Michael Jordan</a></td>
        <td>32.6</td>
        </tr>
        </tbody>
        </table>
        </div>
        </div>
        </div>
        <div style="clear: both;"></div>
        <h2 class="clearfix" style="line-height: 42px;">
        1991-1992 Chicago Bulls Depth Chart
        </h2>
        <div class="large-column-left">
        <table class="basketball">
        <thead>
        <tr>
        <th class="nosort">&nbsp;</th>
        <th class="nosort">PG</th>
        <th class="nosort">SG</th>
        <th class="nosort">SF</th>
        <th class="nosort">PF</th>
        <th class="nosort">C</th>
        </tr>
        </thead>
        <tbody>
        <tr class="depth_starters">
        <td data-th="Role"><strong>Starters</strong></td>
        <td data-th="PG" class="depth-chart-cell">
        <a href="/player/John-Paxson/Summary/42871">John Paxson</a><br>
        8p 1r 3a </td>
        <td data-th="SG" class="depth-chart-cell">
        <a href="/player/Michael-Jordan/Summary/1192">Michael Jordan</a><br>
        35p 6r 6a </td>
        <td data-th="SF" class="depth-chart-cell">
        <a href="/player/Scottie-Pippen/Summary/725">Scottie Pippen</a><br>
        20p 9r 7a </td>
        <td data-th="PF" class="depth-chart-cell">
        <a href="/player/Horace-Grant/Summary/985">Horace Grant</a><br>
        11p 9r 3a </td>
        <td data-th="C" class="depth-chart-cell">
        <a href="/player/Bill-Cartwright/Summary/42872">B. Cartwright</a><br>
        6p 5r 2a </td>
        </tr>
        <tr class="depth_rotation">
        <td data-th="Role"><strong>Rotation</strong></td>
        <td data-th="PG" class="depth-chart-cell">
        <a href="/player/BJ-Armstrong/Summary/1373">B.J. Armstrong</a><br>
        7p 1r 2a </td>
        <td data-th="SG" class="depth-chart-cell">
        <a href="/player/Bobby-Hansen/Summary/4669">Bobby Hansen</a><br>
        2p 1r 1a </td>
        <td data-th="PF" class="depth-chart-cell">&nbsp;</td>
        <td data-th="PF" class="depth-chart-cell">
        <a href="/player/Cliff-Levingston/Summary/42868">C. Levingston</a><br>
        3p 2r </td>
        <td data-th="C" class="depth-chart-cell">
        <a href="/player/Scott-Williams/Summary/705">Scott Williams</a><br>
        4p 4r </td>
        </tr>
        <tr class="depth_rotation">
        <td data-th="Role"><strong>Rotation</strong></td>
        <td data-th="PG" class="depth-chart-cell">
        <a href="/player/Craig-Hodges/Summary/4623">Craig Hodges</a><br>
        3p </td>
        <td data-th="PF" class="depth-chart-cell">&nbsp;</td>
        <td data-th="PF" class="depth-chart-cell">&nbsp;</td>
        <td data-th="PF" class="depth-chart-cell">
        <a href="/player/Stacey-King/Summary/1407">Stacey King</a><br>
        4p 1r </td>
        <td data-th="C" class="depth-chart-cell">
        <a href="/player/Will-Perdue/Summary/1271">Will Perdue</a><br>
        3p 2r 1a </td>
        </tr>
        </tbody>
        </table>
        </div>
        <div class="small-column-right">
        <div class="portal widget">
        <h3 style="margin-top: 0;">1991-1992 Bulls Leaders</h3>
        <div class="content">
        <table style="width: 100%;">
        <tbody>
        <tr>
        <th style="text-align: left;">MPG</th>
        <td><a href="/player/Michael-Jordan/Summary/1192">Michael Jordan</a></td>
        <td>38.8</td>
        </tr>
        <tr>
        <th style="text-align: left;">FG%</th>
        <td><a href="/player/Horace-Grant/Summary/985">Horace Grant</a></td>
        <td>.578</td>
        </tr>
        <tr>
        <th style="text-align: left;">3P%</th>
        <td><a href="/player/Will-Perdue/Summary/1271">Will Perdue</a></td>
        <td>.500</td>
        </tr>
        <tr>
        <th style="text-align: left;">FT%</th>
        <td><a href="/player/Craig-Hodges/Summary/4623">Craig Hodges</a></td>
        <td>.941</td>
        </tr>
        <tr>
        <th style="text-align: left;">ORPG</th>
        <td><a href="/player/Horace-Grant/Summary/985">Horace Grant</a></td>
        <td>4.2</td>
        </tr>
        <tr>
        <th style="text-align: left;">DRPG</th>
        <td><a href="/player/Horace-Grant/Summary/985">Horace Grant</a></td>
        <td>5.7</td>
        </tr>
        <tr>
        <th style="text-align: left;">RPG</th>
        <td><a href="/player/Horace-Grant/Summary/985">Horace Grant</a></td>
        <td>10.0</td>
        </tr>
        <tr>
        <th style="text-align: left;">APG</th>
        <td><a href="/player/Scottie-Pippen/Summary/725">Scottie Pippen</a></td>
        <td>7.0</td>
        </tr>
        <tr>
        <th style="text-align: left;">BPG</th>
        <td><a href="/player/Horace-Grant/Summary/985">Horace Grant</a></td>
        <td>1.6</td>
        </tr>
        <tr>
        <th style="text-align: left;">SPG</th>
        <td><a href="/player/Michael-Jordan/Summary/1192">Michael Jordan</a></td>
        <td>2.3</td>
        </tr>
        <tr>
        <th style="text-align: left;">PPG</th>
        <td><a href="/player/Michael-Jordan/Summary/1192">Michael Jordan</a></td>
        <td>30.1</td>
        </tr>
        </tbody>
        </table>
        </div>
        </div>
        </div>
        <div style="clear: both;"></div>
        <h2 class="clearfix" style="line-height: 42px;">
        """

INDIVIDUAL_HTML = """
<body style="">
      <div id="site-takeover">
      
         <div id="header_wrap" class="scroll">
         
            <header class="wrapper clearfix">
            
               <div class="container">
               
                  <div class="tabs-container clearfix">
                  
                     <div class="logo-container clearfix">
                        <a href="/"><img src="/images/basketball/5.0/template/realgm-basketball-logo-175-80.png" class="logo"></a>
                     </div>
                     
                     <div class="secondary-ad-container"></div>
                     
                     <div id="social-menu" class="topmenu">
                        <ul>
                           <li class="instagram"><a href="https://www.instagram.com/realgmnba" title="RealGM on Instagram"></a></li>
                           <li class="facebook"><a href="https://www.facebook.com/RealGM" title="RealGM on Facebook"></a></li>
                           <li class="twitter"><a href="https://twitter.com/RealGM" title="RealGM on Twitter"></a></li>
                        </ul>
                     </div>
                     
                     <div id="sports-menu" class="topmenu">
                        <div id="sports-menu-container">
                           <ul>
                              <li class="top-icon navitem nbalink selected"><a href="/"><span></span><nav>Basketball</nav></a></li>
                              <li class="top-icon navitem nfllink"><a href="https://football.realgm.com/"><span></span><nav>Football</nav></a></li>
                              <li class="top-icon navitem mlblink"><a href="https://baseball.realgm.com/"><span></span><nav>Baseball</nav></a></li>
                              <li class="top-icon navitem soccerlink"><a href="https://soccer.realgm.com/"><span></span><nav>Soccer</nav></a></li>
                              <li class="top-icon navitem nhllink"><a href="https://hockey.realgm.com/"><span></span><nav>Hockey</nav></a></li>
                              <li class="top-icon navitem forumlink"><a href="https://forums.realgm.com/boards/index.php"><span></span><nav>Forums</nav></a></li>
                                                            <li class="top-icon navitem tixlink"><a href="https://www.vividseats.com/?wsUser=958" target="_blank"><span></span><nav>Tickets</nav></a></li>
                              <li class="top-icon navitem instagram"><a href="https://www.instagram.com/realgmnba" title="RealGM on Instagram"><span></span></a></li>
                              <li class="top-icon navitem facebook"><a href="https://www.facebook.com/RealGM" title="RealGM on Facebook"><span></span></a></li>
                              <li class="top-icon navitem twitter"><a href="https://twitter.com/RealGM" title="RealGM on Twitter"><span></span></a></li>
                           </ul>
                        </div>
                     </div>
                     
                     <div class="searchbar">
                        <form action="/search" method="get" class="searchbox" id="playersearch" autocomplete="off">
                           <input type="text" class="searchbox-text ui-autocomplete-input" placeholder="Search..." name="q" id="searchfield" onkeyup="searchButtonUp();" required="required" autocomplete="off"><input type="submit" class="searchbox-submit" value="Go">
                        </form>
                     </div>
                     
                  </div>
                  
               </div>
            </header>
               
            <div class="top-nav-container">
<div class="wrapper clearfix">
<div id="menu-button" class="clearfix">
<a href="/" class="home_logo"><img src="/images/basketball/5.0/template/realgm-basketball-logo-130-60.png" style="height: 30px; width: 65px;"></a>
<a href="javascript:void(0);" class="menu-link"><span></span><nav>Menu</nav></a>
<a href="javascript:void(0);" onclick="showSportsNav()"><nav id="primary-sport-menu-icon"><u>NBA</u></nav></a>
</div><nav id="top-level-nav" role="navigation" class="container has-subnav">
<ul class="primary-nav">
<li class="search-nav with-js">
<form action="/search" method="get" class="searchbox" autocomplete="off">
<input type="text" class="searchbox-text ui-autocomplete-input" placeholder="Search..." name="q" required="required" autocomplete="off"><input type="submit" class="searchbox-submit" value="Go">
</form>
</li>
<li class="mobile-menu with-js"><a href="javascript: void(0);" onclick="showSecondaryNav();"><span>« Back</span></a></li><li class="has-subnav with-js">
<a href="/nba" id="change-sports-menu">NBA</a>
<div class="primary-nav-ddl">
<ul>
<li class="with-js"><a href="/nba">NBA</a></li><li class="with-js"><a href="/ncaa">NCAA</a></li><li class="with-js"><a href="/gleague">G League</a></li><li class="with-js"><a href="/international">International</a></li><li class="with-js"><a href="/national">National</a></li><li class="with-js"><a href="/highschool">High School</a></li></ul>
</div>
</li><li class="has-subnav with-js">
<a href="https://forums.realgm.com/boards/viewforum.php?f=243">Forums</a>
<div class="primary-nav-ddl">
<ul class="primary-nav-col" style="width: 15em; float: left;">
<li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=243">Basketball Forums</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=6">The General Board</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=64">Player Comparisons</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=2">Trades &amp; Transactions</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=344">Statistical Analysis</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=39">Fantasy Basketball</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=465">Gambling</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=3">NBA Draft</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=36">NCAA Basketball</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=350">G League</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=5">International Basketball</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=346">High School Basketball</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=69">Current Affairs</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=42">Off-Topic Board</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=4">CBA &amp; Business</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=40">Feedback</a></li></ul>
<div style="float: left; border-left: 1px solid black; padding-left: 1em;">
<div style="float: left; width: 16em;">
<p style="padding-left: 15px;">Atlantic Division</p>
<ul class="primary-nav-col" style="font-weight: normal;">
<li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=8">Boston Celtics</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=23">Brooklyn Nets</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=24">New York Knicks</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=26">Philadelphia Sixers</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=32">Toronto Raptors</a></li></ul>
</div>
<div style="float: left; width: 16em;">
<p style="padding-left: 15px;">Central Division</p>
<ul class="primary-nav-col" style="font-weight: normal;">
<li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=10">Chicago Bulls</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=11">Cleveland Cavaliers</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=14">Detroit Pistons</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=17">Indiana Pacers</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=21">Milwaukee Bucks</a></li></ul>
</div>
<div style="float: left; width: 16em;">
<p style="padding-left: 15px;">Southeast Division</p>
<ul class="primary-nav-col" style="font-weight: normal;">
<li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=7">Atlanta Hawks</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=53">Charlotte Hornets</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=20">Miami Heat</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=25">Orlando Magic</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=35">Washington Wizards</a></li></ul>
</div>
<div style="clear: both; height: 1em;" class="sep"></div>
<div style="float: left; width: 16em;">
<p style="padding-left: 15px;">Northwest Division</p>
<ul class="primary-nav-col" style="font-weight: normal;">
<li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=13">Denver Nuggets</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=22">Minnesota Timberwolves</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=334">Oklahoma City Thunder</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=28">Portland Trail Blazers</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=33">Utah Jazz</a></li></ul>
</div>
<div style="float: left; width: 16em;">
<p style="padding-left: 15px;">Pacific Division</p>
<ul class="primary-nav-col" style="font-weight: normal;">
<li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=15">Golden State Warriors</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=18">Los Angeles Clippers</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=19">Los Angeles Lakers</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=27">Phoenix Suns</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=29">Sacramento Kings</a></li></ul>
</div>
<div style="float: left; width: 16em;">
<p style="padding-left: 15px;">Southwest Division</p>
<ul class="primary-nav-col" style="font-weight: normal;">
<li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=12">Dallas Mavericks</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=16">Houston Rockets</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=34">Memphis Grizzlies</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=9">New Orleans Pelicans</a></li><li class="with-js"><a href="https://forums.realgm.com/boards/viewforum.php?f=30">San Antonio Spurs</a></li></ul>
</div>
</div>
<div style="clear: both;"></div>
</div>
</li><li class="with-js">
<a href="/nba/news">News</a>
<div class="primary-nav-ddl">
<ul class="primary-nav-col" style="width: 15em; float: left;">
<li class="with-js"><a href="/news/wiretap/tags/15/NBA">All Rumors</a></li><li class="with-js"><a href="/news/wiretap/tags/16/Signing-Rumor">Free Agent Rumors</a></li><li class="with-js"><a href="/news/wiretap/tags/18/Trade Rumor">Trade Rumors</a></li><li class="with-js"><a href="/news/wiretap/tags/53/Waiver">Waivers</a></li><li class="with-js"><a href="/news/wiretap/tags/25/NBA-Draft">NBA Draft</a></li><li class="with-js"><a href="/news/wiretap/tags/52/CBA">CBA</a></li><li class="with-js"><a href="/news/wiretap/tags/24/Injury">Injuries</a></li><li class="with-js"><a href="/news/wiretap/tags/55/Award">Awards</a></li><li class="with-js"><a href="/news/wiretap/tags/63/Fines">Fines</a></li><li class="with-js"><a href="/news/wiretap/tags/23/Suspension">Suspensions</a></li><li class="with-js"><a href="/news/wiretap/tags/69/B-Ball-IQ">B-Ball IQ</a></li><li class="with-js"><a href="/news/wiretap/tags/97/Preseason">Preseason</a></li><li class="with-js"><a href="/news/wiretap/tags/98/Playoffs">Playoffs</a></li><li class="with-js"><a href="/news/wiretap/tags/95/Summer-League">Summer League</a></li><li class="with-js"><a href="/news/wiretap/tags/54/All-Star">All-Star</a></li><li class="with-js"><a href="/news/wiretap/tags/22/NBA">Rankings</a></li></ul>
<div class="portal" style="float: left; border-left: 1px solid black; padding-left: 1em; max-width: 50em;">
<div class="secondary-story-container" style="border-top: 0;"><div class="secondary-story">
<a class="article-image" href="/wiretap/274748/Nets-Fire-Jacque-Vaughn" style="background-image: url('https://basketball.realgm.com/images/nba/4.2/wiretap/photos/2006/Vaughn_Jacque_bkn_221114.jpg');"></a>
<div class="article-title"><a style="padding-left: 0;" href="/wiretap/274748/Nets-Fire-Jacque-Vaughn">Nets Fire Jacque Vaughn</a></div>
<div class="article-content" style="font-weight: normal;"></div>
</div>
<div class="secondary-story">
<a class="article-image" href="/wiretap/274747/Stephen-Curry-On-Retirement-I-Dont-Think-Im-Anywhere-Close-To-That" style="background-image: url('https://basketball.realgm.com/images/nba/4.2/wiretap/photos/2006/Curry_Stephen_gsw_230311.jpg');"></a>
<div class="article-title"><a style="padding-left: 0;" href="/wiretap/274747/Stephen-Curry-On-Retirement-I-Dont-Think-Im-Anywhere-Close-To-That">Stephen Curry On Retirement: I Don't Think I'm Anywhere Close To That</a></div>
<div class="article-content" style="font-weight: normal;"></div>
</div>
<div class="secondary-story">
<a class="article-image" href="/wiretap/274746/LeBron-James-To-Have-Treatment-On-Left-Ankle-Could-Miss-Thursdays-Game" style="background-image: url('https://basketball.realgm.com/images/nba/4.2/wiretap/photos/2006/James_LeBron_lal_240116.jpg');"></a>
<div class="article-title"><a style="padding-left: 0;" href="/wiretap/274746/LeBron-James-To-Have-Treatment-On-Left-Ankle-Could-Miss-Thursdays-Game">LeBron James To Have Treatment On Left Ankle, Could Miss Thursday's Game</a></div>
<div class="article-content" style="font-weight: normal;"></div>
</div>
<div class="secondary-story">
<a class="article-image" href="/wiretap/274745/Bradley-Beal-On-Track-To-Return-Thursday-From-Hamstring-Injury" style="background-image: url('https://basketball.realgm.com/images/nba/4.2/wiretap/photos/2006/Beal_Bradley_phx_231117.jpg');"></a>
<div class="article-title"><a style="padding-left: 0;" href="/wiretap/274745/Bradley-Beal-On-Track-To-Return-Thursday-From-Hamstring-Injury">Bradley Beal On Track To Return Thursday From Hamstring Injury</a></div>
<div class="article-content" style="font-weight: normal;"></div>
</div>
</div>
</div>
<div style="clear: both;"></div>
</div>
</li><li class="with-js">
<a href="/nba/news/analysis">Analysis</a>
<div class="primary-nav-ddl">
<ul class="primary-nav-col" style="width: 15em; float: left; padding-top: 0.5em;">
<li class="label with-js"><u>Featured Writers</u></li><li class="with-js"><a href="/news/analysis/author/217/Colin-McGowan">Colin McGowan</a></li><li class="with-js"><a href="/news/analysis/author/226/John-Wilmes">John Wilmes</a></li><li class="with-js"><a href="/news/analysis/author/245/Micah-Wimmer">Micah Wimmer</a></li><li class="label with-js">&nbsp;</li><li class="label with-js"><u>More Contributors</u></li><li class="with-js"><a href="/news/analysis/author/258/Zachary-Cohen">Zachary Cohen</a></li><li class="with-js"><a href="/news/analysis/author/257/Wes-Goldberg">Wes Goldberg</a></li><li class="with-js"><a href="/news/analysis/author/145/RealGM-Staff-Report">RealGM Staff Report</a></li><li class="with-js"><a href="/news/analysis/author/248/Jack-Tien-Dana">Jack Tien-Dana</a></li><li class="with-js"><a href="/news/analysis/author/247/Kevin-Yeung">Kevin Yeung</a></li></ul>
<div class="portal" style="float: left; border-left: 1px solid black; padding-left: 1em; max-width: 50em;">
<div class="secondary-story-container" style="border-top: 0;"><div class="secondary-story">
<a class="article-image" href="/analysis/274590/Are-The-Cavaliers-For-Real" style="background-image: url('https://basketball.realgm.com/images/nba/4.2/wiretap/photos/2006/Mitchell_Donovan_cle_240102.jpg');"></a>
<div class="article-title"><a style="padding-left: 0;" href="/analysis/274590/Are-The-Cavaliers-For-Real">Are The Cavaliers For Real?</a></div>
<p class="author-details" style="margin: 0 0 0.5em;">
by <a href="/news/analysis/author/257/Wes-Goldberg" style="text-decoration: none;">Wes Goldberg</a></p>
<div class="article-content" style="font-weight: normal;">The Cavaliers have surged since the turn of the calendar in large part due to Donovan Mitchell and Jarrett Allen establishing themselves as their top two stars and others stepping into roles that complement their strengths.</div>
</div>
<div class="secondary-story">
<a class="article-image" href="/analysis/274567/NBA-Draft-Report-Stephon-Castle-Of-UConn" style="background-image: url('https://basketball.realgm.com/images/nba/4.2/wiretap/photos/2006/Castle_Stephon_uconn_240202.jpg');"></a>
<div class="article-title"><a style="padding-left: 0;" href="/analysis/274567/NBA-Draft-Report-Stephon-Castle-Of-UConn">NBA Draft Report: Stephon Castle Of UConn</a></div>
<p class="author-details" style="margin: 0 0 0.5em;">
by <a href="/news/analysis/author/258/Zachary-Cohen" style="text-decoration: none;">Zachary Cohen</a></p>
<div class="article-content" style="font-weight: normal;">Stephon Castle's biggest strength is his point of attack defense and his ability to make plays off the dribble. If his jumper develops, Castle can become a special NBA player.</div>
</div>
<div class="secondary-story">
<a class="article-image" href="/analysis/274486/Welcome-To-Giannis-Revisionism" style="background-image: url('https://basketball.realgm.com/images/nba/4.2/wiretap/photos/2006/Antetokounmpo_Giannis_mil_231027.jpg');"></a>
<div class="article-title"><a style="padding-left: 0;" href="/analysis/274486/Welcome-To-Giannis-Revisionism">Welcome To Giannis Revisionism</a></div>
<p class="author-details" style="margin: 0 0 0.5em;">
by <a href="/news/analysis/author/226/John-Wilmes" style="text-decoration: none;">John Wilmes</a></p>
<div class="article-content" style="font-weight: normal;">Giannis Antetokounmpo was unassailable in the public realm, but he ultimately is more like other stars than previously imagined, and less the exception to their characteristic profile than assumed.</div>
</div>
<div class="secondary-story">
<a class="article-image" href="/analysis/274484/NBA-Draft-Report-JaKobe-Walter-Of-Baylor" style="background-image: url('https://basketball.realgm.com/images/nba/4.2/wiretap/photos/2006/Walter_Jakobe_bay_240126.jpg');"></a>
<div class="article-title"><a style="padding-left: 0;" href="/analysis/274484/NBA-Draft-Report-JaKobe-Walter-Of-Baylor">NBA Draft Report: Ja'Kobe Walter Of Baylor</a></div>
<p class="author-details" style="margin: 0 0 0.5em;">
by <a href="/news/analysis/author/258/Zachary-Cohen" style="text-decoration: none;">Zachary Cohen</a></p>
<div class="article-content" style="font-weight: normal;">Ja'Kobe Walter has the size, shooting and tenacity on the wing every team in the NBA is always prioritizing to make him a safe bet for a lottery pick.</div>
</div>
</div>
</div>
<div style="clear: both;"></div>
</div>
</li><li class="has-subnav with-js">
<a href="/nba/teams" class="selected">Teams</a>
<div class="primary-nav-ddl">
<div style="float: left; width: 16em;">
<p style="padding-left: 15px;">Atlantic Division</p>
<ul class="primary-nav-col" style="font-weight: normal;">
<li class="with-js"><a href="/nba/teams/Boston-Celtics/2/Home">Boston Celtics</a></li><li class="with-js"><a href="/nba/teams/Brooklyn-Nets/38/Home">Brooklyn Nets</a></li><li class="with-js"><a href="/nba/teams/New-York-Knicks/20/Home">New York Knicks</a></li><li class="with-js"><a href="/nba/teams/Philadelphia-Sixers/22/Home">Philadelphia Sixers</a></li><li class="with-js"><a href="/nba/teams/Toronto-Raptors/28/Home">Toronto Raptors</a></li></ul>
</div>
<div style="float: left; width: 16em;">
<p style="padding-left: 15px;">Central Division</p>
<ul class="primary-nav-col" style="font-weight: normal;">
<li class="with-js"><a href="/nba/teams/Chicago-Bulls/4/Home">Chicago Bulls</a></li><li class="with-js"><a href="/nba/teams/Cleveland-Cavaliers/5/Home">Cleveland Cavaliers</a></li><li class="with-js"><a href="/nba/teams/Detroit-Pistons/8/Home">Detroit Pistons</a></li><li class="with-js"><a href="/nba/teams/Indiana-Pacers/11/Home">Indiana Pacers</a></li><li class="with-js"><a href="/nba/teams/Milwaukee-Bucks/16/Home">Milwaukee Bucks</a></li></ul>
</div>
<div style="float: left; width: 16em;">
<p style="padding-left: 15px;">Southeast Division</p>
<ul class="primary-nav-col" style="font-weight: normal;">
<li class="with-js"><a href="/nba/teams/Atlanta-Hawks/1/Home">Atlanta Hawks</a></li><li class="with-js"><a href="/nba/teams/Charlotte-Hornets/3/Home">Charlotte Hornets</a></li><li class="with-js"><a href="/nba/teams/Miami-Heat/15/Home">Miami Heat</a></li><li class="with-js"><a href="/nba/teams/Orlando-Magic/21/Home">Orlando Magic</a></li><li class="with-js"><a href="/nba/teams/Washington-Wizards/30/Home">Washington Wizards</a></li></ul>
</div>
<div style="clear: both; height: 1em;" class="sep"></div>
<div style="float: left; width: 16em;">
<p style="padding-left: 15px;">Northwest Division</p>
<ul class="primary-nav-col" style="font-weight: normal;">
<li class="with-js"><a href="/nba/teams/Denver-Nuggets/7/Home">Denver Nuggets</a></li><li class="with-js"><a href="/nba/teams/Minnesota-Timberwolves/17/Home">Minnesota Timberwolves</a></li><li class="with-js"><a href="/nba/teams/Oklahoma-City-Thunder/33/Home">Oklahoma City Thunder</a></li><li class="with-js"><a href="/nba/teams/Portland-Trail-Blazers/24/Home">Portland Trail Blazers</a></li><li class="with-js"><a href="/nba/teams/Utah-Jazz/29/Home">Utah Jazz</a></li></ul>
</div>
<div style="float: left; width: 16em;">
<p style="padding-left: 15px;">Pacific Division</p>
<ul class="primary-nav-col" style="font-weight: normal;">
<li class="with-js"><a href="/nba/teams/Golden-State-Warriors/9/Home">Golden State Warriors</a></li><li class="with-js"><a href="/nba/teams/Los-Angeles-Clippers/12/Home">Los Angeles Clippers</a></li><li class="with-js"><a href="/nba/teams/Los-Angeles-Lakers/13/Home">Los Angeles Lakers</a></li><li class="with-js"><a href="/nba/teams/Phoenix-Suns/23/Home">Phoenix Suns</a></li><li class="with-js"><a href="/nba/teams/Sacramento-Kings/25/Home">Sacramento Kings</a></li></ul>
</div>
<div style="float: left; width: 16em;">
<p style="padding-left: 15px;">Southwest Division</p>
<ul class="primary-nav-col" style="font-weight: normal;">
<li class="with-js"><a href="/nba/teams/Dallas-Mavericks/6/Home">Dallas Mavericks</a></li><li class="with-js"><a href="/nba/teams/Houston-Rockets/10/Home">Houston Rockets</a></li><li class="with-js"><a href="/nba/teams/Memphis-Grizzlies/14/Home">Memphis Grizzlies</a></li><li class="with-js"><a href="/nba/teams/New-Orleans-Pelicans/19/Home">New Orleans Pelicans</a></li><li class="with-js"><a href="/nba/teams/San-Antonio-Spurs/26/Home">San Antonio Spurs</a></li></ul>
</div>
<div style="clear: both;"></div>
</div>
</li><li class="has-subnav with-js">
<a href="#">GM Laboratory</a>
<div class="primary-nav-ddl">
<p style="margin-bottom: 0; color: #F36E21; text-align: center; font-style: italic; font-size: 1.5em;">Tools and Resources Used by Real General Managers.</p>
<div style="float: left; width: 15em;">
<p style="text-decoration: underline; padding: 0.3em 0.8em; margin-bottom: 0;"><a href="/nba/players">Players</a></p>
<ul class="primary-nav-col" style="font-weight: normal;">
<li class="with-js"><a href="/nba/players">Current Players</a></li><li class="with-js"><a href="/nba/depth-charts">Depth Charts</a></li><li class="with-js"><a href="/nba/birth-cities">Birth Cities</a></li><li class="with-js"><a href="/nba/birth-countries">Birth Countries</a></li><li class="with-js"><a href="/nba/birth-dates">Birth Dates</a></li><li class="with-js"><a href="/nba/players-abroad">NBA Players Abroad</a></li></ul>
<p style="text-decoration: underline; padding: 0.3em 0.8em; margin-bottom: 0;"><a href="/nba/awards">Awards</a></p>
<ul class="primary-nav-col" style="font-weight: normal;">
<li class="with-js"><a href="/nba/awards/by_season">By Season</a></li><li class="with-js"><a href="/nba/awards/by_type">By Type</a></li><li class="with-js"><a href="/nba/awards/by_player">By Player</a></li><li class="with-js"><a href="/nba/awards/top_75">NBA's Top 75</a></li><li class="with-js"><a href="/nba/hall-of-fame">Hall of Fame</a></li><li class="with-js"><a href="/nba/retired-numbers">Retired Jerseys</a></li></ul>
<p style="text-decoration: underline; padding: 0.3em 0.8em; margin-bottom: 0;"><a href="/nba/staff-members">Staff Members</a></p>
<ul class="primary-nav-col" style="font-weight: normal;">
<li class="with-js"><a href="/nba/staff-members/20/Head-Coach/Current">Head Coaches</a></li><li class="with-js"><a href="/nba/staff-members/16/General-Manager/Current">General Managers</a></li></ul>
</div>
<div style="float: left; width: 15em;">
<p style="text-decoration: underline; padding: 0.3em 0.8em; margin-bottom: 0;"><a href="/nba/transactions">Transactions</a></p>
<ul class="primary-nav-col" style="font-weight: normal;">
<li class="with-js"><a href="/nba/transactions/league">Transactions History</a></li><li class="with-js"><a href="/nba/transactions/composition">Roster Compositions</a></li><li class="with-js"><a href="/nba/transactions/composition_search">Compositions Search</a></li><li class="with-js"><a href="/nba/transactions/trade-deadline">Trade Deadline</a></li><li class="with-js"><a href="/nba/player_tracker/trade">Trade Tracker</a></li><li class="with-js"><a href="/nba/current_free_agents">Current Free Agents</a></li><li class="with-js"><a href="/nba/future_free_agents">Future Free Agents</a></li><li class="with-js"><a href="/nba/free_agent_options">Contract Options</a></li><li class="with-js"><a href="/nba/player_tracker/free_agent">Free Agent Tracker</a></li><li class="with-js"><a href="/nba/offseason">Offseason Recap</a></li><li class="with-js"><a href="/nba/roster-turnover">Roster Turnover</a></li></ul>
<p style="text-decoration: underline; padding: 0.3em 0.8em; margin-bottom: 0;"><a href="/nba/agent-client-list">Agents</a></p>
<ul class="primary-nav-col" style="font-weight: normal;">
<li class="with-js"><a href="/nba/agent-client-list">Agent Client Lists</a></li><li class="with-js"><a href="/nba/agent-relationships">Agent Relationships</a></li></ul>
</div>
<div style="float: left; width: 15em;">
<p style="text-decoration: underline; padding: 0.3em 0.8em; margin-bottom: 0;"><a href="/nba/draft/future_drafts/team">Future Draft Picks</a></p>
<ul class="primary-nav-col" style="font-weight: normal;">
<li class="with-js"><a href="/nba/draft/future_drafts/team">Team Summary</a></li><li class="with-js"><a href="/nba/draft/future_drafts/yearly">Yearly Summary</a></li><li class="with-js"><a href="/nba/draft/future_drafts/detailed">Pick Details</a></li></ul>
<p style="text-decoration: underline; padding: 0.3em 0.8em; margin-bottom: 0;">NBA Draft Tools</p>
<ul class="primary-nav-col" style="font-weight: normal;">
<li class="with-js"><a href="/nba/draft/draft_simulator">Mock Draft Simulator</a></li><li class="with-js"><a href="/nba/draft/lottery_simulator">Lottery Simulator</a></li><li class="with-js"><a href="/nba/draft/prospects/stats">Prospect Stats</a></li></ul>
<p style="text-decoration: underline; padding: 0.3em 0.8em; margin-bottom: 0;"><a href="/nba/draft">NBA Draft History</a></p>
<ul class="primary-nav-col" style="font-weight: normal;">
<li class="with-js"><a href="/nba/draft/past-drafts">Past Drafts</a></li><li class="with-js"><a href="/nba/teams/Atlanta-Hawks/1/Draft_History/Historical">Team Draft History</a></li><li class="with-js"><a href="/nba/draft/draft-rights">Draft Rights</a></li><li class="with-js"><a href="/nba/draft/lottery_winners">Lottery Winners</a></li><li class="with-js"><a href="/nba/draft/lottery_results">Lottery History</a></li><li class="with-js"><a href="/nba/draft/lottery_results/by_team">Team Lottery History</a></li><li class="with-js"><a href="/nba/draft/search">NBA Draft Search</a></li><li class="with-js"><a href="/nba/draft/early_entry/by_year">Early Entrants</a></li><li class="with-js"><a href="/nba/draft/special_events">Special Events</a></li></ul>
</div>
<div style="float: left; width: 15em;">
<p style="text-decoration: underline; padding: 0.3em 0.8em; margin-bottom: 0;"><a href="/nba/scores">Games</a></p>
<ul class="primary-nav-col" style="font-weight: normal;">
<li class="with-js"><a href="/nba/scores">Scores</a></li><li class="with-js"><a href="/nba/schedules">Schedules</a></li><li class="with-js"><a href="/nba/standings">Standings</a></li><li class="with-js"><a href="/nba/venues">Venues</a></li></ul>
<p style="text-decoration: underline; padding: 0.3em 0.8em; margin-bottom: 0;">Events</p>
<ul class="primary-nav-col" style="font-weight: normal;">
<li class="with-js"><a href="/nba/preseason">Preseason</a></li><li class="with-js"><a href="/nba/summer">Summer League</a></li><li class="with-js"><a href="/nba/regular_season/history">Regular Season</a></li><li class="with-js"><a href="/nba/nba-cup">NBA Cup</a></li><li class="with-js"><a href="/nba/allstar">All-Star Weekend</a></li><li class="with-js"><a href="/nba/playoffs">Playoffs</a></li><li class="with-js"><a href="/nba/draft">NBA Draft</a></li></ul>
<p style="text-decoration: underline; padding: 0.3em 0.8em; margin-bottom: 0;"><a href="/nba/info/salary_cap">Salary Cap</a></p>
<ul class="primary-nav-col" style="font-weight: normal;">
<li class="with-js"><a href="/nba/info/salary_cap">Salary Cap History</a></li><li class="with-js"><a href="/nba/info/minimum_scale">Minimum Scale</a></li><li class="with-js"><a href="/nba/info/rookie_scale">Rookie Scale</a></li><li class="with-js"><a href="http://www.cbafaq.com/salarycap.htm" target="_blank">NBA Salary Cap FAQ</a></li></ul>
</div>
<div style="clear: both;"></div>
</div>
</li><li class="has-subnav with-js">
<a href="/nba/stats">Stats</a>
<div class="primary-nav-ddl">
<ul class="primary-nav-col" style="width: 15em; float: left;">
<li class="with-js"><a href="/nba/stats">Player Stats</a></li><li class="with-js"><a href="/nba/team-stats">Team Stats</a></li><li class="with-js"><a href="/nba/individual-games">Individual Games</a></li><li class="with-js"><a href="/nba/individual-seasons">Individual Seasons</a></li><li class="with-js"><a href="/nba/daily-leaders">Daily Leaders</a></li></ul>
<ul class="primary-nav-col" style="width: 15em; float: left;">
<li class="with-js"><a href="/nba/stats/2024/Averages/Qualified/points/All/desc/1/Playoffs">Playoff Stats</a></li><li class="with-js"><a href="/nba/stats/2024/Averages/Qualified/points/All/desc/1/Preseason">Preseason Stats</a></li><li class="with-js"><a href="/nba/stats/2024/Averages/Qualified/points/All/desc/1/Summer_League">Summer League Stats</a></li></ul>
<ul class="primary-nav-col" style="width: 15em; float: left;">
<li class="with-js"><a href="/nba/stats/2024/Advanced_Stats/Qualified/points/All/desc/1/Regular_Season">Advanced Stats</a></li><li class="with-js"><a href="/nba/stats/2024/Misc_Stats/Qualified/per/All/desc/1/Regular_Season">Misc. Stats</a></li></ul>
<ul class="primary-nav-col" style="width: 15em; float: left;">
<li class="with-js"><a href="/nba/team-stats/2024/Advanced_Stats/Team_Totals/Regular_Season/ediff/desc">Team Net Rating</a></li><li class="with-js"><a href="/nba/team-stats/2024/Advanced_Stats/Team_Totals/Regular_Season/ortg/desc">Offensive Efficiency</a></li><li class="with-js"><a href="/nba/team-stats/2024/Advanced_Stats/Team_Totals/Regular_Season/drtg/desc">Defensive Efficiency</a></li></ul>
<div style="clear: both;"></div>
</div>
</li><li class="with-js"><a href="/nba/scores">Scores</a></li><li class="with-js">
<a href="/tradechecker">Trade Checker</a>
<div class="primary-nav-ddl">
<div id="tcwrapper">
<h2 style="font-weight: bold;">RealGM Trade Checker™</h2>
<ul id="checkerNav" class="threeStep" style="margin: 1em 0;">
<li class="current with-js"><em>Step 1: Select the Teams</em><span>Choose at least two teams from the menus below to start your trade.</span></li><li class="with-js"><em>Step 2: Choose the Players</em><span>Select the players you wish to trade from the rosters below.</span></li><li class="mainNavNoBg with-js"><em>Step 3: Verify the Trade</em><span>Confirm that your trade proposal is valid according to the NBA collective bargaining agreement.</span></li></ul><form method="post" action="/tradechecker/select_player">
<div class="selectwrap">
<div class="bluehead" style="font-weight: bold;">Team One *</div>
<div class="bluebody" style="font-weight: normal;">Select the first team from the drop down menu.<br><br>
<select name="team1">
<option></option>
<option value="1" selected="">Atlanta</option>
<option value="2">Boston</option>
<option value="38">Brooklyn</option>
<option value="3">Charlotte</option>
<option value="4">Chicago</option>
<option value="5">Cleveland</option>
<option value="6">Dallas</option>
<option value="7">Denver</option>
<option value="8">Detroit</option>
<option value="9">Golden State</option>
<option value="10">Houston</option>
<option value="11">Indiana</option>
<option value="12">L.A. Clippers</option>
<option value="13">L.A. Lakers</option>
<option value="14">Memphis</option>
<option value="15">Miami</option>
<option value="16">Milwaukee</option>
<option value="17">Minnesota</option>
<option value="19">New Orleans</option>
<option value="20">New York</option>
<option value="33">Oklahoma City</option>
<option value="21">Orlando</option>
<option value="22">Philadelphia</option>
<option value="23">Phoenix</option>
<option value="24">Portland</option>
<option value="25">Sacramento</option>
<option value="26">San Antonio</option>
<option value="28">Toronto</option>
<option value="29">Utah</option>
<option value="30">Washington</option>
</select>
</div>
</div>
<div class="selectwrap">
<div class="bluehead">Team Two *</div>
<div class="bluebody">Select the second team from the drop down menu.<br><br>
<select name="team2">
<option></option>
<option value="1">Atlanta</option>
<option value="2" selected="">Boston</option>
<option value="38">Brooklyn</option>
<option value="3">Charlotte</option>
<option value="4">Chicago</option>
<option value="5">Cleveland</option>
<option value="6">Dallas</option>
<option value="7">Denver</option>
<option value="8">Detroit</option>
<option value="9">Golden State</option>
<option value="10">Houston</option>
<option value="11">Indiana</option>
<option value="12">L.A. Clippers</option>
<option value="13">L.A. Lakers</option>
<option value="14">Memphis</option>
<option value="15">Miami</option>
<option value="16">Milwaukee</option>
<option value="17">Minnesota</option>
<option value="19">New Orleans</option>
<option value="20">New York</option>
<option value="33">Oklahoma City</option>
<option value="21">Orlando</option>
<option value="22">Philadelphia</option>
<option value="23">Phoenix</option>
<option value="24">Portland</option>
<option value="25">Sacramento</option>
<option value="26">San Antonio</option>
<option value="28">Toronto</option>
<option value="29">Utah</option>
<option value="30">Washington</option>
</select>
</div>
</div>
<div class="selectwrap">
<div class="bluehead">Team Three</div>
<div class="bluebody">Select the third team from the drop down menu.<br><br>
<select name="team3">
<option></option>
<option value="1">Atlanta</option>
<option value="2">Boston</option>
<option value="38">Brooklyn</option>
<option value="3">Charlotte</option>
<option value="4">Chicago</option>
<option value="5">Cleveland</option>
<option value="6">Dallas</option>
<option value="7">Denver</option>
<option value="8">Detroit</option>
<option value="9">Golden State</option>
<option value="10">Houston</option>
<option value="11">Indiana</option>
<option value="12">L.A. Clippers</option>
<option value="13">L.A. Lakers</option>
<option value="14">Memphis</option>
<option value="15">Miami</option>
<option value="16">Milwaukee</option>
<option value="17">Minnesota</option>
<option value="19">New Orleans</option>
<option value="20">New York</option>
<option value="33">Oklahoma City</option>
<option value="21">Orlando</option>
<option value="22">Philadelphia</option>
<option value="23">Phoenix</option>
<option value="24">Portland</option>
<option value="25">Sacramento</option>
<option value="26">San Antonio</option>
<option value="28">Toronto</option>
<option value="29">Utah</option>
<option value="30">Washington</option>
</select>
</div>
</div>
<div class="selectwrap">
<div class="bluehead">Team Four</div>
<div class="bluebody">Select the fourth team from the drop down menu.<br><br>
<select name="team4">
<option></option>
<option value="1">Atlanta</option>
<option value="2">Boston</option>
<option value="38">Brooklyn</option>
<option value="3">Charlotte</option>
<option value="4">Chicago</option>
<option value="5">Cleveland</option>
<option value="6">Dallas</option>
<option value="7">Denver</option>
<option value="8">Detroit</option>
<option value="9">Golden State</option>
<option value="10">Houston</option>
<option value="11">Indiana</option>
<option value="12">L.A. Clippers</option>
<option value="13">L.A. Lakers</option>
<option value="14">Memphis</option>
<option value="15">Miami</option>
<option value="16">Milwaukee</option>
<option value="17">Minnesota</option>
<option value="19">New Orleans</option>
<option value="20">New York</option>
<option value="33">Oklahoma City</option>
<option value="21">Orlando</option>
<option value="22">Philadelphia</option>
<option value="23">Phoenix</option>
<option value="24">Portland</option>
<option value="25">Sacramento</option>
<option value="26">San Antonio</option>
<option value="28">Toronto</option>
<option value="29">Utah</option>
<option value="30">Washington</option>
</select>
</div>
</div>
<div class="buttons"><input type="submit" value="Continue" class="pushbutton"></div>
</form>
<div class="clearfloat">&nbsp;</div>
</div>
</div>
</li><li class="with-js"><a href="https://www.vividseats.com/nba-basketball/?wsUser=958" target="_blank">Tickets</a></li>
<li class="has-subnav with-js">
<a href="/nba/odds">Odds</a>
<div class="primary-nav-ddl">
<ul class="primary-nav-col" style="width: 15em; float: left;">
<li class="with-js"><a href="/nba/odds">Betting Preview</a></li><li class="with-js"><a href="/nba/how-to-watch">How To Watch</a></li><li class="with-js"><a href="/nba/injuries">Injury Report</a></li><li class="with-js"><a href="/nba/stat-leaders">Stat Leaders</a></li><li class="with-js"><a href="/nba/day-preview-best-best">Best Bets</a></li><li class="with-js"><a href="/nba/player-props">Player Props</a></li><li class="with-js"><a href="/nba/award-futures">Awards</a></li><li class="with-js"><a href="/nba/team-futures">Team Futures</a></li></ul>
<div class="portal" style="float: left; border-left: 1px solid black; padding-left: 1em; max-width: 50em;">
<div class="secondary-story-container" style="border-top: 0;"><div class="secondary-story">
<a class="article-image" href="https://basketball.realgm.com/nba/odds/6789/nba-injury-news-2-15-2024" style="background-image: url('https://cdn.dataskrive.com/api/asset/rJSC7Fj.jpg');"></a>
<div class="article-title"><a style="padding-left: 0;" href="https://basketball.realgm.com/nba/odds/6789/nba-injury-news-2-15-2024">NBA Injury Report Today: Thursday, February 15</a></div>
<div class="article-content" style="font-weight: normal;">Stay in the loop with our daily NBA injury report for Thursday, February 15, with active/inactive lists for every game.</div>
</div>
<div class="secondary-story">
<a class="article-image" href="https://basketball.realgm.com/nba/odds/6684/rebounds-leaders" style="background-image: url('https://cdn.dataskrive.com/api/asset/c56iRFB.jpg');"></a>
<div class="article-title"><a style="padding-left: 0;" href="https://basketball.realgm.com/nba/odds/6684/rebounds-leaders">Who Led the NBA in Rebounds Yesterday?</a></div>
<div class="article-content" style="font-weight: normal;">See who filled up the stat sheet on Wednesday, with NBA rebounds leaders for February 14.</div>
</div>
<div class="secondary-story">
<a class="article-image" href="https://basketball.realgm.com/nba/odds/6683/blocks-leaders" style="background-image: url('https://cdn.dataskrive.com/api/asset/ToW061R.jpg');"></a>
<div class="article-title"><a style="padding-left: 0;" href="https://basketball.realgm.com/nba/odds/6683/blocks-leaders">Who Led the NBA in Blocks Yesterday?</a></div>
<div class="article-content" style="font-weight: normal;">See who filled up the stat sheet on Wednesday, with NBA blocks leaders for February 14.</div>
</div>
<div class="secondary-story">
<a class="article-image" href="https://basketball.realgm.com/nba/odds/6682/assists-leaders" style="background-image: url('https://cdn.dataskrive.com/api/asset/rlMwJvW.jpg');"></a>
<div class="article-title"><a style="padding-left: 0;" href="https://basketball.realgm.com/nba/odds/6682/assists-leaders">Who Led the NBA in Assists Yesterday?</a></div>
<div class="article-content" style="font-weight: normal;">See who filled up the stat sheet on Wednesday, with NBA assists leaders for February 14.</div>
</div>
</div>
</div>
<div style="clear: both;"></div>
</div>
</li></ul>
</nav>
<div class="second-level-nav-container">
<nav id="second-level-nav" role="navigation" class="container">
<ul class="level-1">
<li class="search-nav">
<form action="/search" method="get" class="searchbox" autocomplete="off">
<input type="text" class="searchbox-text ui-autocomplete-input" placeholder="Search..." name="q" required="required" autocomplete="off"><input type="submit" class="searchbox-submit" value="Go">
</form>
</li>
<li class="mobile-menu"><a href="javascript: void(0);" onclick="showPrimaryNav();"><span>« NBA Menu</span></a></li><li><a href="/nba/teams/Chicago-Bulls/4/Home"><span>Bulls</span></a></li><li><a href="https://forums.realgm.com/boards/viewforum.php?f=10"><span>Forum</span></a></li><li><a href="/nba/teams/Chicago-Bulls/4/news/wiretap"><span>News</span></a></li><li class="has-subnav with-js">
<a href="/nba/teams/Chicago-Bulls/4/Rosters/Regular"><span class="down">Rosters</span></a>
<ul class="level-2">
<li><a href="/nba/teams/Chicago-Bulls/4/Rosters/Regular">Regular Season</a></li><li><a href="/nba/teams/Chicago-Bulls/4/Rosters/Playoff">Playoff</a></li><li><a href="/nba/teams/Chicago-Bulls/4/Rosters/Opening_Day">Opening Day</a></li><li><a href="/nba/teams/Chicago-Bulls/4/Rosters/Training_Camp">Training Camp</a></li><li><a href="/nba/teams/Chicago-Bulls/4/Rosters/Summer_League">Summer League</a></li><li><a href="/nba/teams/Chicago-Bulls/4/Rosters/Preseason">Preseason</a></li></ul>
</li><li><a href="/nba/players/2024/Chicago-Bulls/4"><span>Players</span></a></li><li><a href="/nba/teams/Chicago-Bulls/4/Schedule"><span>Schedule</span></a></li><li class="has-subnav with-js">
<a href="/nba/teams/Chicago-Bulls/4/Stats" class="selected"><span class="down">Stats</span></a>
<ul class="level-2">
<li><a href="/nba/teams/Chicago-Bulls/4/Stats">Player Stats</a></li><li><a href="/nba/teams/Chicago-Bulls/4/individual-games">Individual Games</a></li><li><a href="/nba/teams/Chicago-Bulls/4/individual-seasons">Individual Seasons</a></li></ul>
</li><li><a href="/nba/teams/Chicago-Bulls/4/depth-charts"><span>Depth Charts</span></a></li><li class="has-subnav with-js">
<a href="/nba/teams/Chicago-Bulls/4/Awards/Season"><span class="down">Awards</span></a>
<ul class="level-2">
<li><a href="/nba/teams/Chicago-Bulls/4/Awards/Season">Awards By Season</a></li><li><a href="/nba/teams/Chicago-Bulls/4/Awards/Type">Awards By Type</a></li><li><a href="/nba/teams/Chicago-Bulls/4/Awards/All_Stars">All-Stars</a></li><li><a href="/nba/teams/Chicago-Bulls/4/Awards/Rising_Stars_Challenge">Rising Stars Challenge</a></li><li><a href="/nba/teams/Chicago-Bulls/4/Awards/Three_Point_Participants">3 Point Contest</a></li><li><a href="/nba/teams/Chicago-Bulls/4/Awards/Dunk_Comp_Participants">Dunk Contest</a></li><li><a href="/nba/teams/Chicago-Bulls/4/Awards/Skill_Challenge_Participants">Skills Contest</a></li></ul>
</li><li class="has-subnav with-js">
<a href="/nba/teams/Chicago-Bulls/4/Free_Agency/Future"><span class="down">Free Agency</span></a>
<ul class="level-2">
<li><a href="/nba/teams/Chicago-Bulls/4/Free_Agency/Future">Future Free Agents</a></li><li><a href="/nba/teams/Chicago-Bulls/4/Free_Agency/Current">Current Free Agents</a></li><li><a href="/nba/teams/Chicago-Bulls/4/Free_Agency/Options">Contract Options</a></li><li><a href="/nba/player_tracker/free_agent/Chicago-Bulls/4">Free Agent Tracker</a></li><li><a href="/nba/player_tracker/trade/Chicago-Bulls/4">Trade Tracker</a></li></ul>
</li><li class="has-subnav with-js">
<a href="/nba/teams/Chicago-Bulls/4/Transaction-History"><span class="down">History</span></a>
<ul class="level-2">
<li><a href="/nba/teams/Chicago-Bulls/4/DLeague-Transactions">G League Transactions</a></li><li><a href="/nba/teams/Chicago-Bulls/4/Draft-History">Draft History</a></li><li><a href="/nba/teams/Chicago-Bulls/4/Hall-of-Fame">Hall of Fame</a></li><li><a href="/nba/teams/Chicago-Bulls/4/Lottery-History">Lottery History</a></li><li><a href="/nba/teams/Chicago-Bulls/4/offseason">Offseason Recap</a></li><li><a href="/nba/teams/Chicago-Bulls/4/Playoff-History">Playoff History</a></li><li><a href="/nba/teams/Chicago-Bulls/4/Regular-Season-History">Regular Season History</a></li><li><a href="/nba/teams/Chicago-Bulls/4/Retired-Numbers">Retired Jerseys</a></li><li><a href="/nba/teams/Chicago-Bulls/4/roster-turnover">Roster Turnover</a></li><li><a href="/nba/teams/Chicago-Bulls/4/staff-members">Staff &amp; Executives</a></li><li><a href="/nba/teams/Chicago-Bulls/4/Transaction-History">Transactions History</a></li><li><a href="/nba/teams/Chicago-Bulls/4/trade-deadline">Trade Deadline</a></li></ul>
</li><li><a href="https://www.vividseats.com/nba-basketball/chicago-bulls-tickets.html?wsUser=958" target="_blank"><span>Tickets</span></a></li>
</ul>
</nav>
</div>
</div>
</div>
<div id="teamnav" class="clearfix"><div class="container"><ul class="clearfix"><li>
<a href="/nba/teams/Atlanta-Hawks/1/individual-games/2024">
ATL
</a>
</li>
<li>
<a href="/nba/teams/Boston-Celtics/2/individual-games/2024">
BOS
</a>
</li>
<li>
<a href="/nba/teams/Brooklyn-Nets/38/individual-games/2024">
BRK
</a>
</li>
<li>
<a href="/nba/teams/Charlotte-Hornets/3/individual-games/2024">
CHA
</a>
</li>
<li>
<a href="/nba/teams/Chicago-Bulls/4/individual-games/2024">
CHI
</a>
</li>
<li>
<a href="/nba/teams/Cleveland-Cavaliers/5/individual-games/2024">
CLE
</a>
</li>
<li>
<a href="/nba/teams/Dallas-Mavericks/6/individual-games/2024">
DAL
</a>
</li>
<li>
<a href="/nba/teams/Denver-Nuggets/7/individual-games/2024">
DEN
</a>
</li>
<li>
<a href="/nba/teams/Detroit-Pistons/8/individual-games/2024">
DET
</a>
</li>
<li>
<a href="/nba/teams/Golden-State-Warriors/9/individual-games/2024">
GOS
</a>
</li>
<li>
<a href="/nba/teams/Houston-Rockets/10/individual-games/2024">
HOU
</a>
</li>
<li>
<a href="/nba/teams/Indiana-Pacers/11/individual-games/2024">
IND
</a>
</li>
<li>
<a href="/nba/teams/Los-Angeles-Clippers/12/individual-games/2024">
LAC
</a>
</li>
<li>
<a href="/nba/teams/Los-Angeles-Lakers/13/individual-games/2024">
LAL
</a>
</li>
<li>
<a href="/nba/teams/Memphis-Grizzlies/14/individual-games/2024">
MEM
</a>
</li>
<li>
<a href="/nba/teams/Miami-Heat/15/individual-games/2024">
MIA
</a>
</li>
<li>
<a href="/nba/teams/Milwaukee-Bucks/16/individual-games/2024">
MIL
</a>
</li>
<li>
<a href="/nba/teams/Minnesota-Timberwolves/17/individual-games/2024">
MIN
</a>
</li>
<li>
<a href="/nba/teams/New-Orleans-Pelicans/19/individual-games/2024">
NOP
</a>
</li>
<li>
<a href="/nba/teams/New-York-Knicks/20/individual-games/2024">
NYK
</a>
</li>
<li>
<a href="/nba/teams/Oklahoma-City-Thunder/33/individual-games/2024">
OKC
</a>
</li>
<li>
<a href="/nba/teams/Orlando-Magic/21/individual-games/2024">
ORL
</a>
</li>
<li>
<a href="/nba/teams/Philadelphia-Sixers/22/individual-games/2024">
PHL
</a>
</li>
<li>
<a href="/nba/teams/Phoenix-Suns/23/individual-games/2024">
PHX
</a>
</li>
<li>
<a href="/nba/teams/Portland-Trail-Blazers/24/individual-games/2024">
POR
</a>
</li>
<li>
<a href="/nba/teams/Sacramento-Kings/25/individual-games/2024">
SAC
</a>
</li>
<li>
<a href="/nba/teams/San-Antonio-Spurs/26/individual-games/2024">
SAN
</a>
</li>
<li>
<a href="/nba/teams/Toronto-Raptors/28/individual-games/2024">
TOR
</a>
</li>
<li>
<a href="/nba/teams/Utah-Jazz/29/individual-games/2024">
UTH
</a>
</li>
<li>
<a href="/nba/teams/Washington-Wizards/30/individual-games/2024">
WAS
</a>
</li>
</ul></div></div>            
         </div>
         
         <div id="header_helper" class="large_header_helper" style="display: block;"></div>

         <div class="main-container">
            
            <div class="main wrapper clearfix container" style="position: relative;">
            
               <div style="text-align: center; margin: 0 1em 1em 1em;"><div data-aaad="true" data-aa-adunit="/22181265/realgm_970v_1"></div></div><div style="text-align: center; margin: 1em 0 1em 0;"><div data-aaad="true" data-aa-adunit="/22181265/realgm_mob_320v_1"></div></div><h2 class="page_title">1991-1992 Chicago Bulls Individual Games
</h2>
<div class="page-navigation open">
<div class="clearfix nav-title">
<a href="javascript:void(0);" onclick="togglePageNavigation();">Change settings?</a></div>
<div class="page-nav-option clearfix">
<label>Season:</label>
<select onchange="open_network(this.options[this.selectedIndex].value)" class="ddl">
<option value="/nba/teams/Chicago-Bulls/4/individual-games/2024/minutes/Playoffs/desc/1">2023-2024</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/2023/minutes/Playoffs/desc/1">2022-2023</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/2022/minutes/Playoffs/desc/1">2021-2022</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/2021/minutes/Playoffs/desc/1">2020-2021</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/2020/minutes/Playoffs/desc/1">2019-2020</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/2019/minutes/Playoffs/desc/1">2018-2019</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/2018/minutes/Playoffs/desc/1">2017-2018</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/2017/minutes/Playoffs/desc/1">2016-2017</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/2016/minutes/Playoffs/desc/1">2015-2016</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/2015/minutes/Playoffs/desc/1">2014-2015</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/2014/minutes/Playoffs/desc/1">2013-2014</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/2013/minutes/Playoffs/desc/1">2012-2013</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/2012/minutes/Playoffs/desc/1">2011-2012</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/2011/minutes/Playoffs/desc/1">2010-2011</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/2010/minutes/Playoffs/desc/1">2009-2010</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/2009/minutes/Playoffs/desc/1">2008-2009</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/2008/minutes/Playoffs/desc/1">2007-2008</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/2007/minutes/Playoffs/desc/1">2006-2007</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/2006/minutes/Playoffs/desc/1">2005-2006</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/2005/minutes/Playoffs/desc/1">2004-2005</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/2004/minutes/Playoffs/desc/1">2003-2004</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/2003/minutes/Playoffs/desc/1">2002-2003</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/2002/minutes/Playoffs/desc/1">2001-2002</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/2001/minutes/Playoffs/desc/1">2000-2001</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/2000/minutes/Playoffs/desc/1">1999-2000</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/1999/minutes/Playoffs/desc/1">1998-1999</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/1998/minutes/Playoffs/desc/1">1997-1998</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/1997/minutes/Playoffs/desc/1">1996-1997</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/1996/minutes/Playoffs/desc/1">1995-1996</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/1995/minutes/Playoffs/desc/1">1994-1995</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/1994/minutes/Playoffs/desc/1">1993-1994</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/1993/minutes/Playoffs/desc/1">1992-1993</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/1992/minutes/Playoffs/desc/1" selected="selected">1991-1992</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/1991/minutes/Playoffs/desc/1">1990-1991</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/1990/minutes/Playoffs/desc/1">1989-1990</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/1989/minutes/Playoffs/desc/1">1988-1989</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/1988/minutes/Playoffs/desc/1">1987-1988</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/1987/minutes/Playoffs/desc/1">1986-1987</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/1986/minutes/Playoffs/desc/1">1985-1986</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/1985/minutes/Playoffs/desc/1">1984-1985</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/1984/minutes/Playoffs/desc/1">1983-1984</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/1983/minutes/Playoffs/desc/1">1982-1983</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/1982/minutes/Playoffs/desc/1">1981-1982</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/1981/minutes/Playoffs/desc/1">1980-1981</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/1980/minutes/Playoffs/desc/1">1979-1980</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/1979/minutes/Playoffs/desc/1">1978-1979</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/1978/minutes/Playoffs/desc/1">1977-1978</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/1977/minutes/Playoffs/desc/1">1976-1977</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/1976/minutes/Playoffs/desc/1">1975-1976</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/1975/minutes/Playoffs/desc/1">1974-1975</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/1974/minutes/Playoffs/desc/1">1973-1974</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/1973/minutes/Playoffs/desc/1">1972-1973</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/1972/minutes/Playoffs/desc/1">1971-1972</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/1971/minutes/Playoffs/desc/1">1970-1971</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/1970/minutes/Playoffs/desc/1">1969-1970</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/1969/minutes/Playoffs/desc/1">1968-1969</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/1968/minutes/Playoffs/desc/1">1967-1968</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/1967/minutes/Playoffs/desc/1">1966-1967</option>
</select></div>
<div class="page-nav-option clearfix">
<label>Games:</label>
<select onchange="open_network(this.options[this.selectedIndex].value)" class="ddl">
<option value="/nba/teams/Chicago-Bulls/4/individual-games/1992/minutes/Regular_Season/desc/1">Regular Season</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/1992/minutes/Playoffs/desc/1" selected="selected">Playoffs</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/1992/minutes/Summer_League/desc/1">Summer League</option>
<option value="/nba/teams/Chicago-Bulls/4/individual-games/1992/minutes/Preseason/desc/1">Preseason</option>
</select></div>
<div class="page-nav-option clearfix">
<label>Team:</label>
<select onchange="open_network(this.options[this.selectedIndex].value)" class="ddl">
<option value="/nba/individual-games/1992/minutes/Playoffs/desc/1">Entire NBA</option>
<option value="/nba/teams/Atlanta-Hawks/1/individual-games/1992/minutes/Playoffs/desc/1">Atlanta Hawks</option>
<option value="/nba/teams/Boston-Celtics/2/individual-games/1992/minutes/Playoffs/desc/1">Boston Celtics</option>
<option value="/nba/teams/Brooklyn-Nets/38/individual-games/1992/minutes/Playoffs/desc/1">Brooklyn Nets</option>
<option value="/nba/teams/Charlotte-Hornets/3/individual-games/1992/minutes/Playoffs/desc/1">Charlotte Hornets</option>
<option selected="selected" value="/nba/teams/Chicago-Bulls/4/individual-games/1992/minutes/Playoffs/desc/1">Chicago Bulls</option>
<option value="/nba/teams/Cleveland-Cavaliers/5/individual-games/1992/minutes/Playoffs/desc/1">Cleveland Cavaliers</option>
<option value="/nba/teams/Dallas-Mavericks/6/individual-games/1992/minutes/Playoffs/desc/1">Dallas Mavericks</option>
<option value="/nba/teams/Denver-Nuggets/7/individual-games/1992/minutes/Playoffs/desc/1">Denver Nuggets</option>
<option value="/nba/teams/Detroit-Pistons/8/individual-games/1992/minutes/Playoffs/desc/1">Detroit Pistons</option>
<option value="/nba/teams/Golden-State-Warriors/9/individual-games/1992/minutes/Playoffs/desc/1">Golden State Warriors</option>
<option value="/nba/teams/Houston-Rockets/10/individual-games/1992/minutes/Playoffs/desc/1">Houston Rockets</option>
<option value="/nba/teams/Indiana-Pacers/11/individual-games/1992/minutes/Playoffs/desc/1">Indiana Pacers</option>
<option value="/nba/teams/Los-Angeles-Clippers/12/individual-games/1992/minutes/Playoffs/desc/1">Los Angeles Clippers</option>
<option value="/nba/teams/Los-Angeles-Lakers/13/individual-games/1992/minutes/Playoffs/desc/1">Los Angeles Lakers</option>
<option value="/nba/teams/Memphis-Grizzlies/14/individual-games/1992/minutes/Playoffs/desc/1">Memphis Grizzlies</option>
<option value="/nba/teams/Miami-Heat/15/individual-games/1992/minutes/Playoffs/desc/1">Miami Heat</option>
<option value="/nba/teams/Milwaukee-Bucks/16/individual-games/1992/minutes/Playoffs/desc/1">Milwaukee Bucks</option>
<option value="/nba/teams/Minnesota-Timberwolves/17/individual-games/1992/minutes/Playoffs/desc/1">Minnesota Timberwolves</option>
<option value="/nba/teams/New-Orleans-Pelicans/19/individual-games/1992/minutes/Playoffs/desc/1">New Orleans Pelicans</option>
<option value="/nba/teams/New-York-Knicks/20/individual-games/1992/minutes/Playoffs/desc/1">New York Knicks</option>
<option value="/nba/teams/Oklahoma-City-Thunder/33/individual-games/1992/minutes/Playoffs/desc/1">Oklahoma City Thunder</option>
<option value="/nba/teams/Orlando-Magic/21/individual-games/1992/minutes/Playoffs/desc/1">Orlando Magic</option>
<option value="/nba/teams/Philadelphia-Sixers/22/individual-games/1992/minutes/Playoffs/desc/1">Philadelphia Sixers</option>
<option value="/nba/teams/Phoenix-Suns/23/individual-games/1992/minutes/Playoffs/desc/1">Phoenix Suns</option>
<option value="/nba/teams/Portland-Trail-Blazers/24/individual-games/1992/minutes/Playoffs/desc/1">Portland Trail Blazers</option>
<option value="/nba/teams/Sacramento-Kings/25/individual-games/1992/minutes/Playoffs/desc/1">Sacramento Kings</option>
<option value="/nba/teams/San-Antonio-Spurs/26/individual-games/1992/minutes/Playoffs/desc/1">San Antonio Spurs</option>
<option value="/nba/teams/Toronto-Raptors/28/individual-games/1992/minutes/Playoffs/desc/1">Toronto Raptors</option>
<option value="/nba/teams/Utah-Jazz/29/individual-games/1992/minutes/Playoffs/desc/1">Utah Jazz</option>
<option value="/nba/teams/Washington-Wizards/30/individual-games/1992/minutes/Playoffs/desc/1">Washington Wizards</option>
</select></div>
<div class="page-nav-option clearfix">
<a href="/info/glossary" target="_blank">Stats Legend</a></div>
</div>
<h2>
1991-1992 Chicago Bulls Playoff Individual Game Leaders</h2>
<div class="overall-leader">
<div class="category-name">Points</div>
<div class="category-container" style="background-image: url('/images/nba/4.2/profiles/photos/2006/Jordan_Michael_nba.jpg'); background-repeat: no-repeat;"><div class="player-container clearfix"><span class="player-name"><a href="/player/Michael-Jordan/Summary/1192">Michael Jordan</a></span><span class="stat">56</span></div><div class="player-container clearfix"><span class="player-name"><a href="/player/Michael-Jordan/Summary/1192">Michael Jordan</a></span><span class="stat">46</span></div><div class="player-container clearfix"><span class="player-name"><a href="/player/Michael-Jordan/Summary/1192">Michael Jordan</a></span><span class="stat">46</span></div><div class="player-container clearfix"><span class="player-name"><a href="/player/Michael-Jordan/Summary/1192">Michael Jordan</a></span><span class="stat">42</span></div><div class="player-container clearfix"><span class="player-name"><a href="/player/Michael-Jordan/Summary/1192">Michael Jordan</a></span><span class="stat">39</span></div></div></div><div class="overall-leader">
<div class="category-name">Rebounds</div>
<div class="category-container" style="background-image: url('/images/nba/4.2/profiles/photos/2006/Pippen_Scottie_nba.jpg'); background-repeat: no-repeat;"><div class="player-container clearfix"><span class="player-name"><a href="/player/Scottie-Pippen/Summary/725">Scottie Pippen</a></span><span class="stat">15</span></div><div class="player-container clearfix"><span class="player-name"><a href="/player/Horace-Grant/Summary/985">Horace Grant</a></span><span class="stat">15</span></div><div class="player-container clearfix"><span class="player-name"><a href="/player/Horace-Grant/Summary/985">Horace Grant</a></span><span class="stat">14</span></div><div class="player-container clearfix"><span class="player-name"><a href="/player/Horace-Grant/Summary/985">Horace Grant</a></span><span class="stat">13</span></div><div class="player-container clearfix"><span class="player-name"><a href="/player/Michael-Jordan/Summary/1192">Michael Jordan</a></span><span class="stat">13</span></div></div></div><div class="overall-leader">
<div class="category-name">Assists</div>
<div class="category-container" style="background-image: url('/images/nba/4.2/profiles/photos/2006/Jordan_Michael_nba.jpg'); background-repeat: no-repeat;"><div class="player-container clearfix"><span class="player-name"><a href="/player/Michael-Jordan/Summary/1192">Michael Jordan</a></span><span class="stat">11</span></div><div class="player-container clearfix"><span class="player-name"><a href="/player/Scottie-Pippen/Summary/725">Scottie Pippen</a></span><span class="stat">11</span></div><div class="player-container clearfix"><span class="player-name"><a href="/player/Scottie-Pippen/Summary/725">Scottie Pippen</a></span><span class="stat">11</span></div><div class="player-container clearfix"><span class="player-name"><a href="/player/Scottie-Pippen/Summary/725">Scottie Pippen</a></span><span class="stat">10</span></div><div class="player-container clearfix"><span class="player-name"><a href="/player/Scottie-Pippen/Summary/725">Scottie Pippen</a></span><span class="stat">10</span></div></div></div><div class="overall-leader">
<div class="category-name">Blocks</div>
<div class="category-container" style="background-image: url('/images/nba/4.2/profiles/photos/2006/Grant_Horace_lal.jpg'); background-repeat: no-repeat;"><div class="player-container clearfix"><span class="player-name"><a href="/player/Horace-Grant/Summary/985">Horace Grant</a></span><span class="stat">5</span></div><div class="player-container clearfix"><span class="player-name"><a href="/player/Will-Perdue/Summary/1271">Will Perdue</a></span><span class="stat">4</span></div><div class="player-container clearfix"><span class="player-name"><a href="/player/Horace-Grant/Summary/985">Horace Grant</a></span><span class="stat">4</span></div><div class="player-container clearfix"><span class="player-name"><a href="/player/Horace-Grant/Summary/985">Horace Grant</a></span><span class="stat">4</span></div><div class="player-container clearfix"><span class="player-name"><a href="/player/Horace-Grant/Summary/985">Horace Grant</a></span><span class="stat">4</span></div></div></div><div class="overall-leader">
<div class="category-name">Steals</div>
<div class="category-container" style="background-image: url('/images/nba/4.2/profiles/photos/2006/Pippen_Scottie_nba.jpg'); background-repeat: no-repeat;"><div class="player-container clearfix"><span class="player-name"><a href="/player/Scottie-Pippen/Summary/725">Scottie Pippen</a></span><span class="stat">4</span></div><div class="player-container clearfix"><span class="player-name"><a href="/player/Scottie-Pippen/Summary/725">Scottie Pippen</a></span><span class="stat">4</span></div><div class="player-container clearfix"><span class="player-name"><a href="/player/Michael-Jordan/Summary/1192">Michael Jordan</a></span><span class="stat">4</span></div><div class="player-container clearfix"><span class="player-name"><a href="/player/Horace-Grant/Summary/985">Horace Grant</a></span><span class="stat">4</span></div><div class="player-container clearfix"><span class="player-name"><a href="/player/Scottie-Pippen/Summary/725">Scottie Pippen</a></span><span class="stat">4</span></div></div></div><div class="overall-leader">
<div class="category-name">Turnovers</div>
<div class="category-container" style="background-image: url('/images/nba/4.2/profiles/photos/2006/Jordan_Michael_nba.jpg'); background-repeat: no-repeat;"><div class="player-container clearfix"><span class="player-name"><a href="/player/Michael-Jordan/Summary/1192">Michael Jordan</a></span><span class="stat">7</span></div><div class="player-container clearfix"><span class="player-name"><a href="/player/Michael-Jordan/Summary/1192">Michael Jordan</a></span><span class="stat">6</span></div><div class="player-container clearfix"><span class="player-name"><a href="/player/Michael-Jordan/Summary/1192">Michael Jordan</a></span><span class="stat">6</span></div><div class="player-container clearfix"><span class="player-name"><a href="/player/Scottie-Pippen/Summary/725">Scottie Pippen</a></span><span class="stat">6</span></div><div class="player-container clearfix"><span class="player-name"><a href="/player/Scottie-Pippen/Summary/725">Scottie Pippen</a></span><span class="stat">5</span></div></div></div><div style="clear: both;"></div><h2>Best 1991-1992 Chicago Bulls Playoff Individual Games</h2><div class="tablesaw-bar mode-swipe"><div class="tablesaw-modeswitch tablesaw-toolbar"><label>Col<span class="a11y-sm">umn</span>s:<span class="btn btn-small btn-select">Swipe<select><option value="stack">Stack</option><option selected="" value="swipe">Swipe</option></select></span></label></div><div class="tablesaw-advance"><a href="#" class="tablesaw-nav-btn btn btn-micro left disabled" title="Previous Column"></a><a href="#" class="tablesaw-nav-btn btn btn-micro right disabled" title="Next Column"></a></div></div><table class="tablesaw tablesaw-swipe" data-tablesaw-mode="swipe" data-tablesaw-mode-switch="" data-tablesaw-mode-exclude="columntoggle" id="table-9774" style="">
<thead>
<tr>
<th data-tablesaw-priority="persist" class="tablesaw-cell-persist">#</th>
<th data-tablesaw-priority="persist" class="tablesaw-cell-persist">Player</th>
<th>Date</th>
<th>Team</th>
<th data-tablesaw-sortable-default-col="" class="tablesaw-sortable-descending tablesaw-cell-persist" data-tablesaw-priority="persist">MIN</th><th><a href="/nba/teams/Chicago-Bulls/4/individual-games/1992/points/Playoffs/desc/1">PTS</a></th><th><a href="/nba/teams/Chicago-Bulls/4/individual-games/1992/fgm/Playoffs/desc/1">FGM</a></th><th><a href="/nba/teams/Chicago-Bulls/4/individual-games/1992/fga/Playoffs/desc/1">FGA</a></th><th><a href="/nba/teams/Chicago-Bulls/4/individual-games/1992/tpfgm/Playoffs/desc/1">3PM</a></th><th><a href="/nba/teams/Chicago-Bulls/4/individual-games/1992/tpfga/Playoffs/desc/1">3PA</a></th><th><a href="/nba/teams/Chicago-Bulls/4/individual-games/1992/ftm/Playoffs/desc/1">FTM</a></th><th><a href="/nba/teams/Chicago-Bulls/4/individual-games/1992/fta/Playoffs/desc/1">FTA</a></th><th><a href="/nba/teams/Chicago-Bulls/4/individual-games/1992/orb/Playoffs/desc/1">ORB</a></th><th><a href="/nba/teams/Chicago-Bulls/4/individual-games/1992/drb/Playoffs/desc/1">DRB</a></th><th><a href="/nba/teams/Chicago-Bulls/4/individual-games/1992/trb/Playoffs/desc/1">REB</a></th><th><a href="/nba/teams/Chicago-Bulls/4/individual-games/1992/assists/Playoffs/desc/1">AST</a></th><th><a href="/nba/teams/Chicago-Bulls/4/individual-games/1992/steals/Playoffs/desc/1">STL</a></th><th><a href="/nba/teams/Chicago-Bulls/4/individual-games/1992/blocks/Playoffs/desc/1">BLK</a></th><th><a href="/nba/teams/Chicago-Bulls/4/individual-games/1992/turnovers/Playoffs/desc/1">TOV</a></th><th><a href="/nba/teams/Chicago-Bulls/4/individual-games/1992/fouls/Playoffs/desc/1">PF</a></th></tr>
</thead>
<tbody>
<tr><td class="rank tablesaw-cell-persist">1</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Michael-Jordan/Summary/1192">Michael Jordan</a></td><td class="nowrap"><a href="/nba/boxscore/1992-06-05/Portland-at-Chicago/119046">Jun 5, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">50:00</td><td>39</td><td>16</td><td>32</td><td>0</td><td>4</td><td>7</td><td>9</td><td>1</td><td>4</td><td>5</td><td>10</td><td>1</td><td>0</td><td>5</td><td>5</td></tr>
<tr><td class="rank tablesaw-cell-persist">2</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Scottie-Pippen/Summary/725">Scottie Pippen</a></td><td class="nowrap"><a href="/nba/boxscore/1992-06-05/Portland-at-Chicago/119046">Jun 5, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">48:00</td><td>16</td><td>6</td><td>19</td><td>0</td><td>3</td><td>4</td><td>6</td><td>3</td><td>5</td><td>8</td><td>10</td><td>3</td><td>0</td><td>6</td><td>4</td></tr>
<tr><td class="rank tablesaw-cell-persist">3</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Horace-Grant/Summary/985">Horace Grant</a></td><td class="nowrap"><a href="/nba/boxscore/1992-06-05/Portland-at-Chicago/119046">Jun 5, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">46:00</td><td>10</td><td>4</td><td>6</td><td>0</td><td>0</td><td>2</td><td>3</td><td>2</td><td>10</td><td>12</td><td>7</td><td>1</td><td>5</td><td>0</td><td>4</td></tr>
<tr><td class="rank tablesaw-cell-persist">4</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Scottie-Pippen/Summary/725">Scottie Pippen</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-10/Chicago-at-New-York/119027">May 10, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">46:00</td><td>13</td><td>4</td><td>13</td><td>0</td><td>1</td><td>5</td><td>10</td><td>2</td><td>6</td><td>8</td><td>7</td><td>1</td><td>0</td><td>1</td><td>5</td></tr>
<tr><td class="rank tablesaw-cell-persist">5</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Scottie-Pippen/Summary/725">Scottie Pippen</a></td><td class="nowrap"><a href="/nba/boxscore/1992-06-12/Chicago-at-Portland/119049">Jun 12, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">45:00</td><td>24</td><td>8</td><td>15</td><td>0</td><td>1</td><td>8</td><td>9</td><td>3</td><td>8</td><td>11</td><td>9</td><td>2</td><td>0</td><td>3</td><td>4</td></tr>
<tr><td class="rank tablesaw-cell-persist">6</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Horace-Grant/Summary/985">Horace Grant</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-29/Chicago-at-Cleveland/119043">May 29, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">45:00</td><td>20</td><td>7</td><td>11</td><td>0</td><td>0</td><td>6</td><td>6</td><td>5</td><td>4</td><td>9</td><td>0</td><td>0</td><td>2</td><td>1</td><td>4</td></tr>
<tr><td class="rank tablesaw-cell-persist">7</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Scottie-Pippen/Summary/725">Scottie Pippen</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-17/New-York-at-Chicago/119030">May 17, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">45:00</td><td>17</td><td>7</td><td>11</td><td>0</td><td>0</td><td>3</td><td>4</td><td>4</td><td>7</td><td>11</td><td>11</td><td>3</td><td>0</td><td>5</td><td>3</td></tr>
<tr><td class="rank tablesaw-cell-persist">8</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Michael-Jordan/Summary/1192">Michael Jordan</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-14/Chicago-at-New-York/119029">May 14, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">45:00</td><td>21</td><td>9</td><td>25</td><td>1</td><td>5</td><td>2</td><td>4</td><td>0</td><td>4</td><td>4</td><td>8</td><td>0</td><td>1</td><td>7</td><td>0</td></tr>
<tr><td class="rank tablesaw-cell-persist">9</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Scottie-Pippen/Summary/725">Scottie Pippen</a></td><td class="nowrap"><a href="/nba/boxscore/1992-04-29/Chicago-at-Miami/119006">Apr 29, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">45:00</td><td>31</td><td>12</td><td>23</td><td>0</td><td>1</td><td>7</td><td>8</td><td>4</td><td>4</td><td>8</td><td>5</td><td>0</td><td>2</td><td>2</td><td>5</td></tr>
<tr><td class="rank tablesaw-cell-persist">10</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Michael-Jordan/Summary/1192">Michael Jordan</a></td><td class="nowrap"><a href="/nba/boxscore/1992-06-10/Chicago-at-Portland/119048">Jun 10, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">44:00</td><td>32</td><td>11</td><td>26</td><td>2</td><td>6</td><td>8</td><td>8</td><td>0</td><td>5</td><td>5</td><td>6</td><td>0</td><td>0</td><td>5</td><td>4</td></tr>
<tr><td class="rank tablesaw-cell-persist">11</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Horace-Grant/Summary/985">Horace Grant</a></td><td class="nowrap"><a href="/nba/boxscore/1992-06-10/Chicago-at-Portland/119048">Jun 10, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">44:00</td><td>8</td><td>4</td><td>10</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>9</td><td>10</td><td>1</td><td>1</td><td>0</td><td>1</td><td>4</td></tr>
<tr><td class="rank tablesaw-cell-persist">12</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Michael-Jordan/Summary/1192">Michael Jordan</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-29/Chicago-at-Cleveland/119043">May 29, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">44:00</td><td>29</td><td>10</td><td>27</td><td>0</td><td>0</td><td>9</td><td>9</td><td>1</td><td>7</td><td>8</td><td>8</td><td>2</td><td>0</td><td>3</td><td>3</td></tr>
<tr><td class="rank tablesaw-cell-persist">13</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Scottie-Pippen/Summary/725">Scottie Pippen</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-25/Chicago-at-Cleveland/119041">May 25, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">44:00</td><td>13</td><td>5</td><td>11</td><td>1</td><td>1</td><td>2</td><td>3</td><td>3</td><td>7</td><td>10</td><td>4</td><td>1</td><td>0</td><td>5</td><td>3</td></tr>
<tr><td class="rank tablesaw-cell-persist">14</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Michael-Jordan/Summary/1192">Michael Jordan</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-25/Chicago-at-Cleveland/119041">May 25, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">44:00</td><td>35</td><td>15</td><td>33</td><td>1</td><td>3</td><td>4</td><td>5</td><td>2</td><td>3</td><td>5</td><td>6</td><td>3</td><td>0</td><td>5</td><td>3</td></tr>
<tr><td class="rank tablesaw-cell-persist">15</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Michael-Jordan/Summary/1192">Michael Jordan</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-10/Chicago-at-New-York/119027">May 10, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">44:00</td><td>29</td><td>12</td><td>26</td><td>0</td><td>2</td><td>5</td><td>6</td><td>2</td><td>2</td><td>4</td><td>4</td><td>0</td><td>0</td><td>0</td><td>1</td></tr>
<tr><td class="rank tablesaw-cell-persist">16</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Michael-Jordan/Summary/1192">Michael Jordan</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-09/Chicago-at-New-York/119026">May 9, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">44:00</td><td>32</td><td>12</td><td>24</td><td>1</td><td>3</td><td>7</td><td>10</td><td>1</td><td>8</td><td>9</td><td>3</td><td>3</td><td>1</td><td>6</td><td>2</td></tr>
<tr><td class="rank tablesaw-cell-persist">17</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Horace-Grant/Summary/985">Horace Grant</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-07/New-York-at-Chicago/119025">May 7, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">44:00</td><td>14</td><td>5</td><td>12</td><td>0</td><td>0</td><td>4</td><td>6</td><td>5</td><td>6</td><td>11</td><td>4</td><td>0</td><td>1</td><td>0</td><td>2</td></tr>
<tr><td class="rank tablesaw-cell-persist">18</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Michael-Jordan/Summary/1192">Michael Jordan</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-05/New-York-at-Chicago/119024">May 5, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">44:00</td><td>31</td><td>12</td><td>23</td><td>0</td><td>0</td><td>7</td><td>8</td><td>1</td><td>5</td><td>6</td><td>3</td><td>1</td><td>3</td><td>2</td><td>4</td></tr>
<tr><td class="rank tablesaw-cell-persist">19</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Scottie-Pippen/Summary/725">Scottie Pippen</a></td><td class="nowrap"><a href="/nba/boxscore/1992-06-14/Portland-at-Chicago/119050">Jun 14, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">43:00</td><td>26</td><td>9</td><td>17</td><td>2</td><td>3</td><td>6</td><td>6</td><td>4</td><td>1</td><td>5</td><td>4</td><td>0</td><td>1</td><td>5</td><td>3</td></tr>
<tr><td class="rank tablesaw-cell-persist">20</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Michael-Jordan/Summary/1192">Michael Jordan</a></td><td class="nowrap"><a href="/nba/boxscore/1992-06-14/Portland-at-Chicago/119050">Jun 14, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">43:00</td><td>33</td><td>13</td><td>24</td><td>2</td><td>3</td><td>5</td><td>5</td><td>1</td><td>3</td><td>4</td><td>4</td><td>4</td><td>1</td><td>4</td><td>3</td></tr>
<tr><td class="rank tablesaw-cell-persist">21</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Scottie-Pippen/Summary/725">Scottie Pippen</a></td><td class="nowrap"><a href="/nba/boxscore/1992-06-07/Chicago-at-Portland/119047">Jun 7, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">43:00</td><td>18</td><td>6</td><td>15</td><td>0</td><td>1</td><td>6</td><td>8</td><td>1</td><td>7</td><td>8</td><td>7</td><td>1</td><td>2</td><td>5</td><td>4</td></tr>
<tr><td class="rank tablesaw-cell-persist">22</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Horace-Grant/Summary/985">Horace Grant</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-25/Chicago-at-Cleveland/119041">May 25, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">43:00</td><td>7</td><td>2</td><td>7</td><td>0</td><td>0</td><td>3</td><td>4</td><td>5</td><td>10</td><td>15</td><td>3</td><td>1</td><td>2</td><td>1</td><td>3</td></tr>
<tr><td class="rank tablesaw-cell-persist">23</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Michael-Jordan/Summary/1192">Michael Jordan</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-23/Chicago-at-Cleveland/119040">May 23, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">43:00</td><td>36</td><td>13</td><td>27</td><td>1</td><td>1</td><td>9</td><td>10</td><td>3</td><td>3</td><td>6</td><td>9</td><td>1</td><td>0</td><td>5</td><td>3</td></tr>
<tr><td class="rank tablesaw-cell-persist">24</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Scottie-Pippen/Summary/725">Scottie Pippen</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-07/New-York-at-Chicago/119025">May 7, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">43:00</td><td>6</td><td>2</td><td>12</td><td>0</td><td>1</td><td>2</td><td>4</td><td>1</td><td>5</td><td>6</td><td>3</td><td>2</td><td>2</td><td>4</td><td>3</td></tr>
<tr><td class="rank tablesaw-cell-persist">25</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Michael-Jordan/Summary/1192">Michael Jordan</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-07/New-York-at-Chicago/119025">May 7, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">43:00</td><td>27</td><td>12</td><td>24</td><td>0</td><td>0</td><td>3</td><td>8</td><td>1</td><td>5</td><td>6</td><td>5</td><td>3</td><td>0</td><td>2</td><td>2</td></tr>
<tr><td class="rank tablesaw-cell-persist">26</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Horace-Grant/Summary/985">Horace Grant</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-05/New-York-at-Chicago/119024">May 5, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">43:00</td><td>9</td><td>4</td><td>9</td><td>0</td><td>0</td><td>1</td><td>1</td><td>3</td><td>1</td><td>4</td><td>5</td><td>0</td><td>1</td><td>0</td><td>4</td></tr>
<tr><td class="rank tablesaw-cell-persist">27</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Michael-Jordan/Summary/1192">Michael Jordan</a></td><td class="nowrap"><a href="/nba/boxscore/1992-04-29/Chicago-at-Miami/119006">Apr 29, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">43:00</td><td>56</td><td>20</td><td>30</td><td>0</td><td>0</td><td>16</td><td>18</td><td>1</td><td>4</td><td>5</td><td>5</td><td>4</td><td>2</td><td>2</td><td>3</td></tr>
<tr><td class="rank tablesaw-cell-persist">28</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Michael-Jordan/Summary/1192">Michael Jordan</a></td><td class="nowrap"><a href="/nba/boxscore/1992-06-12/Chicago-at-Portland/119049">Jun 12, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">42:00</td><td>46</td><td>14</td><td>23</td><td>2</td><td>4</td><td>16</td><td>19</td><td>0</td><td>5</td><td>5</td><td>4</td><td>0</td><td>1</td><td>4</td><td>5</td></tr>
<tr><td class="rank tablesaw-cell-persist">29</td><td class="nowrap tablesaw-cell-persist"><a href="/player/John-Paxson/Summary/42871">John Paxson</a></td><td class="nowrap"><a href="/nba/boxscore/1992-06-05/Portland-at-Chicago/119046">Jun 5, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">42:00</td><td>16</td><td>6</td><td>14</td><td>4</td><td>7</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>4</td><td>0</td><td>0</td><td>1</td><td>2</td></tr>
<tr><td class="rank tablesaw-cell-persist">30</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Scottie-Pippen/Summary/725">Scottie Pippen</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-29/Chicago-at-Cleveland/119043">May 29, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">42:00</td><td>29</td><td>11</td><td>23</td><td>0</td><td>1</td><td>7</td><td>8</td><td>3</td><td>9</td><td>12</td><td>5</td><td>4</td><td>4</td><td>5</td><td>5</td></tr>
<tr><td class="rank tablesaw-cell-persist">31</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Scottie-Pippen/Summary/725">Scottie Pippen</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-19/Cleveland-at-Chicago/119038">May 19, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">42:00</td><td>29</td><td>9</td><td>17</td><td>1</td><td>3</td><td>10</td><td>10</td><td>4</td><td>8</td><td>12</td><td>9</td><td>1</td><td>3</td><td>4</td><td>2</td></tr>
<tr><td class="rank tablesaw-cell-persist">32</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Michael-Jordan/Summary/1192">Michael Jordan</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-17/New-York-at-Chicago/119030">May 17, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">42:00</td><td>42</td><td>15</td><td>29</td><td>0</td><td>0</td><td>12</td><td>13</td><td>3</td><td>3</td><td>6</td><td>4</td><td>2</td><td>3</td><td>5</td><td>3</td></tr>
<tr><td class="rank tablesaw-cell-persist">33</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Horace-Grant/Summary/985">Horace Grant</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-12/New-York-at-Chicago/119028">May 12, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">42:00</td><td>13</td><td>6</td><td>8</td><td>0</td><td>0</td><td>1</td><td>4</td><td>3</td><td>2</td><td>5</td><td>0</td><td>2</td><td>2</td><td>1</td><td>2</td></tr>
<tr><td class="rank tablesaw-cell-persist">34</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Horace-Grant/Summary/985">Horace Grant</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-10/Chicago-at-New-York/119027">May 10, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">42:00</td><td>13</td><td>6</td><td>8</td><td>0</td><td>1</td><td>1</td><td>6</td><td>3</td><td>3</td><td>6</td><td>4</td><td>2</td><td>3</td><td>0</td><td>4</td></tr>
<tr><td class="rank tablesaw-cell-persist">35</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Scottie-Pippen/Summary/725">Scottie Pippen</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-05/New-York-at-Chicago/119024">May 5, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">42:00</td><td>22</td><td>8</td><td>18</td><td>0</td><td>0</td><td>6</td><td>6</td><td>4</td><td>4</td><td>8</td><td>9</td><td>0</td><td>3</td><td>1</td><td>4</td></tr>
<tr><td class="rank tablesaw-cell-persist">36</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Horace-Grant/Summary/985">Horace Grant</a></td><td class="nowrap"><a href="/nba/boxscore/1992-04-29/Chicago-at-Miami/119006">Apr 29, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">42:00</td><td>8</td><td>4</td><td>9</td><td>0</td><td>0</td><td>0</td><td>0</td><td>5</td><td>3</td><td>8</td><td>3</td><td>2</td><td>0</td><td>1</td><td>2</td></tr>
<tr><td class="rank tablesaw-cell-persist">37</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Scottie-Pippen/Summary/725">Scottie Pippen</a></td><td class="nowrap"><a href="/nba/boxscore/1992-04-24/Miami-at-Chicago/119004">Apr 24, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">42:00</td><td>11</td><td>4</td><td>9</td><td>0</td><td>0</td><td>3</td><td>3</td><td>0</td><td>6</td><td>6</td><td>11</td><td>3</td><td>1</td><td>1</td><td>3</td></tr>
<tr><td class="rank tablesaw-cell-persist">38</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Michael-Jordan/Summary/1192">Michael Jordan</a></td><td class="nowrap"><a href="/nba/boxscore/1992-06-07/Chicago-at-Portland/119047">Jun 7, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">41:00</td><td>26</td><td>11</td><td>22</td><td>0</td><td>1</td><td>4</td><td>4</td><td>2</td><td>5</td><td>7</td><td>4</td><td>3</td><td>0</td><td>5</td><td>4</td></tr>
<tr><td class="rank tablesaw-cell-persist">39</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Bill-Cartwright/Summary/42872">Bill Cartwright</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-29/Chicago-at-Cleveland/119043">May 29, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">41:00</td><td>10</td><td>5</td><td>11</td><td>0</td><td>0</td><td>0</td><td>0</td><td>3</td><td>6</td><td>9</td><td>2</td><td>1</td><td>2</td><td>0</td><td>1</td></tr>
<tr><td class="rank tablesaw-cell-persist">40</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Horace-Grant/Summary/985">Horace Grant</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-17/New-York-at-Chicago/119030">May 17, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">41:00</td><td>14</td><td>6</td><td>10</td><td>0</td><td>0</td><td>2</td><td>3</td><td>3</td><td>3</td><td>6</td><td>4</td><td>4</td><td>4</td><td>1</td><td>3</td></tr>
<tr><td class="rank tablesaw-cell-persist">41</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Scottie-Pippen/Summary/725">Scottie Pippen</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-12/New-York-at-Chicago/119028">May 12, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">41:00</td><td>10</td><td>4</td><td>11</td><td>0</td><td>2</td><td>2</td><td>2</td><td>4</td><td>6</td><td>10</td><td>8</td><td>2</td><td>0</td><td>3</td><td>3</td></tr>
<tr><td class="rank tablesaw-cell-persist">42</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Scottie-Pippen/Summary/725">Scottie Pippen</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-09/Chicago-at-New-York/119026">May 9, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">41:00</td><td>26</td><td>7</td><td>12</td><td>2</td><td>2</td><td>10</td><td>12</td><td>0</td><td>5</td><td>5</td><td>3</td><td>2</td><td>1</td><td>4</td><td>6</td></tr>
<tr><td class="rank tablesaw-cell-persist">43</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Bill-Cartwright/Summary/42872">Bill Cartwright</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-05/New-York-at-Chicago/119024">May 5, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">41:00</td><td>6</td><td>3</td><td>7</td><td>0</td><td>0</td><td>0</td><td>2</td><td>4</td><td>4</td><td>8</td><td>0</td><td>0</td><td>0</td><td>3</td><td>3</td></tr>
<tr><td class="rank tablesaw-cell-persist">44</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Michael-Jordan/Summary/1192">Michael Jordan</a></td><td class="nowrap"><a href="/nba/boxscore/1992-04-24/Miami-at-Chicago/119004">Apr 24, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">41:00</td><td>46</td><td>21</td><td>34</td><td>0</td><td>0</td><td>4</td><td>4</td><td>1</td><td>10</td><td>11</td><td>9</td><td>3</td><td>1</td><td>5</td><td>4</td></tr>
<tr><td class="rank tablesaw-cell-persist">45</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Michael-Jordan/Summary/1192">Michael Jordan</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-19/Cleveland-at-Chicago/119038">May 19, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">40:00</td><td>33</td><td>15</td><td>29</td><td>1</td><td>2</td><td>2</td><td>2</td><td>1</td><td>5</td><td>6</td><td>7</td><td>2</td><td>1</td><td>1</td><td>0</td></tr>
<tr><td class="rank tablesaw-cell-persist">46</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Michael-Jordan/Summary/1192">Michael Jordan</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-12/New-York-at-Chicago/119028">May 12, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">40:00</td><td>37</td><td>11</td><td>23</td><td>0</td><td>0</td><td>15</td><td>17</td><td>2</td><td>3</td><td>5</td><td>3</td><td>1</td><td>0</td><td>4</td><td>3</td></tr>
<tr><td class="rank tablesaw-cell-persist">47</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Horace-Grant/Summary/985">Horace Grant</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-27/Cleveland-at-Chicago/119042">May 27, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">39:00</td><td>13</td><td>4</td><td>9</td><td>0</td><td>0</td><td>5</td><td>6</td><td>7</td><td>7</td><td>14</td><td>2</td><td>2</td><td>3</td><td>1</td><td>4</td></tr>
<tr><td class="rank tablesaw-cell-persist">48</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Michael-Jordan/Summary/1192">Michael Jordan</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-27/Cleveland-at-Chicago/119042">May 27, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">39:00</td><td>37</td><td>13</td><td>28</td><td>0</td><td>0</td><td>11</td><td>12</td><td>0</td><td>3</td><td>3</td><td>5</td><td>4</td><td>0</td><td>0</td><td>4</td></tr>
<tr><td class="rank tablesaw-cell-persist">49</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Scottie-Pippen/Summary/725">Scottie Pippen</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-23/Chicago-at-Cleveland/119040">May 23, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">39:00</td><td>23</td><td>9</td><td>14</td><td>0</td><td>0</td><td>5</td><td>8</td><td>2</td><td>7</td><td>9</td><td>7</td><td>2</td><td>0</td><td>5</td><td>3</td></tr>
<tr><td class="rank tablesaw-cell-persist">50</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Bill-Cartwright/Summary/42872">Bill Cartwright</a></td><td class="nowrap"><a href="/nba/boxscore/1992-06-10/Chicago-at-Portland/119048">Jun 10, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">38:00</td><td>9</td><td>4</td><td>8</td><td>0</td><td>0</td><td>1</td><td>2</td><td>0</td><td>4</td><td>4</td><td>2</td><td>2</td><td>0</td><td>2</td><td>3</td></tr>
<tr><td class="rank tablesaw-cell-persist">51</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Horace-Grant/Summary/985">Horace Grant</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-23/Chicago-at-Cleveland/119040">May 23, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">38:00</td><td>15</td><td>7</td><td>10</td><td>0</td><td>0</td><td>1</td><td>2</td><td>2</td><td>9</td><td>11</td><td>1</td><td>0</td><td>4</td><td>3</td><td>5</td></tr>
<tr><td class="rank tablesaw-cell-persist">52</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Horace-Grant/Summary/985">Horace Grant</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-19/Cleveland-at-Chicago/119038">May 19, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">38:00</td><td>12</td><td>4</td><td>11</td><td>0</td><td>0</td><td>4</td><td>4</td><td>7</td><td>3</td><td>10</td><td>7</td><td>1</td><td>0</td><td>2</td><td>2</td></tr>
<tr><td class="rank tablesaw-cell-persist">53</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Horace-Grant/Summary/985">Horace Grant</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-14/Chicago-at-New-York/119029">May 14, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">38:00</td><td>10</td><td>3</td><td>7</td><td>0</td><td>0</td><td>4</td><td>4</td><td>2</td><td>4</td><td>6</td><td>2</td><td>1</td><td>1</td><td>2</td><td>3</td></tr>
<tr><td class="rank tablesaw-cell-persist">54</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Scottie-Pippen/Summary/725">Scottie Pippen</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-14/Chicago-at-New-York/119029">May 14, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">38:00</td><td>18</td><td>5</td><td>15</td><td>0</td><td>1</td><td>8</td><td>11</td><td>3</td><td>7</td><td>10</td><td>5</td><td>4</td><td>2</td><td>1</td><td>2</td></tr>
<tr><td class="rank tablesaw-cell-persist">55</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Horace-Grant/Summary/985">Horace Grant</a></td><td class="nowrap"><a href="/nba/boxscore/1992-06-07/Chicago-at-Portland/119047">Jun 7, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">37:00</td><td>18</td><td>7</td><td>12</td><td>0</td><td>0</td><td>4</td><td>5</td><td>1</td><td>7</td><td>8</td><td>6</td><td>1</td><td>1</td><td>1</td><td>4</td></tr>
<tr><td class="rank tablesaw-cell-persist">56</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Scottie-Pippen/Summary/725">Scottie Pippen</a></td><td class="nowrap"><a href="/nba/boxscore/1992-04-26/Miami-at-Chicago/119005">Apr 26, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">37:00</td><td>30</td><td>10</td><td>15</td><td>0</td><td>0</td><td>10</td><td>12</td><td>2</td><td>2</td><td>4</td><td>5</td><td>4</td><td>1</td><td>1</td><td>0</td></tr>
<tr><td class="rank tablesaw-cell-persist">57</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Horace-Grant/Summary/985">Horace Grant</a></td><td class="nowrap"><a href="/nba/boxscore/1992-06-14/Portland-at-Chicago/119050">Jun 14, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">36:00</td><td>2</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>5</td><td>5</td><td>5</td><td>0</td><td>1</td><td>0</td><td>2</td></tr>
<tr><td class="rank tablesaw-cell-persist">58</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Scottie-Pippen/Summary/725">Scottie Pippen</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-21/Cleveland-at-Chicago/119039">May 21, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">36:00</td><td>11</td><td>4</td><td>14</td><td>0</td><td>2</td><td>3</td><td>6</td><td>3</td><td>6</td><td>9</td><td>3</td><td>2</td><td>1</td><td>2</td><td>0</td></tr>
<tr><td class="rank tablesaw-cell-persist">59</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Bill-Cartwright/Summary/42872">Bill Cartwright</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-14/Chicago-at-New-York/119029">May 14, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">36:00</td><td>10</td><td>5</td><td>9</td><td>0</td><td>0</td><td>0</td><td>0</td><td>4</td><td>3</td><td>7</td><td>2</td><td>0</td><td>0</td><td>1</td><td>4</td></tr>
<tr><td class="rank tablesaw-cell-persist">60</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Bill-Cartwright/Summary/42872">Bill Cartwright</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-12/New-York-at-Chicago/119028">May 12, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">36:00</td><td>4</td><td>2</td><td>6</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>5</td><td>5</td><td>2</td><td>0</td><td>0</td><td>0</td><td>2</td></tr>
<tr><td class="rank tablesaw-cell-persist">61</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Horace-Grant/Summary/985">Horace Grant</a></td><td class="nowrap"><a href="/nba/boxscore/1992-04-24/Miami-at-Chicago/119004">Apr 24, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">36:00</td><td>15</td><td>6</td><td>9</td><td>0</td><td>0</td><td>3</td><td>3</td><td>5</td><td>2</td><td>7</td><td>4</td><td>1</td><td>0</td><td>0</td><td>2</td></tr>
<tr><td class="rank tablesaw-cell-persist">62</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Michael-Jordan/Summary/1192">Michael Jordan</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-21/Cleveland-at-Chicago/119039">May 21, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">35:00</td><td>20</td><td>7</td><td>22</td><td>0</td><td>0</td><td>6</td><td>7</td><td>8</td><td>3</td><td>11</td><td>3</td><td>3</td><td>2</td><td>6</td><td>3</td></tr>
<tr><td class="rank tablesaw-cell-persist">63</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Horace-Grant/Summary/985">Horace Grant</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-09/Chicago-at-New-York/119026">May 9, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">35:00</td><td>10</td><td>2</td><td>4</td><td>0</td><td>0</td><td>6</td><td>8</td><td>4</td><td>9</td><td>13</td><td>2</td><td>0</td><td>1</td><td>0</td><td>1</td></tr>
<tr><td class="rank tablesaw-cell-persist">64</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Michael-Jordan/Summary/1192">Michael Jordan</a></td><td class="nowrap"><a href="/nba/boxscore/1992-04-26/Miami-at-Chicago/119005">Apr 26, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">35:00</td><td>33</td><td>12</td><td>23</td><td>0</td><td>0</td><td>9</td><td>10</td><td>4</td><td>9</td><td>13</td><td>6</td><td>2</td><td>0</td><td>4</td><td>3</td></tr>
<tr><td class="rank tablesaw-cell-persist">65</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Bill-Cartwright/Summary/42872">Bill Cartwright</a></td><td class="nowrap"><a href="/nba/boxscore/1992-06-05/Portland-at-Chicago/119046">Jun 5, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">34:00</td><td>10</td><td>4</td><td>4</td><td>0</td><td>0</td><td>2</td><td>4</td><td>1</td><td>3</td><td>4</td><td>1</td><td>0</td><td>1</td><td>1</td><td>3</td></tr>
<tr><td class="rank tablesaw-cell-persist">66</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Michael-Jordan/Summary/1192">Michael Jordan</a></td><td class="nowrap"><a href="/nba/boxscore/1992-06-03/Portland-at-Chicago/119045">Jun 3, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">34:00</td><td>39</td><td>16</td><td>27</td><td>6</td><td>10</td><td>1</td><td>1</td><td>2</td><td>1</td><td>3</td><td>11</td><td>2</td><td>0</td><td>1</td><td>0</td></tr>
<tr><td class="rank tablesaw-cell-persist">67</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Bill-Cartwright/Summary/42872">Bill Cartwright</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-07/New-York-at-Chicago/119025">May 7, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">34:00</td><td>2</td><td>1</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>2</td><td>3</td><td>0</td><td>0</td><td>1</td><td>5</td></tr>
<tr><td class="rank tablesaw-cell-persist">68</td><td class="nowrap tablesaw-cell-persist"><a href="/player/John-Paxson/Summary/42871">John Paxson</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-05/New-York-at-Chicago/119024">May 5, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">34:00</td><td>12</td><td>6</td><td>10</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>3</td><td>3</td><td>2</td><td>0</td><td>0</td><td>0</td><td>3</td></tr>
<tr><td class="rank tablesaw-cell-persist">69</td><td class="nowrap tablesaw-cell-persist"><a href="/player/John-Paxson/Summary/42871">John Paxson</a></td><td class="nowrap"><a href="/nba/boxscore/1992-06-12/Chicago-at-Portland/119049">Jun 12, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">33:00</td><td>12</td><td>6</td><td>11</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>3</td><td>2</td><td>0</td><td>1</td><td>2</td></tr>
<tr><td class="rank tablesaw-cell-persist">70</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Horace-Grant/Summary/985">Horace Grant</a></td><td class="nowrap"><a href="/nba/boxscore/1992-06-12/Chicago-at-Portland/119049">Jun 12, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">33:00</td><td>6</td><td>2</td><td>4</td><td>0</td><td>0</td><td>2</td><td>5</td><td>0</td><td>5</td><td>5</td><td>3</td><td>1</td><td>4</td><td>3</td><td>6</td></tr>
<tr><td class="rank tablesaw-cell-persist">71</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Scottie-Pippen/Summary/725">Scottie Pippen</a></td><td class="nowrap"><a href="/nba/boxscore/1992-06-03/Portland-at-Chicago/119045">Jun 3, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">33:00</td><td>24</td><td>8</td><td>14</td><td>0</td><td>1</td><td>8</td><td>9</td><td>3</td><td>6</td><td>9</td><td>10</td><td>2</td><td>1</td><td>1</td><td>2</td></tr>
<tr><td class="rank tablesaw-cell-persist">72</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Bill-Cartwright/Summary/42872">Bill Cartwright</a></td><td class="nowrap"><a href="/nba/boxscore/1992-04-29/Chicago-at-Miami/119006">Apr 29, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">33:00</td><td>1</td><td>0</td><td>3</td><td>0</td><td>0</td><td>1</td><td>4</td><td>1</td><td>4</td><td>5</td><td>2</td><td>0</td><td>0</td><td>1</td><td>5</td></tr>
<tr><td class="rank tablesaw-cell-persist">73</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Horace-Grant/Summary/985">Horace Grant</a></td><td class="nowrap"><a href="/nba/boxscore/1992-04-26/Miami-at-Chicago/119005">Apr 26, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">33:00</td><td>11</td><td>5</td><td>8</td><td>0</td><td>0</td><td>1</td><td>2</td><td>3</td><td>7</td><td>10</td><td>1</td><td>2</td><td>1</td><td>2</td><td>4</td></tr>
<tr><td class="rank tablesaw-cell-persist">74</td><td class="nowrap tablesaw-cell-persist"><a href="/player/John-Paxson/Summary/42871">John Paxson</a></td><td class="nowrap"><a href="/nba/boxscore/1992-04-24/Miami-at-Chicago/119004">Apr 24, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">33:00</td><td>8</td><td>4</td><td>6</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>6</td><td>0</td><td>0</td><td>0</td><td>2</td></tr>
<tr><td class="rank tablesaw-cell-persist">75</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Scottie-Pippen/Summary/725">Scottie Pippen</a></td><td class="nowrap"><a href="/nba/boxscore/1992-06-10/Chicago-at-Portland/119048">Jun 10, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">32:00</td><td>17</td><td>8</td><td>13</td><td>0</td><td>0</td><td>1</td><td>4</td><td>3</td><td>6</td><td>9</td><td>6</td><td>1</td><td>0</td><td>3</td><td>4</td></tr>
<tr><td class="rank tablesaw-cell-persist">76</td><td class="nowrap tablesaw-cell-persist"><a href="/player/John-Paxson/Summary/42871">John Paxson</a></td><td class="nowrap"><a href="/nba/boxscore/1992-06-07/Chicago-at-Portland/119047">Jun 7, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">32:00</td><td>8</td><td>3</td><td>5</td><td>0</td><td>1</td><td>2</td><td>2</td><td>0</td><td>0</td><td>0</td><td>2</td><td>2</td><td>0</td><td>1</td><td>1</td></tr>
<tr><td class="rank tablesaw-cell-persist">77</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Scottie-Pippen/Summary/725">Scottie Pippen</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-27/Cleveland-at-Chicago/119042">May 27, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">32:00</td><td>14</td><td>6</td><td>14</td><td>0</td><td>0</td><td>2</td><td>6</td><td>3</td><td>12</td><td>15</td><td>6</td><td>1</td><td>1</td><td>3</td><td>4</td></tr>
<tr><td class="rank tablesaw-cell-persist">78</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Bill-Cartwright/Summary/42872">Bill Cartwright</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-17/New-York-at-Chicago/119030">May 17, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">32:00</td><td>5</td><td>2</td><td>3</td><td>0</td><td>0</td><td>1</td><td>3</td><td>1</td><td>4</td><td>5</td><td>2</td><td>0</td><td>0</td><td>1</td><td>5</td></tr>
<tr><td class="rank tablesaw-cell-persist">79</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Horace-Grant/Summary/985">Horace Grant</a></td><td class="nowrap"><a href="/nba/boxscore/1992-06-03/Portland-at-Chicago/119045">Jun 3, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">31:00</td><td>11</td><td>5</td><td>8</td><td>0</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>7</td><td>2</td><td>1</td><td>3</td><td>0</td><td>0</td></tr>
<tr><td class="rank tablesaw-cell-persist">80</td><td class="nowrap tablesaw-cell-persist"><a href="/player/John-Paxson/Summary/42871">John Paxson</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-19/Cleveland-at-Chicago/119038">May 19, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">31:00</td><td>4</td><td>2</td><td>4</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>2</td><td>4</td><td>0</td><td>0</td><td>1</td><td>2</td></tr>
<tr><td class="rank tablesaw-cell-persist">81</td><td class="nowrap tablesaw-cell-persist"><a href="/player/John-Paxson/Summary/42871">John Paxson</a></td><td class="nowrap"><a href="/nba/boxscore/1992-06-10/Chicago-at-Portland/119048">Jun 10, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">30:00</td><td>9</td><td>3</td><td>7</td><td>2</td><td>4</td><td>1</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>4</td></tr>
<tr><td class="rank tablesaw-cell-persist">82</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Horace-Grant/Summary/985">Horace Grant</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-21/Cleveland-at-Chicago/119039">May 21, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">30:00</td><td>10</td><td>5</td><td>10</td><td>0</td><td>0</td><td>0</td><td>0</td><td>7</td><td>5</td><td>12</td><td>0</td><td>1</td><td>0</td><td>1</td><td>3</td></tr>
<tr><td class="rank tablesaw-cell-persist">83</td><td class="nowrap tablesaw-cell-persist"><a href="/player/John-Paxson/Summary/42871">John Paxson</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-09/Chicago-at-New-York/119026">May 9, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">30:00</td><td>5</td><td>2</td><td>4</td><td>1</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>4</td><td>1</td><td>0</td><td>2</td><td>3</td></tr>
<tr><td class="rank tablesaw-cell-persist">84</td><td class="nowrap tablesaw-cell-persist"><a href="/player/John-Paxson/Summary/42871">John Paxson</a></td><td class="nowrap"><a href="/nba/boxscore/1992-06-14/Portland-at-Chicago/119050">Jun 14, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">29:00</td><td>13</td><td>6</td><td>9</td><td>1</td><td>4</td><td>0</td><td>0</td><td>0</td><td>3</td><td>3</td><td>2</td><td>2</td><td>0</td><td>2</td><td>2</td></tr>
<tr><td class="rank tablesaw-cell-persist">85</td><td class="nowrap tablesaw-cell-persist"><a href="/player/BJ-Armstrong/Summary/1373">B.J. Armstrong</a></td><td class="nowrap"><a href="/nba/boxscore/1992-06-03/Portland-at-Chicago/119045">Jun 3, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">29:00</td><td>11</td><td>5</td><td>11</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>3</td><td>3</td><td>6</td><td>0</td><td>0</td><td>3</td><td>3</td></tr>
<tr><td class="rank tablesaw-cell-persist">86</td><td class="nowrap tablesaw-cell-persist"><a href="/player/John-Paxson/Summary/42871">John Paxson</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-29/Chicago-at-Cleveland/119043">May 29, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">29:00</td><td>4</td><td>2</td><td>3</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>2</td><td>2</td><td>0</td><td>0</td><td>0</td><td>1</td><td>4</td></tr>
<tr><td class="rank tablesaw-cell-persist">87</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Bill-Cartwright/Summary/42872">Bill Cartwright</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-27/Cleveland-at-Chicago/119042">May 27, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">29:00</td><td>6</td><td>3</td><td>4</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>7</td><td>7</td><td>1</td><td>2</td><td>0</td><td>1</td><td>1</td></tr>
<tr><td class="rank tablesaw-cell-persist">88</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Scott-Williams/Summary/705">Scott Williams</a></td><td class="nowrap"><a href="/nba/boxscore/1992-06-03/Portland-at-Chicago/119045">Jun 3, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">28:00</td><td>12</td><td>6</td><td>6</td><td>0</td><td>0</td><td>0</td><td>0</td><td>4</td><td>5</td><td>9</td><td>1</td><td>0</td><td>2</td><td>2</td><td>4</td></tr>
<tr><td class="rank tablesaw-cell-persist">89</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Bill-Cartwright/Summary/42872">Bill Cartwright</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-23/Chicago-at-Cleveland/119040">May 23, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">28:00</td><td>2</td><td>1</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>5</td><td>5</td><td>2</td><td>1</td><td>0</td><td>2</td><td>4</td></tr>
<tr><td class="rank tablesaw-cell-persist">90</td><td class="nowrap tablesaw-cell-persist"><a href="/player/John-Paxson/Summary/42871">John Paxson</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-14/Chicago-at-New-York/119029">May 14, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">28:00</td><td>8</td><td>4</td><td>10</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>5</td><td>5</td><td>2</td><td>0</td><td>0</td><td>1</td><td>1</td></tr>
<tr><td class="rank tablesaw-cell-persist">91</td><td class="nowrap tablesaw-cell-persist"><a href="/player/BJ-Armstrong/Summary/1373">B.J. Armstrong</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-10/Chicago-at-New-York/119027">May 10, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">28:00</td><td>11</td><td>4</td><td>7</td><td>0</td><td>1</td><td>3</td><td>3</td><td>0</td><td>4</td><td>4</td><td>0</td><td>1</td><td>0</td><td>0</td><td>2</td></tr>
<tr><td class="rank tablesaw-cell-persist">92</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Bill-Cartwright/Summary/42872">Bill Cartwright</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-09/Chicago-at-New-York/119026">May 9, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">27:00</td><td>7</td><td>3</td><td>7</td><td>0</td><td>0</td><td>1</td><td>2</td><td>2</td><td>1</td><td>3</td><td>2</td><td>1</td><td>1</td><td>0</td><td>4</td></tr>
<tr><td class="rank tablesaw-cell-persist">93</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Bill-Cartwright/Summary/42872">Bill Cartwright</a></td><td class="nowrap"><a href="/nba/boxscore/1992-04-24/Miami-at-Chicago/119004">Apr 24, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">27:00</td><td>8</td><td>3</td><td>5</td><td>0</td><td>0</td><td>2</td><td>2</td><td>1</td><td>1</td><td>2</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td></tr>
<tr><td class="rank tablesaw-cell-persist">94</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Bill-Cartwright/Summary/42872">Bill Cartwright</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-25/Chicago-at-Cleveland/119041">May 25, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">26:00</td><td>4</td><td>2</td><td>4</td><td>0</td><td>0</td><td>0</td><td>2</td><td>1</td><td>1</td><td>2</td><td>1</td><td>1</td><td>0</td><td>0</td><td>3</td></tr>
<tr><td class="rank tablesaw-cell-persist">95</td><td class="nowrap tablesaw-cell-persist"><a href="/player/John-Paxson/Summary/42871">John Paxson</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-25/Chicago-at-Cleveland/119041">May 25, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">26:00</td><td>11</td><td>5</td><td>7</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>3</td><td>0</td><td>0</td><td>0</td><td>6</td></tr>
<tr><td class="rank tablesaw-cell-persist">96</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Bill-Cartwright/Summary/42872">Bill Cartwright</a></td><td class="nowrap"><a href="/nba/boxscore/1992-06-07/Chicago-at-Portland/119047">Jun 7, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">25:00</td><td>6</td><td>3</td><td>7</td><td>0</td><td>0</td><td>0</td><td>2</td><td>2</td><td>5</td><td>7</td><td>3</td><td>0</td><td>0</td><td>1</td><td>6</td></tr>
<tr><td class="rank tablesaw-cell-persist">97</td><td class="nowrap tablesaw-cell-persist"><a href="/player/John-Paxson/Summary/42871">John Paxson</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-27/Cleveland-at-Chicago/119042">May 27, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">25:00</td><td>4</td><td>2</td><td>3</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>2</td></tr>
<tr><td class="rank tablesaw-cell-persist">98</td><td class="nowrap tablesaw-cell-persist"><a href="/player/John-Paxson/Summary/42871">John Paxson</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-23/Chicago-at-Cleveland/119040">May 23, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">25:00</td><td>12</td><td>5</td><td>6</td><td>2</td><td>2</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>3</td><td>0</td><td>0</td><td>0</td><td>1</td></tr>
<tr><td class="rank tablesaw-cell-persist">99</td><td class="nowrap tablesaw-cell-persist"><a href="/player/Scott-Williams/Summary/705">Scott Williams</a></td><td class="nowrap"><a href="/nba/boxscore/1992-06-14/Portland-at-Chicago/119050">Jun 14, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">24:00</td><td>4</td><td>2</td><td>5</td><td>0</td><td>0</td><td>0</td><td>0</td><td>3</td><td>5</td><td>8</td><td>0</td><td>0</td><td>2</td><td>0</td><td>2</td></tr>
<tr><td class="rank tablesaw-cell-persist">100</td><td class="nowrap tablesaw-cell-persist"><a href="/player/John-Paxson/Summary/42871">John Paxson</a></td><td class="nowrap"><a href="/nba/boxscore/1992-05-21/Cleveland-at-Chicago/119039">May 21, 1992</a></td><td>CHI</td><td class="tablesaw-cell-persist">24:00</td><td>5</td><td>2</td><td>6</td><td>1</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td></tr>
</tbody>
</table>
<p style="text-align: center;"><a href="/nba/teams/Chicago-Bulls/4/individual-games/1992/minutes/Playoffs/desc/2">Next Page »</a></p>               <div style="clear: both;"></div>
               
               <input type="hidden" name="pageid" value="nba_teams_individual_games">
            
            </div> <!-- #main -->
         
                     
         </div> <!-- #main-container -->

         <footer class="container wrapper">
            <div class="footer-logo-container wrapper clearfix">
               <a href="/" class="footer-logo mobile-only"></a>
               <a href="#" class="backtotop">↑</a>
            </div>
            
            <div class="link-lists-container">
               <div class="link-lists">
   <div class="list-column">
      <h3><a href="/nba">NBA</a></h3>
      <div class="links">
         <a href="https://forums.realgm.com/boards/viewforum.php?f=6">Forums</a>
         <a href="/nba/news">News</a>
         <a href="/nba/news/analysis">Analysis</a>
         <a href="/tradechecker">Trade Checker</a>
         <a href="/nba/teams">Teams</a>
         <a href="/nba/players">Players</a>
         <a href="/nba/scores">Scores</a>
         <a href="/nba/standings">Standings</a>
         <a href="/nba/stats">Stats</a>
         <a href="/nba/depth-charts">Depth Charts</a>
         <a href="/nba/awards">Awards</a>
         <a href="https://www.vividseats.com/?wsUser=958" target="_blank">Tickets</a>
      </div>
   </div>

   <div class="list-column">
      <h3><a href="/ncaa">NCAA</a></h3>
      <div class="links">
         <a href="https://forums.realgm.com/boards/viewforum.php?f=36">Forums</a>
         <a href="/ncaa/news">News</a>
         <a href="/ncaa/news/analysis">Analysis</a>
         <a href="/ncaa/teams">Teams</a>
         <a href="/ncaa/tournaments">Tournaments</a>
         <a href="/ncaa/players">Players</a>
         <a href="/ncaa/scores">Scores</a>
         <a href="/ncaa/standings">Standings</a>
         <a href="/ncaa/stats">Stats</a>
         <a href="/ncaa/conferences/America-East-Conference/18/depth-charts/2014">Depth Charts</a>
         <a href="/ncaa/awards">Awards</a>
               </div>
   </div>

   <div class="list-column">
      <h3><a href="/dleague">G League</a></h3>
      <div class="links">
         <a href="https://forums.realgm.com/boards/viewforum.php?f=350">Forums</a>
         <a href="/gleague/news">News</a>
         <a href="/gleague/news/analysis">Analysis</a>
         <a href="/gleague/teams">Teams</a>
         <a href="/gleague/players">Players</a>
         <a href="/gleague/scores">Scores</a>
         <a href="/gleague/standings">Standings</a>
         <a href="/gleague/stats">Stats</a>
         <a href="/gleague/depth-charts">Depth Charts</a>
         <a href="/gleague/awards">Awards</a>
      </div>
   </div>
</div>
<div class="link-lists">
   <div class="list-column">
      <h3><a href="/international">International</a></h3>
      <div class="links">
         <a href="https://forums.realgm.com/boards/viewforum.php?f=5">Forums</a>
         <a href="/international/news">News</a>
         <a href="/international/news/analysis">Analysis</a>
         <a href="/international/teams">Teams</a>
         <a href="/international/leagues">Leagues</a>
         <a href="/international/schedules">Schedules</a>
         <a href="/international/scores">Scores</a>
         <a href="/international/stats">Stats</a>
      </div>
   </div>
   
   <div class="list-column">
      <h3><a href="/national">National</a></h3>
      <div class="links">
         <a href="https://forums.realgm.com/boards/viewforum.php?f=347">Forums</a>
         <a href="/national/news">News</a>
         <a href="/national/news/analysis">Analysis</a>
         <a href="/national/countries">Countries</a>
         <a href="/national/tournaments">Events</a>
         <a href="/national/schedules">Schedules</a>
         <a href="/national/scores">Scores</a>
         <a href="/national/stats">Stats</a>
      </div>
   </div>
   
   <div class="list-column">
      <h3><a href="/highschool">High School</a></h3>
      <div class="links">
         <a href="https://forums.realgm.com/boards/viewforum.php?f=346">Forums</a>
         <a href="/highschool/news">News</a>
         <a href="/highschool/news/analysis">Analysis</a>
         <a href="/highschool/schools">Schools</a>
         <a href="/highschool/allstar">All-Star Games</a>
         <a href="/highschool/awards">Awards</a>
      </div>
   </div>
</div>
            </div>
            
            <div class="about-us-container">
               <div class="social clearfix">
                  <h3>Follow Us</h3>
<ul class="rrssb-buttons clearfix rrssb-1 large-format">
   <li class="email" data-initwidth="25" style="width: 25%;" data-size="76">
      <a href="https://realgm.m-pages.com/ug2pDT/sign-up" target="_blank">
         <span class="icon">
            <svg xmlns="https://www.w3.org/2000/svg" xmlns:xlink="https://www.w3.org/1999/xlink" version="1.1" x="0px" y="0px" width="28px" height="28px" viewBox="0 0 28 28" enable-background="new 0 0 28 28" xml:space="preserve">
               <g>
                  <path d="M20.111 26.147c-2.336 1.051-4.361 1.401-7.125 1.401c-6.462 0-12.146-4.633-12.146-12.265 c0-7.94 5.762-14.833 14.561-14.833c6.853
                     0 11.8 4.7 11.8 11.252c0 5.684-3.194 9.265-7.399 9.3 c-1.829 0-3.153-0.934-3.347-2.997h-0.077c-1.208 1.986-2.96 2.997-5.023 2.997c-2.532
                     0-4.361-1.868-4.361-5.062 c0-4.749 3.504-9.071 9.111-9.071c1.713 0 3.7 0.4 4.6 0.973l-1.169 7.203c-0.388 2.298-0.116 3.3 1 3.4 c1.673 0
                     3.773-2.102 3.773-6.58c0-5.061-3.27-8.994-9.303-8.994c-5.957 0-11.175 4.673-11.175 12.1 c0 6.5 4.2 10.2 10 10.201c1.986 0 4.089-0.43
                     5.646-1.245L20.111 26.147z M16.646 10.1 c-0.311-0.078-0.701-0.155-1.207-0.155c-2.571 0-4.595 2.53-4.595 5.529c0 1.5 0.7 2.4 1.9 2.4 c1.441
                     0 2.959-1.828 3.311-4.087L16.646 10.068z"></path>
               </g>
            </svg>
         </span>
         <span class="text">newsletter</span>
      </a>
   </li>
   <li class="twitter" data-initwidth="25" style="width: 25%;" data-size="49">
      <a href="https://twitter.com/RealGM" target="_blank">
         <span class="icon">
              <svg version="1.1" id="Layer_1" xmlns="https://www.w3.org/2000/svg" xmlns:xlink="https://www.w3.org/1999/xlink" x="0px" y="0px" width="28px" height="28px" viewBox="0 0 28 28" enable-background="new 0 0 28 28" xml:space="preserve">
                  <path d="M24.253,8.756C24.689,17.08,18.297,24.182,9.97,24.62c-3.122,0.162-6.219-0.646-8.861-2.32
                  c2.703,0.179,5.376-0.648,7.508-2.321c-2.072-0.247-3.818-1.661-4.489-3.638c0.801,0.128,1.62,0.076,2.399-0.155
                  C4.045,15.72,2.215,13.6,2.115,11.077c0.688,0.275,1.426,0.407,2.168,0.386c-2.135-1.65-2.729-4.621-1.394-6.965
                  C5.575,7.816,9.54,9.84,13.803,10.071c-0.842-2.739,0.694-5.64,3.434-6.482c2.018-0.623,4.212,0.044,5.546,1.683
                  c1.186-0.213,2.318-0.662,3.329-1.317c-0.385,1.256-1.247,2.312-2.399,2.942c1.048-0.106,2.069-0.394,3.019-0.851
                  C26.275,7.229,25.39,8.196,24.253,8.756z"></path>
              </svg>
         </span>
         <span class="text">twitter</span>
      </a>
   </li>
   <li class="facebook" data-initwidth="25" style="width: 25%;" data-size="62">
      <a href="https://www.facebook.com/RealGM" target="_blank">
         <span class="icon">
            <svg version="1.1" id="Layer_1" xmlns="https://www.w3.org/2000/svg" xmlns:xlink="https://www.w3.org/1999/xlink" x="0px" y="0px" width="28px" height="28px" viewBox="0 0 28 28" enable-background="new 0 0 28 28" xml:space="preserve">
               <path d="M27.825,4.783c0-2.427-2.182-4.608-4.608-4.608H4.783c-2.422,0-4.608,2.182-4.608,4.608v18.434
                  c0,2.427,2.181,4.608,4.608,4.608H14V17.379h-3.379v-4.608H14v-1.795c0-3.089,2.335-5.885,5.192-5.885h3.718v4.608h-3.726
                  c-0.408,0-0.884,0.492-0.884,1.236v1.836h4.609v4.608h-4.609v10.446h4.916c2.422,0,4.608-2.188,4.608-4.608V4.783z"></path>
            </svg>
         </span>
         <span class="text">facebook</span>
      </a>
   </li>
   <li class="instagram" data-initwidth="25" style="width: 25%;" data-size="66">
      <a href="https://www.instagram.com/realgmnba" target="_blank">
         <span class="icon">
            <svg width="48px" height="48px" viewBox="0 0 48 48" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
             <title>Instagram</title>
             <defs></defs>
             <g id="Icons" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                 <g id="Black" transform="translate(-642.000000, -295.000000)" fill="#000000">
                     <path d="M666.000048,295 C659.481991,295 658.664686,295.027628 656.104831,295.144427 C653.550311,295.260939 651.805665,295.666687 650.279088,296.260017 C648.700876,296.873258 647.362454,297.693897 646.028128,299.028128 C644.693897,300.362454 643.873258,301.700876 643.260017,303.279088 C642.666687,304.805665 642.260939,306.550311 642.144427,309.104831 C642.027628,311.664686 642,312.481991 642,319.000048 C642,325.518009 642.027628,326.335314 642.144427,328.895169 C642.260939,331.449689 642.666687,333.194335 643.260017,334.720912 C643.873258,336.299124 644.693897,337.637546 646.028128,338.971872 C647.362454,340.306103 648.700876,341.126742 650.279088,341.740079 C651.805665,342.333313 653.550311,342.739061 656.104831,342.855573 C658.664686,342.972372 659.481991,343 666.000048,343 C672.518009,343 673.335314,342.972372 675.895169,342.855573 C678.449689,342.739061 680.194335,342.333313 681.720912,341.740079 C683.299124,341.126742 684.637546,340.306103 685.971872,338.971872 C687.306103,337.637546 688.126742,336.299124 688.740079,334.720912 C689.333313,333.194335 689.739061,331.449689 689.855573,328.895169 C689.972372,326.335314 690,325.518009 690,319.000048 C690,312.481991 689.972372,311.664686 689.855573,309.104831 C689.739061,306.550311 689.333313,304.805665 688.740079,303.279088 C688.126742,301.700876 687.306103,300.362454 685.971872,299.028128 C684.637546,297.693897 683.299124,296.873258 681.720912,296.260017 C680.194335,295.666687 678.449689,295.260939 675.895169,295.144427 C673.335314,295.027628 672.518009,295 666.000048,295 Z M666.000048,299.324317 C672.40826,299.324317 673.167356,299.348801 675.69806,299.464266 C678.038036,299.570966 679.308818,299.961946 680.154513,300.290621 C681.274771,300.725997 682.074262,301.246066 682.91405,302.08595 C683.753934,302.925738 684.274003,303.725229 684.709379,304.845487 C685.038054,305.691182 685.429034,306.961964 685.535734,309.30194 C685.651199,311.832644 685.675683,312.59174 685.675683,319.000048 C685.675683,325.40826 685.651199,326.167356 685.535734,328.69806 C685.429034,331.038036 685.038054,332.308818 684.709379,333.154513 C684.274003,334.274771 683.753934,335.074262 682.91405,335.91405 C682.074262,336.753934 681.274771,337.274003 680.154513,337.709379 C679.308818,338.038054 678.038036,338.429034 675.69806,338.535734 C673.167737,338.651199 672.408736,338.675683 666.000048,338.675683 C659.591264,338.675683 658.832358,338.651199 656.30194,338.535734 C653.961964,338.429034 652.691182,338.038054 651.845487,337.709379 C650.725229,337.274003 649.925738,336.753934 649.08595,335.91405 C648.246161,335.074262 647.725997,334.274771 647.290621,333.154513 C646.961946,332.308818 646.570966,331.038036 646.464266,328.69806 C646.348801,326.167356 646.324317,325.40826 646.324317,319.000048 C646.324317,312.59174 646.348801,311.832644 646.464266,309.30194 C646.570966,306.961964 646.961946,305.691182 647.290621,304.845487 C647.725997,303.725229 648.246066,302.925738 649.08595,302.08595 C649.925738,301.246066 650.725229,300.725997 651.845487,300.290621 C652.691182,299.961946 653.961964,299.570966 656.30194,299.464266 C658.832644,299.348801 659.59174,299.324317 666.000048,299.324317 Z M666.000048,306.675683 C659.193424,306.675683 653.675683,312.193424 653.675683,319.000048 C653.675683,325.806576 659.193424,331.324317 666.000048,331.324317 C672.806576,331.324317 678.324317,325.806576 678.324317,319.000048 C678.324317,312.193424 672.806576,306.675683 666.000048,306.675683 Z M666.000048,327 C661.581701,327 658,323.418299 658,319.000048 C658,314.581701 661.581701,311 666.000048,311 C670.418299,311 674,314.581701 674,319.000048 C674,323.418299 670.418299,327 666.000048,327 Z M681.691284,306.188768 C681.691284,307.779365 680.401829,309.068724 678.811232,309.068724 C677.22073,309.068724 675.931276,307.779365 675.931276,306.188768 C675.931276,304.598171 677.22073,303.308716 678.811232,303.308716 C680.401829,303.308716 681.691284,304.598171 681.691284,306.188768 Z" id="Instagram"></path>
                 </g>
                 <g id="Credit" transform="translate(-1734.000000, -472.000000)"></g>
             </g>
         </svg>
         </span>
         <span class="text">instagram</span>
      </a>
   </li>
</ul>
<!-- Buttons end here -->               </div>
               
               <div class="list-column">
                  <h3>RealGM</h3>
                  <div class="links">
                     <a href="/info/contact-us">Contact Us</a>
                     <a href="/info/about-us">About Us</a>
                     <a href="/info/contact-us/advertising">Advertising</a>
                     <a href="/info/privacy-policy">Privacy Policy</a>
                     <a href="/info/terms-of-use">Terms of Use</a>
                  </div>
               </div>
            </div>
            
            <p class="copyright">All content © 2000-2024 RealGM, L.L.C. All rights reserved.</p>
            
            <div style="height: 7em;">&nbsp;</div>
         </footer>
      
      </div> <!-- #site-takeover -->

      <script src="/js/vendor/jquery.hoverIntent.min.js"></script>
      <script src="/js/main.js?v3"></script>
      <script src="/js/plugins.js?v3"></script>
     
      <script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
  ga('create', 'UA-1568648-1', 'auto');
  ga('send', 'pageview');
</script><div id="StickyLeft"><div data-aaad="true" data-aa-adunit="/22181265/realgm_sidewall_rail"></div></div><div style="text-align: center;"><div data-aaad="true" data-aa-adunit="/22181265/realgm_sticky_footer"></div></div><div style="text-align: center;"><div data-aaad="true" data-aa-adunit="/22181265/realgm_mob_sticky_footer"></div></div>    
<ul class="ui-autocomplete ui-front ui-menu ui-widget ui-widget-content" id="ui-id-1" tabindex="0" style="display: none;"></ul><span role="status" aria-live="assertive" aria-relevant="additions" class="ui-helper-hidden-accessible"></span><iframe name="__tcfapiLocator" style="display: none;"></iframe><iframe name="__uspapiLocator" style="display: none;"></iframe></body>
"""
