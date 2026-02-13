A = [
    [2, 4, -2],
    [4, 9, -3],
    [-2, -3, 7]
]

n = len(A)

for p in range(n):
    # Controllo e scambio se il pivot è zero
    if A[p][p] == 0:
        for s in range(p + 1, n):
            if A[s][p] != 0:
                A[p], A[s] = A[s], A[p]
                break
    
    pivot = A[p][p]
    
    # Se dopo lo scambio è ancora zero, la matrice non è risolvibile
    if pivot != 0:
        for j in range(p, n):
            A[p][j] = A[p][j] / pivot
            
        for i in range(n):
            if i != p:
                fattore = A[i][p]
                for j in range(p, n):
                    A[i][j] = A[i][j] - (fattore * A[p][j])

print("Matrice finale:")
for riga in A:
    print(riga)
