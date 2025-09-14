# Docente: Alessandra  
# Lezioni di Informatica — AI — Rete CNN con Keras

import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.optimizers import Adam

# Carica il dataset MNIST (immagini di cifre scritte a mano)
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Pre-processing: ridimensiona le immagini e normalizza
x_train = np.expand_dims(x_train, axis=-1).astype('float32') / 255.0
x_test = np.expand_dims(x_test, axis=-1).astype('float32') / 255.0

# Converti le etichette in one-hot encoding
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# Crea il modello CNN
model = Sequential()

# Aggiungi il layer convoluzionale (32 filtri 3x3, con funzione di attivazione ReLU)
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)))

# Aggiungi un layer di pooling (max pooling 2x2)
model.add(MaxPooling2D(pool_size=(2, 2)))

# Aggiungi un altro layer convoluzionale (64 filtri 3x3, con ReLU)
model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))

# Aggiungi un altro layer di pooling (max pooling 2x2)
model.add(MaxPooling2D(pool_size=(2, 2)))

# Appiattisci il risultato per passarlo ai layer densi
model.add(Flatten())

# Aggiungi un layer denso con 128 neuroni e ReLU
model.add(Dense(128, activation='relu'))

# Aggiungi il layer di output (softmax per classificazione multiclass)
model.add(Dense(10, activation='softmax'))

# Compila il modello
model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])

# Addestra il modello
model.fit(x_train, y_train, epochs=5, batch_size=64, validation_data=(x_test, y_test))

# Valuta il modello
test_loss, test_accuracy = model.evaluate(x_test, y_test, verbose=0)

print(f"Test Loss: {test_loss:.4f}")
print(f"Test Accuracy: {test_accuracy * 100:.2f}%")

