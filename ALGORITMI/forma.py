from tkinter import *
import loadDatabase as DB
from tkinter import ttk
import LinearnaRegresija as LR
import KNN as KNN


def createFormWindow():

    def clean(e):
        stanjeVozila.set("")
        marka.set("")
        model.set("")
        godiste.delete(0,END)
        kilometraza.delete(0,END)
        kubikaza.set("")
        snagaMotora.set("")
        KFaktor.delete(0,END)
        rastojanje.set("")

    def stanjeVozilaOdabir(e):
        print(stanjeVozila.get())

    def markaOdabrano(e):
        print(marka.get())

        odabrano=marka.get()

        values = DB.Models(odabrano)
        labels = list()
        for val in values:
            labels.append(val[0])

        model.config(value=labels)

    def modelOdabrano(e):
        print(model.get())

    def snagaMotoraOdabrano(e):
        print(snagaMotora.get())

    def kubikazaOdabrano(e):
        print(kubikaza.get())

    def LinRegV1(e):
        raditiLinearnuRegresiju(1)

    def LinRegV2(e):
        raditiLinearnuRegresiju(2)

    def raditiLinearnuRegresiju(type):
        DB.Helpers.chosenParamsValues=list()
        if(stanjeVozila.get()!="" and marka.get() != "" and model.get() !="" and snagaMotora!= "" and kubikaza != ""):
            DB.Helpers.chosenParamsValues.append(stanjeVozila.get());
            DB.Helpers.chosenParamsValues.append(marka.get());
            DB.Helpers.chosenParamsValues.append(model.get());
            if(godiste.get() != ""):
                DB.Helpers.chosenParamsValues.append(godiste.get());
            else:
                return
            if kilometraza.get() != "" :
                DB.Helpers.chosenParamsValues.append(kilometraza.get());
            else:
                return
            DB.Helpers.chosenParamsValues.append(kubikaza.get());
            DB.Helpers.chosenParamsValues.append(snagaMotora.get().split()[0]);
        else:
            return

        if type==1:
            h=LR.cenaAutomobilaJe(DB.Helpers._W0,DB.Helpers._W)
        else:
            h=LR.cenaAutomobilaJeV2(DB.Helpers._W0V2,DB.Helpers._WV2)

        procenjenaCena.config(text="procenjena cena automobila je {0}".format(h))

    def raditiKNN(e):
        DB.Helpers.chosenParamsValues=list()
        if(stanjeVozila.get()!="" and marka.get() != "" and model.get() !="" and snagaMotora!= "" and kubikaza != ""):
            DB.Helpers.chosenParamsValues.append(stanjeVozila.get());
            DB.Helpers.chosenParamsValues.append(marka.get());
            DB.Helpers.chosenParamsValues.append(model.get());
            if(godiste.get() != ""):
                DB.Helpers.chosenParamsValues.append(godiste.get());
            else:
                return
            if kilometraza.get() != "" :
                DB.Helpers.chosenParamsValues.append(kilometraza.get());
            else:
                return
            DB.Helpers.chosenParamsValues.append(kubikaza.get());
            DB.Helpers.chosenParamsValues.append(snagaMotora.get().split()[0]);
        else:
            return

        if(KFaktor.get()==""):
            DB.Helpers.K=0
        else:
            DB.Helpers.K=int(KFaktor.get())

        klasa = KNN.KNN(rastojanje.get())
        procenjenaCena.config(text=klasa)

    root = Tk()
    root.title("prodaja automobila")
    root.geometry("550x700")

    stanjeVozilaLabel = ttk.Label(root, text="Stanje vozila")
    stanjeVozilaLabel.grid(row=1,column=0,pady=20,padx=50)
    stanjeVozila= ttk.Combobox(root, value=["Polovno vozilo", "Novo vozilo"])
    stanjeVozila.grid(row=1, column=1)
    stanjeVozila.bind("<<ComboboxSelected>>", stanjeVozilaOdabir)

    values=DB.MarkaAutomobila()
    labels=list()
    for val in values:
        labels.append(val[0])

    markaLabel = ttk.Label(root, text="Marka vozila")
    markaLabel.grid(row=2,column=0,pady=20,padx=50)
    marka= ttk.Combobox(root, value=labels)
    marka.grid(row=2, column=1)
    marka.bind("<<ComboboxSelected>>", markaOdabrano)

    modelLabel = ttk.Label(root, text="Model vozila")
    modelLabel.grid(row=3,column=0,pady=20,padx=50)
    model= ttk.Combobox(root, value=[""])
    model.grid(row=3, column=1)
    model.bind("<<ComboboxSelected>>", modelOdabrano)

    modelLabel = ttk.Label(root, text="Model vozila")
    modelLabel.grid(row=3,column=0,pady=20,padx=50)
    model= ttk.Combobox(root, value=[""])
    model.grid(row=3, column=1)
    model.bind("<<ComboboxSelected>>", modelOdabrano)

    godisteLabel = ttk.Label(root, text="Godiste vozila")
    godisteLabel.grid(row=4,column=0,pady=20,padx=50)
    godiste= Entry()
    godiste.grid(row=4, column=1)


    kilometrazaLabel = ttk.Label(root, text="Kilometraza vozila (u hiljadama)")
    kilometrazaLabel.grid(row=5,column=0,pady=20,padx=50)
    kilometraza= Entry()
    kilometraza.grid(row=5, column=1)

    values=DB.kubikaza()
    labels=list()
    for val in values:
        labels.append(val[0])

    kubikazaLabel = ttk.Label(root, text="Kubikaza")
    kubikazaLabel.grid(row=6,column=0,pady=20,padx=50)
    kubikaza= ttk.Combobox(root, value=labels)
    kubikaza.grid(row=6, column=1)
    kubikaza.bind("<<ComboboxSelected>>", kubikazaOdabrano)

    values=DB.snagaMotora()
    labels=list()
    for val in values:
        labels.append(val[0])

    snagaMotoraLabel = ttk.Label(root, text="Snaga Motora")
    snagaMotoraLabel.grid(row=7,column=0,pady=20,padx=50)
    snagaMotora= ttk.Combobox(root, value=labels)
    snagaMotora.grid(row=7, column=1)
    snagaMotora.bind("<<ComboboxSelected>>", snagaMotoraOdabrano)

    rastojanjeLabel = ttk.Label(root, text="funkcija rastojanja (KNN)")
    rastojanjeLabel.grid(row=8,column=0,pady=10,padx=100)
    rastojanje= ttk.Combobox(root, value=["Euklidsko", "Manhattan","Hamming"])
    rastojanje.grid(row=9,column=0,pady=5,padx=100)

    KFaktorLabel = ttk.Label(root, text="vrednost K faktora (KNN)")
    KFaktorLabel.grid(row=10, column=0, pady=10, padx=50)
    KFaktor= ttk.Entry()
    KFaktor.grid(row=11, column=0, pady=5, padx=50)

    linearnaRegresija = Button(text="Linearna regresija")
    linearnaRegresija.grid(row=9,column=1)
    linearnaRegresija.bind("<Button-1>", LinRegV1)

    linearnaRegresija = Button(text="Linearna regresija V2")
    linearnaRegresija.grid(row=10,column=1)
    linearnaRegresija.bind("<Button-1>", LinRegV2)

    obrisi = Button(text="Obrisi")
    obrisi.grid(row=11,column=1)
    obrisi.bind("<Button-1>", clean)

    KNNButton = Button(text="KNN")
    KNNButton.grid(row=12, column=0, pady=5, padx=50)
    KNNButton.bind("<Button-1>", raditiKNN)

    procenjenaCena=ttk.Label(root)
    procenjenaCena.grid(row=13,column=0,pady=20,padx=50)

    root.mainloop()