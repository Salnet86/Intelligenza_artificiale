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
neuroni = 100 # neuroni dello stato nascosto

# Target (esempio)
target = [0] * len(vocabolario)
target[0] = 1

# Pesi feedforward
pesi = [[random.uniform(0, 0.1) for _ in range(neuroni)] for _ in range(len(vocabolario))]
bias = [random.uniform(0, 0.2) for _ in range(neuroni)]
output_per_parola = {parola: [] for parola in vocabolario}
Out_RNN = []

# -----------------------------
# Addestramento feedforward (Non modificato, genera Out_RNN)
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
        
        # Aggiornamento Out_RNN solo una volta per epoca
        if iterate_epoche == epoche - 1:
             output_per_parola[vocabolario[vocabolo]].append(a1)
             
for vocabolo in vocabolario:
    # Calcola la media finale dell'attivazione per ogni parola, che diventa l'input per l'RNN
    Out_RNN.append(sum(output_per_parola[vocabolo]) / len(output_per_parola[vocabolo]))


# -----------------------------
# Inizializzazione RNN
# -----------------------------
WT = [random.uniform(0, 0.2) for _ in range(neuroni)] # Pesi per l'input corrente x_t
WH = [random.uniform(0, 0.2) for _ in range(neuroni)] # Pesi per lo stato nascosto precedente h_{t-1}
bias_t = [random.uniform(0, 0.2) for _ in range(neuroni)]
hidden_state = [0.0 for _ in range(neuroni)] # Stato iniziale h_0

# Layer di output che mappa hidden_state al vocabolario
W_out = [[random.uniform(0, 0.2) for _ in range(neuroni)] for _ in range(len(vocabolario))]
b_out = [random.uniform(0, 0.2) for _ in range(len(vocabolario))]

# -----------------------------
# Funzione RNN con CICLO TEMPORALE (MODIFICATA) 🔄
# -----------------------------
def RNN_sequenziale(sequenza_input, hidden_state_iniziale):
    """Elabora la sequenza input un elemento alla volta, aggiornando lo stato nascosto."""
    
    # h_corrente è lo stato h_{t-1}
    h_corrente = list(hidden_state_iniziale)
    
    # Per ogni elemento della sequenza (x_t)
    for x_t in sequenza_input:
        
        nuovo_hidden_t = [0.0] * neuroni # Sarà il nuovo stato h_t
        
        for n in range(neuroni):
            # Equazione RNN standard per un neurone (usando tanh come attivazione):
            # h_t = tanh( W_T * x_t + W_H * h_{t-1} + bias_t )
            
            # W_T * x_t: Pesi per l'input corrente
            # W_H * h_corrente[n]: Pesi per lo stato precedente
            somma_attivazione = WT[n] * x_t + WH[n] * h_corrente[n] + bias_t[n]
            
            nuovo_hidden_t[n] = math.tanh(somma_attivazione)
            
        # AGGIORNAMENTO ESSENZIALE: h_t diventa h_{t-1} per il passo successivo
        h_corrente = nuovo_hidden_t
        
    # Restituisce l'ultimo stato nascosto (la memoria di tutta la sequenza)
    return h_corrente 

# -----------------------------
# Aggiornamento RNN (MODIFICATO)
# -----------------------------
# Chiamiamo la funzione che esegue l'unrolling nel tempo
hidden_state_finale = RNN_sequenziale(Out_RNN, hidden_state)

print("Stato RNN finale (primi 10 neuroni):", hidden_state_finale[:10], "...")
print(f"La sequenza è stata elaborata in {len(Out_RNN)} passi temporali.")

# -----------------------------
# Calcolo output sul vocabolario (USA LO STATO FINALE)
# -----------------------------
logits = []
for j in range(len(vocabolario)):
    somma = 0.0
    for i in range(neuroni):
        # Utilizziamo lo stato finale come input per il layer di output
        somma += hidden_state_finale[i] * W_out[j][i]
    logits.append(somma + b_out[j])

# Softmax per probabilità
output_prob = softmax(logits)
print("Probabilità softmax:", output_prob)

# Scelta parola più probabile
parola_scelta = vocabolario[output_prob.index(max(output_prob))]
print("Parola di risposta:", parola_scelta)
