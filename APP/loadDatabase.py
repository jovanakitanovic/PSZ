
import MySQLdb
import pyodbc

class Automobili:


    def __init__(self, stanje, marka, model, godiste, kilometraza, karoserija, gorivo, kubikaza, snagaMotora, menjac, brojVrata, boja, lokacija, brojSedista,pogon,
                 materijalEnterijera, klima, brDodatneOpreme, cena):
        self.stanje=stanje
        self.marka=marka
        self.model=model
        self.godiste=godiste
        self.kilometraza=kilometraza
        self.karoserija=karoserija
        self.gorivo=gorivo
        self.kubikaza=kubikaza
        self.menjac=menjac
        self.brojVrata=brojVrata
        self.boja=boja
        self.lokacija=lokacija
        self.brojSedista=brojSedista
        self.materijalEnterijera=materijalEnterijera
        self.klima=klima
        self.brDodatneOpreme=brDodatneOpreme
        self.cena=cena
        self.pogon=pogon
        self.snagaMotora=snagaMotora

class Helpers:
    listOfCars= list()
    filteredListOfCars=list()
    filteredListOfCarsV2=list()
    chosenParams = ["stanje","marka","model","godiste","kilometraza","kubikaza","snagaMotora"] #,"dodatnaOprema"]
    chosenParamsValues=list()
    classifiedListOfCars=list()

    stanjeDict = dict()
    markaDict = dict()
    modelDict = dict()
    karoserijaDict = dict()
    kilometrazaDict=dict()
    kubikazaDict=dict()
    godisteDict=dict()
    gorivoDict = dict()
    menjacDict = dict()
    brojVrataDict = dict()
    bojaDict = dict()
    lokacijaDict = dict()
    pogonDict = dict()
    klimaDict = dict()
    snagaMotoraDict=dict()
    brojSedistaDict=dict()

    dodatnaOpremaDictV2=dict()
    stanjeDictV2 = dict()
    markaDictV2 = dict()
    modelDictV2 = dict()
    kilometrazaDictV2=dict()
    kubikazaDictV2=dict()
    godisteDictV2=dict()
    snagaMotoraDictV2=dict()
    brojSedistaDictV2=dict()

    stanjeDictKNN=dict()
    markaDictKNN=dict()
    modelDictKNN=dict()
    snagaMotoraDictKNN=dict()

    _W0=0.2
    _W=list()

    _W0V2=0.2
    _WV2=list()

    K=0

def readDatabaseToList():
    con = pyodbc.connect('DRIVER={SQL Server};'
                            'SERVER=localhost;'
                            'DATABASE=psz;'
                            'UID=DESKTOP-O4EE418\.Jovana;'
                            'PWD=;'
                           'Trusted_Connection=yes;')
    cursor = con.cursor()

    #cursor.execute("select * from dbo.CarAds where cena >= 1000 and kubikaza <=7000")
    cursor.execute("select * from dbo.CarAds where cena >= 1000  and kubikaza <=7000 order by godiste asc")

    cars = cursor.fetchall();

    for car in cars:
         Helpers.listOfCars.append(Automobili(car[0],car[1],car[2],car[3],car[4],car[5],car[6],car[7],car[8].split()[0],car[9],car[10].split()[0],
                               car[11],car[12].lower(),car[13],car[14],car[15],car[16],car[17], car[18]))


def Models(models):
    con = pyodbc.connect('DRIVER={SQL Server};'
                         'SERVER=localhost;'
                         'DATABASE=psz;'
                         'UID=DESKTOP-O4EE418\.Jovana;'
                         'PWD=;'
                         'Trusted_Connection=yes;')
    cursor = con.cursor()

    cursor.execute(f"select distinct model from dbo.CarAds where marka = '{models}'")
    allModels = cursor.fetchall();
    return allModels

def MarkaAutomobila():
    con = pyodbc.connect('DRIVER={SQL Server};'
                         'SERVER=localhost;'
                         'DATABASE=psz;'
                         'UID=DESKTOP-O4EE418\.Jovana;'
                         'PWD=;'
                         'Trusted_Connection=yes;')
    cursor = con.cursor()
    cursor.execute("select distinct marka from dbo.CarAds")
    allData = cursor.fetchall();

    return allData

