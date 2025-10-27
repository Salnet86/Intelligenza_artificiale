INPUT = "come stai"
input_words = INPUT.strip().split()
parola = "ciao come stai ciao buona giornata buona in fatti".strip().split()

vettore = []
vocabolario = []
One_Hot = []

# 1️⃣ Aggiungiamo tutte le parole a vettore
for i in range(len(parola)):
    vettore.append(parola[i])

# 2️⃣ Creiamo il vocabolario contando le parole
for i in range(len(vettore)):
    count = 0
    for j in range(len(vocabolario)):
        if vettore[i] == vocabolario[j]:
            count += 1
    if count == 0:
        vocabolario.append(vettore[i])

# 3️⃣ Creiamo il vettore One-Hot
for i in range(len(vocabolario)):
    Parole = False
    for j in range(len(input_words)):
        if vocabolario[i] == input_words[j]:
            Parole = True
    if Parole:
        One_Hot.append(1)
    else:
        One_Hot.append(0)

print("Vocabolario:", vocabolario)
print("One-Hot:", One_Hot)
