# `stock-manager/`

## Gestion de stock avec statistiques et visualisation 📈

Ce projet est une application en **Python** conçue pour la gestion simple d'un stock de produits. Elle permet d'effectuer des opérations de gestion de base, de calculer des **statistiques** clés et de visualiser les données du stock à l'aide de **graphiques**.

---

## Objectif du Projet

L'objectif principal est de développer une application qui non seulement gère un inventaire de produits mais utilise également les bibliothèques **NumPy** pour les calculs statistiques et **Matplotlib** pour la visualisation des données.

---

## Fonctionnalités

L'application propose les fonctionnalités suivantes, accessibles via un menu interactif en console:

### 1. Gestion du Stock

Le stock est représenté comme une liste (ou un tableau NumPy) de produits, où chaque produit est structuré comme **`["nom_produit", quantité, prix_unitaire]`**.

* **Ajouter** un produit (nom, quantité, prix).
* **Supprimer** un produit.
* **Mettre à jour** la quantité d'un produit existant.
* **Afficher** la liste des produits disponibles.

### 2. Statistiques sur le Stock

Des calculs statistiques sont effectués à l'aide de la librairie **NumPy**:

* **Valeur totale** du stock ($\sum (\text{prix} \times \text{quantité})$).
* **Prix moyen** des produits.
* Prix **minimum** et **maximum**.
* Identification du produit le **plus cher** et le **moins cher**.

### 3. Visualisations

L'application génère au moins deux types de graphiques en utilisant **Matplotlib**:

* **Graphique en barres (Bar Chart)**: Représentation de la quantité par produit.
* **Camembert (Pie Chart)**: Répartition de la valeur totale du stock par produit. La valeur d'un produit est calculée comme $\text{quantité} \times \text{prix unitaire}$.

---

## Structure du Projet

Le projet suit une structure modulaire et claire:
```
stock-manager/
├── src/
│   ├── main.py           # Point d'entrée et menu principal
│   ├── stock.py          # Fonctions de gestion du stock (ajout, suppression, mise à jour...)
│   ├── stats.py          # Fonctions de calculs statistiques avec numpy
│   └── visualize.py      # Fonctions de visualisation avec matplotlib
├── README.md             # Documentation du projet
├── requirements.txt      # Dépendances du projet (numpy, matplotlib)
└── .gitignore            # Fichiers et dossiers à ignorer par Git
```

---

## Installation et Lancement

### 1. Cloner le dépôt

*(Pour un environnement réel, les instructions de clonage Git iraient ici)*

### 2. Installer les dépendances

Le projet nécessite **NumPy** et **Matplotlib**. Installez-les en utilisant `pip` et le fichier `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 3. Lancer l'application

Exécutez le point d'entrée principal de l'application :

```bash
python src/main.py
```

## Organisation et Collaboration

Ce projet a été développé en binôme, en respectant une organisation professionnelle:

* **Git**: Utilisation de Git pour la contribution collaborative.
* **Jira**: Planification et suivi des tâches via l'outil Jira.

