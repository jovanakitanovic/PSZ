using HtmlAgilityPack;
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

List<PolovniAutomobil> polovniAutomobili = new List<PolovniAutomobil>();
List<PodaciOAutomobilu> podaciOAutomobilu = new List<PodaciOAutomobilu>();

polovniAutomobili=WriteToDatabaseClass.GetData();

var indexProxy = polovniAutomobiliHeplers.GetProxyValues();
var docProxy = polovniAutomobiliHeplers.GetProxyValues();

StreamWriter fileWithCars = new StreamWriter("C:/Users/Jovana/Desktop/MASTER SEMESTAR 2/PSZ/zadatak1/greskeUCitanju.txt");
string[] _Args = { $"--proxy-server={indexProxy.ip}:{indexProxy.port}" };

var options = new LaunchOptions()
{
    Headless = true,
    ExecutablePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    //Args = _Args
};

var browser = await Puppeteer.LaunchAsync(options, null);


Thread tAuto = new Thread(new ThreadStart(ThreadProc));
Thread tLink = new Thread(new ThreadStart(ThreadProc2));


async void ThreadProc2()
{
    for (int i = 0; polovniAutomobili.Count < 30000; i++)
    {
        try
        {

            while (i >= polovniAutomobili.Count) ;

            if (!polovniAutomobili[i].link.Contains("attp"))
            {
                await Index(polovniAutomobili[i].link, polovniAutomobili[i].sajt);
                Console.WriteLine("AUTO " + podaciOAutomobilu.Count + " LINKOVI " + polovniAutomobili.Count);

            }

        }
        catch (Exception ex)
        {
            Console.WriteLine("DOHVATANJE LINKOVA" + ex.ToString());
        }

    }

}

