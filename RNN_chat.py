import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import TextVectorization, Embedding, SimpleRNN, Dense
import numpy as np

# 1. Dataset di addestramento (Il "cervello" del bot)
# Categorizziamo in: 0 = Saluto, 1 = Problema Tecnico, 2 = Domanda Generica
training_data = [
    ("ciao come stai", 0), ("buongiorno", 0),
    ("il circuito è rotto", 1), ("non funziona il display", 1), ("errore di compilazione", 1),
    ("cosa è un trasformatore", 2), ("spiegami la rnn", 2)
]
texts = [x[0] for x in training_data]
labels = [x[1] for x in training_data]

# 2. Pipeline di Preprocessing
vectorizer = TextVectorization(max_tokens=100, output_sequence_length=10)
vectorizer.adapt(texts)

# 3. Costruzione del modello RNN
model = Sequential([
    tf.keras.Input(shape=(1,), dtype=tf.string),
    vectorizer,
    Embedding(input_dim=100, output_dim=16),
    SimpleRNN(32, activation='tanh'),
    Dense(3, activation='softmax') # 3 categorie in output
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')

# Addestramento rapido (pochissime epoche per demo)
model.fit(np.array(texts), np.array(labels), epochs=20, verbose=0)

# 4. Loop di Chat Interattivo
print("--- Bot Analizzatore RNN (Scrivi 'esci' per chiudere) ---")
risposte = ["Ciao! Come va?", "Sembra un guasto tecnico, controlla il datasheet.", "Ottima domanda teorica!"]

while True:
    input_text = input("Tu: ")
    if input_text.lower() == 'esci':
        break
        
    # Predizione
    prediction = model.predict([input_text], verbose=0)
    categoria = np.argmax(prediction)
    
    print(f"Bot (Rilevato Intento {categoria}): {risposte[categoria]}\n")
