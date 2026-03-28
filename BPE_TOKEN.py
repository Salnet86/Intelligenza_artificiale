# Il nostro punto di partenza
vocabolario = {
    'l o w </w>': 5,
    'l o w e r </w>': 2,
    'n e w e s t </w>': 6,
    'w i d e s t </w>': 3
}

stats = {} # Il tuo dizionario delle frequenze

# 1. Ciclo su ogni parola nel vocabolario
for parola in vocabolario:
    frequenza = vocabolario[parola] # Quante volte appare quella parola
    simboli = parola.split()       # Dividiamo la stringa in una lista di caratteri
    
    # 2. Il tuo ciclo for per le coppie (all'interno di ogni parola)
    for i in range(len(simboli) - 1):
        coppia = (simboli[i], simboli[i+1])
        
        # 3. La tua logica if/else per aggiornare il conteggio
        if coppia in stats:
            stats[coppia] += frequenza
        else:
            stats[coppia] = frequenza

# Visualizziamo i risultati
print(stats)
