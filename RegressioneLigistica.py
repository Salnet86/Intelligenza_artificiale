from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# Dataset di esempio: email testuali e label (1=spam, 0=no spam)
emails = [
    "offerta gratis clicca",
    "ciao come stai",
    "clicca ora offerta speciale",
    "ciao ho un regalo per te",
    "offerta limitata clicca subito",
    "come va tutto bene"
]
labels = [1, 0, 1, 0, 1, 0]


# Creiamo un vettorizzatore "bag of words" (simile a One-Hot ma conta frequenze)
vectorizer = CountVectorizer(binary=True) # binary=True -> presenza assente (0/1)


# Trasformiamo le email in vettori binari
X = vectorizer.fit_transform(emails)


# Dividiamo in training e test
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.33, random_state=42)


# Creiamo il modello di regressione logistica
model = LogisticRegression()


# Alleniamo il modello
model.fit(X_train, y_train)


# Predizioni su test set
y_pred = model.predict(X_test)


# Valutiamo l'accuratezza
acc = accuracy_score(y_test, y_pred)
print(f"Accuratezza sul test set: {acc*100:.2f}%")


# Proviamo a classificare una nuova email
new_email = ["clicca ora per il regalo speciale"]
X_new = vectorizer.transform(new_email)
pred = model.predict(X_new)[0]
prob = model.predict_proba(X_new)[0][1]


print(f"\nNuova email: '{new_email[0]}'")
print(f"Predizione: {'Spam' if pred == 1 else 'No spam'} con probabilità {prob*100:.2f}%")

