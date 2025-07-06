import random

bias = 0.6
NumeriReuroni = 2 # Questo si riferisce al numero di input per il percettrone

x = [[0, 0], [0, 1], [1, 0], [1, 1]]
out = [0, 1, 1, 1]  # Questi sono i tuoi output desiderati

def funzione_attivazione(somma):
    """Funzione di attivazione con soglia 1"""
    return 1 if somma >= 1 else 0

def ReteNeuralePercetrone(NumeriReuroni, learning_rate=0.1, epoche=10):
    # Inizializza i pesi casualmente e il bias
    pesi = [random.uniform(-0.2, 1.0) for _ in range(NumeriReuroni)]
    current_bias = bias # Usiamo una variabile separata per il bias che si aggiorna

    print(f"Pesi iniziali: {pesi}, Bias iniziale: {current_bias}\n")

    # Ciclo di addestramento
    for epoca in range(epoche):
        print(f"--- Epoca {epoca + 1}/{epoche} ---")
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
            print(f"  Input: {Trane_X}, Target: {target}, Previsto: {output_previsto}, Errore: {errore}")

        print(f"  Pesi dopo Epoca {epoca + 1}: {pesi}, Bias: {current_bias}")
        print(f"  Errori in questa epoca: {errori_in_epoca}\n")

        # Se non ci sono stati errori in questa epoca, il percettrone ha imparato
        if errori_in_epoca == 0:
            print("Il percettrone ha imparato! Nessun errore in questa epoca.")
            break # Esci dal ciclo di addestramento

    print("\n--- Addestramento completato ---")
    print(f"Pesi finali: {pesi}, Bias finale: {current_bias}")

    # Testiamo il percettrone addestrato
    print("\n--- Test del percettrone addestrato ---")
    for Trane_X in x:
        somma = 0
        for i in range(NumeriReuroni):
            somma += pesi[i] * Trane_X[i]
        somma += current_bias
        output_finale = funzione_attivazione(somma)
        print(f"Input: {Trane_X}, Output Previsto: {output_finale}")


# Esegui il percettrone con addestramento
# Puoi regolare learning_rate e epoche per vedere come influenzano l'apprendimento
ReteNeuralePercetrone(NumeriReuroni, learning_rate=0.1, epoche=20)
