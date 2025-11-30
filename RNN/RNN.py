import random
import math

# -----------------------------
# Funzioni
# -----------------------------
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def sigmoid_deriv_from_activation(a):
    return a * (1 - a)

def softmax(x):
    e_x = [math.exp(i) for i in x]
    somma = sum(e_x)
    return [i / somma for i in e_x]

# -----------------------------
# Input utente
# -----------------------------
input_utente = input("Inserisci una frase: ").lower()
parole_input = input_utente.split()

dati = {
    "tag": "salutare",
    "partens": ['ciao', 'come', 'stai', 'ciao'],
    "response": ['bene, grazie, tutto bene']
}

# Vocabolario unico
vocabolario = []
for parola in dati['partens']:
    if parola not in vocabolario:
        vocabolario.append(parola)

# One-hot encoding
one_hot = [1 if parola in parole_input else 0 for parola in vocabolario]

# -----------------------------
# Parametri rete
# -----------------------------
epoche = 500
rate = 0.8
neuroni = 100  # neuroni dello stato nascosto

# Target (esempio)
target = [0] * len(vocabolario)
target[0] = 1

# Pesi feedforward
pesi = [[random.uniform(0, 0.1) for _ in range(neuroni)] for _ in range(len(vocabolario))]
bias = [random.uniform(0, 0.2) for _ in range(neuroni)]

output_per_parola = {parola: [] for parola in vocabolario}
Out_RNN = []

# -----------------------------
# Addestramento feedforward
# -----------------------------
for iterate_epoche in range(epoche):
    for vocabolo in range(len(vocabolario)):
        one = one_hot[vocabolo]
        for n in range(neuroni):
            z1 = pesi[vocabolo][n] * one + bias[n]
            a1 = sigmoid(z1)
            errore = a1 - target[vocabolo]
            derivata_sigmoid = sigmoid_deriv_from_activation(a1)

            pesi[vocabolo][n] -= rate * errore * derivata_sigmoid * one
            bias[n] -= rate * errore * derivata_sigmoid

            output_per_parola[vocabolario[vocabolo]].append(a1)

        Out_RNN.append(sum(output_per_parola[vocabolario[vocabolo]]) / len(output_per_parola[vocabolario[vocabolo]]))

# -----------------------------
# Inizializzazione RNN
# -----------------------------
WT = [random.uniform(0, 0.2) for _ in range(neuroni)]
WH = [random.uniform(0, 0.2) for _ in range(neuroni)]
bias_t = [random.uniform(0, 0.2) for _ in range(neuroni)]
hidden_state = [0.0 for _ in range(neuroni)]

# Layer di output che mappa hidden_state al vocabolario
W_out = [[random.uniform(0, 0.2) for _ in range(neuroni)] for _ in range(len(vocabolario))]
b_out = [random.uniform(0, 0.2) for _ in range(len(vocabolario))]

# -----------------------------
# Funzione RNN
# -----------------------------
def RNN(Out_RNN, hidden_state):
    nuovo_hidden = []
    for n in range(neuroni):
        somma = 0.0
        for i in range(len(Out_RNN)):
            somma += math.tanh(WT[n] * Out_RNN[i] + WH[n] * hidden_state[n] + bias_t[n])
        nuovo_hidden.append(somma / len(Out_RNN))
    return nuovo_hidden

# -----------------------------
# Aggiornamento RNN
# -----------------------------
hidden_state = RNN(Out_RNN, hidden_state)
print("Stato RNN finale (primi 10 neuroni):", hidden_state[:10], "...")

# -----------------------------
# Calcolo output sul vocabolario
# -----------------------------
logits = []
for j in range(len(vocabolario)):
    somma = 0.0
    for i in range(neuroni):
        somma += hidden_state[i] * W_out[j][i]
    logits.append(somma + b_out[j])

# Softmax per probabilità
output_prob = softmax(logits)
print("Probabilità softmax:", output_prob)

# Scelta parola più probabile
parola_scelta = vocabolario[output_prob.index(max(output_prob))]
print("Parola di risposta:", parola_scelta)
