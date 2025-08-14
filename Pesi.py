import numpy as np
import random as rd

# Pesi casuali per 2 neuroni e 4 input
pesi = np.array([
    [rd.uniform(0, 1) for _ in range(4)],
    [rd.uniform(0, 1) for _ in range(4)]
])

# Input
x = [200, 100, 200, 300]

# Bias
bias = 0.8

# Numero di epoche
epoche = 2

# Lista per salvare gli output
a1 = []

# Ciclo per epoche
for n in range(epoche):
    output_epoca = []  # output dei neuroni in questa epoca
    
    # Ciclo sui neuroni
    for neurone in range(2):
        z1 = 0
        # Ciclo sugli input
        for i in range(4):
            z1 += pesi[neurone][i] * x[i]
        z1 += bias
        output_epoca.append(z1)
    
    a1.append(output_epoca)

print("Output per ogni epoca:", a1)
