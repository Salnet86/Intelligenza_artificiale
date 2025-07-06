import random


bias=0.6
NumeriReuroni=2


x=[[0,0],[0,1],[1,0],[1,1]]

out = [0, 1, 1, 1]

def funzione_attivazione(somma):
    """Funzione di attivazione con soglia 1"""
    return 1 if somma >= 1 else 0
def ReteNeuralePercetrone(NumeriReuroni):

    pesi=[random.uniform(-0.2, 1.0) for _ in range(NumeriReuroni)]

    for Trane_X in x:


        somma=0

        for i in range(NumeriReuroni):

            somma+=pesi[i]*Trane_X[i]+bias

            output = funzione_attivazione(somma)
            # Stampa il risultato per l'input corrente
        print(f"Input: {Trane_X}, Somma ponderata: {somma}, Output: {output}, Target: {out[i]}")








ReteNeuralePercetrone(NumeriReuroni)
