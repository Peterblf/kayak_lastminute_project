# Kayak Last-Minute - Projet étudiant (pandas + matplotlib)

Ce projet reprend la logique pédagogique des notebooks fournis et utilise **pandas** pour la gestion des données et **matplotlib** pour la visualisation.

## Contenu du dépôt
- `main.py` : script principal pour exécuter un exemple complet
- `modules/data.py` : création et lecture des données (DataFrame)
- `modules/processing.py` : fonctions pour filtrer et résumer les données
- `modules/viz.py` : fonctions pour tracer des graphiques simples
- `tests/test_basic.py` : tests unitaires avec `unittest`
- `figs/` : dossier pour les figures générées

## Installation
1. Créer un environnement virtuel (optionnel) :
   ```bash
   python -m venv venv
   source venv/bin/activate  # mac/linux
   venv\\Scripts\\activate  # windows
   ```
2. Installer les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

## Usage
- Lancer le script principal :
  ```bash
  python main.py
  ```
- Lancer les tests :
  ```bash
  python -m unittest discover -v
  ```

## Notes pour débutant
- Le projet utilise pandas : DataFrame = table en mémoire.
- Les fonctions dans `modules/` sont commentées simplement en français.
- Le graphique est sauvegardé dans `figs/price_by_destination.png`.
