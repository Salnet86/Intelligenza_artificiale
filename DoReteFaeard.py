import random as rd
import math

# Funzione sigmoid e derivata
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def sigmoid_deriv(x):
    return x * (1 - x)  # x deve essere già l'output della sigmoid

# Input normalizzati (tra 0 e 1)
x = [50/100, 20/100, 30/100, 60/100]  

# Target (2 neuroni)
target = [0.1, 0.4]

# Numero di epoche
epoche = 10
# Learning rate
lr = 0.5

# Inizializzazione pesi piccoli tra -0.5 e 0.5
pesi = [[rd.uniform(-0.5, 0.5) for _ in range(4)] for _ in range(2)]
# Bias iniziale
bias = 0.0

for n in range(epoche):
    outputs = []
    z_values = []
    # --- FORWARD PASS ---
    for neurone in range(2):
        z = sum(pesi[neurone][i] * x[i] for i in range(4)) + bias
        out = sigmoid(z)
        outputs.append(out)
        z_values.append(z)
    
    # Calcolo MSE con 1/2
    mse = sum(0.5 * (outputs[i] - target[i])**2 for i in range(2))
    
    print(f"Epoca {n+1}: Output = {outputs}, MSE = {mse:.4f}")
    
    # --- BACKPROPAGATION ---
    deltas = [ (outputs[i] - target[i]) * sigmoid_deriv(outputs[i]) for i in range(2)]
    
    # Aggiornamento pesi e bias
    for neurone in range(2):
        for i in range(4):
            pesi[neurone][i] -= lr * deltas[neurone] * x[i]
    bias -= lr * sum(deltas)  # aggiornamento bias condiviso

