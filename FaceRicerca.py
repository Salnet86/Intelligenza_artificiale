"""
face_recognition_demo.py


Esegue il riconoscimento facciale confrontando una o più immagini conosciute
con una immagine sconosciuta e disegnando riquadri sui volti rilevati.


Requisiti:
    pip install face_recognition opencv-python pillow numpy


Uso:
    python face_recognition_demo.py known.jpg unknown.jpg
"""


import sys
import face_recognition
import cv2
import numpy as np
from PIL import Image


# 1. Controllo parametri
if len(sys.argv) < 3:
    print("Uso: python face_recognition_demo.py immagine_conosciuta.jpg immagine_sconosciuta.jpg")
    sys.exit(1)


known_image_path = sys.argv[1] # Immagine della persona conosciuta
unknown_image_path = sys.argv[2] # Immagine da analizzare


# 2. Carico e codifico la faccia conosciuta
known_image = face_recognition.load_image_file(known_image_path)
known_encoding = face_recognition.face_encodings(known_image)[0] # Codifica 128-dim della faccia


# 3. Carico e analizzo immagine sconosciuta
unknown_image = face_recognition.load_image_file(unknown_image_path)


# 4. Trovo i volti e calcolo le codifiche
face_locations = face_recognition.face_locations(unknown_image)
face_encodings = face_recognition.face_encodings(unknown_image, face_locations)


# 5. Converto per OpenCV (BGR)
image_cv = cv2.cvtColor(unknown_image, cv2.COLOR_RGB2BGR)


# 6. Confronto ogni volto trovato con quello conosciuto
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces([known_encoding], face_encoding)
    name = "Sconosciuto"


    if True in matches:
        name = "Persona conosciuta"


    # Disegno riquadro e nome
    cv2.rectangle(image_cv, (left, top), (right, bottom), (0, 255, 0), 2)
    cv2.rectangle(image_cv, (left, bottom - 20), (right, bottom), (0, 255, 0), cv2.FILLED)
    cv2.putText(image_cv, name, (left + 2, bottom - 5), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 0), 1)


# 7. Mostro il risultato
cv2.imshow("Risultato", image_cv)
cv2.waitKey(0)
cv2.destroyAllWindows()