def snagaMotora():
    con = pyodbc.connect('DRIVER={SQL Server};'
                         'SERVER=localhost;'
                         'DATABASE=psz;'
                         'UID=DESKTOP-O4EE418\.Jovana;'
                         'PWD=;'
                         'Trusted_Connection=yes;')
    cursor = con.cursor()
    cursor.execute("select distinct snagaMotora from dbo.CarAds")
    allData = cursor.fetchall();

    return allData

def kubikaza():
    con = pyodbc.connect('DRIVER={SQL Server};'
                         'SERVER=localhost;'
                         'DATABASE=psz;'
                         'UID=DESKTOP-O4EE418\.Jovana;'
                         'PWD=;'
                         'Trusted_Connection=yes;')
    cursor = con.cursor()
    cursor.execute("select distinct kubikaza from dbo.CarAds")
    allData = cursor.fetchall();

    return allData

def encodeParamValesV2():

    con = pyodbc.connect('DRIVER={SQL Server};'
                         'SERVER=localhost;'
                         'DATABASE=psz;'
                         'UID=DESKTOP-O4EE418\.Jovana;'
                         'PWD=;'
                         'Trusted_Connection=yes;')
#---------BEGIN-STANJE-----------------------------------
    cursor = con.cursor()
    cursor.execute("select distinct stanje from dbo.CarAds")
    allData = cursor.fetchall();

    for i in range(0, len(allData)):
        if allData[i][0] == 'Polovno vozilo':
            Helpers.stanjeDictV2[allData[i][0]]=0
        else:
            Helpers.stanjeDictV2[allData[i][0]] =1
# ---------END-STANJE-----------------------------------

# ---------BEGIN-MARKA-----------------------------------
    cursor.execute("select marka, Avg(cena) from dbo.CarAds GROUP BY marka Order by Avg(cena) asc")
    allData = cursor.fetchall();

    for i in range(0, len(allData)):
        if allData[i][1] < 11000:
            Helpers.markaDictV2[allData[i][0]] = 0
        else:
            #print('{0} - {1}'.format(allData[i][0], (allData[i][1])/(11000)))
            Helpers.markaDictV2[allData[i][0]]=float((allData[i][1])/(11000))
        #Helpers.markaDict[allData[i][0]]=float((i+1))
# ---------END-MARKA-----------------------------------

# ---------BEGIN-MODEL-----------------------------------
    cursor.execute("select model, Avg(cena) from dbo.CarAds GROUP BY model Order by Avg(cena) asc")
    allData = cursor.fetchall();

    for i in range(0, len(allData)):
        if allData[i][1]<11000:
            Helpers.modelDictV2[allData[i][0]] = float((allData[i][1])/(100000))
        else:
            Helpers.modelDictV2[allData[i][0]]=float((allData[i][1])/(10000))
        #print('{0} - {1}'.format(allData[i][0], float((allData[i][1]) / (10000))))
        #Helpers.modelDict[allData[i][0]]=float((i)/(761))
# ---------END-MODEL-----------------------------------

# ---------BEGIN-MARKA-----------------------------------
    cursor.execute("select brojDodatneOpreme from dbo.CarAds")
    allData = cursor.fetchall();

    for i in range(0, len(allData)):
        # if allData[i][1] < 11000:
        #    Helpers.markaDict[allData[i][0]] = 0
        # else:
        #   Helpers.markaDict[allData[i][0]]=float((allData[i][1])/(11000))
        Helpers.dodatnaOpremaDictV2[allData[i][0]] = float(allData[i][0] / 95)

# ---------END-MARKA-----------------------------------

