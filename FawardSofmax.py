import numpy as np


# Input
x = np.array([1.0, 2.0, 3.0])


# Pesi (3 neuroni output, 3 input ciascuno)
W = np.array([
    [0.2, 0.4, 0.1],
    [0.5, 0.1, 0.3],
    [0.3, 0.7, 0.2]
])


# Bias
b = np.array([0.1, 0.2, 0.3])


# Calcolo logits (z)
z = W.dot(x) + b


print("Logits (z):", z)


# Funzione softmax
def softmax(z):
    exp_z = np.exp(z)
    return exp_z / exp_z.sum()


# Calcolo output softmax
y = softmax(z)


print("Output softmax (probabilità):", y)
print("Classe predetta:", np.argmax(y) + 1) # +1 per indicare classe 1,2,3

