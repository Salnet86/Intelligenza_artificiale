import random
import math

# Funzione Sigmoid
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Funzione derivata Sigmoid
def sigmoid_deriv(x):
    return sigmoid(x) * (1 - sigmoid(x))

# Input utente
input_utente = input("Inserisci una frase: ").lower()
parole_input = input_utente.split()

# Dati di esempio
dati = {
    "tag": "salutare",
    "partens": ['ciao', 'come', 'stai', 'ciao'],
    "response": ['bene, grazie, tutto bene']
}

# Creazione del vocabolario unico
vocabolario = []
for parola in dati['partens']:
    if parola not in vocabolario:  # Evita duplicati
        vocabolario.append(parola)

# Creazione one-hot
one_hot = []
for parola in vocabolario:
    if parola in parole_input:  # Confronto parola per parola
        one_hot.append(1)
    else:
        one_hot.append(0)

# Parametri della rete neurale
epoche = 2
rate = 0.8
neuroni = 100

# Inizializzazione del target (qui assumiamo che vogliamo classificare correttamente una parola)
target = [0] * len(vocabolario)  # Inizializziamo un target one-hot per ogni parola
target[0] = 1  # Supponiamo che la parola corretta sia la prima (ad esempio 'ciao')

# Inizializzazione pesi e bias
pesi = [[random.uniform(0, 0.1) for _ in range(neuroni)] for _ in range(len(vocabolario))]
bias = [random.uniform(0, 0.2) for _ in range(neuroni)]

# Dizionario per memorizzare gli output per ogni parola
output_per_parola = {parola: [] for parola in vocabolario}

# Ciclo di addestramento
for iterate_epoche in range(epoche):
    for vocabolo in range(len(vocabolario)):  # Itera su ogni parola del vocabolario
        one = one_hot[vocabolo]  # One-hot per la parola corrente
        
        for n in range(neuroni):  # Per ogni neurone
            z1 = pesi[vocabolo][n] * one + bias[n]  # Calcolo del valore z1
            a1 = sigmoid(z1)  # Attivazione con sigmoid
            
            # Calcolo dell'errore (target vs output)
            errore = a1 - target[vocabolo]
            
            # Derivata della funzione sigmoide
            derivata_sigmoid = sigmoid_deriv(a1)

            # Aggiornamento dei pesi
            pesi[vocabolo][n] -= rate * errore * derivata_sigmoid * one

            # Aggiornamento dei bias
            bias[n] -= rate * errore * derivata_sigmoid
            
            # Salvataggio dell'output per ciascuna parola
            output_per_parola[vocabolario[vocabolo]].append(a1)

# Stampa finale per verificare gli output per ogni parola
for outputs in output_per_parola.items():
    print(f"Output finali (attivazioni): {outputs}")