# ---------BEGIN-KILOMETRAZA-----------------------------------
    cursor.execute("select distinct kilometraza from dbo.CarAds")
    allData = cursor.fetchall();

    for i in range(0, len(allData)):
        if (allData[i][0] <= 13.00):
            Helpers.kilometrazaDictV2[allData[i][0]] = 4
        if (allData[i][0] > 13.00 and allData[i][0] <= 50.00):
            Helpers.kilometrazaDictV2[allData[i][0]] = 3
        if (allData[i][0] > 50.00 and allData[i][0] <= 100.00):
            Helpers.kilometrazaDictV2[allData[i][0]] = 2
        if (allData[i][0] > 100.00 and allData[i][0] <= 150.00):
            Helpers.kilometrazaDictV2[allData[i][0]] = 1
        if (allData[i][0] > 150.00 and allData[i][0] <= 200.00):
            Helpers.kilometrazaDictV2[allData[i][0]] = 0.5
        if (allData[i][0] > 200.00 and allData[i][0] <= 250.00):
            Helpers.kilometrazaDictV2[allData[i][0]] = 0.04
        if (allData[i][0] > 250.00 and allData[i][0]<= 300.00):
            Helpers.kilometrazaDictV2[allData[i][0]] = 0.03
        if (allData[i][0] > 300.00 and allData[i][0] <= 350.00):
            Helpers.kilometrazaDictV2[allData[i][0]] = 0.002
        if (allData[i][0] > 350.00 and allData[i][0] <= 400.00):
            Helpers.kilometrazaDictV2[allData[i][0]] = 0.0001
        if (allData[i][0] > 400.00 and allData[i][0] <= 450.00):
            Helpers.kilometrazaDictV2[allData[i][0]] = 0
        if (allData[i][0] > 450.00):
            Helpers.kilometrazaDictV2[allData[i][0]] = 0

        #print('{0} - {1}'.format(allData[i][0], Helpers.kilometrazaDict[allData[i][0]]))

    # ---------END-KILOMETRAZA-----------------------------------

# ---------BEGIN-GODISTE-----------------------------------
    cursor.execute("select distinct godiste from dbo.CarAds")
    allData = cursor.fetchall();

    for i in range(0, len(allData)):
        Helpers.godisteDictV2[allData[i][0]] = float(((allData[i][0]-1956)/(2022-1956))-0.5)
        #print('{0} - {1}'.format(allData[i][0], Helpers.godisteDict[allData[i][0]]))
        #Helpers.godisteDict[allData[i][0]] = float((allData[i][0]))

# ---------END-GODISTE-----------------------------------

# ---------BEGIN-KUBIKAZA-----------------------------------
    cursor.execute("select distinct kubikaza from dbo.CarAds")
    allData = cursor.fetchall();

    for i in range(0, len(allData)):
        #print('{0} - {1}'.format(allData[i][0], i))
        Helpers.kubikazaDictV2[allData[i][0]] = float((allData[i][0]-100)/(6492))
        #Helpers.kubikazaDict[allData[i][0]] = float((allData[i][0]))
# ---------END-KUBIKAZA-----------------------------------

# ---------BEGIN-SNAGA MOTORA-----------------------------------
    cursor.execute("select distinct snagaMotora from dbo.CarAds")
    allData = cursor.fetchall();

    for i in range(0, len(allData)):
        #print('{0} - {1}'.format(allData[i][0].split()[0], i))
        Helpers.snagaMotoraDictV2[allData[i][0].split()[0]] = float(i/266)
        #Helpers.snagaMotoraDict[allData[i][0].split()[0]] = float(int(allData[i][0].split()[0].split("/")[0])/662)
        #Helpers.snagaMotoraDict[allData[i][0].split()[0]] = float(i+1)
# ---------END-SNAGA MOTORA-----------------------------------


