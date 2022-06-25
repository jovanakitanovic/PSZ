import loadDatabase as DB

def readValuesV2():
    DB.Helpers.chosenParamsValues=list()

    print("stanje >>")
    stanje = input();
    DB.Helpers.chosenParamsValues.append(stanje);
    #DB.Helpers.chosenParamsValues.append("Novo vozilo");

    print("marka >>")
    marka = input();
    DB.Helpers.chosenParamsValues.append(marka);
    #DB.Helpers.chosenParamsValues.append("Opel");

    print("model >>")
    model = input();
    DB.Helpers.chosenParamsValues.append(model);
    #DB.Helpers.chosenParamsValues.append("Astra J");

    print("godiste >>")
    godiste = input();
    DB.Helpers.chosenParamsValues.append(godiste);
    #DB.Helpers.chosenParamsValues.append("2022");

    print("kilometraza >>")
    kilometraza = input();
    DB.Helpers.chosenParamsValues.append(kilometraza);
    #DB.Helpers.chosenParamsValues.append("10.00");

    print("kubikaza >>")
    kubikaza = input();
    DB.Helpers.chosenParamsValues.append(kubikaza);
    #DB.Helpers.chosenParamsValues.append("1686");

    print("snagaMotora >>")
    snagaMotora = input();
    DB.Helpers.chosenParamsValues.append(snagaMotora);
    #DB.Helpers.chosenParamsValues.append("103/140");


def readValues():
    for car in DB.Helpers.listOfCars:
        carParams=dict();

        carParams["stanje"]=DB.Helpers.stanjeDict[car.stanje]
        carParams["marka"]=DB.Helpers.markaDict[car.marka]
        carParams["model"] = DB.Helpers.modelDict[car.model]
        carParams["godiste"] = DB.Helpers.godisteDict[car.godiste]
        carParams["kilometraza"] = DB.Helpers.kilometrazaDict[car.kilometraza]
        carParams["kubikaza"] = DB.Helpers.kubikazaDict[car.kubikaza]
        carParams["snagaMotora"] = DB.Helpers.snagaMotoraDict[car.snagaMotora]

        DB.Helpers.filteredListOfCars.append(carParams)

    for i in range (0, len(DB.Helpers.filteredListOfCars)):
        #DB.Helpers.filteredListOfCars[i]["cena"]=((DB.Helpers.listOfCars[i].cena-1000)/(299000))
        DB.Helpers.filteredListOfCars[i]["cena"]=DB.Helpers.listOfCars[i].cena

    print('{0} i {1}'.format(len(DB.Helpers.listOfCars), len(DB.Helpers.filteredListOfCars)))

def readValuesV2():
    for car in DB.Helpers.listOfCars:
        carParams=dict();

        carParams["stanje"]=DB.Helpers.stanjeDictV2[car.stanje]
        carParams["marka"]=DB.Helpers.markaDictV2[car.marka]
        carParams["model"] = DB.Helpers.modelDictV2[car.model]
        carParams["godiste"] = DB.Helpers.godisteDictV2[car.godiste]
        carParams["kilometraza"] = DB.Helpers.kilometrazaDictV2[car.kilometraza]
        carParams["kubikaza"] = DB.Helpers.kubikazaDictV2[car.kubikaza]
        carParams["snagaMotora"] = DB.Helpers.snagaMotoraDictV2[car.snagaMotora]

        DB.Helpers.filteredListOfCarsV2.append(carParams)

    for i in range (0, len(DB.Helpers.filteredListOfCarsV2)):
        #DB.Helpers.filteredListOfCars[i]["cena"]=((DB.Helpers.listOfCars[i].cena-1000)/(299000))
        DB.Helpers.filteredListOfCarsV2[i]["cena"]=DB.Helpers.listOfCars[i].cena

    #print('{0} i {1}'.format(len(DB.Helpers.listOfCars), len(DB.Helpers.filteredListOfCarsV2)))
