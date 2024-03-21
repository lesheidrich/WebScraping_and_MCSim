using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace NBA_Sim_View
{
    internal class Response
    {
        private int status;

        public int Status
        {
            get { return status; }
            set { status = value; }
        }


        private string message;

        public string Message
        {
            get { return message; }
            set { message = value; }
        }

        private string image;

        public string Image
        {
            get { return image; }
            set { image = value; }
        }

        private string image2;

        public string Image2
        {
            get { return image2; }
            set { image2 = value; }
        }


    }
}
