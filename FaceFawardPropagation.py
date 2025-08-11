"""
Autori:
Valentina,
Salvatore,
Paola,
Fabrizzio,
Tutor Rizzo
Stagisti Corso Addetto alla logistica automatica ambito IOT


Esempio semplice di forward propagation per classificazione facciale.


Input:
- feature vettoriale (es. vettore di lunghezza 5, simulazione di caratteristiche estratte)


Rete:
- Input layer: 5 neuroni
- Hidden layer: 3 neuroni, funzione sigmoid
- Output layer: 2 neuroni (probabilità due classi), sigmoid
"""


import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# Funzione forward propagation
def forward_propagation(x, W1, b1, W2, b2):
    z1 = np.dot(x, W1) + b1
    a1 = sigmoid(z1)
    z2 = np.dot(a1, W2) + b2
    output = sigmoid(z2)
    return output


# Dati di input (feature facciali simulati)
x_input = np.array([0.5, 0.3, 0.2, 0.1, 0.4]) # esempio vettore feature


# Pesi e bias fissi per esempio
W1 = np.array([[0.2, -0.3, 0.4],
               [0.7, 0.1, -0.5],
               [-0.6, 0.8, 0.2],
               [0.1, -0.4, 0.6],
               [0.5, 0.2, -0.1]])


b1 = np.array([0.1, -0.2, 0.05])


W2 = np.array([[0.3, -0.6],
               [-0.1, 0.4],
               [0.5, -0.3]])


b2 = np.array([0.05, -0.05])


# Eseguo forward propagation
output = forward_propagation(x_input, W1, b1, W2, b2)


print("Output rete (probabilità classi):", output)
print("Classe predetta:", np.argmax(output))

