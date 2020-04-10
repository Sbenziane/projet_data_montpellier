# projet_data_montpellier => Nginx, OpenMapTiles et Flask

Docker exécutant Nginx, OpenMapTiles et Flask (Python).

## Aperçu

1. [Installer les prérequis](#installer-prerequis)

    Avant d'installer le projet, assurez-vous que les conditions préalables suivantes ont été remplies.	

2. [Cloner le projet](#cloner-le-projet)

    Vous devez télécharger le code depuis son dépôt sur GitHub.

4. [Exécuter l'application](#executer-application)

    À ce stade, vous aurez tous les éléments du projet en place.


___

## Installer les prérequis

Toutes les conditions requises doivent être disponibles pour votre distribution. Les plus importants sont :

* [Git](https://git-scm.com/downloads)
* [Docker](https://docs.docker.com/engine/installation/)
* [Docker Compose](https://docs.docker.com/compose/install/)

Vérifiez si `docker-compose` est déjà installé en entrant la commande suivante : 

```sh
which docker-compose
```

Vérifier la comptatibilité de Docker Compose :

 - [La référence de la version 3 du fichier Compose](https://docs.docker.com/compose/compose-file/)

---

### Images à utiliser

* [Nginx](https://hub.docker.com/_/nginx/)
* [Openmaptiles-server](https://hub.docker.com/r/klokantech/openmaptiles-server/)
* [Python](https://hub.docker.com/_/python)

Vous devez faire attention lors de l'installation de serveurs Web tiers tels que MySQL ou Nginx

Ce projet utilise les ports suivants :

| Server              | Port |
| ------------------- | ---- |
| Openmaptiles-server | 8081 |
| Python              | 5000 |
| Nginx               | 8080 |

---

## Cloner le projet

Pour installer [Git](https://git-scm.com/book/fr/v2/Démarrage-rapide-Installation-de-Git), téléchargez-le et installez-le en suivant les instructions : 

```sh
git clone https://github.com/Sbenziane/projet_data_montpellier.git
```

Allez dans le répertoire du projet : 

```sh
cd ./projet_data_montpellier/
```

### Arbre du projet 

```sh
.
├── README.md
├── maps
│	├── 2017-07-03_france_montpellier.mbtiles
│   └── config.json
│	├── styles
│       └── style.json
│       └── style_1.json
│       └── style_2.json
├── docker-compose.yml
├── app
│	├── style.css
│	├── index.html
│	├── kepler.html
│   └── Dockerfile
└── api
	├── app.py
	├── requirements.txt
	└── Dockerfile

```

---

## Exécuter l'application

2. Démarrez l'environnement :

    ```sh
    docker-compose up -d
    ```

    **Veuillez patienter, cela peut prendre plusieurs minutes...**

    ```sh
    docker-compose logs -f # Suit la sortie du journal
    ```

3. Ouvrez le dans votre navigateur :

    * [http://localhost:8080](http://localhost:8080/) si vous disposez de windows 10 pro
	
4. Arrêter et effacer les services

    ```sh
    docker-compose down -v
    ```

