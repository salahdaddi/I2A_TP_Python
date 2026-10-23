# Student Data Simulation Project

## Bibliothèques utilisées
- **NumPy** : génération aléatoire des dates et des notes, moyenne, médiane, écart-type, minimum et maximum.
- **pandas** : affichage des données sous forme de tableaux et calcul de la moyenne d'âge.

## Fichiers
- `main.ipynb` : exécute la simulation, affiche les données et les statistiques, puis écrit le rapport.
- `students.py` : génère les identifiants, dates de naissance, trois notes et moyennes.
- `analysis.py` : calcule les âges et les statistiques et prépare le rapport.
- `results/report.txt` : rapport texte généré automatiquement.

## Exécution
Dans un terminal ouvert dans ce dossier, installez les dépendances :

```bash
pip install numpy pandas notebook
```

Puis lancez Jupyter :

```bash
jupyter notebook
```

Ouvrez `main.ipynb` et choisissez **Run All**. Le dossier `results` est créé automatiquement s'il n'existe pas.

Le notebook utilise une graine aléatoire fixe (`42`) afin de rendre les résultats reproductibles. Les âges sont calculés à la date d'exécution. L'écart-type est l'écart-type de population (`ddof=0`) des moyennes des étudiants.
