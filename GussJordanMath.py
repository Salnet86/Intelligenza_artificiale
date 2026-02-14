matrix = [
    [1, 2, 7, 9],
    [9, 0, 0, 5],
    [8, 0, 4, 1],
    [3, 7, 0, 1]
]

n = len(matrix)

for i in range(n):
    max_riga = i

    # Ricerca pivot massimo (pivot parziale)
    for k in range(i + 1, n):
        if abs(matrix[k][i]) > abs(matrix[max_riga][i]):
            max_riga = k

    # Scambio righe
    matrix[i], matrix[max_riga] = matrix[max_riga], matrix[i]

    pivot = matrix[i][i]

    if pivot == 0:
        continue

    # Eliminazione
    for k in range(i + 1, n):
        fattore = matrix[k][i] / pivot
        matrix[k][i] = 0  # annullo esplicitamente

        for j in range(i + 1, n):
            matrix[k][j] -= fattore * matrix[i][j]

# Stampa risultato
for riga in matrix:
    print(riga)
