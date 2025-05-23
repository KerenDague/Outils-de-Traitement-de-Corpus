# Outils-de-Traitement-de-Corpus

## Mon Projet

- 1) Dans quel besoin vous inscrivez vous ?

Je m'intéresse à l’analyse automatique des avis en ligne, en particulier dans le domaine culturel comme le cinéma, où les retours des spectateurs sont nombreux mais souvent inexploités. Les plateformes comme AlloCiné concentrent un grand volume de commentaires exprimant l’opinion des spectateurs, mais exploiter ces données de maniere systématique nécessite des outils de traitement automatique du langage naturel. Mon objectif est de développer un modèle capable de comprendre un commentaire rédigé en français et d’en prédire la note correspondante. Une telle approche peut notamment srvir à alimenter des systèmes de recommandation, à générer des synthèses d’opinions ou à identifier des anomalies dans les retours utilisateurs.

- 2) Quel sujet allez vous traiter ?

Je vais traiter le sujet de la prédiction automatique de la note d’un film à partir d’un commentaire. Il s’agit d’un problème orienté vers l’analyse d’opinion où l’objectif est de comprendre la tonalité implicite d’un commentaire pour en déduire une note numérique, arrondie entre 1 et 5. Le projet se concentre sur un corpus extrait autour du film *Sinners*, disponible sur la plateforme AlloCiné.

- 3) Quel type de tâche allez vous réaliser ?

Je vais réaliser une tâche de classification supervisée multiclasse, dans laquelle chaque exemple d'entraînement est constitué d’un texte de commentaire et de la note que l’utilisateur a donnée. Le modèle apprend à associer certaines structures linguistiques, certains termes et tournures à une note spécifique. Pour cela, j’utilise à la fois des techniques classiques (vectorisation TF-IDF + modèle de type Random Forest) et un modèle préentraîné comme CamemBERT, que je fine-tune sur mon corpus.

- 4) Quel type de données allez vous exploiter ?

J’exploite un jeu de données composé de commentaires textuels issus du site AlloCiné, accompagnés de leur note attribuée par les utilisateurs. Chaque entrée contient un texte rédigé en français exprimant une opinion personnelle sur le film *Sinners* , et une note numerique allant de 0.5 à 5 étoiles, que j’ai arrondie pour la transformer en classes discrètes. Le corpus a également été enrichi via de l’augmentation de données (remplacement de mots par des synonymes, notamment sur les adjectifs et noms fréquents).

- 5) Où allez vous récupérer vos données ?

J’ai récupéré les données directement sur le site AlloCiné, en ciblant la page des critiques spectateurs du film Sinners. Pour cela, j’ai développé un script de web scraping, qui inclut des pauses entre les requêtes pour ne pas surcharger les serveurs. Le script collecte le texte du commentaire ainsi que la note attribuée par l'utilisateur.

- 6) Sont-elles libres d'accès ?

Les données collectées sont accessibles publiquement sur le site AlloCiné. Cependant, elles restent soumises à des conditions d'utilisation. Dans le cadre de ce projet, je m’assure de respecter une démarche éthique : le projet est réalisé à des fins exclusivement pédagogiques, sans visée commerciale, sans publication ni diffusion publique des données. Les données ne seront utilisées que pour expérimenter localement des modèles de traitement du langage.

## Etude de cas d'un corpus préexistant : CoNLL 2003

- 1) Quelle type de tâche propose CoNLL 2003 ?

CoNLL 2003 propose une tâche d’étiquetage de séquences, plus précisément une tâche de reconnaissance d'entités nommées. Les entités annotées sont : LOC (lieux), PER (personnes), ORG (organisations), MISC (divers, ex. gentilés, événements).

- 2)   Quel type de données y a-t-il dans CoNLL 2003 ?

Le corpus CoNLL 2003 est composé de 8 fichiers répartis en deux langues : l’anglais et l’allemand. Pour chaque langue, on trouve quatre fichiers : un fichier d’entraînement, un de développement, un de test, ainsi qu’un fichier de données non annotées. Les données en anglais proviennent du Reuters Corpus, constitué d’articles de presse publiés entre 1996 et 1997, tandis que les données en allemand sont extraites du ECI Multilingual Text Corpus, en particulier du journal Frankfurter Rundschau, avec des articles datant de 1992.

- 3) A quel besoin répond CoNLL 2003 ?

Il sert à entraîner des modèles de reconnaissance d’entités nommées basés sur l’apprentissage profond.

- 4) Quels types de modèles ont été entraînés sur CoNLL 2003 ?

En tout, 16 systèmes différents ont été entraînés sur le corpus CoNLL 2003, chacun développé par un participant différent. Chacun utilisait sa propre combinaison de techniques de machine learning, comme les HMM ou les CRF. À l’époque, on trouvait aussi des méthodes comme les SVM ou les perceptrons structurés. Plus récemment, des modèles plus puissants basés sur le deep learning ont été testés, par exemple des réseaux BiLSTM avec CRF ou des modèles Transformers comme BERT, LUKE, FLERT ou encore ACE, qui sont entraînés spécifiquement pour reconnaître les entités nommées.

- 5) Est un corpus monolingue ou multilingue ?

C’est un corpus multilingue anglais / allemand.