def encodeParamVales():

        con = pyodbc.connect('DRIVER={SQL Server};'
                             'SERVER=localhost;'
                             'DATABASE=psz;'
                             'UID=DESKTOP-O4EE418\.Jovana;'
                             'PWD=;'
                             'Trusted_Connection=yes;')
        # ---------BEGIN-STANJE-----------------------------------
        cursor = con.cursor()
        cursor.execute("select distinct stanje from dbo.CarAds")
        allData = cursor.fetchall();

        for i in range(0, len(allData)):
            if allData[i][0] == 'Polovno vozilo':
                Helpers.stanjeDict[allData[i][0]] = 0
            else:
                Helpers.stanjeDict[allData[i][0]] = 1
        # ---------END-STANJE-----------------------------------

        # ---------BEGIN-MARKA-----------------------------------
        cursor.execute("select marka, Avg(cena) from dbo.CarAds group by marka")
        allData = cursor.fetchall();

        for i in range(0, len(allData)):
            # if allData[i][1] < 11000:
            #    Helpers.markaDict[allData[i][0]] = 0
            # else:
            #   Helpers.markaDict[allData[i][0]]=float((allData[i][1])/(11000))
            Helpers.markaDict[allData[i][0]] = float(allData[i][1] / 65872)
            print('{0} - {1}'.format(allData[i][0], Helpers.markaDict[allData[i][0]]))

        # ---------END-MARKA-----------------------------------

        # ---------BEGIN-MODEL-----------------------------------
        cursor.execute("select model ,  Avg(cena) from dbo.CarAds group by model")
        allData = cursor.fetchall();

        for i in range(0, len(allData)):
            #    if allData[i][1]<11000:
            #        Helpers.modelDict[allData[i][0]] = float((allData[i][1])/(100000))
            #    else:
            #        Helpers.modelDict[allData[i][0]]=float((allData[i][1])/(10000))
            Helpers.modelDict[allData[i][0]] = float((allData[i][1]) / (275900))
            print('{0} - {1}'.format(allData[i][0], Helpers.modelDict[allData[i][0]]))

        # ---------END-MODEL-----------------------------------

        # ---------BEGIN-KAROSERIJA-----------------------------------
        cursor.execute("select distinct karoserija from dbo.CarAds")
        allData = cursor.fetchall();

        for i in range(0, len(allData)):
            # print('{0} - {1}'.format(allData[i][0], i))
            Helpers.karoserijaDict[allData[i][0]] = i + 1
        # ---------END-KAROSERIJA-----------------------------------

        # ---------BEGIN-KILOMETRAZA-----------------------------------
        cursor.execute("select distinct kilometraza from dbo.CarAds")
        allData = cursor.fetchall();

        for i in range(0, len(allData)):
            # if (allData[i][0] <= 13.00):
            #    Helpers.kilometrazaDict[allData[i][0]] = 4
            # if (allData[i][0] > 13.00 and allData[i][0] <= 50.00):
            #    Helpers.kilometrazaDict[allData[i][0]] = 3
            # if (allData[i][0] > 50.00 and allData[i][0] <= 100.00):
            #    Helpers.kilometrazaDict[allData[i][0]] = 2
            # if (allData[i][0] > 100.00 and allData[i][0] <= 150.00):
            #    Helpers.kilometrazaDict[allData[i][0]] = 1
            # if (allData[i][0] > 150.00 and allData[i][0] <= 200.00):
            #    Helpers.kilometrazaDict[allData[i][0]] = 0.5
            # if (allData[i][0] > 200.00 and allData[i][0] <= 250.00):
            #    Helpers.kilometrazaDict[allData[i][0]] = 0.04
            # if (allData[i][0] > 250.00 and allData[i][0]<= 300.00):
            #    Helpers.kilometrazaDict[allData[i][0]] = 0.03
            # if (allData[i][0] > 300.00 and allData[i][0] <= 350.00):
            #    Helpers.kilometrazaDict[allData[i][0]] = 0.002
            # if (allData[i][0] > 350.00 and allData[i][0] <= 400.00):
            #    Helpers.kilometrazaDict[allData[i][0]] = 0.0001
            # if (allData[i][0] > 400.00 and allData[i][0] <= 450.00):
            #    Helpers.kilometrazaDict[allData[i][0]] = 0
            # if (allData[i][0] > 450.00):
            #    Helpers.kilometrazaDict[allData[i][0]] = 0
            Helpers.kilometrazaDict[allData[i][0]] = allData[i][0] / 1000
            print('{0} - {1}'.format(allData[i][0], Helpers.kilometrazaDict[allData[i][0]]))

        # ---------END-KILOMETRAZA-----------------------------------

        # ---------BEGIN-GODISTE-----------------------------------
        cursor.execute("select distinct godiste from dbo.CarAds")
        allData = cursor.fetchall();

        for i in range(0, len(allData)):
            Helpers.godisteDict[allData[i][0]] = float(((allData[i][0] - 1956) / (2022 - 1956)))
            print('{0} - {1}'.format(allData[i][0], Helpers.godisteDict[allData[i][0]]))
            # Helpers.godisteDict[allData[i][0]] = float((allData[i][0]))

        # ---------END-GODISTE-----------------------------------


        # ---------BEGIN-KUBIKAZA-----------------------------------
        cursor.execute("select distinct kubikaza from dbo.CarAds")
        allData = cursor.fetchall();

        for i in range(0, len(allData)):
            # print('{0} - {1}'.format(allData[i][0], i))
            Helpers.kubikazaDict[allData[i][0]] = float((allData[i][0] - 100) / (6492))
            # Helpers.kubikazaDict[allData[i][0]] = float((allData[i][0]))
        # ---------END-KUBIKAZA-----------------------------------

        # ---------BEGIN-SNAGA MOTORA-----------------------------------
        cursor.execute("select distinct snagaMotora from dbo.CarAds")
        allData = cursor.fetchall();

        for i in range(0, len(allData)):
            # print('{0} - {1}'.format(allData[i][0].split()[0], i))
            Helpers.snagaMotoraDict[allData[i][0].split()[0]] = float(i / 266)
            # Helpers.snagaMotoraDict[allData[i][0].split()[0]] = float(i+1)
        # ---------END-SNAGA MOTORA-----------------------------------


