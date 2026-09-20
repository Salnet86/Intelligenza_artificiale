# --- PARTE 1: La tua preparazione del vocabolario iniziale ---
testo = "il gatto e il cane"
parole = testo.split()

frequenze = {}
for parola in parole:
    if parola in frequenze:
        frequenze[parola] += 1
    else:
        frequenze[parola] = 1

vocabolario = {}
for parola, freq in frequenze.items():
    lettere = []
    for i in range(len(parola)):
        if i == 0:
            lettere.append(parola[i])
        else:
            lettere.append("##" + parola[i])
    vocabolario[" ".join(lettere)] = freq


# --- PARTE 2: Dove va la FORMULA ---

# 1. Calcoliamo le frequenze di ogni singolo token (es. "i", "##l", "g", ...)
freq_elementi = {}
for parola_divisa, freq in vocabolario.items():
    tokens = parola_divisa.split()
    for t in tokens:
        if t in freq_elementi:
            freq_elementi[t] += freq
        else:
            freq_elementi[t] = freq

# 2. Calcoliamo le frequenze delle coppie vicine (es. ("i", "##l"))
freq_coppie = {}
for parola_divisa, freq in vocabolario.items():
    tokens = parola_divisa.split()
    for i in range(len(tokens) - 1):
        coppia = (tokens[i], tokens[i+1])
        if coppia in freq_coppie:
            freq_coppie[coppia] += freq
        else:
            freq_coppie[coppia] = freq

# 3. QUI APPLICHIAMO LA FORMULA DI WORDPIECE PER OGNI COPPIA
# Punteggio = Freq(A, B) / (Freq(A) * Freq(B))
punteggi = {}
for coppia, freq_coppia in freq_coppie.items():
    elemento_A = coppia[0]
    elemento_B = coppia[1]
    
    freq_A = freq_elementi[elemento_A]
    freq_B = freq_elementi[elemento_B]
    
    # Ecco la formula:
    punteggio = freq_coppia / (freq_A * freq_B)
    punteggi[coppia] = punteggio

# 4. Troviamo la coppia con il punteggio più alto
coppia_migliore = None
punteggio_massimo = -1

for coppia, punteggio in punteggi.items():
    if punteggio > punteggio_massimo:
        punteggio_massimo = punteggio
        coppia_migliore = coppia

print("Punteggi di tutte le coppie:")
for coppia, p in punteggi.items():
    print(coppia, "->", p)

print("\nCoppia scelta per la fusione:", coppia_migliore)
