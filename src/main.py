from stock import *
from Data import data


Products = data

def menu():

    Choix = 0
    while Choix != 5:
        print('1 Pour Ajouter un produit.')
        print('2 Pour Remove un produit.')
        print('3 Pour Update Quantity un produit.')
        print('4 Pour Display  produits.')
        print('5 Quitter')
        Choix = int(input('Choix (1-4): '))
        if Choix == 1:
            AddProduct()
        elif Choix == 2:
            RemoveProduct()
        elif Choix == 3:
            UpdateProduct()
        elif Choix == 4:
            DisplayProducts()
        else:
            print('Trouv un nombre entre 1 et 4')

menu()
