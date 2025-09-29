from Data import data
from numpy import np

Products = data

def AddProduct():
    Nom = str(input("Entry Product Name :"))
    Qunt = int(input("Entre Quantité :"))
    Prix = float(input("Entre Prix de produit :"))

    NewData = np.append(Products, [Nom, Qunt, Prix])

    print(NewData)

AddProduct()