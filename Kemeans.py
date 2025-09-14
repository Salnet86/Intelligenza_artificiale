# Docente: Alessandra  
# Lezioni di Informatica — AI — K-Means con tensione e corrente, visualizzazione con Matplotlib

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Dati di esempio: tensione e corrente
# Esempio fittizio di dati di tensione (V) e corrente (A)
tensione = np.array([10, 12, 13, 15, 16, 18, 20, 21, 23, 24, 30, 35, 40, 50, 55])
corrente = np.array([2, 2.5, 2.8, 3, 3.2, 3.5, 3.8, 4, 4.5, 4.8, 5, 5.5, 6, 6.5, 7])

# Combinazione dei dati in un'unica matrice (tensione, corrente)
X = np.array(list(zip(tensione, corrente)))

# Creiamo il modello KMeans con 3 cluster
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

# Otteniamo i centri dei cluster e le etichette dei punti
centri_cluster = kmeans.cluster_centers_
etichetta_cluster = kmeans.labels_

# Visualizzazione dei dati
plt.figure(figsize=(8, 6))

# Plot dei dati con colore in base ai cluster
plt.scatter(tensione, corrente, c=etichetta_cluster, cmap='viridis', marker='o', label='Dati Clustering')

# Plot dei centri dei cluster
plt.scatter(centri_cluster[:, 0], centri_cluster[:, 1], s=200, c='red', marker='X', label='Centri Cluster')

# Aggiungere etichette e titolo
plt.title('K-Means Clustering: Tensione vs Corrente')
plt.xlabel('Tensione (V)')
plt.ylabel('Corrente (A)')
plt.legend()
plt.grid(True)

# Mostra il grafico
plt.show()

# Stampa dei centri dei cluster e delle etichette
print("Centri dei cluster:", centri_cluster)
print("Etichette dei cluster per ogni punto:", etichetta_cluster)
