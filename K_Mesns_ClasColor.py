"""
Script: color_clustering.py
Descrizione: Usa K-means per trovare i colori dominanti in un'immagine.
Risultati:
 - Immagine ricostruita con i colori dei cluster
 - Palette con i colori dominanti
 - Percentuali di ogni colore


Requisiti:
    pip install pillow numpy scikit-learn matplotlib
"""


import argparse # Per leggere parametri da riga di comando
from PIL import Image # Per aprire e salvare immagini
import numpy as np # Per gestire array di pixel
from sklearn.cluster import KMeans # Algoritmo K-means
import os
import math


# -----------------------------
# Carica immagine e ridimensiona
# -----------------------------
def load_image(path, resize=None):
    img = Image.open(path).convert("RGB") # Apre l'immagine e forza il formato RGB
    if resize:
        # Ridimensiona mantenendo proporzioni
        w, h = img.size
        scale = resize / max(w, h) # Calcola fattore di scala in base al lato più lungo
        new_size = (max(1, math.floor(w * scale)), max(1, math.floor(h * scale)))
        img = img.resize(new_size, Image.LANCZOS) # Ridimensiona con filtro di alta qualità
    return img


# -----------------------------
# Converte immagine in array 2D
# -----------------------------
def image_to_data(img):
    arr = np.array(img) # Converte in array NumPy (altezza x larghezza x 3)
    pixels = arr.reshape(-1, 3).astype(np.float32) # Trasforma in lista di pixel [R, G, B]
    return pixels


# -----------------------------
# Esegue K-means sui pixel
# -----------------------------
def cluster_colors(pixels, k=5, random_state=42):
    kmeans = KMeans(n_clusters=k, random_state=random_state, n_init=10)  
    labels = kmeans.fit_predict(pixels) # Assegna ogni pixel al cluster più vicino
    centers = kmeans.cluster_centers_.astype(int) # Trova colori medi (centroidi)
    return labels, centers


# -----------------------------
# Ricostruisce immagine quantizzata
# -----------------------------
def recreate_image(labels, centers, img_size):
    new_pixels = centers[labels] # Sostituisce ogni pixel col colore del cluster
    new_img = new_pixels.reshape(img_size[1], img_size[0], 3) # Ricostruisce l'immagine
    return Image.fromarray(np.uint8(new_img)) # Converte in immagine PIL


# -----------------------------
# Funzione principale
# -----------------------------
def main():
    parser = argparse.ArgumentParser(description="Color clustering con K-means")
    parser.add_argument("image_path", help="Percorso dell'immagine")
    parser.add_argument("--k", type=int, default=5, help="Numero di colori (cluster)")
    parser.add_argument("--resize", type=int, default=None, help="Ridimensiona lato max")
    parser.add_argument("--out_prefix", default="output", help="Prefisso per i file di output")
    args = parser.parse_args()


    # Carica immagine
    img = load_image(args.image_path, args.resize)
    pixels = image_to_data(img)


    # Clustering
    labels, centers = cluster_colors(pixels, args.k)


    # Ricostruzione immagine
    new_img = recreate_image(labels, centers, img.size)
    new_img.save(f"{args.out_prefix}_clustered.png") # Salva immagine ricostruita


    # Mostra colori dominanti
    print("Colori dominanti (RGB):")
    for i, color in enumerate(centers):
        percent = np.sum(labels == i) / len(labels) * 100
        print(f"Cluster {i+1}: {color} - {percent:.2f}%")


if __name__ == "__main__":
    main()

