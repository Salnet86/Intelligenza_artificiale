#AUTORI DEL CODICE VALENTINA SALVATORE 
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense

# --- 1. DATI DI TRAINING E VOCABOLARIO ---
domande = ["ciao", "buongiorno", "ehi", "che tempo fa", "previsioni meteo", "piove"]
etichette = np.array([0, 0, 0, 1, 1, 1]) # 0=Saluto, 1=Meteo

vocabolario_risposte = {
    0: "Ciao ! Come posso aiutarti?",
    1: "Le previsioni indicano cielo variabile."
}

# --- 2. TOKENIZZAZIONE E PREPARAZIONE ---
tokenizer = Tokenizer(num_words=100, oov_token="<OOV>")
tokenizer.fit_on_texts(domande)
sequenze = tokenizer.texts_to_sequences(domande)
dati_training = pad_sequences(sequenze, maxlen=5, padding='post')

# --- 3. CREAZIONE E ADDESTRAMENTO RAPIDO ---
model = Sequential([
    Embedding(input_dim=100, output_dim=8),
    SimpleRNN(16),
    Dense(1, activation='sigmoid') # Uscita tra 0 e 1
])
model.compile(optimizer='adam', loss='binary_crossentropy')
model.fit(dati_training, etichette, epochs=300, verbose=0)

# --- 4. INPUT UTENTE E LOGICA DI RISPOSTA ---
testo_utente = input("Scrivi qualcosa (es. 'ciao' o 'meteo'): ")

# Trasformiamo l'input
seq_utente = tokenizer.texts_to_sequences([testo_utente])
pad_utente = pad_sequences(seq_utente, maxlen=5, padding='post')

# La RNN fa la predizione (il numero decimale)
predizione = model.predict(pad_utente, verbose=0)[0][0]

# --- LA TUA LOGICA CON IF ---
if predizione > 0.5:
    indice = 1
else:
    indice = 0

print(f"\nValore RNN: {predizione:.4f}")
print(f"Chatbot: {vocabolario_risposte[indice]}")
