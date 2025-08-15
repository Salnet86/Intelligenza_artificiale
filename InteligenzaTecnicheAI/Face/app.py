from flask import Flask, request, render_template
import cv2
import os

app = Flask(__name__)
UPLOAD_FOLDER = "static/upload"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Classificatore per i volti
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

@app.route("/", methods=["GET", "POST"])
def index():
    alert = ""
    img1_url = ""
    img2_url = ""

    if request.method == "POST":
        file1 = request.files.get("file1")
        file2 = request.files.get("file2")

        if file1 and file2:
            # Salva le immagini
            img1_url = os.path.join(UPLOAD_FOLDER, file1.filename)
            img2_url = os.path.join(UPLOAD_FOLDER, file2.filename)
            file1.save(img1_url)
            file2.save(img2_url)

            # Carica le immagini in scala di grigi
            dati1 = cv2.cvtColor(cv2.imread(img1_url), cv2.COLOR_BGR2GRAY)
            dati2 = cv2.cvtColor(cv2.imread(img2_url), cv2.COLOR_BGR2GRAY)

            # Rileva un volto per immagine
            faces1 = face_cascade.detectMultiScale(dati1, 1.1, 5)
            faces2 = face_cascade.detectMultiScale(dati2, 1.1, 5)

            if len(faces1)==0 or len(faces2)==0:
                alert = "Non ci sono volti in una delle due immagini"
            else:
                x1, y1, w1, h1 = faces1[0]
                x2, y2, w2, h2 = faces2[0]

                # Ritaglia i volti e ridimensiona
                im1 = cv2.resize(dati1[y1:y1+h1, x1:x1+w1], (100,100))
                im2 = cv2.resize(dati2[y2:y2+h2, x2:x2+w2], (100,100))

                # Confronto semplice template
                res = cv2.matchTemplate(im1, im2, cv2.TM_CCOEFF_NORMED)
                alert = "⚠️ Volti UGUALI!" if res >= 0.6 else "Volti diversi"

    return render_template("index.html", alert=alert, img1=img1_url, img2=img2_url)

if __name__=="__main__":
    app.run(debug=True)

