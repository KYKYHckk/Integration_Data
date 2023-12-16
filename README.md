Introduction
Bienvenue dans cet exercice d'intégration de données.

Le but de ce projet, faire une intégration de données avec le fichier fournis et mettre dans une base de donnée, les données du code INSEE, code postal et nom de commune.

Ensuite rajouter des éléments pour faciliter la lecture des données (TRIGGER ET VIEW). En vous guidant à travers plusieurs étapes pour l'ajout de fonctionnalités dans une base de données. Les principales tâches comprennent la création d'un trigger, l'établissement d'une vue, l'intégration d'informations de population depuis une API, et la sécurisation de la connexion à la base de données.

Nous allons d'abord commencer par le choix des technologies pour la réalisation du projet.

Prérequis
Assurez-vous d'avoir les éléments suivants installés et configurés sur votre système :

Python: La version 3.x est recommandée. DBeaver: Un gestionnaire de base de données qui sera utilisé pour exécuter des requêtes SQL et vérifier les résultats.

Création d'un Trigger 
Un trigger est un mécanisme qui se déclenche automatiquement lorsqu'une action (comme l'insertion de données) est effectuée sur une table. Objectif: Suivre les étapes ci-dessous pour créer un trigger qui enregistre l'intégrateur lors de l'insertion de codes INSEE.

Création d'une Vue 'villes_nord_pas_de_calais'
Une vue est une représentation virtuelle des données extraites d'une ou plusieurs tables. Objectif: Créer une vue qui affiche les villes du Nord Pas de Calais (codes postaux commençant par 59 et 62).


Récupération des Informations de Population 'recuperationINSEE.py'
Dans cette étape, nous allons utiliser une API gouvernementale pour obtenir des informations de population à partir des codes INSEE.

Objectif: Utilisez le script Python recuperationINSEE.py fourni pour récupérer les informations de population depuis l'API Geo.

Instructions:
Assurez-vous d'avoir installé les bibliothèques Python nécessaires en exécutant pip install requests et pip install pymysql dans votre environnement virtuel.

Remarques:

Le script nécessite une connexion à une base de données MySQL. Assurez-vous de configurer correctement les paramètres de connexion dans le script. Intégration des Données de Population Une fois les informations de population récupérées, nous les intégrerons dans la même table que les codes postaux INSEE.

Conclusion
En suivant ces étapes, vous avez enrichi votre base de données, créé un trigger, une vue, et récupéré des informations externes.
