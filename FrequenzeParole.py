testo = "il gatto e il cane"
parole = testo.split()

# 1. Calcola le frequenze delle parole (come hai fatto tu, ma con un dizionario sintetico)
frequenze_parole = {}
for parola in parole:
    frequenze_parole[parola] = frequenze_parole.get(parola, 0) + 1

# 2. Prepara il vocabolario iniziale diviso in caratteri con il prefisso '##' per WordPiece
# "gatto" -> "g ##a ##t ##t ##o"
vocabolario_parole = {}
for parola, freq in frequenze_parole.items():
    # Il primo carattere rimane normale, i successivi prendono '##'
    caratteri = [parola[0]] + [f"##{c}" for c in parola[1:]]
    vocabolario_parole[" ".join(caratteri)] = freq

print("Frequenze parole iniziali per WordPiece:")
print(vocabolario_parole)
# Output: {'i ##l': 2, 'g ##a ##t ##t ##o': 1, 'e': 1, 'c ##a ##n ##e': 1}
