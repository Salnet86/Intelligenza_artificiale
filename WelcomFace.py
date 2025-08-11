"""
face_recognition_webcam.py


Esegue il riconoscimento facciale in tempo reale usando la webcam.
Confronta il volto rilevato con un'immagine conosciuta.


Requisiti:
    pip install face_recognition opencv-python pillow numpy


Uso:
    python face_recognition_webcam.py known.jpg
"""


import sys
import face_recognition
import cv2
import numpy as np


# 1. Controllo parametro (immagine conosciuta)
if len(sys.argv) < 2:
    print("Uso: python face_recognition_webcam.py immagine_conosciuta.jpg")
    sys.exit(1)


known_image_path = sys.argv[1] # Immagine persona conosciuta


# 2. Carico immagine conosciuta e calcolo encoding
known_image = face_recognition.load_image_file(known_image_path)
known_encoding = face_recognition.face_encodings(known_image)[0]


# 3. Creo lista encodings e nomi associati (puoi aggiungerne altri)
known_encodings = [known_encoding]
known_names = ["Persona conosciuta"]


# 4. Avvio webcam
video_capture = cv2.VideoCapture(0)


print("Premi 'q' per uscire.")


while True:
    # 5. Leggo frame dalla webcam
    ret, frame = video_capture.read()
    if not ret:
        break


    # 6. Converto BGR → RGB (face_recognition lavora in RGB)
    rgb_frame = frame[:, :, ::-1]


    # 7. Trovo facce e encoding nel frame corrente
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)


    # 8. Confronto con volti conosciuti
    face_names = []
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_encodings, face_encoding)
        name = "Sconosciuto"


        if True in matches:
            first_match_index = matches.index(True)
            name = known_names[first_match_index]


        face_names.append(name)


    # 9. Disegno riquadri e nomi
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2) # riquadro volto
        cv2.rectangle(frame, (left, bottom - 20), (right, bottom), (0, 255, 0), cv2.FILLED) # box nome
        cv2.putText(frame, name, (left + 2, bottom - 5), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 0), 1)


    # 10. Mostro video
    cv2.imshow('Riconoscimento facciale', frame)


    # 11. Uscita con 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# 12. Rilascio risorse
video_capture.release()
cv2.destroyAllWindows()

