using System;
using System.IO;
using System.Net;
using System.Text;
using xNet;

namespace restClient
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Добро пожаловать в нашу систему! Выберите действие:");
            while (true)
            {
                Console.WriteLine("1. Вывести список кафедр" +
                    "\n2. Добавить кафедру");
                int choice = Int32.Parse(Console.ReadLine());
                switch(choice)
                {
                    case 1:
                        GetPulpits();
                        break;
                    case 2:
                        Console.WriteLine("Введите название кафедры:");
                        string title = Console.ReadLine();
                        Console.WriteLine("Введите описание кафедры:");
                        string description = Console.ReadLine();
                        InsertPulpit(title, description);
                        break;
                }
            }
        }

        static void Post(string jsonstring, string url)
        {
            string json = jsonstring;
            Byte[] body = Encoding.UTF8.GetBytes(json);

            HttpWebRequest request = (HttpWebRequest)WebRequest.Create(url);
            request.Method = "POST";
            request.ContentType = "application/json";
            request.ContentLength = body.Length;

            using (Stream stream = request.GetRequestStream())
            {
                stream.Write(body, 0, body.Length);
                stream.Close();
            }

            using (HttpWebResponse response = (HttpWebResponse)request.GetResponse())
            {
                response.Close();
            }
        }

        static void Get(string url)
        {
            HttpRequest request = new HttpRequest();
            request.Cookies = new CookieDictionary();
            HttpResponse response = request.Get(url);
            Console.WriteLine(response.ToString());
        }

        static void GetPulpits()
        {
            Get("http://localhost:5000/pulpits/get");
        }

        static void InsertPulpit(string title, string description)
        {
            //string json = "{\"title\":\"asfsad\", \"description\":\"asljf\"}";

            string json = "{\"title\":\"" + title + "\", \"description\":\"" + description + "\"}";
            Post(json, "http://localhost:5000/pulpits/post");
        }
    }
}
