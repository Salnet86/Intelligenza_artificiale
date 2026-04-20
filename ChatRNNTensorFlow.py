import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

# Dataset semplice (domanda -> risposta)
domande = [
    "ciao",
    "come stai",
    "chi sei",
    "arrivederci"
]

risposte = [
    "ciao!",
    "sto bene",
    "sono un bot",
    "a presto"
]

# Tokenizzazione
tokenizer = Tokenizer()
tokenizer.fit_on_texts(domande + risposte)

# Converti testo in numeri
X = tokenizer.texts_to_sequences(domande)
y = tokenizer.texts_to_sequences(risposte)

# Padding (stessa lunghezza)
max_len = 5
X = pad_sequences(X, maxlen=max_len, padding='post')
y = pad_sequences(y, maxlen=max_len, padding='post')

# Modello
model = Sequential([
    Embedding(input_dim=1000, output_dim=64, input_length=max_len),
    LSTM(64, return_sequences=True),
    Dense(1000, activation='softmax')
])

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam')

# Reshape y per compatibilità
y = np.expand_dims(y, -1)

# Training
model.fit(X, y, epochs=500, verbose=0)

# Funzione chat
def rispondi(frase):
    seq = tokenizer.texts_to_sequences([frase])
    seq = pad_sequences(seq, maxlen=max_len, padding='post')
    
    pred = model.predict(seq)
    pred = np.argmax(pred, axis=-1)
    
    # Converti numeri → parole
    risposta = []
    for i in pred[0]:
        parola = tokenizer.index_word.get(i, '')
        if parola != '':
            risposta.append(parola)
    
    return " ".join(risposta)

# Test
print(rispondi("ciao"))
