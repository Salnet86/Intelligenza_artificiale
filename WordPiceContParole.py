# WordSpice conteggio coppie patole 

# 1. Definisci la coppia target
primo_token = n[i]
secondo_token = n[i+1]
coppia_target = (primo_token, secondo_token)

# Inizializza i contatori
conteggio_coppia = 0
conteggio_primo = 0
conteggio_secondo = 0

# 2. Scorri la lista dei token con un ciclo for
# Contiamo prima le frequenze dei singoli token
for token in lista_token:
    if token == primo_token:
        conteggio_primo += 1
    if token == secondo_token:
        conteggio_secondo += 1

# Contiamo le coppie adiacenti scorrendo fino al penultimo elemento
for j in range(len(lista_token) - 1):
    if lista_token[j] == primo_token and lista_token[j+1] == secondo_token:
        conteggio_coppia += 1

# 3. Calcoli il punteggio WordPiece (gestendo la divisione per zero)
if conteggio_primo * conteggio_secondo > 0:
    punteggio = (conteggio_coppia * N) / (conteggio_primo * conteggio_secondo)
else:
    punteggio = 0.0
