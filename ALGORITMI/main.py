import Helpers
import forma as F
import random
import loadDatabase as DB
import KNN
import LinearnaRegresija as LR

if __name__ == '__main__':
    print('hi')


    DB.readDatabaseToList();
    DB.encodeParamVales()
    DB.encodeParamValesV2()
    DB.encodeParamValuesKNN()
    KNN.classifyByKNN()

    Helpers.readValues()
    Helpers.readValuesV2()

    for i in range(0, len(DB.Helpers.filteredListOfCars[0]) - 1):
        DB.Helpers._W.append(DB.Helpers._W0)
        DB.Helpers._WV2.append(DB.Helpers._W0V2)

    random.shuffle(DB.Helpers.filteredListOfCars)
    random.shuffle(DB.Helpers.filteredListOfCarsV2)

    index = int((len(DB.Helpers.filteredListOfCars)/100)*70)
    trainCars = DB.Helpers.filteredListOfCars[0:index]
    testCars = DB.Helpers.filteredListOfCars[index:len(DB.Helpers.filteredListOfCars)]

    trainCarsV2 = DB.Helpers.filteredListOfCarsV2[0:index]
    testCarsV2 = DB.Helpers.filteredListOfCarsV2[index:len(DB.Helpers.filteredListOfCarsV2)]

    DB.Helpers.W0, DB.Helpers.W, J = LR.linearnaRegresija(DB.Helpers._W0,DB.Helpers._W,trainCars)
    DB.Helpers.W0V2, DB.Helpers.WV2, J2 = LR.linearnaRegresija(DB.Helpers._W0V2,DB.Helpers._WV2,trainCarsV2)


    LR.proveraLinearneRegresije(DB.Helpers._W0,DB.Helpers._W,trainCars)
    LR.proveraLinearneRegresije(DB.Helpers._W0,DB.Helpers._W,testCars)

    LR.proveraLinearneRegresije(DB.Helpers._W0V2,DB.Helpers._WV2,trainCarsV2)
    LR.proveraLinearneRegresije(DB.Helpers._W0V2,DB.Helpers._WV2,testCarsV2)

    F.createFormWindow()

