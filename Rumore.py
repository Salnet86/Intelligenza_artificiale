import random

# Parametri
n_vettori = 64        # Numero di immagini nel batch
dim_latente = 100     # Lunghezza di ogni vettore di rumore

# Genera una matrice (lista di liste) di rumore Gaussiano (media 0, dev 1)
rumore_batch = [[random.gauss(0, 1) for _ in range(dim_latente)] for _ in range(n_vettori)]

# Per vedere, ad esempio, il primo numero del primo vettore:
print(rumore_batch)
