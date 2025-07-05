# Vocabolario
vocab = ["accendi", "la", "luce", "spento", "spegni"]

# Frasi predefinite
frasi_target = {
    "accendi_luce": ["accendi", "la", "luce"],
    "spegni_luce": ["spegni", "la", "luce"]
}

# Frase utente → input + one-hot
frase = input("Scrivi una frase: ").lower()
parole = frase.split()

convert = []
for parola in vocab:
    if parola in parole:
        convert.append(1)
    else:
        convert.append(0)

print("Vettore one-hot:", convert)

# --- Rete neurale semplice (percettrone) ---

# Pesi fissi per 2 neuroni (accendi_luce, spegni_luce)
pesi = [
    [0.9, 0.8, 0.7, 0.1, 0.0],  # Neurone accendi_luce
    [0.1, 0.8, 0.7, 0.0, 0.9]   # Neurone spegni_luce
]
bias = [0.1, 0.1]

output = []

for i in range(2):  # 2 neuroni
    somma = 0
    for j in range(len(convert)):
        somma += convert[j] * pesi[i][j]
    somma += bias[i]
    output.append(somma)

print("\nOutput dei neuroni:", output)

# Risposta basata sul neurone con output più alto
if output[0] > output[1]:
    print("Risposta percettrone: accendi_luce")
else:
    print("Risposta percettrone: spegni_luce")
