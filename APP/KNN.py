import loadDatabase as DB
import math

def KNN(type):
    print ("KNN")

    theCar = DB.Helpers.chosenParamsValues;
    K=0
    if(DB.Helpers.K==0):
        K = math.sqrt(len(DB.Helpers.classifiedListOfCars))
        K= K if K % 2 == 0 else K+1
    else:
        K=DB.Helpers.K

    if type == "Euklidsko" or type == "Euklidsko V2": #euklidska distanca
        for car in DB.Helpers.classifiedListOfCars:
            distance= math.sqrt((car["stanje"]-DB.Helpers.stanjeDictKNN[theCar[0]])**2+
                                (car["marka"]-DB.Helpers.markaDictKNN[theCar[1]])**2+
                                (car["model"]-DB.Helpers.modelDictKNN[theCar[2]])**2+
                                (car["godiste"]-int(theCar[3]))**2+
                                (float(car["kilometraza"])-float(theCar[4]))**2+
                                (car["kubikaza"]-int(theCar[5]))**2+
                                (car["snagaMotora"]-int(theCar[6].split("/")[0]))**2)
            car["distance"]=distance

    if type == "Manhattan" or type=="Manhattan V2":
        for car in DB.Helpers.classifiedListOfCars:
            distance= abs(car["stanje"]-DB.Helpers.stanjeDictKNN[theCar[0]])+\
                      abs(car["marka"]-DB.Helpers.markaDictKNN[theCar[1]])+\
                      abs(car["model"]-DB.Helpers.modelDictKNN[theCar[2]])+\
                      abs(car["godiste"]-int(theCar[3]))+\
                      abs(float(car["kilometraza"])-float(theCar[4]))+\
                      abs(car["kubikaza"]-int(theCar[5]))+\
                      abs(car["snagaMotora"]-int(theCar[6].split("/")[0]))
            car["distance"]=distance

    if type == "Chebyshev" or type=="Chebyshev V2":
        for car in DB.Helpers.classifiedListOfCars:
            distance= max(abs(car["stanje"]-DB.Helpers.stanjeDictKNN[theCar[0]]),
                          abs(car["marka"]-DB.Helpers.markaDictKNN[theCar[1]]),
                          abs(car["model"]-DB.Helpers.modelDictKNN[theCar[2]]),
                          abs(car["godiste"]-int(theCar[3])),
                          abs(float(car["kilometraza"])-float(theCar[4]))+abs(car["kubikaza"]-int(theCar[5])),
                          abs(car["snagaMotora"]-int(theCar[6].split("/")[0])))
            car["distance"]=distance

    if type == "Hamming - Euklidsko":
        for car in DB.Helpers.classifiedListOfCars:
            hammingMarka=hammingDistance(car["marka"],DB.Helpers.markaDictKNN[theCar[1]])
            hammingModel=hammingDistance(car["model"],DB.Helpers.modelDictKNN[theCar[2]])
            hammingStanje=hammingDistance(car["stanje"],DB.Helpers.stanjeDictKNN[theCar[0]])

            distance=math.sqrt((hammingMarka) ** 2 +
                        (hammingModel) ** 2 +
                        (hammingStanje) ** 2 +
                        (car["godiste"] - int(theCar[3])) ** 2 +
                        (float(car["kilometraza"]) - float(theCar[4])) ** 2 +
                        (car["kubikaza"] - int(theCar[5])) ** 2 +
                        (car["snagaMotora"] - int(theCar[6].split("/")[0])) ** 2)
            car["distance"]=distance

    DB.Helpers.classifiedListOfCars = sorted(DB.Helpers.classifiedListOfCars, key=lambda d: d['distance'])

    print("{0} || {1}".format(DB.Helpers.modelDictKNN[theCar[2]],DB.Helpers.markaDictKNN[theCar[1]]))
    for x in range(0,int(K)):
        print("{0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} | cena: {8} | distanca :{9} | {10}".format(DB.Helpers.classifiedListOfCars[x]['modelO'],DB.Helpers.classifiedListOfCars[x]['model'], DB.Helpers.classifiedListOfCars[x]['markaO'],
                                                    DB.Helpers.classifiedListOfCars[x]['marka'],DB.Helpers.classifiedListOfCars[x]['kilometraza'], DB.Helpers.classifiedListOfCars[x]['godiste'],
                                                                           DB.Helpers.classifiedListOfCars[x]['kubikaza'], DB.Helpers.classifiedListOfCars[x]['snagaMotora'],DB.Helpers.classifiedListOfCars[x]['cena'],DB.Helpers.classifiedListOfCars[x]['distance'],DB.Helpers.classifiedListOfCars[x]['stanje']))


    top_K_results= DB.Helpers.classifiedListOfCars[0:int(K)]

    numClass1 =sum(p['klasa'] == 1 for p in top_K_results)
    numClass2 = sum(p['klasa'] == 2 for p in top_K_results)
    numClass3 = sum(p['klasa'] == 3 for p in top_K_results)
    numClass4 = sum(p['klasa'] == 4 for p in top_K_results)
    numClass5 = sum(p['klasa'] == 5 for p in top_K_results)
    numClass6 = sum(p['klasa'] == 6 for p in top_K_results)
    numClass7 = sum(p['klasa'] == 7 for p in top_K_results)
    numClass8 = sum(p['klasa'] == 8 for p in top_K_results)
    numClass9 = sum(p['klasa'] == 9 for p in top_K_results)

    print(" {0} | {1} | {2} | {3} | {4} | {5}  | {6} | {7} | {8}".format(numClass1, numClass2,numClass3, numClass4,numClass5,numClass6,numClass7,numClass8, numClass9))

    maxClass = maxValueClass([numClass1,numClass2,numClass3,numClass4,numClass5,numClass6,numClass7,numClass8,numClass9])
    print ("najveca klasa je > {0} ".format(maxClass))

    avgPrice = sum(p['cena'] for p in top_K_results)

    print ("prosečna cena u odnosu na sve susede bi bila {0} >> ".format(avgPrice/K))

    return retunKlasa(maxClass)

