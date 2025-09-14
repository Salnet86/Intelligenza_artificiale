# Docente: Alessandra  
# Lezioni di Informatica — AI — Libreria con FNN e Perceptron

import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from sklearn.metrics import accuracy_score

# ---- Funzione per creare un Feedforward Neural Network (FNN) ----
def create_ffnn(input_dim, hidden_units=8, output_units=1, activation='relu', output_activation='sigmoid'):
    """
    Crea un modello Feedforward Neural Network (FNN) per classificazione binaria o regressione.
    - input_dim: Numero di feature in input
    - hidden_units: Numero di neuroni nel layer nascosto
    - output_units: Numero di neuroni nel layer di output
    - activation: Funzione di attivazione per il layer nascosto (default='relu')
    - output_activation: Funzione di attivazione per il layer di output (default='sigmoid')
    """
    model = Sequential()
    model.add(Dense(hidden_units, input_dim=input_dim, activation=activation))
    model.add(Dense(output_units, activation=output_activation))
    model.compile(optimizer=Adam(), loss='binary_crossentropy', metrics=['accuracy'])
    return model

# ---- Funzione per creare un Perceptron ----
def create_perceptron(input_dim, output_units=1, activation='sigmoid'):
    """
    Crea un modello Perceptron per classificazione binaria.
    - input_dim: Numero di feature in input
    - output_units: Numero di neuroni nel layer di output
    - activation: Funzione di attivazione per il layer di output (default='sigmoid')
    """
    model = Sequential()
    model.add(Dense(output_units, input_dim=input_dim, activation=activation))
    model.compile(optimizer=Adam(), loss='binary_crossentropy', metrics=['accuracy'])
    return model

# ---- Esempio di utilizzo con dati fittizi ----

# Dati di esempio (2 feature)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Input: combinazioni di 2 variabili
y = np.array([0, 1, 1, 0])  # Target: XOR (classificazione)

# Crea un modello Feedforward Neural Network (FNN)
fnn_model = create_ffnn(input_dim=2, hidden_units=4, output_units=1, activation='relu', output_activation='sigmoid')

# Addestra il modello FNN
fnn_model.fit(X, y, epochs=100, batch_size=1, verbose=0)

# Crea un modello Perceptron
perceptron_model = create_perceptron(input_dim=2, output_units=1, activation='sigmoid')

# Addestra il modello Perceptron
perceptron_model.fit(X, y, epochs=100, batch_size=1, verbose=0)

# Predizione con il FNN
fnn_pred = fnn_model.predict(X).round()

# Predizione con il Perceptron
perceptron_pred = perceptron_model.predict(X).round()

# Calcola l'accuratezza per entrambi i modelli
fnn_accuracy = accuracy_score(y, fnn_pred)
perceptron_accuracy = accuracy_score(y, perceptron_pred)

# Stampa i risultati
print(f"FNN Predictions: {fnn_pred.flatten()}")
print(f"Perceptron Predictions: {perceptron_pred.flatten()}")
print(f"FNN Accuracy: {fnn_accuracy * 100:.2f}%")
print(f"Perceptron Accuracy: {perceptron_accuracy * 100:.2f}%")
