import numpy as np


labels = ['Sunny', 'Overcast', 'Rain', 'Sunny', 'Rain']
unique_labels = sorted(set(labels))


# Mappa ogni etichetta a un indice
label_to_index = {label: i for i, label in enumerate(unique_labels)}


# Crea la matrice one-hot
one_hot = np.zeros((len(labels), len(unique_labels)))


for i, label in enumerate(labels):
    idx = label_to_index[label]
    one_hot[i, idx] = 1


print("One-hot encoding (manuale):\n", one_hot)