def encodeParamValuesKNNV2():
    stanjeDictKNN=dict()
    markaDictKNN=dict()
    modelDictKNN=dict()
    snagaMotoraDictKNN=dict()

    con = pyodbc.connect('DRIVER={SQL Server};'
                         'SERVER=localhost;'
                         'DATABASE=psz;'
                         'UID=DESKTOP-O4EE418\.Jovana;'
                         'PWD=;'
                         'Trusted_Connection=yes;')
    # ---------BEGIN-STANJE-----------------------------------
    cursor = con.cursor()
    cursor.execute("select distinct stanje from dbo.CarAds")
    allData = cursor.fetchall();

    for i in range(0, len(allData)):
        if allData[i][0] == 'Polovno vozilo':
            Helpers.stanjeDictKNN[allData[i][0]] = 0
        else:
            Helpers.stanjeDictKNN[allData[i][0]] = 1
    # ---------END-STANJE-----------------------------------

    # ---------BEGIN-MARKA-----------------------------------
    #cursor.execute("select distinct marka from dbo.CarAds")
    cursor.execute("select marka, Avg(cena) from dbo.CarAds group by marka order by Avg(cena)")
    allData = cursor.fetchall();

    for i in range(0, len(allData)):
        Helpers.markaDictKNN[allData[i][0]] = allData[i][1]
        #print('{0} - {1}'.format(allData[i][0], Helpers.markaDictKNN[allData[i][0]]))
    # ---------END-MARKA-----------------------------------

    # ---------BEGIN-MODEL-----------------------------------
    #cursor.execute("select model from dbo.CarAds")
    cursor.execute("select model ,  Avg(cena) from dbo.CarAds group by model order by Avg(cena)")
    allData = cursor.fetchall();

    for i in range(0, len(allData)):
        Helpers.modelDictKNN[allData[i][0]] = allData[i][1]

    # ---------END-MODEL-----------------------------------

    # ---------BEGIN-SNAGA MOTORA-----------------------------------
    cursor.execute("select distinct snagaMotora from dbo.CarAds")
    allData = cursor.fetchall();

    for i in range(0, len(allData)):
        Helpers.snagaMotoraDictKNN[allData[i][0].split()[0]] =int(allData[i][0].split()[0].split("/")[0])
        #print('{0} - {1}'.format(allData[i][0], Helpers.snagaMotoraDictKNN[allData[i][0].split()[0]]))
    # ---------END-SNAGA MOTORA-----------------------------------

