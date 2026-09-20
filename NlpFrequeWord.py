parole = "il gatto e il cane"
parole = testo.split() # Separa direttamente per spazi: ["il", "gatto", "e", "il", "cane"]

frequenze = {}
for parola in parole:
    if parola in frequenze:
        frequenze[parola] += 1
    else:
        frequenze[parola] = 1
