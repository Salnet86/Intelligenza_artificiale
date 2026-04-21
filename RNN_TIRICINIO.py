import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense

# --- 1. I DATI DI ADDESTRAMENTO ---
domande = ["ciao", "buongiorno", "che tempo fa", "piove oggi"]
etichette = np.array([0, 0, 1, 1]) # 0 = Saluto, 1 = Meteo

# --- 2. TOKENIZZAZIONE ---
tokenizer = Tokenizer(num_words=100, oov_token="<OOV>")
tokenizer.fit_on_texts(domande)
sequenze = tokenizer.texts_to_sequences(domande)
dati_x = pad_sequences(sequenze, maxlen=5, padding='post')

# --- 3. COSTRUZIONE E ADDESTRAMENTO RNN ---
model = Sequential([
    Embedding(input_dim=100, output_dim=8),
    SimpleRNN(16),
    Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy')
model.fit(dati_x, etichette, epochs=200, verbose=0)

# --- 4. INPUT UTENTE E RISPOSTA ---
InputText = input('Scrivi qualcosa: ')

# Trasformiamo quello che ha scritto l'utente
user_seq = tokenizer.texts_to_sequences([InputText])
user_pad = pad_sequences(user_seq, maxlen=5, padding='post')

# La RNN decide
predizione = model.predict(user_pad, verbose=0)
indice = int(np.round(predizione[0][0]))

# Database delle risposte
risposte = ["Ciao, io sono un'intelligenza artificiale!", "Oggi c'è il sole."]

print("Chatbot:", risposte[indice])
