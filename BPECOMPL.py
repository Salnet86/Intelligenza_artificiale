import collections

# Testo di esempio
testo_addestramento = "ciao gatto come stai gatto mangia"

# Numero di merge BPE
num_merge = 10

# 1️⃣ Dividiamo il testo in parole
parole = testo_addestramento.split()

# 2️⃣ Ogni parola diventa lista di caratteri + token di fine parola
vocab = [list(parola) + ["</w>"] for parola in parole]

# 3️⃣ Ciclo principale BPE
for _ in range(num_merge):
    
    # Conteggio coppie adiacenti
    coppie = collections.defaultdict(int)
    
    for parola in vocab:
        for i in range(len(parola) - 1):
            coppie[(parola[i], parola[i+1])] += 1
    
    # Se non ci sono più coppie interrompiamo
    if not coppie:
        break
    
    # Troviamo la coppia più frequente
    coppia_vincente = max(coppie, key=coppie.get)
    
    # Creiamo il nuovo vocabolario fondendo la coppia vincente
    nuovo_vocab = []
    
    for parola in vocab:
        nuova_parola = []
        i = 0
        
        while i < len(parola):
            
            # Se troviamo la coppia da fondere
            if (i < len(parola) - 1 and
                (parola[i], parola[i+1]) == coppia_vincente):
                
                nuova_parola.append(parola[i] + parola[i+1])
                i += 2
            else:
                nuova_parola.append(parola[i])
                i += 1
        
        nuovo_vocab.append(nuova_parola)
    
    vocab = nuovo_vocab

# 4️⃣ Creiamo il vocabolario finale token → ID
token_unici = sorted(set(token for parola in vocab for token in parola))
vocabolario = {token: idx for idx, token in enumerate(token_unici)}

print(vocabolario)
