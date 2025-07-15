# Apriamo il file e leggiamo le righe
file = open('immagine.txt', 'r')
righe = file.readlines()
file.close()

matrice = []
for linea in righe:
# Dividiamo la linea in numeri e li convertiamo in interi
valori = linea.strip().split()
riga = []
for val in valori:
riga.append(int(val))
matrice.append(riga)

print("Matrice immagine:")
for riga in matrice:
print(riga)

# Appiattiamo la matrice in un vettore
vettore = []
for riga in matrice:
for pixel in riga:
vettore.append(pixel)

print("\nVettore immagine appiattito:")
print(vettore)
