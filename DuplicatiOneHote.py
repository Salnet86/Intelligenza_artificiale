parola = ["ciao", "ciao", "bene", "bene", "grazie","stai","stai"]
vocabolario = []

for i in range(len(parola)):
    c = 0
    
    for j in range(i + 1):
        if parola[i] == parola[j]:
            c += 1
    if c == 1:  # aggiungiamo solo la prima occorrenza
        vocabolario.append(parola[i])

# Stampiamo il risultato
for p in vocabolario:
    print(p)

