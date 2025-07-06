import random

bias = 0.6
NumeriReuroni = 2
learning_rate = 0.1  # Tasso di apprendimento

x = [[0, 0], [0, 1], [1, 0], [1, 1]]
out = [0, 1, 1, 1]  # Gli output desiderati

def funzione_attivazione(somma):
    """Funzione di attivazione con soglia 1"""
    return 1 if somma >= 1 else 0

def ReteNeuralePercetrone(NumeriReuroni, learning_rate, epoche):

    # Inizializza i pesi casualmente
    pesi = [random.uniform(-0.2, 1.0) for _ in range(NumeriReuroni)]
    current_bias = bias  # Bias iniziale

    print(f"Pesi iniziali: {pesi}, Bias iniziale: {current_bias}\n")

    # Ciclo di addestramento per un numero di epoche
    for epoca in range(epoche):  # Esegui per il numero di epoche specificato
        print(f"--- Epoca {epoca + 1} ---")
        errori_in_epoca = 0

        # Itera su ogni esempio di input nel set di addestramento
        for idx, Trane_X in enumerate(x):
            somma = 0
            # Calcola la somma pesata degli input
            for i in range(NumeriReuroni):
                somma += pesi[i] * Trane_X[i]
            somma += current_bias  # Aggiungi il bias

            # Ottieni l'output dal percettrone
            output_previsto = funzione_attivazione(somma)

            # Ottieni l'output desiderato per l'input corrente
            target = out[idx]

            # Calcola l'errore
            errore = target - output_previsto

            # Se c'è un errore, aggiorna i pesi e il bias
            if errore != 0:
                errori_in_epoca += 1
                for i in range(NumeriReuroni):
                    pesi[i] += learning_rate * errore * Trane_X[i]
                current_bias += learning_rate * errore

            # Stampa i risultati per l'input corrente
            print(f"  Input: {Trane_X}, Target: {target}, Previsto: {output_previsto}, Errore: {errore}, Bias: {current_bias}")

        print(f"  Pesi dopo Epoca {epoca + 1}: {pesi}, Bias: {current_bias}")
        print(f"  Errori in questa epoca: {errori_in_epoca}\n")

        # Se non ci sono stati errori in questa epoca, il percettrone ha imparato
        if errori_in_epoca == 0:
            print("Il percettrone ha imparato! Nessun errore in questa epoca.")
            break  # Esci dal ciclo di addestramento

    print("\n--- Addestramento completato ---")
    print(f"Pesi finali: {pesi}, Bias finale: {current_bias}")

# Esegui il percettrone con addestramento
ReteNeuralePercetrone(NumeriReuroni, learning_rate, epoche=10)
