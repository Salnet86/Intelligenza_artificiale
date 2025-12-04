# ====================================================================
# Propagazione in Avanti (Forward Pass) per un singolo Strato Nascosto
# (Senza librerie, usando Python "puro")
# ====================================================================


# 1. PARAMETRI E INPUT
# --------------------
X = 0.5 # Input scalare
W = [0.2, -0.6, 0.9] # Vettore dei 3 Pesi
B = [0.1, 0.5, -0.3] # Vettore dei 3 Bias


# 2. STRUTTURA DI OUTPUT
# -----------------------
output_attivato = []


# 3. FUNZIONE DI ATTIVAZIONE (ReLU)
# ---------------------------------
def relu(z):
    """Funzione di Attivazione ReLU: max(0, z)"""
    return max(0, z)


# 4. CALCOLO DELLA PROPAGAZIONE (con ciclo for)
# ----------------------------------------------
# Il ciclo esegue il calcolo per ogni neurone J
for j in range(len(W)):
    # Recupero i parametri specifici del neurone corrente
    peso_j = W[j]
    bias_j = B[j]
    
    # Calcolo della Somma Pesata (z_j)
    # z_j = X * W_j + b_j
    somma_pesata_z = X * peso_j + bias_j
    
    # Applicazione della Funzione di Attivazione (h_j)
    attivazione_h = relu(somma_pesata_z)
    
    # Aggiunge il risultato al vettore di output
    output_attivato.append(attivazione_h)


# 5. STAMPA DEL RISULTATO FINALE
# ---------------------------------
print(f"Input (X): {X}")
print(f"Pesi (W): {W}")
print(f"Bias (B): {B}")
print("---")
print(f"Vettore di output dello Strato Nascosto (H): {output_attivato}")
# ====================================================================

