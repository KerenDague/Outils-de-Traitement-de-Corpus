"""
Script d'augmentation de données textuelles à partir de commentaires AlloCiné. J'ai choisi d'augmenter mes données en remplacant certains mots par des synonymes. 
Grace au script précedent "analyse_corpus.py" je connais les noms et les adjectifs les plus utilisés dans mon corpus  donc j'ai trouvé leurs synonymes.

Ce script :
1. Remplace certains adjectifs (au hasard) par leurs synonymes dans une copie des commentaires
2. Génère un nouveau dataset "augmenté"
3. Fusionne ce dataset avec le dataset original

Ce processus permet de doubler le corpus initial en introduisant de la diversité lexicale
tout en conservant le sens général et les notes.

"""

import pandas as pd
import random
import spacy
from collections import Counter

# Chargement du modèle linguistique spaCy pour le français
nlp = spacy.load("fr_core_news_sm")

# Chargement des données d'origine (à adapter selon ton nom de fichier)
df = pd.read_csv("avis_sinners.csv")

# Dictionnaire de synonymes adaptés aux adjectifs fréquents dans le corpus
synonymes = {
    "bon": ["excellent", "agréable", "positif"],
    "incroyable": ["fabuleux", "impressionnant", "hallucinant"],
    "magnifique": ["splendide", "superbe", "merveilleux"],
    "intense": ["puissant", "fort", "profond"],
    "exceptionnel": ["remarquable","hors-norme", "extraordinaire"],
    "long": ["étendu", "prolongé"],
    "excellent": ["remarquable", "brillant"],
    "premier": ["initial", "précurseur"],
    "autre": ["différent", "alternatif"],
    "original": ["novateur","créatif"],
    "intéressant": ["captivant", "stimulant"],
    "musique": ["chanson"],
    "histoire": ["scénario", "intrigue"],
    "acteur": ["interprète", "artiste"],
    "émotion": ["ressenti","sentiment"],
}

# Fonction de remplacement d’adjectifs par leurs synonymes
def remplacer_termes(commentaire, taux=0.5):
    doc = nlp(str(commentaire))
    nouveaux_mots = []
    for token in doc:
        # Remplacement si le lemme est connu, c'est un adjectif, et selon une proba
        if token.lemma_ in synonymes and token.pos_ == "ADJ" and random.random() < taux:
            nouveau = random.choice(synonymes[token.lemma_])
            nouveaux_mots.append(nouveau)
        else:
            nouveaux_mots.append(token.text)
    return " ".join(nouveaux_mots)

# Génération du dataset augmenté
df_augmente = df.copy()
df_augmente["commentaire"] = df_augmente["commentaire"].astype(str).apply(remplacer_termes)

# Fusion avec le dataset original
df_synthetique = pd.concat([df, df_augmente], ignore_index=True)

# Affichage de confirmation
print(f" Dataset original : {len(df)} commentaires")
print(f" Dataset augmenté : {len(df_augmente)} commentaires")
print(f" Total après fusion : {len(df_synthetique)} commentaires")

# Sauvegarde optionnelle
df_synthetique.to_csv("avis_sinners_augmente.csv", index=False)
print("Données augmentées sauvegardées dans 'avis_sinners_augmente.csv'.")
