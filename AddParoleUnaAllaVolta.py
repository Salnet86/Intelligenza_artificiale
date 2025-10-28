parola = ["ciao", "ciao", "bene", "bene", "grazie"]
vocabolario = []

for i in range(len(parola)):
    aggiungi = True
    for j in range(len(vocabolario)):
        if parola[i] == vocabolario[j]:
            aggiungi = False
            break
    if aggiungi:
        vocabolario.append(parola[i])

# Stampiamo le parole una sola volta
for p in vocabolario:
    print(p)
