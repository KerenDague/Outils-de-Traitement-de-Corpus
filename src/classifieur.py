"""
Script d'entraînement d'un modèle de classification de notes de films à partir de commentaires texte (AlloCiné).

Étapes principales :
1. Chargement des données augmentées (avis_sinners_augmente.csv), contenant des commentaires et des notes utilisateurs.
2. Nettoyage des notes : suppression des valeurs non numériques et arrondi pour obtenir une variable de classification.
3. Nettoyage des commentaires avec spaCy : suppression des chiffres, ponctuation, stopwords et lemmatisation.
4. Vectorisation des commentaires via TF-IDF (avec unigrams et bigrams, max 3000 features).
5. Entraînement d’un modèle Random Forest pour prédire la note à partir du commentaire.
6. Sauvegarde du modèle (`modele_rf.pkl`) et du vectorizer (`vectorizer.pkl`).
7. Sauvegarde des jeux de données test (`X_test.csv`, `y_test.csv`) pour l'évaluation.

"""

import pandas as pd
import re
import string
import spacy
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier

# Chargement du modèle spaCy français
nlp = spacy.load("fr_core_news_sm")

# Chargement du CSV
df = pd.read_csv("avis_sinners_augmente.csv")

# Nettoyage des notes : on ne garde que les valeurs numériques
df = df[df['note'].astype(str).str.replace('.', '', 1).str.isnumeric()]
df['note'] = df['note'].astype(float)
df['note_classe'] = df['note'].round().astype(int)

# Nettoyage et traitement des commentaires avec spaCy
def nettoyer_avec_spacy(commentaire):
    commentaire = commentaire.lower()
    commentaire = re.sub(r"http\S+", "", commentaire)  # suppression des liens
    commentaire = re.sub(r"\d+", "", commentaire)      # suppression des chiffres
    commentaire = commentaire.translate(str.maketrans('', '', string.punctuation))  # ponctuation
    doc = nlp(commentaire)
    mots_utiles = [
        token.lemma_ for token in doc
        if not token.is_stop and not token.is_punct and len(token.text) > 2
    ]
    return " ".join(mots_utiles)

df['commentaire_nettoye'] = df['commentaire'].astype(str).apply(nettoyer_avec_spacy)

# Séparation train/test
X_train, X_test, y_train, y_test = train_test_split(
    df['commentaire_nettoye'], df['note_classe'], test_size=0.2, random_state=42, stratify=df['note_classe']
)

# Vectorisation TF-IDF sur unigrams et bigrams
vectorizer = TfidfVectorizer(max_features=3000, ngram_range=(1, 2))
X_train_vect = vectorizer.fit_transform(X_train)
X_test_vect = vectorizer.transform(X_test)

# Modèle Random Forest
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train_vect, y_train)

# Sauvegarde du modèle
with open("modele_rf.pkl", "wb") as f:
    pickle.dump(clf, f)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

# Sauvegarde des données test pour l'évaluation 
X_test.to_csv("X_test.csv", index=False)
y_test.to_csv("y_test.csv", index=False)

print("Modèle entraîné et sauvegardé avec spaCy. Données test prêtes.")
