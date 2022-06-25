using System;
using System.Linq;
using PSZ;
using MySql.Data.MySqlClient;
using System.Data.SqlClient;
using System.Configuration;
using System.Text.RegularExpressions;

namespace PSZ_WriteToDatabase
{
    public static class WriteToDatabaseClass
    {
        static SqlConnection connection;
        static List<PodaciZaBazu> podaciZaBazu = new List<PodaciZaBazu>();
        static WriteToDatabaseClass()
        {
            connection = new SqlConnection(@"Data Source=localhost;Initial Catalog=psz; User ID=DESKTOP-O4EE418\.Jovana;TrustServerCertificate=true;Trusted_Connection=true");
        }

        public static void ModifyForDatabase(PodaciOAutomobilu podatak, StreamWriter file)
        {
           

            try
            {

                var divs = podatak.autoPodaci[0].Descendants("div")
                .Where(node => node.GetAttributeValue("class", "").Contains("uk-grid")).ToList();

                var dataDivs = podatak.autoPodaci[0].Descendants("div")
                .Where(node => node.GetAttributeValue("class", "").Contains("uk-width-1-2 uk-text-bold")).ToList();

                PodaciZaBazu zaBazu = new PodaciZaBazu();

                zaBazu.cena = podatak.cena;
                zaBazu.link = podatak.link;

                zaBazu.stanje = dataDivs[0].InnerText.Trim();
                zaBazu.marka = dataDivs[1].InnerText.Trim();
                zaBazu.model = dataDivs[2].InnerText.Trim();
                zaBazu.godiste = int.Parse(dataDivs[3].InnerText.Split(".")[0].Trim());
                zaBazu.kilometraza = decimal.Parse(dataDivs[4].InnerText.Split(" ")[0].Trim());
                zaBazu.karoserija = dataDivs[5].InnerText.Trim();
                zaBazu.gorivo = dataDivs[6].InnerText.Trim();
                zaBazu.kubikaza = int.Parse(dataDivs[7].InnerText.Split(" ")[0].Trim());
                zaBazu.snagaMotora = dataDivs[8].InnerText.Trim();

                divs = podatak.autoPodaci[1].Descendants("div")
                        .Where(node => node.GetAttributeValue("class", "").Contains("uk-grid")).ToList();

                dataDivs = podatak.autoPodaci[1].Descendants("div")
                            .Where(node => node.GetAttributeValue("class", "").Contains("uk-width-1-2 uk-text-bold")).ToList();

                zaBazu.pogon = dataDivs[1].InnerText.Trim();
                zaBazu.menjac = dataDivs[2].InnerText.Trim();
                zaBazu.brojVrata = dataDivs[3].InnerText.Trim();
                zaBazu.brojSedista = int.Parse(dataDivs[4].InnerText.Split(" ")[0].Trim());
                zaBazu.klima = dataDivs[6].InnerText.Trim();
                zaBazu.boja = dataDivs[7].InnerText.Trim();
                zaBazu.materijalEnterijera = dataDivs[8].InnerText.Trim();

                divs = podatak.autoPodaci[3].Descendants("div")
                    .Where(node => node.GetAttributeValue("class", "").Contains("uk-width-medium-1-4 uk-width-1-2 uk-margin-small-bottom")).ToList();

                zaBazu.brojDodatneOpreme = divs.Count;

                divs = podatak.autoPodaci[podatak.autoPodaci.Count - 1].DescendantsAndSelf("div")
                        .Where(node => node.GetAttributeValue("class", "").Equals("uk-width-1-2")).ToList();

                //var divLokacija = divs.First<HtmlAgilityPack.HtmlNode>(x => Regex.IsMatch(x.InnerHtml, @"\buk-width-1-2\b"));

                var lokacija = divs[0].InnerText;

                foreach (var slovo in lokacija)
                {
                    if (slovo != '\n' && slovo != '\t' && slovo != ' ')

                        zaBazu.lokacija += slovo;
                    else
                        if ((slovo == '\n' || slovo == '\t') && zaBazu.lokacija?.Length > 0)
                        break;
                }

                WriteToDatabase(zaBazu);

                file.WriteLine(zaBazu.stanje + " " + zaBazu.marka + " " + zaBazu.model + " " + zaBazu.godiste + " " + zaBazu.kilometraza + " " + zaBazu.karoserija + " " + zaBazu.gorivo + " " +
                    zaBazu.kubikaza + " " + zaBazu.snagaMotora + " " + zaBazu.menjac + " " + zaBazu.brojVrata + " " + zaBazu.boja + " " + zaBazu.lokacija + " " + zaBazu.brojSedista + " " + zaBazu.pogon + " " +
                    zaBazu.materijalEnterijera + " " + zaBazu.klima + " " + zaBazu.brojDodatneOpreme + " " + zaBazu.cena + " " + zaBazu.link);
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex);
                ModifyForDatabaseV2(podatak, file);
            }

        }


