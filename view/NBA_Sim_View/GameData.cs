using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace NBA_Sim_View
{
    internal class GameData
    {
        public int id { get; set; }
        public string date { get; set; }
        public string visitor_team { get; set; }
        public int visitor_pts { get; set; }
        public string home_team { get; set; }
        public int home_pts { get; set; }
        public string ot { get; set; }
        public int attendance { get; set; }
        public string arena { get; set; }
        public string game_type { get; set; }
    }
        
}
