from google.cloud import vision

# Crea un client
client = vision.ImageAnnotatorClient()

# Carica l'immagine
image = vision.Image()
image.source.image_uri = 'https://pbs.twimg.com/profile_images/642451771051409408/6w-5w-xb_400x400.jpg'

# Rilevamento dei volti
response = client.face_detection(image=image)
faces = response.face_annotations

# Stampa il numero di volti trovati
print(f'Trovati {len(faces)} volti.')

# Stampa le coordinate dei volti
for face in faces:
    print(f'Volto trovato con coordinate: {face.bounding_poly}')
