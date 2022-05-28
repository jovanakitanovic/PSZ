using HtmlAgilityPack;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Threading.Tasks;
using System.Net;
using System.Text;
using System.IO;
using PSZ;


List<string> linksOnThePage = new List<string>();

GetLinksFromThePage(polovniAutomobiliHeplers.baseAddresses[0], sajtPolovnihAutomobila.polovniAutomobili);
GetLinksFromThePage(polovniAutomobiliHeplers.baseAddresses[1], sajtPolovnihAutomobila.mojAuto);

string[] probaLInks = { "https://www.polovniautomobili.com/auto-oglasi/19996271/mercedes-benz-e-200?attp=p8_pv0_pc1_pl9_plv0",
    "https://www.polovniautomobili.com/auto-oglasi/19939205/skoda-octavia?attp=p8_pv0_pc1_pl9_plv0",
    "https://www.polovniautomobili.com/auto-oglasi/19864480/kia-sportage?attp=p8_pv0_pc1_pl9_plv0",
    "https://www.polovniautomobili.com/auto-oglasi/19986043/volkswagen-polo?attp=p8_pv0_pc1_pl9_plv0"};


for(int i = 0; i < probaLInks.Length; i++)
{
    var rez = await GetData(probaLInks[i]);
}

//for (int index = 0; index < 20000; index++)
//{
//    if (linksOnThePage.Count > index)
//    {
//        GetDocument(linksOnThePage[index]);
//        var rez=await GetData("https://www.polovniautomobili.com/auto-oglasi/19996271/mercedes-benz-e-200?attp=p8_pv0_pc1_pl9_plv0");
//    }
//}  



HtmlDocument GetDocument(string url)
{
    var responseStatus = HttpStatusCode.OK;
    HtmlDocument document=null;

    try
    {
        do
        {
            HtmlWeb webPage = new HtmlWeb();
            document = webPage.Load(url);
            responseStatus = webPage.StatusCode;

            if (responseStatus == HttpStatusCode.TooManyRequests)
                System.Threading.Thread.Sleep((600000));

        } while (responseStatus == HttpStatusCode.TooManyRequests);

    }catch(Exception ex)
    {
        Console.WriteLine(ex.Message);
    }

     return document;

}


void GetLinksFromThePage(string url, sajtPolovnihAutomobila sajt)
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

    HtmlDocument document = GetDocument(url);
    HtmlNodeCollection AllLinks = document.DocumentNode.SelectNodes("//a[@href]");
    var baseUri = new Uri(url);

    foreach (var link in AllLinks)
    {
        string href = link.Attributes["href"].Value;
        var linkToAddToList = new Uri(baseUri, href).AbsoluteUri;

        Console.WriteLine(linkToAddToList);

        if (linkToAddToList.Contains(containsInURL) && !linksOnThePage.Contains(linkToAddToList))
            linksOnThePage.Add(linkToAddToList);
    }
}

 async Task<string>GetData(string url)
{

    HttpClient client = new HttpClient();
    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls13;
    client.DefaultRequestHeaders.Accept.Clear();
    var response = await client.GetStringAsync(url);

    HtmlDocument htmlDoc = new HtmlDocument();
    htmlDoc.LoadHtml(response);
    var programmerLinks = htmlDoc.DocumentNode.Descendants("div")
            .Where(node => node.GetAttributeValue("class", "").Contains("infoBox")).ToList();

    var vals = programmerLinks.FindAll(node => !node.InnerText.Contains("POŠALJI PORUKU"));

    List<string> wikiLink = new List<string>();

    return "";
}