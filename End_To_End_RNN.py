import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import TextVectorization, Embedding, SimpleRNN, Dense

# 1. Dati di esempio (Sostituisci con il tuo dataset)
frasi = ["Il circuito è interrotto", "Il componente è difettoso", "La tensione è stabile"]
etichette = [1, 1, 0]  # Esempio: 1 = Guasto, 0 = Ok

# 2. Configurazione del Preprocessing
max_tokens = 1000  # Dimensione vocabolario
max_len = 10       # Lunghezza massima della sequenza

vectorizer = TextVectorization(max_tokens=max_tokens, output_sequence_length=max_len)
vectorizer.adapt(frasi)  # Il layer "impara" il vocabolario dal testo

# 3. Costruzione del Modello
model = Sequential([
    # Input Layer (gestisce testo)
    tf.keras.Input(shape=(1,), dtype=tf.string),
    vectorizer,
    
    # Embedding: trasforma gli ID in vettori da 32 dimensioni
    Embedding(input_dim=max_tokens, output_dim=32),
    
    # RNN: elabora la sequenza
    SimpleRNN(64, activation='tanh'),
    
    # Output: classificazione binaria
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# 4. Esecuzione del test (Inference)
testo_input = ["Il circuito è difettoso"]
predizione = model.predict(testo_input)

print(f"Probabilità di guasto: {predizione[0][0]:.4f}")
