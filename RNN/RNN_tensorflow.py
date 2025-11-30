import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense

# -------------------------------
# 1. Creazione dei dati di esempio
# -------------------------------
# Sequenze numeriche da 0 a 9
sequence_length = 5
data = np.array([i for i in range(10)])

# Funzione per creare sequenze X e y
def create_sequences(data, seq_length):
    X = []
    y = []
    for i in range(len(data) - seq_length):
        X.append(data[i:i+seq_length])
        y.append(data[i+seq_length])
    return np.array(X), np.array(y)

X, y = create_sequences(data, sequence_length)

# RNN si aspetta input 3D: [batch_size, timesteps, features]
X = X.reshape((X.shape[0], X.shape[1], 1))

print("X shape:", X.shape)
print("y shape:", y.shape)

# -------------------------------
# 2. Creazione del modello RNN
# -------------------------------
model = Sequential()
model.add(SimpleRNN(50, activation='relu', input_shape=(sequence_length, 1)))
model.add(Dense(1))  # Output singolo

model.compile(optimizer='adam', loss='mse')

# -------------------------------
# 3. Addestramento del modello
# -------------------------------
model.fit(X, y, epochs=200, verbose=1)

# -------------------------------
# 4. Previsione
# -------------------------------
test_input = np.array([5, 6, 7, 8, 9])
test_input = test_input.reshape((1, sequence_length, 1))

predicted = model.predict(test_input, verbose=0)
print("Predizione per la sequenza [5,6,7,8,9]:", predicted[0][0])
