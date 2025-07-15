# Leggi immagine da file
file = open('immagine.txt', 'r')
righe = file.readlines()
file.close()

matrice = []
for linea in righe:
valori = linea.strip().split()
riga = []
for val in valori:
riga.append(int(val))
matrice.append(riga)

print("Matrice immagine:")
for r in matrice:
print(r)

# Appiattisci la matrice in vettore
vettore = []
for r in matrice:
for pixel in r:
vettore.append(pixel)

print("\nVettore immagine appiattito:")
print(vettore)

# Pesi e bias
pesi = [0.2, -0.1, 0.4, 0.3] # adatta la lunghezza in base alla dimensione vettore
bias = -30

# Calcola somma pesata z
z = 0
for i in range(len(vettore)):
z += pesi[i] * vettore[i]
z += bias

# Funzione step
if z >= 0:
output = 1
else:
output = 0

print(f"\nSomma pesata z = {z}")
print(f"Output neurone = {output}")

# Target (output desiderato)
target = 1 # 1 = gatto, 0 = cane

# Calcola errore
errore = target - output
print(f"Target = {target}")
print(f"Errore = {errore}")
