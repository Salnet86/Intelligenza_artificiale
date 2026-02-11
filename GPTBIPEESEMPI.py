# 1. INPUT: Iniziamo con la tua frase "cane sta mangiando" splitata
# Usiamo una lista di liste: ogni lista è una parola spezzettata
parole = [
    ['c', 'a', 'n', 'e'],
    ['s', 't', 'a'],
    ['m', 'a', 'n', 'g', 'i', 'a', 'n', 'd', 'o']
]

# 2. CONTEGGIO (Lo "Spiffero")
conteggio = {}

for p in parole:
    # Per ogni parola, guardiamo le coppie (i e i+1)
    for i in range(len(p) - 1):
        coppia = (p[i], p[i+1])
        if coppia in conteggio:
            conteggio[coppia] += 1
        else:
            conteggio[coppia] = 1

print("Frequenze trovate dallo spiffero:")
print(conteggio)

# 3. SELEZIONE (Cerchiamo il massimo)
coppia_regina = max(conteggio, key=conteggio.get)
frequenza_massima = conteggio[coppia_regina]

print(f"\nLa coppia che vince è {coppia_regina} con {frequenza_massima} presenze.")

# 4. MERGE (Creiamo i nuovi vettori)
nuove_parole = []
t_a, t_b = coppia_regina
nuovo_token = t_a + t_b

for p in parole:
    nuova_p = []
    i = 0
    while i < len(p):
        # Se troviamo la coppia regina, la uniamo
        if i < len(p) - 1 and p[i] == t_a and p[i+1] == t_b:
            nuova_p.append(nuovo_token)
            i += 2 # Saltiamo due elementi perché li abbiamo uniti
        else:
            nuova_p.append(p[i])
            i += 1
    nuove_parole.append(nuova_p)

print("\nRisultato dopo il primo merge:")
for p in nuove_parole:
    print(p)
