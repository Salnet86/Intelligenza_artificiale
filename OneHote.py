from sklearn.preprocessing import OneHotEncoder
import numpy as np


# Etichette testuali
labels = np.array(['Sunny', 'Overcast', 'Rain', 'Sunny', 'Rain']).reshape(-1, 1)


# Inizializza encoder
encoder = OneHotEncoder(sparse=False)


# Fai il fit e trasforma
one_hot = encoder.fit_transform(labels)


print("Etichette originali:", labels.ravel())
print("One-hot encoding:\n", one_hot)

