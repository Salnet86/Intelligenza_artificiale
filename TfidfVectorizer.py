from sklearn.feature_extraction.text import TfidfVectorizer

# 1. Definiamo un piccolo corpus di documenti (frasi)
documenti = [
    "Il gatto mangia il pesce",
    "Il cane abbaia forte",
    "Un gatto e un cane giocano nel parco",
]

# 2. Creiamo l'oggetto TfidfVectorizer
# (internamente prende ogni documento e fa il equivalente di .split())
vectorizer = TfidfVectorizer()

# 3. Calcoliamo il TF-IDF
matrice_tfidf = vectorizer.fit_transform(documenti)

# 4. Stampiamo i risultati
print("Parole nel vocabolario (le colonne):")
print(vectorizer.get_feature_names_out())

print("\nMatrice dei pesi TF-IDF (righe = documenti, colonne = parole):")
print(matrice_tfidf.toarray())
