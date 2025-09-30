import Data
import numpy as np

produit=Data.data

nom=produit[:,0]
qte=produit[:,1].astype(float)
prix=produit[:,2].astype(float)


def total_stock(qte,prix):
    sum = np.sum(qte*prix)
    print(sum)

def moyen_prix(prix):
    moy=np.mean(prix)
    print(moy)

def min_max_prix(prix):
    max=np.max(prix)
    min=np.min(prix)
    print(f'le prix max :',str(max),'dhs et le prix min :', str(min), 'dhs')
    
def produit_cher(prix):
        idx_max = np.argmax(prix)
        idx_min = np.argmin(prix)

        print(f"Produit le plus cher : {nom[idx_max]} ({prix[idx_max]} dhs)")
        print(f"Produit le moins cher : {nom[idx_min]} ({prix[idx_min]} dhs)")




#total_stock(qte,prix)
#moyen_prix(prix)
#min_max_prix(prix)
#produit_cher(prix)