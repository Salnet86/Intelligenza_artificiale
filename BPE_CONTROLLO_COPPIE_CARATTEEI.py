stats = {}  # Il tuo dizionario delle frequenze

# Immaginiamo che 'parola' sia una lista di simboli: ['l', 'o', 'w', '</w>']
for i in range(len(parola) - 1):
    coppia = (parola[i], parola[i+1])  # Creiamo la coppia (bigramma)
    
    if coppia in stats:
        stats[coppia] += 1
    else:
        stats[coppia] = 1
