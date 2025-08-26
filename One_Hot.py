# input utente
input_utente = input("Inserisci una frase: ").lower()
parole_input = input_utente.split()

dati = {
    "tag": "salutare",
    "partens": ['ciao', 'come', 'stai', 'ciao'],
    "response": ['bene, grazie, tutto bene']
}

vocabolario = []
one_hot = []

# costruzione vocabolario unico
for parola in dati['partens']:
    if parola not in vocabolario:  # evita duplicati
        vocabolario.append(parola)

# costruzione one-hot
for parola in vocabolario:
    if parola in parole_input:  # confronto parola per parola
        one_hot.append(1)

    else:
        one_hot.append(0)


print("Vocabolario:", vocabolario)
print("One-hot:", one_hot)
