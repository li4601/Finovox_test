# Finovox_test

Une application web Python (Flask) permettant de lister et télécharger des fichiers depuis un volume Docker monté.

---

## Installation & Lancement

### Commande unique pour construire et exécuter l’application :

```bash
sudo docker build -t file-downloader . && sudo docker run -p 5000:5000 -v $(pwd)/files:/app/files file-downloader
```

* Construit l’image Docker nommée `file-downloader`.
* Lance le conteneur sur le port 5000.
* Monte le dossier local `files/` dans le conteneur Docker.

---

## Interface Web

Ouvrir l’URL suivante dans votre navigateur :

```
http://localhost:5000/
```

Vous verrez la liste des fichiers disponibles dans le volume Docker avec un bouton pour chaque téléchargement.

---

## API Endpoints

| Méthode | URL                          | Description                                             |
| ------- | ---------------------------- | ------------------------------------------------------- |
| GET     | `/`                          | Page HTML listant les fichiers à télécharger            |
| GET     | `/api/files`                 | Renvoie la liste des fichiers disponibles (format JSON) |
| GET     | `/download/<nom_du_fichier>` | Permet de télécharger un fichier spécifique             |

---

## Exemples d’appels API

### Lister les fichiers disponibles :

```bash
curl http://localhost:5000/api/files
```

**Exemple de réponse :**

```json
["Finovox - test technique DataEngineer_DevOps.pdf","testfile.txt","img.jpg"]
```

---

### Télécharger un fichier :

```bash
curl -O http://localhost:5000/download/img.jpg
```

---

## Exécuter les tests automatiques

### 1. Installer les dépendances nécessaires :

```bash
pip install -r requirements.txt
```

### 2. Lancer les tests avec Pytest :

```bash
pytest tests/
```

### Résultat attendu :

```
================== test session starts ==================


tests/test_app.py ...                                 [100%]

=================== 3 passed in X.XXs ==================
```

---

## Volume Docker utilisé

Le dossier local `files/` est monté dans le conteneur Docker :

```bash
-v $(pwd)/files:/app/files
```

Tous les fichiers placés dans ce dossier seront accessibles depuis l’application web.

---

## Versions utilisées

* **Python** : 3.11
* **Flask** : 3.0.3
* **Docker** : 28.2.2

---

## ℹ️ Remarques

* Assurez-vous que le dossier `files/` existe à la racine du projet avant de lancer l’application.

