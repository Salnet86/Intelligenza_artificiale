# 1. TESTO DI PARTENZA E TOKENIZZAZIONE INIZIALE
testo = "ciao ciao"

# Dividiamo il testo in singoli caratteri e aggiungiamo il marcatore di fine parola '</w>'
# (Usiamo .split() per separare le parole e poi le scomponiamo)
parole = testo.split(" ")
vettore_token = []

for parola in parole:
  # Trasformiamo la parola in lista di lettere e aggiungiamo '</w>' alla fine
  lettere = list(parola)
  lettere.append("</w>")
  vettore_token.extend(lettere)

print("Inizio (caratteri separati):", vettore_token)


# 2. CICLO DI FUSIONE (BPE) - Facciamo un giro di prova
# Creiamo il dizionario per contare le frequenze delle coppie adiacenti
frequenza = {}

# Scorriamo la lista fino al penultimo elemento
for i in range(len(vettore_token) - 1):
  coppia = (vettore_token[i], vettore_token[i + 1])

  # Contiamo la frequenza usando 'not in' o '.get()'
  if coppia not in frequenza:
    frequenza[coppia] = 1
  else:
    frequenza[coppia] += 1

print("\nFrequenza delle coppie:", frequenza)


# 3. TROVARE LA COPPIA CON IL MASSIMO VALORE
max_frequenza = 0
migliore_coppia = None

for coppia in frequenza:
  if frequenza[coppia] > max_frequenza:
    max_frequenza = frequenza[coppia]
    migliore_coppia = coppia

print("\nLa coppia più frequente è:", migliore_coppia)


# 4. CREARE IL NUOVO TOKEN E AGGIORNARE IL VOCABOLARIO
vocabolario = []

if migliore_coppia is not None:
  # Uniamo i due elementi della coppia per formare un nuovo token
  nuovo_token = migliore_coppia[0] + migliore_coppia[1]
  
  # Aggiungiamo il nuovo pezzo al vocabolario
  vocabolario.append(nuovo_token)
  
  print(f"\nNuovo token aggiunto al vocabolario: {nuovo_token}")
  print("Vocabolario attuale:", vocabolario)
