import random

size = 412
WK = []

# Primo ciclo: scorre le righe e crea un "contenitore" nuovo per ciascuna
for i in range(size):
  contenitore = []  # Questo è il contenitore temporaneo per la singola riga

  # Secondo ciclo: scorre le colonne e riempie il contenitore
  for j in range(size):
    # Generiamo un numero decimale casuale piccolo (perfetto per i pesi)
    p = random.uniform(-0.1, 0.1)
    contenitore.append(p)

  # Una volta pieno, infiliamo il contenitore dentro la matrice principale WK
  WK.append(contenitore)

print(
    f"Matrice WK creata con successo! Contenitori totali: {len(WK)}, Elementi"
    f" per contenitore: {len(WK[0])}"
)
