testo = "il gatto e il cane"
parole = testo.split()

# 1. Calcolo frequenze (solo ciclo for e if/else)
frequenze = {}
for parola in parole:
    if parola in frequenze:
        frequenze[parola] += 1
    else:
        frequenze[parola] = 1

# 2. Formattazione con '##' per WordPiece (solo cicli for e if/else)
vocabolario = {}

for parola, freq in frequenze.items():
    lettere_formattate = []
    
    # Usiamo un ciclo for con indice per sapere qual è la prima lettera
    for i in range(len(parola)):
        if i == 0:
            # La prima lettera resta normale
            lettere_formattate.append(parola[i])
        else:
            # Dalla seconda lettera in poi aggiungiamo '##'
            lettere_formattate.append("##" + parola[i])
    
    # Uniamo le lettere formattate con uno spazio
    parola_separata = " ".join(lettere_formattate)
    
    # Salviamo nel dizionario
    vocabolario[parola_separata] = freq

print(vocabolario)
