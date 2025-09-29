# `stock-manager/`

## Gestion de stock avec statistiques et visualisation 📈

Ce projet est une application en **Python** conçue pour la gestion simple d'un stock de produits. [cite_start]Elle permet d'effectuer des opérations de gestion de base, de calculer des **statistiques** clés et de visualiser les données du stock à l'aide de **graphiques**[cite: 1, 4].

---

## Objectif du Projet

[cite_start]L'objectif principal est de développer une application qui non seulement gère un inventaire de produits mais utilise également les bibliothèques **NumPy** pour les calculs statistiques [cite: 21] [cite_start]et **Matplotlib** pour la visualisation des données[cite: 26].

---

## Fonctionnalités

[cite_start]L'application propose les fonctionnalités suivantes, accessibles via un menu interactif en console[cite: 32, 33]:

### 1. Gestion du Stock

[cite_start]Le stock est représenté comme une liste (ou un tableau NumPy) de produits [cite: 13][cite_start], où chaque produit est structuré comme **`["nom_produit", quantité, prix_unitaire]`**[cite: 14].

* [cite_start]**Ajouter** un produit (nom, quantité, prix)[cite: 16, 34].
* [cite_start]**Supprimer** un produit[cite: 17, 35].
* [cite_start]**Mettre à jour** la quantité d'un produit existant[cite: 18, 36].
* [cite_start]**Afficher** la liste des produits disponibles[cite: 19, 37].

### 2. Statistiques sur le Stock

[cite_start]Des calculs statistiques sont effectués à l'aide de la librairie **NumPy**[cite: 21]:

* [cite_start]**Valeur totale** du stock ($\sum (\text{prix} \times \text{quantité})$)[cite: 22].
* [cite_start]**Prix moyen** des produits[cite: 23].
* [cite_start]Prix **minimum** et **maximum**[cite: 24].
* [cite_start]Identification du produit le **plus cher** et le **moins cher**[cite: 25].

### 3. Visualisations

[cite_start]L'application génère au moins deux types de graphiques en utilisant **Matplotlib**[cite: 26, 27]:

* [cite_start]**Graphique en barres (Bar Chart)**: Représentation de la quantité par produit[cite: 28].
* [cite_start]**Camembert (Pie Chart)**: Répartition de la valeur totale du stock par produit[cite: 29]. [cite_start]La valeur d'un produit est calculée comme $\text{quantité} \times \text{prix unitaire}$[cite: 30, 31].

---

## Structure du Projet

[cite_start]Le projet suit une structure modulaire et claire[cite: 8]:
stock-manager/
├── src/
│   ├── main.py           # Point d'entrée et menu principal 


│   ├── stock.py          # Fonctions de gestion du stock (ajout, suppression, mise à jour...) 

│   ├── stats.py          # Fonctions de calculs statistiques avec numpy 

│   └── visualize.py      # Fonctions de visualisation avec matplotlib 

├── README.md             # Documentation du projet 

├── requirements.txt      # Dépendances du projet (numpy, matplotlib) 

└── .gitignore            # Fichiers et dossiers à ignorer par Git 

---

## Installation et Lancement

### 1. Cloner le dépôt

*(Pour un environnement réel, les instructions de clonage Git iraient ici)*

### 2. Installer les dépendances

Le projet nécessite **NumPy** et **Matplotlib**. Installez-les en utilisant `pip` et le fichier `requirements.txt`:

```bash
pip install -r requirements.txt
3. Lancer l'application
Exécutez le point d'entrée principal de l'application :

Bash

python src/main.py
Organisation et Collaboration
Ce projet a été développé en binôme, en respectant une organisation professionnelle:


Git: Utilisation de Git pour la contribution collaborative.


Jira: Planification et suivi des tâches via l'outil Jira.