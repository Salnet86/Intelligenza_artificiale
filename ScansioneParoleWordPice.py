# --- 0. DICHIARAZIONE DELLA LISTA (Mancava!) ---
testo = "casa cane"
n = list(testo)  # n = ['c', 'a', 's', 'a', ' ', 'c', 'a', 'n', 'e']

N = len(n)  # Lunghezza totale della lista
i = 0       # Indice della posizione corrente da esaminare

# 1. Definisci la coppia target a partire dalla lista n
primo_token = n[i]
secondo_token = n[i+1]
coppia_target = (primo_token, secondo_token)

# Inizializza i contatori
conteggio_coppia = 0
conteggio_primo = 0
conteggio_secondo = 0

# 2. Scorri la lista n con un ciclo for
# Contiamo prima le frequenze dei singoli token
for token in n:
    if token == primo_token:
        conteggio_primo += 1
    if token == secondo_token:
        conteggio_secondo += 1

# Contiamo le coppie adiacenti scorrendo n fino al penultimo elemento
for j in range(len(n) - 1):
    if n[j] == primo_token and n[j+1] == secondo_token:
        conteggio_coppia += 1

# 3. Calcoli il punteggio WordPiece
if conteggio_primo * conteggio_secondo > 0:
    punteggio = (conteggio_coppia * N) / (conteggio_primo * conteggio_secondo)
else:
    punteggio = 0.0
