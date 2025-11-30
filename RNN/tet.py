# Vocabolario
vocabolario = ["ciao", "come", "stai"]

# Dizionario output per parola
output_per_parola = {parola: [] for parola in vocabolario}

# Simuliamo le attivazioni dei neuroni (ad esempio 3 neuroni)
attivazioni = [
    [0.52, 0.48, 0.55],  # "ciao"
    [0.43, 0.50, 0.47],  # "come"
    [0.60, 0.58, 0.59]   # "stai"
]

# Ciclo sulle parole e sui neuroni
for vocabolo in range(len(vocabolario)):
    parola = vocabolario[vocabolo]  # parola corrente
    for a1 in attivazioni[vocabolo]:  # simuliamo output di ciascun neurone
        output_per_parola[parola].append(a1)  # append dell'attivazione

# Verifica
for parola, outputs in output_per_parola.items():
    print(parola, outputs)
