#Lezione WordSpice AI ML Conteggio coppie parole 
# 1. Definisci la coppia unita
vopoia = n[i] + n[i+1]

# 2. Recuperi i conteggi globali dal testo
conteggio_coppia = testo.count(vopoia)
conteggio_primo = testo.count(n[i])
conteggio_secondo = testo.count(n[i+1])

# 3. Calcoli il punteggio WordPiece
punteggio = (conteggio_coppia * N) / (conteggio_primo * conteggio_secondo)
