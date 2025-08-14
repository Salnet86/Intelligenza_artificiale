import numpy as np

# Definizione della matrice 2x2
matrix = np.array([[3, 1],
                   [1, 1]])

# Stampa della matrice
print("Matrice originale:")
print(matrix)

# Dimensioni della matrice
print("\nDimensioni della matrice:")
print(matrix.shape)

# Accesso a singoli elementi
print("\nElementi singoli:")
print("Prima riga, primo elemento:", matrix[0, 0])
print("Seconda riga, secondo elemento:", matrix[1, 1])

# Trasposta della matrice
print("\nTrasposta della matrice:")
print(matrix.T)

# Determinante della matrice
det = np.linalg.det(matrix)
print("\nDeterminante della matrice:")
print(det)

# Inversa della matrice (solo se determinante ≠ 0)
if det != 0:
    inv = np.linalg.inv(matrix)
    print("\nInversa della matrice:")
    print(inv)
else:
    print("\nLa matrice non ha inversa.")
