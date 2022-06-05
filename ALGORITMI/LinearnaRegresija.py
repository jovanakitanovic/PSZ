import random
import Helpers
import math
import sys
import loadDatabase as DB

class Automobili:


    def __init__(self, stanje, marka, model, godiste, kilometraza, karoserija, gorivo, kubikaza, snagaMotora, menjac, brojVrata, boja, lokacija, brojSedista,
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
        self.snagaMotora=snagaMotora



def linearnaRegresija(_W0,_W,_set):


    W0=_W0
    W0min=0;

    L0=0
    L=list()

    W=_W
    Wmin=list;

    alpha =0.5;
    lam=0
    numMax=0

    trainCars=_set
    index=len(_set)

    J=1;
    Jmin=sys.maxsize

    for i in range(0, len(DB.Helpers.filteredListOfCars[0]) - 1):
        L.append(0)



    for num in range(0,1000):

        L0=0
        a=0
        for i in range(0, len(W)):
            L[i]=0

        for trainCar in trainCars:

            trainCar["h"]=W0
            for i in range(0,len(W)):
                trainCar['h'] += W[i] * float(trainCar[DB.Helpers.chosenParams[i]])

            #print('h {0} >> y {1} '.format(trainCar["h"],trainCar['cena']))


        for trainCar in trainCars:
            L0+=float(trainCar["h"])-trainCar["cena"]+float(W0*lam)
            for j in range(0,len(W)):
                L[j] += (float(trainCar["h"])-trainCar["cena"]) * float(trainCar[DB.Helpers.chosenParams[j]])+float(W[j]*lam)

        W0 = W0 - alpha * (1 / index) * L0

        Wsum=0
        for j in range(0, len(W)):
            Wsum = W[j] * W[j]
            W[j]=W[j]-alpha*(1/index)*L[j]

        J=(1/(2*index))*(float(L0)*float(L0)+lam*Wsum)

        if Jmin>J:
            numMax = 0
            W0min=W0
            Jmin=J
            Wmin=W
        else:
            numMax+=1
            if numMax > 2:
                return W0,Wmin, Jmin

        #print(J)


def proveraLinearneRegresije(W0,W,collection):

    num=0

    RMSE=0
    sumaY=0
    sumaH=0

    for emlem in collection:

        emlem["h"] = W0
        for i in range(0, len(W)):
            emlem['h'] += W[i] * float(emlem[DB.Helpers.chosenParams[i]])

        sumaY+=emlem['cena']
        sumaH+=emlem['h']

        RMSE+=(sumaH-sumaY)*(sumaH-sumaY)
        percentage = 100-abs(float((emlem['h']-emlem['cena'])/emlem['cena']))*100
        print('h {0} >> y {1} | TAČNOST > % {2}'.format(emlem["h"], emlem['cena'],percentage))

        num+=1

        if num==1000:
            num=0
            print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

    RMSE=math.sqrt(RMSE/len(collection))

    percentage = 100-abs(float((sumaH - sumaY) / sumaY)) * 100
    print("ukupna razlika u cenama u procenutu >> {0}".format(percentage))
    print("RMSE >> {0}".format(RMSE))

def cenaAutomobilaJe(W0,W):

    elem=dict()

    elem["stanje"]=DB.Helpers.stanjeDict[DB.Helpers.chosenParamsValues[0]]
    elem["marka"]=DB.Helpers.markaDict[DB.Helpers.chosenParamsValues[1]]
    elem["model"]=DB.Helpers.modelDict[DB.Helpers.chosenParamsValues[2]]
    elem["godiste"]=DB.Helpers.godisteDict[int(DB.Helpers.chosenParamsValues[3])]
    elem["kilometraza"]=DB.Helpers.kilometrazaDict[float(DB.Helpers.chosenParamsValues[4])]
    elem["kubikaza"]=DB.Helpers.kubikazaDict[int(DB.Helpers.chosenParamsValues[5])]
    elem["snagaMotora"]=DB.Helpers.snagaMotoraDict[DB.Helpers.chosenParamsValues[6]]

    h = W0
    for i in range(0, len(W)):
        h += W[i] * float(elem[DB.Helpers.chosenParams[i]])

    print("cena automobila je > {0}".format(h))

    return h

def cenaAutomobilaJeV2(W0,W):

    elem=dict()

    elem["stanje"]=DB.Helpers.stanjeDictV2[DB.Helpers.chosenParamsValues[0]]
    elem["marka"]=DB.Helpers.markaDictV2[DB.Helpers.chosenParamsValues[1]]
    elem["model"]=DB.Helpers.modelDictV2[DB.Helpers.chosenParamsValues[2]]
    elem["godiste"]=DB.Helpers.godisteDictV2[int(DB.Helpers.chosenParamsValues[3])]
    elem["kilometraza"]=DB.Helpers.kilometrazaDictV2[float(DB.Helpers.chosenParamsValues[4])]
    elem["kubikaza"]=DB.Helpers.kubikazaDictV2[int(DB.Helpers.chosenParamsValues[5])]
    elem["snagaMotora"]=DB.Helpers.snagaMotoraDictV2[DB.Helpers.chosenParamsValues[6]]

    h = W0
    for i in range(0, len(W)):
        h += W[i] * float(elem[DB.Helpers.chosenParams[i]])

    print("cena automobila je > {0}".format(h))

    return h