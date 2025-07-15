from PIL import Image

# Carica l'immagine input e la converte in scala di grigi
img_input = Image.open("volto_input.jpg").convert("L")
# Carica l'immagine target (volto registrato)
img_target = Image.open("volto_target.jpg").convert("L")

# Ridimensiona entrambe le immagini alla stessa dimensione (es. 64x64)
img_input = img_input.resize((64, 64))
img_target = img_target.resize((64, 64))

# Converte le immagini in vettori (lista di pixel)
vettore_input = list(img_input.getdata())
vettore_target = list(img_target.getdata())

# Normalizza pixel tra 0 e 1
vettore_input = [p / 255.0 for p in vettore_input]
vettore_target = [p / 255.0 for p in vettore_target]

# Calcola prodotto scalare tra vettore input e target
prodotto_scalare = 0
for i in range(len(vettore_input)):
prodotto_scalare += vettore_input[i] * vettore_target[i]

# Soglia arbitraria per decidere se il volto è lo stesso
soglia = 15 # da tarare in base alle immagini

if prodotto_scalare >= soglia:
print("Volto riconosciuto")
else:
print("Volto NON riconosciuto")

print("Prodotto scalare:", prodotto_scalare)
