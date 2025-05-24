"""
Script de scraping des avis spectateurs AlloCiné pour le film "Sinners".

Ce script récupère jusqu'à 2000 avis spectateurs sur la page AlloCiné du film "Sinners".
Il extrait pour chaque avis :
    - La note donnée par l'utilisateur (si présente)
    - Le commentaire associé

Le script :
    - Suit automatiquement la pagination via l'URL ?page=
    - S'arrête soit lorsqu'il atteint le nombre maximal d'avis demandé (2000), soit lorsqu'il n'y a plus de page
    - Enregistre le tout dans un fichier CSV local

Librairies utilisées :
    - requests : pour envoyer des requêtes HTTP au site AlloCiné
    - BeautifulSoup : pour parser et naviguer dans le HTML de la page
    - pandas : pour structurer les données et les exporter proprement
    - time et random : pour ajouter un délai aléatoire entre les pages (évite blocage ou bannissement)

Note : Ce script est à usage éducatif uniquement. Le scraping d'AlloCiné est soumis à leurs Conditions Générales d'Utilisation.
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

def scrap_avis_allocine_limite(base_url, max_avis=2000):
    all_reviews = []  # Liste qui stocke tous les avis extraits
    page = 1  # Compteur de pages à visiter

    # Définir un User-Agent pour que le site pense que c'est un vrai navigateur (anti blocage)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/122.0.0.0 Safari/537.36'
    }

    while True:
        # Construit l'URL complète de la page
        url = f"{base_url}?page={page}"
        print(f"Scraping de la page {page} : {url}")

        # Envoie la requête GET avec les bons headers
        response = requests.get(url, headers=headers)

        # Si le site retourne une erreur (exemple: 404), on arrête
        if response.status_code != 200:
            print(f"Erreur HTTP {response.status_code} à la page {page}. Le script s'arrête.")
            break

        # Analyse du HTML de la page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Trouve tous les avis sur la page actuelle. Chaque avis est dans une <div> bien identifié
        avis_divs = soup.find_all('div', class_='hred review-card cf')

        # Si aucun avis trouvé sur cette page
        if not avis_divs:
            print("Aucun avis trouvé sur cette page. Fin du scraping.")
            break

        # Parcours de chaque avis trouvé
        for avis in avis_divs:
            # Recherche de la note (note sous forme de texte, exemple: '4,0')
            note_tag = avis.find('span', class_='stareval-note')
            note = note_tag.text.strip().replace(',', '.') if note_tag else 'Non noté'

            # Recherche du commentaire (souvent dans un bloc <div> à part)
            commentaire_tag = avis.find('div', class_='content-txt review-card-content')
            commentaire = commentaire_tag.text.strip() if commentaire_tag else 'Pas de commentaire'

            # On ajoute l'avis à notre liste globale
            all_reviews.append({'note': note, 'commentaire': commentaire})

            # Si on a atteint notre limite max_avis, on arrête immédiatement
            if len(all_reviews) >= max_avis:
                print(f"{max_avis} avis atteints. Fin du scraping.")
                return all_reviews

        # Affiche un message de progression après chaque page, pour vérifier que tout se passe bien 
        print(f"Page {page} terminée : {len(avis_divs)} avis extraits sur cette page.")
        print(f"Total cumulé : {len(all_reviews)} avis.")

        # Passe à la page suivante
        page += 1

        # Ajoute une pause entre 2 et 5 secondes pour respecter le site
        time.sleep(random.uniform(2, 5))

    # Retourne la liste complète des avis extraits
    return all_reviews

# URL AlloCiné de la page de critiques spectateurs du film Sinners
film_reviews_url = "https://www.allocine.fr/film/fichefilm-326355/critiques/spectateurs/"

# Lance le scraping avec une limite de 2000 avis
avis = scrap_avis_allocine_limite(film_reviews_url, max_avis=2000)

# Transforme la liste d'avis en DataFrame pandas (tableau structuré)
df = pd.DataFrame(avis)

# Sauvegarde le résultat dans un fichier CSV encodé en UTF-8 (lisible partout)
df.to_csv("avis_sinners_2000.csv", index=False, encoding='utf-8')

# Message de fin
print(f"Scraping terminé. {len(df)} avis enregistrés dans le fichier 'avis_sinners.csv'.")
