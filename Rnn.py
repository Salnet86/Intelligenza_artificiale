import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense

# Configurazione parametri
vocab_size = 500  # Dimensione del vocabolario (quella del tuo BPE)
embedding_dim = 16
seq_length = 10   # Lunghezza della sequenza

model = Sequential([
    # Embedding: converte gli ID dei token in vettori densi
    Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=seq_length),
    
    # SimpleRNN: Il cuore ricorrente
    SimpleRNN(32, activation='tanh', return_sequences=False),
    
    # Output: Classificazione
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy')

# Visualizza la struttura
model.summary()
