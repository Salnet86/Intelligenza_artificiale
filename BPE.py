import numpy as np
import math

# --- 1. CONFIGURAZIONE ---
vocab_size = 1000
embedding_dim = 512

# Tabella degli embedding (numeri casuali piccoli)
embedding_table = np.random.randn(vocab_size, embedding_dim) * 0.01

# --- 2. VOCABOLARIO (risultato del BPE) ---
# Mappa parola → ID
vocabolario = {
    "ciao": 0,
    "come": 1,
    "stai": 2,
    "gatto": 3
}

# --- 3. INPUT DELL'UTENTE ---
testo = input("Digita una frase: ")   # es: "ciao come stai"
parole = testo.split()                # tokenizzazione semplice

# --- 4. CICLO DI ELABORAZIONE ---
for i, p in enumerate(parole):  # i = posizione, p = parola
    if p in vocabolario:

        # A. Recupero ID ed embedding della parola
        word_id = vocabolario[p]
        v_embedding = embedding_table[word_id]

        # B. Creazione del vettore posizionale
        v_posizione = np.zeros(embedding_dim)

        for j in range(embedding_dim):
            angolo = i / (10000 ** (2 * (j // 2) / embedding_dim))

            if j % 2 == 0:
                v_posizione[j] = math.sin(angolo)
            else:
                v_posizione[j] = math.cos(angolo)

        # C. Somma embedding + posizione
        vettore_finale = v_embedding + v_posizione

        print(f"\n--- Elaborazione parola: '{p}' ---")
        print(f"ID: {word_id}")
        print(f"Posizione nella frase: {i}")
        print(f"Vettore finale (primi 3 valori): {vettore_finale[:3]}...")

    else:
        print(f"\nLa parola '{p}' non è nel vocabolario!")
