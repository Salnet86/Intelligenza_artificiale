import random

bias = 0.6
NumeroNeuroni = 2
currente_bias = 0
epoche = 10
learning_rate = 0.1

def funzioneAttivazione(somma):

    return 1 if somma >= 1 else 0

def ReteNeuronale(NumeroNeuroni, epoche, bias):
    currente_bias = bias
    x = [[0, 0], [0, 1], [1, 0], [1, 1]]
    target = [0, 0, 0, 1]
    pesi = [random.uniform(-0.1, 0.5) for _ in range(NumeroNeuroni)]

    for epoca in range(epoche):
        print(f"\nEpoca {epoca+1}")
        for Trane_x in range(len(x)):
            somma = 0
            for i in range(NumeroNeuroni):
                somma += pesi[i] * x[Trane_x][i]
            somma += currente_bias
            output_previsto = funzioneAttivazione(somma)
            errore=target[Trane_x] - output_previsto


            # Aggiorna i pesi e il bias
            for i in range(NumeroNeuroni):
                pesi[i] += learning_rate * errore * x[Trane_x][i]  # Aggiorna ciascun peso
            currente_bias += learning_rate * errore
            # Stampo informazioni per vedere come cambiano
            print(f"Input: {x[Trane_x]}, Target: {target[Trane_x]}, Output previsto: {output_previsto}")
            print(f"Errore: {errore}")
           # print(f"Pesi aggiornati: {pesi}")
           # print(f"Bias aggiornato: {currente_bias}\n")




ReteNeuronale(NumeroNeuroni, epoche, bias)