        public static void ModifyForDatabaseV2(PodaciOAutomobilu podatak, StreamWriter file)
        {


            try
            {

                var divs = podatak.autoPodaci[0].Descendants("div")
                .Where(node => node.GetAttributeValue("class", "").Contains("uk-grid")).ToList();

                var dataDivs = podatak.autoPodaci[0].Descendants("div")
                .Where(node => node.GetAttributeValue("class", "").Contains("uk-width-1-2 uk-text-bold")).ToList();

                PodaciZaBazu zaBazu = new PodaciZaBazu();

                zaBazu.cena = podatak.cena;
                zaBazu.link = podatak.link;

                zaBazu.stanje = dataDivs[0].InnerText.Trim();
                zaBazu.marka = dataDivs[1].InnerText.Trim();
                zaBazu.model = dataDivs[2].InnerText.Trim();
                zaBazu.godiste = int.Parse(dataDivs[3].InnerText.Split(".")[0].Trim());
                zaBazu.kilometraza = decimal.Parse(dataDivs[4].InnerText.Split(" ")[0].Trim());
                zaBazu.karoserija = dataDivs[5].InnerText.Trim();
                zaBazu.gorivo = dataDivs[6].InnerText.Trim();
                zaBazu.kubikaza = int.Parse(dataDivs[7].InnerText.Split(" ")[0].Trim());
                zaBazu.snagaMotora = dataDivs[8].InnerText.Trim();

                divs = podatak.autoPodaci[1].Descendants("div")
                        .Where(node => node.GetAttributeValue("class", "").Contains("uk-grid")).ToList();

                dataDivs = podatak.autoPodaci[1].Descendants("div")
                            .Where(node => node.GetAttributeValue("class", "").Contains("uk-width-1-2 uk-text-bold")).ToList();

                zaBazu.pogon = dataDivs[2].InnerText.Trim();
                zaBazu.menjac = dataDivs[3].InnerText.Trim();
                zaBazu.brojVrata = dataDivs[4].InnerText.Trim();
                zaBazu.brojSedista = int.Parse(dataDivs[5].InnerText.Split(" ")[0].Trim());
                zaBazu.klima = dataDivs[7].InnerText.Trim();
                zaBazu.boja = dataDivs[8].InnerText.Trim();
                zaBazu.materijalEnterijera = dataDivs[9].InnerText.Trim();

                divs = podatak.autoPodaci[3].Descendants("div")
                    .Where(node => node.GetAttributeValue("class", "").Contains("uk-width-medium-1-4 uk-width-1-2 uk-margin-small-bottom")).ToList();

                zaBazu.brojDodatneOpreme = divs.Count;

                divs = podatak.autoPodaci[podatak.autoPodaci.Count - 1].DescendantsAndSelf("div")
                        .Where(node => node.GetAttributeValue("class", "").Equals("uk-width-1-2")).ToList();

                //var divLokacija = divs.First<HtmlAgilityPack.HtmlNode>(x => Regex.IsMatch(x.InnerHtml, @"\buk-width-1-2\b"));

                var lokacija = divs[0].InnerText;

                foreach (var slovo in lokacija)
                {
                    if (slovo != '\n' && slovo != '\t' && slovo != ' ')

                        zaBazu.lokacija += slovo;
                    else
                        if ((slovo == '\n' || slovo == '\t') && zaBazu.lokacija?.Length > 0)
                        break;
                }

                WriteToDatabase(zaBazu);

                file.WriteLine(zaBazu.stanje + " " + zaBazu.marka + " " + zaBazu.model + " " + zaBazu.godiste + " " + zaBazu.kilometraza + " " + zaBazu.karoserija + " " + zaBazu.gorivo + " " +
                    zaBazu.kubikaza + " " + zaBazu.snagaMotora + " " + zaBazu.menjac + " " + zaBazu.brojVrata + " " + zaBazu.boja + " " + zaBazu.lokacija + " " + zaBazu.brojSedista + " " + zaBazu.pogon + " " +
                    zaBazu.materijalEnterijera + " " + zaBazu.klima + " " + zaBazu.brojDodatneOpreme + " " + zaBazu.cena + " " + zaBazu.link);
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex);
                WriteFaliedLInkToDatabase(podatak.link);
            }

        }


        public static void WriteToDatabase(PodaciZaBazu zaBazu)
        {
            connection = new SqlConnection(@"Data Source=localhost;Initial Catalog=psz; User ID=DESKTOP-O4EE418\.Jovana;TrustServerCertificate=true;Trusted_Connection=true");

            try
            {
                string query = "INSERT INTO Cars (stanje, marka ,model,godiste,kilometraza,karoserija,gorivo,kubikaza,snagaMotora,menjac,brojVrata,boja,lokacija,brojSedista,pogon,materijalEnterijera,klima,brojDodatneOpreme,cena, link) " +
                    "values (@stanje, @marka ,@model,@godiste,@kilometraza,@karoserija,@gorivo,@kubikaza,@snagaMotora,@menjac,@brojVrata,@boja,@lokacija,@brojSedista,@pogon,@materijalEnterijera,@klima,@brojDodatneOpreme,@cena,@link)";
                connection.Open();

                using (SqlCommand command = new SqlCommand(query, connection))
                {
                    command.Parameters.AddWithValue("@stanje", zaBazu.stanje);
                    command.Parameters.AddWithValue("@marka", zaBazu.marka);
                    command.Parameters.AddWithValue("@model", zaBazu.model);
                    command.Parameters.AddWithValue("@godiste", zaBazu.godiste);
                    command.Parameters.AddWithValue("@kilometraza", zaBazu.kilometraza);
                    command.Parameters.AddWithValue("@karoserija", zaBazu.karoserija);
                    command.Parameters.AddWithValue("@gorivo", zaBazu.gorivo);
                    command.Parameters.AddWithValue("@kubikaza", zaBazu.kubikaza);
                    command.Parameters.AddWithValue("@snagaMotora", zaBazu.snagaMotora);
                    command.Parameters.AddWithValue("@menjac", zaBazu.menjac);
                    command.Parameters.AddWithValue("@brojVrata", zaBazu.brojVrata);
                    command.Parameters.AddWithValue("@boja", zaBazu.boja);
                    command.Parameters.AddWithValue("@lokacija", zaBazu.lokacija);
                    command.Parameters.AddWithValue("@brojSedista", zaBazu.brojSedista);
                    command.Parameters.AddWithValue("@pogon", zaBazu.pogon);
                    command.Parameters.AddWithValue("@materijalEnterijera", zaBazu.materijalEnterijera);
                    command.Parameters.AddWithValue("@klima", zaBazu.klima);
                    command.Parameters.AddWithValue("@brojDodatneOpreme", zaBazu.brojDodatneOpreme);
                    command.Parameters.AddWithValue("@cena", zaBazu.cena);
                    command.Parameters.AddWithValue("@link", zaBazu.link);

                    command.ExecuteNonQuery();
                }

                connection.Close();
            }
            catch (Exception ex)
            {
                Console.WriteLine(zaBazu.stanje + " " + zaBazu.marka + " " + zaBazu.model + " " +
                    zaBazu.godiste + " " + zaBazu.kilometraza + " " + zaBazu.karoserija + " " + zaBazu.gorivo +
                    " " + zaBazu.kubikaza + " " + zaBazu.snagaMotora + " " + zaBazu.menjac + " " + zaBazu.brojVrata + " " + zaBazu.boja + " " +
                    zaBazu.lokacija + " " + zaBazu.brojSedista + " " + zaBazu.pogon + " " + zaBazu.materijalEnterijera + " " + zaBazu.klima + " " + zaBazu.brojDodatneOpreme);
            }
        }

        public static void WriteLINKToDatabase(string url)
        {
            connection = new SqlConnection(@"Data Source=localhost;Initial Catalog=psz; User ID=DESKTOP-O4EE418\.Jovana;TrustServerCertificate=true;Trusted_Connection=true");

            try
            {
                string query = "INSERT INTO links (link) VALUES(@link)";
                connection.Open();

                using (SqlCommand command = new SqlCommand(query, connection))
                {
                    command.Parameters.AddWithValue("@link", url);

                    command.ExecuteNonQuery();
                }

                connection.Close();
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex);
            }
        }

        public static void WriteFaliedLInkToDatabase(string url)
        {
            try
            {
                string query = "INSERT INTO failedLinks (link) VALUES(@link)";
                connection.Open();

                using (SqlCommand command = new SqlCommand(query, connection))
                {
                    command.Parameters.AddWithValue("@link", url);

                    command.ExecuteNonQuery();
                }

                connection.Close();
            }
            catch (Exception ex)
            {
            }
        }

        public static List<PolovniAutomobil> GetData()
        {
            List<PolovniAutomobil> polovniAutomobili = new List<PolovniAutomobil>();

            using (connection)
            using (SqlCommand command = new SqlCommand("select * from links", connection))
            {
                connection.Open();
                using (SqlDataReader reader = command.ExecuteReader())
                {
                    while(reader.Read())
                    {
                       polovniAutomobili.Add(new PolovniAutomobil(reader.GetString(0),sajtPolovnihAutomobila.polovniAutomobili));
                    }
                }
            }

            connection.Close();
            return polovniAutomobili;
        }

    }
}