# Scegliamo la dimensione della matrice
n = 4

# Creiamo una matrice 4x4 di numeri reali di esempio
matrice = [
    [2,  1,  1,  3],
    [4,  8,  3,  2],
    [2,  3,  7,  1],
    [6,  5,  2,  9]
]

print("--- MATRICE DI PARTENZA ---")
for riga in matrice:
    print(riga)

print("\n--- INIZIO ELABORAZIONE ---")

for i in range(n):
    # 1. Prendiamo il pivot sulla diagonale principale
    pivot = matrice[i][i]
    print(f"\n--> Analizzo la riga {i}, il pivot sulla diagonale è: {pivot} (in pos [{i}][{i}])")
    
    # Controllo di sicurezza per evitare divisioni per zero
    if pivot == 0:
        continue
    
    for j in range(n):
        if j <= i:
            # Qui ci troviamo sulla diagonale (se j == i) o sopra (se j < i)
            # Questi valori non vengono toccati in questa fase
            pass
        else:
            # Qui ci troviamo sotto la diagonale (j > i)
            # 2. Calcoliamo il fattore di moltiplicazione per azzerare l'elemento
            fattore = matrice[j][i] / pivot
            print(f"   Posizione [{j}][{i}]: j > i -> Azzero calcolando il fattore {fattore}")
            
            # 3. Azzeriamo formalmente l'elemento corrente
            matrice[j][i] = 0
            
            # 4. Aggiorniamo tutta la riga j scorrendo le colonne successive (k)
            for k in range(i + 1, n):
                matrice[j][k] = matrice[j][k] - fattore * matrice[i][k]

print("\n--- MATRICE FINALE (TRIANGOLARE SUPERIORE) ---")
for riga in matrice:
    print(riga)
