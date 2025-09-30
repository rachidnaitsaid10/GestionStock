import matplotlib.pyplot as plt
from stats import nom, qte ,prix

def bar_chart(nom,qte):
    plt.bar(nom,qte , tick_label=nom , width=0.6)
    plt.xlabel('nom des produit')
    plt.ylabel('quantite')
    plt.title('bar graph')
    plt.show()

def pie_chart(nom,qte,prix):
    vp=qte*prix
    plt.pie(vp,labels=nom)
    plt.legend()
    plt.show()





#bar_chart(nom,qte)
#pie_chart(nom,qte,prix)



