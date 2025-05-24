# Projet : Prédiction de notes de films à partir de commentaires AlloCiné

 Construire un modèle de machine learning capable de prédire automatiquement la note (de 1 à 5) attribuée à un film à partir du commentaire d’un spectateur.

 ---

Étapes du projet:

1. [Collecte de données](src/scrap.py)

    La première étape a consisté à automatiser la récupération des avis spectateurs du film *Sinners* depuis la page dédiée sur le site AlloCiné. Pour chaque avis, deux éléments ont été extraits : la note attribuée par l’utilisateur, lorsqu’elle est présente, et le commentaire textuel associé. Le script a parcouru automatiquement les différentes pages du site en suivant la pagination, jusqu’à atteindre un maximum de 2000 avis. Des pauses aléatoires ont été insérées entre chaque requête afin de simuler un comportement humain et d’éviter le blocage par le site.

2. [Analyse du corpus](src/analyse_corpus.ipynb)

    Une analyse linguistique a été réalisée avec spaCy. Cette étape avait pour but d’identifier les adjectifs et noms les plus utilisés dans les commentaires. Ces informations sont précieuses pour comprendre le vocabulaire dominant du corpus, et surtout pour sélectionner les mots à remplacer lors de l’augmentation de données.

3. [Augmentation de données](src/augmentation_commentaire.py)

   L’augmentation de données a été réalisée en remplaçant certains mots fréquents (adjectifs, noms) par des synonymes choisis manuellement. Cette opération a été réalisée via un dictionnaire, intégrant plusieurs synonymes pour chaque mot cible. Chaque commentaire original a ainsi été dupliqué plusieurs fois avec des variantes lexicales crédibles, produisant un ensemble enrichi.

4. [Entraînement d’un modèle de classification Sklearn](src/classifieur.py)

    Une fois les données enrichies, un modèle de classification supervisée a été entraîné. Le texte des commentaires a été vectorisé grâce à `TfidfVectorizer`, en considérant les unigrams et bigrams les plus représentatifs. Le modèle choisi est un `RandomForestClassifier`, bien adapté pour les tâches de classification multi-classes. L’entraînement a été réalisé sur 80 % des données, avec une séparation 20 % pour le test. Le modèle final a été sauvegardé (`modele_rf.pkl`) ainsi que le transformateur TF-IDF (`vectorizer.pkl`). Les jeux de test ont été exportés dans `X_test.csv` et `y_test.csv` pour être réutilisés indépendamment.

  >J’ai choisi de m’appuyer sur un modèle de type Scikit-learn, car l'utilisation des modèles préentraînés via Hugging Face provoquait des plantages sur ma machine. Ce choix a donc été motivé par des contraintes techniques indépendantes de ma volonté.

5. [Évaluation du modèle](src/evaluation_classifieur.ipynb)

   L’évaluation du modèle a été effectuée à l’aide de métriques classiques de classification telles que la précision, le rappel et la F1-score. Une matrice de confusion a été tracée pour visualiser les bonnes et mauvaises classifications par classe. Des analyses complémentaires ont permis de mesurer la gravité des erreurs (écart entre note réelle et note prédite), ainsi que la distribution des classes avec ou sans erreur.
