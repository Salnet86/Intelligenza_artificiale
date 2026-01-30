import random
import math

# -----------------------------
# Funzioni di attivazione
# -----------------------------
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def sigmoid_deriv(a):
    return a * (1 - a)

def tanh(x):
    return math.tanh(x)

def softmax(x):
    e = [math.exp(i) for i in x]
    s = sum(e)
    return [i / s for i in e]

# -----------------------------
# Dati di esempio
# -----------------------------
dati = {
    "tag": "salutare",
    "patterns": ['ciao', 'come', 'stai', 'ciao'],
    "response": ['bene, grazie, tutto bene']
}

# -----------------------------
# Vocabolario unico
# -----------------------------
vocabolario = list(set(dati['patterns']))

# -----------------------------
# Input utente
# -----------------------------
frase = input("Inserisci una frase: ").lower()
parole_input = frase.split()

# One-hot encoding input
sequence = []
for parola in parole_input:
    vettore = [1 if parola == w else 0 for w in vocabolario]
    sequence.append(vettore)

# -----------------------------
# Parametri feedforward
# -----------------------------
epoche = 500
rate = 0.8
neuroni_ff = 10  # neuroni feedforward

# Pesi feedforward (input -> hidden)
pesi_ff = [[random.uniform(0, 0.1) for _ in range(neuroni_ff)] for _ in range(len(vocabolario))]
bias_ff = [random.uniform(0, 0.2) for _ in range(neuroni_ff)]

# Target (per semplicità: prima parola "ciao")
target_ff = [0] * len(vocabolario)
target_ff[0] = 1

# -----------------------------
# Addestramento feedforward
# -----------------------------
output_ff = []
for ep in range(epoche):
    for i, parola in enumerate(vocabolario):
        one = [1 if j == i else 0 for j in range(len(vocabolario))]
        out_neuroni = []
        for n in range(neuroni_ff):
            z = pesi_ff[i][n] * one[i] + bias_ff[n]
            a = sigmoid(z)
            errore = a - target_ff[i]
            grad = sigmoid_deriv(a)
            pesi_ff[i][n] -= rate * errore * grad * one[i]
            bias_ff[n] -= rate * errore * grad
            out_neuroni.append(a)
        output_ff.append(out_neuroni)

# -----------------------------
# Parametri RNN
# -----------------------------
input_size = len(vocabolario)
hidden_size = 20
output_size = len(vocabolario)

Wxh = [[random.uniform(-0.1,0.1) for _ in range(input_size)] for _ in range(hidden_size)]
Whh = [[random.uniform(-0.1,0.1) for _ in range(hidden_size)] for _ in range(hidden_size)]
Why = [[random.uniform(-0.1,0.1) for _ in range(hidden_size)] for _ in range(output_size)]

bh = [0.0 for _ in range(hidden_size)]
by = [0.0 for _ in range(output_size)]

# -----------------------------
# Funzione RNN forward
# -----------------------------
def rnn_forward(sequence):
    h = [0.0 for _ in range(hidden_size)]
    for x in sequence:  # sequenza parola per parola
        h_new = []
        for i in range(hidden_size):
            s = bh[i]
            for j in range(input_size):
                s += Wxh[i][j] * x[j]
            for j in range(hidden_size):
                s += Whh[i][j] * h[j]
            h_new.append(tanh(s))
        h = h_new
    # output softmax
    y = []
    for i in range(output_size):
        s = by[i]
        for j in range(hidden_size):
            s += Why[i][j] * h[j]
        y.append(s)
    return softmax(y)

# -----------------------------
# Calcolo output RNN
# -----------------------------
output_prob = rnn_forward(sequence)
parola_scelta = vocabolario[output_prob.index(max(output_prob))]

print("Vocabolario:", vocabolario)
print("Probabilità softmax:", output_prob)
print("Parola di risposta:", parola_scelta)