def encodeParamValuesKNN():
    stanjeDictKNN=dict()
    markaDictKNN=dict()
    modelDictKNN=dict()
    snagaMotoraDictKNN=dict()

    con = pyodbc.connect('DRIVER={SQL Server};'
                         'SERVER=localhost;'
                         'DATABASE=psz;'
                         'UID=DESKTOP-O4EE418\.Jovana;'
                         'PWD=;'
                         'Trusted_Connection=yes;')
    # ---------BEGIN-STANJE-----------------------------------
    cursor = con.cursor()
    cursor.execute("select distinct stanje from dbo.CarAds")
    allData = cursor.fetchall();

    for i in range(0, len(allData)):
        nazivNum = 0
        for letter in allData[i][0]:
            nazivNum += ord(letter)

        Helpers.stanjeDictKNN[allData[i][0]] = nazivNum
    # ---------END-STANJE-----------------------------------

    # ---------BEGIN-MARKA-----------------------------------
    #cursor.execute("select distinct marka from dbo.CarAds")
    cursor.execute("select marka from dbo.CarAds")
    allData = cursor.fetchall();

    for i in range(0, len(allData)):
        nazivNum=0
        for letter in allData[i][0]:
            nazivNum+=ord(letter)

        Helpers.markaDictKNN[allData[i][0]] = nazivNum
        #print('{0} - {1}'.format(allData[i][0], Helpers.markaDictKNN[allData[i][0]]))
    # ---------END-MARKA-----------------------------------

    # ---------BEGIN-MODEL-----------------------------------
    #cursor.execute("select model from dbo.CarAds")
    cursor.execute("select model from dbo.CarAds ")
    allData = cursor.fetchall();

    for i in range(0, len(allData)):
        nazivNum=0
        for letter in allData[i][0]:
            nazivNum+=ord(letter)

        Helpers.modelDictKNN[allData[i][0]] = nazivNum
        #print('{0} - {1}'.format(allData[i][0], Helpers.modelDictKNN[allData[i][0]]))

    # ---------END-MODEL-----------------------------------

    # ---------BEGIN-SNAGA MOTORA-----------------------------------
    cursor.execute("select distinct snagaMotora from dbo.CarAds")
    allData = cursor.fetchall();

    for i in range(0, len(allData)):
        Helpers.snagaMotoraDictKNN[allData[i][0].split()[0]] =int(allData[i][0].split()[0].split("/")[0])
        #print('{0} - {1}'.format(allData[i][0], Helpers.snagaMotoraDictKNN[allData[i][0].split()[0]]))
    # ---------END-SNAGA MOTORA-----------------------------------

def encodeParamValuesKNNHamming():
    stanjeDictKNN=dict()
    markaDictKNN=dict()
    modelDictKNN=dict()
    snagaMotoraDictKNN=dict()

    con = pyodbc.connect('DRIVER={SQL Server};'
                         'SERVER=localhost;'
                         'DATABASE=psz;'
                         'UID=DESKTOP-O4EE418\.Jovana;'
                         'PWD=;'
                         'Trusted_Connection=yes;')
    # ---------BEGIN-STANJE-----------------------------------
    cursor = con.cursor()
    cursor.execute("select distinct stanje from dbo.CarAds")
    allData = cursor.fetchall();

    for i in range(0, len(allData)):
            Helpers.stanjeDictKNN[allData[i][0]] = allData[i][0]
    # ---------END-STANJE-----------------------------------

    # ---------BEGIN-MARKA-----------------------------------
    #cursor.execute("select distinct marka from dbo.CarAds")
    cursor.execute("select marka from dbo.CarAds")
    allData = cursor.fetchall();

    for i in range(0, len(allData)):
        Helpers.markaDictKNN[allData[i][0]] = allData[i][0]
        #print('{0} - {1}'.format(allData[i][0], Helpers.markaDictKNN[allData[i][0]]))
    # ---------END-MARKA-----------------------------------

    # ---------BEGIN-MODEL-----------------------------------
    #cursor.execute("select model from dbo.CarAds")
    cursor.execute("select model from dbo.CarAds ")
    allData = cursor.fetchall();

    for i in range(0, len(allData)):
        Helpers.modelDictKNN[allData[i][0]] = allData[i][0]
        #print('{0} - {1}'.format(allData[i][0], Helpers.modelDictKNN[allData[i][0]]))

    # ---------END-MODEL-----------------------------------

    # ---------BEGIN-SNAGA MOTORA-----------------------------------
    cursor.execute("select distinct snagaMotora from dbo.CarAds")
    allData = cursor.fetchall();

    for i in range(0, len(allData)):
        Helpers.snagaMotoraDictKNN[allData[i][0].split()[0]] =int(allData[i][0].split()[0].split("/")[0])
        #print('{0} - {1}'.format(allData[i][0], Helpers.snagaMotoraDictKNN[allData[i][0].split()[0]]))
    # ---------END-SNAGA MOTORA-----------------------------------
