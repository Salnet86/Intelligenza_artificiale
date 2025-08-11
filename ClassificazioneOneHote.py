"""
Autore: Salvato Platania, Elisa, Stefania, Michele


Esempio:
- input testuale (es. parola o classe)
- one-hot encoding
- embedding layer (matrice pesi) per trasformare one-hot in vettore denso
"""


import numpy as np


# Dizionario delle parole (vocabolario)
vocab = ['cane', 'gatto', 'uccello', 'pesce']


# Funzione per creare vettore one-hot dato un indice
def one_hot(index, size):
    vec = np.zeros(size)
    vec[index] = 1
    return vec


# Simulo embedding layer: matrice di pesi (dim vocab x dim embedding)
embedding_dim = 3
embedding_matrix = np.array([
    [0.1, 0.2, 0.3], # embedding per 'cane'
    [0.4, 0.5, 0.6], # embedding per 'gatto'
    [0.7, 0.8, 0.9], # embedding per 'uccello'
    [1.0, 1.1, 1.2], # embedding per 'pesce'
])


# Input parola da codificare
input_word = 'gatto'


# Trovo indice parola
index = vocab.index(input_word)


# Creo vettore one-hot
one_hot_vec = one_hot(index, len(vocab))


# Calcolo embedding (moltiplicazione matrice)
embedding_vec = np.dot(one_hot_vec, embedding_matrix)


print("Parola input:", input_word)
print("One-hot vector:", one_hot_vec)
print("Embedding vettore:", embedding_vec)

