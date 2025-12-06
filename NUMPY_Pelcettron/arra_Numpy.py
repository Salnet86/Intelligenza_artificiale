import numpy as np
'''
X = np.array([[1, 2]])     # shape (1, 2)
W = np.array([[3], [4]])   # shape (2, 1)
'''


import numpy as np

X = np.array([1, 2])      # vettore 1×2
W = np.array([[3],
              [4]])       # matrice 2×1  x * 3 * x * 4=  1⋅3+2⋅4=3+8=11

print(X @ W)  # -> [[11]]
