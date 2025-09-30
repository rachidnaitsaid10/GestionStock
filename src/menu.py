from stock import *
from Data import data
from stats import *
import matplotlib.pyplot as plt
from stats import nom, qte,prix
from visualize import *

produit=Data.data

nom=produit[:,0]
qte=produit[:,1].astype(float)
prix=produit[:,2].astype(float)

Products = data



def menugraphique():
    ChoixGraphique = 0
    while ChoixGraphique != 3:
        ChoixGraphique = int(input(' 1 Pour bar chart et 2 Pour pie chart 3 pour Quitter : '))
        if ChoixGraphique == 1:
                pie_chart(nom,qte,prix)
        elif ChoixGraphique == 2:
                bar_chart(nom,qte)


def menu():
    Choix = 0
    while Choix != 8:
        print('1 Pour Ajouter un produit.')
        print('2 Pour Remove un produit.')
        print('3 Pour Update Quantity un produit.')
        print('4 Pour Display  produits.')
        print('5 Pour Afficher le stock.')
        print('6 Pour Afficher les statistiques.')
        print('7 Afficher un graphique.')
        print('8 Pour Quitter')
        Choix = int(input('Choix (1-8): '))
        if Choix == 1:
            AddProduct()
        elif Choix == 2:
            RemoveProduct()
        elif Choix == 3:
            UpdateProduct() 
        elif Choix == 4:
            DisplayProducts()
        elif Choix == 5:
            total_stock(qte,prix)
        elif Choix == 6:
            moyen_prix(prix)
            min_max_prix(prix)
            produit_cher(prix)
        elif Choix == 7:
            menugraphique()
        else:
            print('Trouv un nombre entre 1 et 4 : ')
