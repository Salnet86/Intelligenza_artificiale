pip install face_recognition opencv-python






import face_recognition
import cv2


# Carica immagine della persona da cercare
reference_image = face_recognition.load_image_file("persona_riferimento.jpg")
reference_encoding = face_recognition.face_encodings(reference_image)[0]


# Carica immagine dove cercare la faccia
search_image = face_recognition.load_image_file("foto_cerca.jpg")
search_encodings = face_recognition.face_encodings(search_image)


# Usa OpenCV per mostrare risultati (opzionale)
image_to_show = cv2.cvtColor(search_image, cv2.COLOR_RGB2BGR)


found_match = False


for encoding in search_encodings:
    # Confronta ogni faccia trovata con quella di riferimento
    matches = face_recognition.compare_faces([reference_encoding], encoding)
    if matches[0]:
        found_match = True
        print("Faccia trovata nella foto!")
        break


if not found_match:
    print("Faccia non trovata.")


# Se vuoi, mostra la foto (opzionale)
cv2.imshow("Ricerca Facciale", image_to_show)
cv2.waitKey(0)
cv2.destroyAllWindows()

