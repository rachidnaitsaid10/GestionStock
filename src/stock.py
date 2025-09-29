import numpy as np
from Data import data

Products = data
print(Products)

def AddProduct():
    Nom = str(input("Entry Product Name :"))
    Qunt = int(input("Entre Quantité :"))
    Prix = float(input("Entre Prix de produit :"))
    element = np.array([[Nom,Qunt,Prix]])

    NewData = np.append(Products, element, axis=0)
    print(np.array(NewData))



def RemoveProduct():
    NomProduct = str(input("Entry Product Name :"))
    index = np.where(Products == NomProduct)

    if len(index[0]) == 0:
        print("Product Not Found")
    else:
        NewData = np.delete(Products, index[0], axis=0)
        print(NewData)

# RemoveProduct()

def UpdateProduct():
    NomProduct = str(input("Entry Product Name :"))
    index = np.where(Products == NomProduct)
    if len(index[0]) == 0:
        print("Product Not Found")
    else:
        Qunt = int(input("Entre Quantit :"))
        Products[index[0], 1] = Qunt
    print(Products)

# UpdateProduct()

def DisplayProducts():
    for product in range(len(Products)):
        Element = Products[product]
        print(f"Nom : {Element[0]} | Qunt : {Element[1]} | Prix : {Element[2]} ")
        print("-"*50)

DisplayProducts()
