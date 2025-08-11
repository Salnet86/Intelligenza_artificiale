"""


Autore: 


Valentina,
Salvatore,
Paola,
Fabrizzio,
, Tutor Rizzo
Stagisti Corso Addetto alla logistica automatica ambito IOT


Descrizione:
    Esempio di forward propagation in una rete neurale feedforward
    con:
        - 2 input (temperatura, pressione)
        - 2 hidden layer da 4 neuroni ciascuno
        - 2 neuroni di output
    Funzione di attivazione: Sigmoid
"""


import numpy as np


# ----------------------------
# Funzione di attivazione Sigmoid
# ----------------------------
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# ----------------------------
# Dati di input (temperatura, pressione)
# ----------------------------
# Esempio: 30°C e 1.02 bar
inputs = np.array([30, 1.02]) # forma: (2,)


# ----------------------------
# Inizializzazione pesi e bias
# ----------------------------
# Layer 1: 2 input → 4 neuroni
W1 = np.random.rand(2, 4) # matrice 2x4
b1 = np.random.rand(4) # bias per 4 neuroni


# Layer 2: 4 input → 4 neuroni
W2 = np.random.rand(4, 4) # matrice 4x4
b2 = np.random.rand(4) # bias per 4 neuroni


# Output layer: 4 input → 2 neuroni
W3 = np.random.rand(4, 2) # matrice 4x2
b3 = np.random.rand(2) # bias per 2 neuroni


# ----------------------------
# Forward propagation
# ----------------------------


# Layer 1
z1 = np.dot(inputs, W1) + b1 # combinazione lineare
a1 = sigmoid(z1) # attivazione


# Layer 2
z2 = np.dot(a1, W2) + b2 # combinazione lineare
a2 = sigmoid(z2) # attivazione


# Output layer
z3 = np.dot(a2, W3) + b3 # combinazione lineare
output = sigmoid(z3) # attivazione finale


# ----------------------------
# Stampa risultati
# ----------------------------
print("Input (Temperatura, Pressione):", inputs)
print("\nLayer 1 - output attivazione:", a1)
print("Layer 2 - output attivazione:", a2)
print("Output finale:", output)