def hammingDistance(str1, str2):

    distance=0

    for i in range(0,min(len(str1),len(str2))):
        if(str1[i]!=str2[i]):
            distance+=1

    distance = abs(len(str1)-len(str2))
    return distance

def maxValueClass(numClass):

    index=0;
    maxValue=0;

    for i in range(0,len(numClass)):
        if maxValue<numClass[i]:
            maxValue=numClass[i]
            index=i

    return  index+1


def classifyByKNN():
    DB.Helpers.classifiedListOfCars=list()

    for car in DB.Helpers.listOfCars:
        carDict=dict()

        carDict["stanje"]=DB.Helpers.stanjeDictKNN[car.stanje]
        carDict["marka"]=DB.Helpers.markaDictKNN[car.marka]
        carDict["model"]=DB.Helpers.modelDictKNN[car.model]
        carDict['markaO']=car.marka
        carDict['modelO']=car.model
        #carDict["godiste"]=(car.godiste-1956)/(2022-1966)
        #carDict["kilometraza"]=(car.kilometraza)/(1000)
        #carDict["kubikaza"]=(car.kubikaza-100)/(6492)
        #carDict["snagaMotora"]=(DB.Helpers.snagaMotoraDict[car.snagaMotora]-100)/(562)
        carDict["godiste"]=car.godiste
        carDict["kilometraza"]=car.kilometraza
        carDict["kubikaza"]=car.kubikaza
        carDict["snagaMotora"]=DB.Helpers.snagaMotoraDictKNN[car.snagaMotora]
        carDict["cena"]=car.cena

        if car.cena<=2000:
            carDict["klasa"]=1
        if car.cena>2000 and car.cena<=5000:
            carDict["klasa"]=2
        if car.cena>5000 and car.cena<=10000:
            carDict["klasa"]=3
        if car.cena>10000 and car.cena<=15000:
            carDict["klasa"]=4
        if car.cena>15000 and car.cena<=20000:
            carDict["klasa"]=5
        if car.cena>20000 and car.cena<=25000:
            carDict["klasa"]=6
        if car.cena>25000 and car.cena<=30000:
            carDict["klasa"]=7
        if car.cena>30000 and car.cena<=50000:
            carDict["klasa"]=8
        if car.cena>50000:
            carDict["klasa"]=9

        DB.Helpers.classifiedListOfCars.append(carDict)

def retunKlasa(klasa):

    if klasa==1:
        return "cena je ispod 2000e"
    if klasa==2:
        return "cena je u opsecu od 2000e do 5000e"
    if klasa==3:
        return "cena je u opsecu od 5000e do 10 000e"
    if klasa==4:
        return "cena je u opsecu od 10 000e do 15 000e"
    if klasa==5:
        return "cena je u opsecu od 15 000e do 20 000e"
    if klasa==6:
        return "cena je u opsecu od 20 000e do 25 000e"
    if klasa==7:
        return "cena je u opsecu od 25 000e do 30 000e"
    if klasa==8:
        return "cena je u opsecu od  30 000e do 50 000e"
    if klasa==9:
        return "cena je veća od 50 000e"