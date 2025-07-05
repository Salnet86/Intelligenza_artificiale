# Vocabolario
vocab = ["accendi", "la", "luce", "spento", "spegni"]

# Frase utente
frase = input("Scrivi una frase: ").lower()
parole = frase.split()

# Vettore one-hot
convert = []
for parola in vocab:
    if parola in parole:
        convert.append(1)
    else:
        convert.append(0)

print("Vettore one-hot:", convert)

# Pesi e bias per un solo neurone
pesi = [0.9, 0.8, 0.7, 0.1, -0.9]  # esempio pesi
bias = 0.0

# Calcolo output neurone
somma = 0
for i in range(len(convert)):
    somma += convert[i] * pesi[i]
somma += bias

print(f"Output neurone: {somma:.2f}")

# Soglia per decidere la classe
soglia = 0.5

if somma >= soglia:
    print("Risposta: accendi_luce")
else:
    print("Risposta: spegni_luce")
