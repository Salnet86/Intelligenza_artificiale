from PIL import Image
import math

# Carica e normalizza le immagini in scala di grigi e stessa dimensione
img1 = Image.open("img1.jpg").convert("L").resize((64, 64))
img2 = Image.open("img2.jpg").convert("L").resize((64, 64))

vec1 = [p / 255.0 for p in img1.getdata()]
vec2 = [p / 255.0 for p in img2.getdata()]

# Calcola prodotto scalare
prodotto_scalare = 0
somma_quadrati_vec1 = 0
somma_quadrati_vec2 = 0

for i in range(len(vec1)):
prodotto_scalare += vec1[i] * vec2[i]
somma_quadrati_vec1 += vec1[i] ** 2
somma_quadrati_vec2 += vec2[i] ** 2

# Calcola norme (lunghezze)
norma_vec1 = math.sqrt(somma_quadrati_vec1)
norma_vec2 = math.sqrt(somma_quadrati_vec2)

# Calcola similarità coseno (protezione divisione per zero)
if norma_vec1 > 0 and norma_vec2 > 0:
similarita_coseno = prodotto_scalare / (norma_vec1 * norma_vec2)
else:
similarita_coseno = 0

# Stampa risultati
print(f"Prodotto scalare: {prodotto_scalare:.4f}")
print(f"Similarità coseno: {similarita_coseno:.4f}")

# Soglie esempio (da tarare in base ai dati)
soglia_prodotto = 15
soglia_coseno = 0.9

print("\nDecisione con prodotto scalare:")
if prodotto_scalare >= soglia_prodotto:
print("Immagini simili")
else:
print("Immagini diverse")

print("\nDecisione con similarità coseno:")
if similarita_coseno >= soglia_coseno:
print("Immagini simili")
else:
print("Immagini diverse")
