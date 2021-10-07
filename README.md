Excercice de développeur backend
==

# Description
Le but cet exercice est d'implémenter une API permettant de jouer au jeu du tic-tac-toe.
Le résultat est à renvoyer dans un .zip contenant le code source complété.

# Fonctionnalités attendues
Le tic-tac-toe, aussi appelé "morpion", est un jeu de réflexion se pratiquant à deux joueurs au tour par tour dont le but est de créer le premier un alignement.
Le jeu se joue généralement avec papier et crayon mais le but de cet exercice est d'implémenter une API REST permettant de jouer à ce jeu.
L'ensemble des règles est disponible sur : https://fr.wikipedia.org/wiki/Tic-tac-toe

Les API REST ont déjà été spécifiées (voir `app/api.yaml`) et doivent être implémentées dans `app/api.py` :
- Création d'une nouvelle partie : **POST** `/api/games`
- Récupération du statut d'une partie : **GET** `/api/games/{game_id}`
- Remplissage  du statut d'une celulle : **PATCH** `/api/games/{game_id}` avec un "request body" particulier


# Stack technologique
Afin de se rapprocher au mieux de notre stack technique, nous avons pré-configuré un projet avec :
- Python 3.6
- Flask : https://flask.palletsprojects.com/en/1.1.x/
- Connexion (aucune expertise nécessaire) : https://connexion.readthedocs.io/en/latest/
- SQLAlchemy : https://www.sqlalchemy.org/
