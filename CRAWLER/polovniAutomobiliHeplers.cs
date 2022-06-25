using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Threading.Tasks;
using System.Net;
using System.Text;
using System.IO;
using PSZ;
using PuppeteerSharp;
using Microsoft.AspNetCore.Mvc;
using PSZ_WriteToDatabase;
using System.Web;
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;

namespace PSZ
{
    public enum sajtPolovnihAutomobila
    {
        polovniAutomobili,
        mojAuto
    }

    public static class polovniAutomobiliHeplers
    {
        public static string[] baseAddresses = { "https://www.polovniautomobili.com", "https://www.mojauto.rs/" };
        static string[] lines = System.IO.File.ReadAllLines(@"C:\Users\Jovana\Desktop\proxy3.txt");


        public static List<ProxyValues> proxy = new List<ProxyValues>();
       
        static polovniAutomobiliHeplers()
        {
            foreach(var line in lines)
            {
                var ipPort=line.Split(":");
                proxy.Add(new ProxyValues(ipPort[0],int.Parse(ipPort[1]),int.Parse(ipPort[2])));
            }
        }

        private static int i = -1;
        public static ProxyValues GetProxyValues()
        {
            int j = 0;
            while (polovniAutomobiliHeplers.proxy[(++i) % polovniAutomobiliHeplers.proxy.Count].numOfCalls > 150)
            {
                j++;
                if (j == polovniAutomobiliHeplers.proxy.Count) break;
            }


            return polovniAutomobiliHeplers.proxy[i % polovniAutomobiliHeplers.proxy.Count];
        }
    }


    public class PolovniAutomobil
    {
        public string link;
        public sajtPolovnihAutomobila sajt;
        public List<HtmlAgilityPack.HtmlNode> autoPodaci;

        public PolovniAutomobil(string _link, sajtPolovnihAutomobila _sajt)
        {
            link = _link;
            sajt = _sajt;
            autoPodaci = new List<HtmlAgilityPack.HtmlNode>();
        }
    }

    public class PodaciOAutomobilu
    {
        public List<HtmlAgilityPack.HtmlNode> autoPodaci;
        public int cena;
        public string link;
        public PodaciOAutomobilu(List<HtmlAgilityPack.HtmlNode> podaci, int _cena, string _link)
        {
            autoPodaci = new List<HtmlAgilityPack.HtmlNode>();
            autoPodaci.AddRange(podaci);
            cena = _cena;
            link = _link;
        }
    }

    public class PodaciZaBazu
    {
        public int cena;
        public string link;
        public string stanje;
        public string marka;
        public string model;
        public string karoserija;
        public int godiste;
        public decimal kilometraza;
        public string gorivo;
        public int kubikaza;
        public string snagaMotora;
        public string menjac;
        public string brojVrata;
        public int brojSedista;
        public string boja;
        public string lokacija;
        public string pogon;
        public string materijalEnterijera;
        public int brojDodatneOpreme;
        public string klima;
    }

    public class ProxyValues
    {

        public string ip;
        public int port;
        public int numOfCalls;

        public ProxyValues(string _ip, int _port, int _numOfCalls=0)
        {
            ip = _ip;
            port = _port;
            numOfCalls = _numOfCalls;
        }

    }



}