async void ThreadProc()
{
    int num = 0;
    for (int i = 0; i < 30016; i++)
    {

        try
        {
            
            while (i >= polovniAutomobili.Count) ;

            if (polovniAutomobili[i].link.Contains("attp"))
            {
                num++;
                HtmlDocument document = await GetDocument(polovniAutomobili[i].link);
                await GetData(polovniAutomobili[i].link, document, polovniAutomobili[i]);
                Console.WriteLine("AUTO " + podaciOAutomobilu.Count);
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine("VADENJE PODATAKA " + ex.ToString());
        }
        if (num == 200)
        {
            num=0;
        }
    }
}

tAuto.Start();
tLink.Start();

while (podaciOAutomobilu.Count < 2000) ;

fileWithCars.Close();
//WriteToDatabaseClass.ModifyForDatabase(podaciOAutomobilu);


async Task<HtmlDocument> GetDocument(string url)
{
    var responseStatus = HttpStatusCode.OK;
    HtmlDocument document = null;
    do
    {
        try
        {

            HtmlWeb web = new HtmlWeb();
            docProxy.numOfCalls++;

            Uri myUri = new Uri(url, UriKind.Absolute);

            //document = web.Load(myUri,docProxy.ip,docProxy.port,"","");
            document = web.Load(myUri);

            responseStatus = HttpStatusCode.OK;
        }
        catch (Exception ex)
        {
            responseStatus = HttpStatusCode.TooManyRequests;
            docProxy = polovniAutomobiliHeplers.GetProxyValues();
            Console.WriteLine(ex.Message);
        }

    } while (responseStatus == HttpStatusCode.TooManyRequests);

    return document;

}


async Task GetLinksFromThePage(string url, HtmlDocument document, sajtPolovnihAutomobila sajt)
{
    try
    {
        string containsInURL = ContainsInUrl(sajt);
        HtmlNodeCollection AllLinks = document.DocumentNode.SelectNodes("//a[@href]");

        //Console.WriteLine("POKRENUT NOVI URL " + url);

        var baseUri = new Uri(url);

        foreach (var link in AllLinks)
        {
            string href = link.Attributes["href"].Value;
            var linkToAddToList = new Uri(baseUri, href).AbsoluteUri;

            //Console.WriteLine(linkToAddToList);

            if (linkToAddToList.Contains(containsInURL) && !polovniAutomobili.Exists(x => linkToAddToList.Contains(x.link)))
            {
                if (!linkToAddToList.Contains("twitter") && !linkToAddToList.Contains("viber") && !linkToAddToList.Contains("whatsapp")
                    && !linkToAddToList.Contains("facebook") && !linkToAddToList.Contains("instagram") && !linkToAddToList.Contains("youtube") && !linkToAddToList.Contains("linkedin"))
                {
                    polovniAutomobili.Add(new PolovniAutomobil(linkToAddToList, sajt));
                    WriteToDatabaseClass.WriteLINKToDatabase(url);

                }
                //Console.WriteLine("POLOVNI AUTOMOBIL: " + linkToAddToList);
            }
        }

    }
    catch (Exception ex)
    {
        Console.WriteLine("GRESKA (get links from the page)" + url);
        Console.WriteLine(ex.Message);
    }
}

async Task GetData(string url, HtmlDocument document, PolovniAutomobil polovniAutomobil)
{
    
    try
    {
        //await GetLinksFromThePage(url, document, polovniAutomobil.sajt);
        //Console.WriteLine("POKRENUT NOVI URL O AUTOMOBILU " + url);

        var programmerLinks = document.DocumentNode.Descendants("div")
                .Where(node => node.GetAttributeValue("class", "").Contains("infoBox")).ToList();

        var cena = document.DocumentNode.Descendants("span").Where(node => node.GetAttributeValue("class", "").Equals("priceClassified regularPriceColor")).ToList();
        PodaciOAutomobilu automobil;

        if(cena.Count==0)
            cena = document.DocumentNode.Descendants("div").Where(node => node.GetAttributeValue("class", "").Equals("discount regularPriceColor")).ToList();

        
        string[] cenaAutomobila;
        if (cena[0].InnerText.Contains("."))
        {
            cenaAutomobila = cena[0].InnerText.Split("€")[0].Split(".");
            podaciOAutomobilu.Add(automobil = new PodaciOAutomobilu(programmerLinks, int.Parse(cenaAutomobila[0] + cenaAutomobila[1]), url));
        }
        else
        {
            cenaAutomobila = cena[0].InnerText.Split("€");
            podaciOAutomobilu.Add(automobil = new PodaciOAutomobilu(programmerLinks, int.Parse(cenaAutomobila[0]), url));

            fileWithCars.WriteLine(programmerLinks + " " + int.Parse(cenaAutomobila[0]));
        }

        WriteToDatabaseClass.ModifyForDatabase(automobil, fileWithCars);
    }
    catch(IndexOutOfRangeException ex)
    {
        Console.WriteLine("index out of range");
    }
    catch (Exception ex)
    {
        Console.WriteLine("GRESKA (get data)" + url);
        Console.WriteLine(ex.Message);
    }
}


string ContainsInUrl(sajtPolovnihAutomobila sajt)
{
    string containsInURL;

    switch (sajt)
    {
        case sajtPolovnihAutomobila.polovniAutomobili:
            containsInURL = "auto-oglasi";
            break;
        case sajtPolovnihAutomobila.mojAuto:
            containsInURL = "polovni-automobili";
            break;
        default:
            containsInURL = "";
            break;
    }

    return containsInURL;
}


async Task Index(string url, sajtPolovnihAutomobila sajt)
{

    HttpStatusCode status = HttpStatusCode.OK;
    Page page = null;
    do
    {
        try
        {

            indexProxy.numOfCalls++;

            page = await browser.NewPageAsync();
            page.DefaultNavigationTimeout = 100000;
            
            var rez = await page.GoToAsync(url);
            

            status = HttpStatusCode.OK;

            var links = @"Array.from(document.querySelectorAll('a')).map(a => a.href);";
            var AllLinks = await page.EvaluateExpressionAsync<string[]>(links);
            if (AllLinks.Length == 0)
                throw new Exception($"proxy: {indexProxy.ip}:{indexProxy.port}");

            string containsInURL = ContainsInUrl(sajt);

            var carNumber = CarNumber(url, sajt);

            foreach (string link in AllLinks)
            {
                if (link.Contains(containsInURL) && !polovniAutomobili.Exists(x => link.Contains(x.link)) && !link.Contains(carNumber))
                {
                    //if (link.Contains("attp"))
                        polovniAutomobili.Add(new PolovniAutomobil(link, sajt));
                        WriteToDatabaseClass.WriteLINKToDatabase(link);
                    //else
                    //    polovniAutomobiliLinkovi.Add(new PolovniAutomobil(link, sajt));

                }
            }
            await page.CloseAsync();
        }
        catch (Exception ex)
        {
            await page.CloseAsync();
            Console.WriteLine("GRESKA (index)" + url+ $"proxy: {indexProxy.ip}:{indexProxy.port}");
            Console.WriteLine(ex.Message);

            indexProxy = polovniAutomobiliHeplers.GetProxyValues();

            await browser.CloseAsync();
            string[] _Args = { $"--proxy-server={indexProxy.ip}:{indexProxy.port}" };

            options = new LaunchOptions()
            {
                Headless = true,
                ExecutablePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
                //Args = _Args
            };

            browser = await Puppeteer.LaunchAsync(options, null);
            status = HttpStatusCode.TooManyRequests;
        }

    } while (status == HttpStatusCode.TooManyRequests);
}

string CarNumber(string url, sajtPolovnihAutomobila sajt)
{
    try
    {
        var numberOfCar = url.Split("/");

        if (sajt == sajtPolovnihAutomobila.polovniAutomobili)
        {
            return numberOfCar[4];
        }
        return "";
    }
    catch (Exception ex)
    {
        return "+1";
    }
}