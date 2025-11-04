# ============================================================
# POLITECNICO DI TORINO
# Autore: Salvatore Brezza
# Stage: Logistica Automatica
# Progetto: Mini rete neurale per analisi temperature sistema
# ============================================================

import psutil as ps
import pandas as pd
import random
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# 1. RACCOLTA DATI TEMPERATURA
# ------------------------------------------------------------
temperatura = ps.sensors_temperatures()
dati = []

for te, item in temperatura.items():
    for dati_sensore in item:
        dati.append({
            "sensore": te,
            "etichetta": dati_sensore.label or "N/A",
            "corrente (°C)": dati_sensore.current,
            "massima (°C)": dati_sensore.high,
            "critica (°C)": dati_sensore.critical
        })

df_temp = pd.DataFrame(dati)

# ------------------------------------------------------------
# 2. PREPARAZIONE E NORMALIZZAZIONE DATI
# ------------------------------------------------------------
dati_rete = []
for colonna in ['corrente (°C)', 'massima (°C)', 'critica (°C)']:
    if colonna in df_temp.columns:
        dati_rete.extend(df_temp[colonna].dropna().tolist())

# Normalizzazione (divido per 100)
x = [val / 100 for val in dati_rete]

# ------------------------------------------------------------
# 3. DEFINIZIONE PARAMETRI RETE NEURALE
# ------------------------------------------------------------
neuroni = 2
epoche = 100
rate = 0.0001
target = 1.0

# Pesi e bias inizializzati una sola volta
H1 = [random.uniform(0, 0.1) for _ in range(neuroni)]  # pesi layer nascosto
B1 = [random.uniform(0, 0.2) for _ in range(neuroni)]  # bias layer nascosto
W_out = [random.uniform(0, 0.3) for _ in range(neuroni)]  # pesi verso output
B_out = random.uniform(0, 0.2)

# Funzioni di attivazione
def relu(x):
    return max(0, x)

def relu_derivative(x):
    return 1 if x > 0 else 0

# ------------------------------------------------------------
# 4. ADDDESTRAMENTO (TRAINING)
# ------------------------------------------------------------
dati_training = []

for i in range(epoche):
    for dati_input in x:
        # Forward pass
        a1 = []
        for j in range(neuroni):
            z1 = H1[j] * dati_input + B1[j]
            a1.append(relu(z1))

        out = sum(W_out[j] * a1[j] for j in range(neuroni)) + B_out
        errore = 0.5 * (target - out) ** 2

        # Backpropagation
        delta_out = (target - out)

        for j in range(neuroni):
            delta_h = delta_out * W_out[j] * relu_derivative(a1[j])
            # Aggiornamento pesi
            W_out[j] += rate * delta_out * a1[j]
            H1[j] += rate * delta_h * dati_input
            B1[j] += rate * delta_h

        B_out += rate * delta_out

    # Salvo media errore e output per l’epoca
    dati_training.append({
        "Epoca": i + 1,
        "Errore_medio": errore,
        "Output": out
    })
    print(f"Epoca {i+1}/{epoche} - Errore medio: {errore:.6f} - Output: {out:.6f}")

# ------------------------------------------------------------
# 5. RISULTATI E GRAFICO
# ------------------------------------------------------------
df_training = pd.DataFrame(dati_training)
df_training["Output_denormalizzato"] = df_training["Output"] * 100

# Grafico dell'andamento
plt.figure(figsize=(8, 5))
plt.plot(df_training["Epoca"], df_training["Output_denormalizzato"], marker='o', linewidth=1)
plt.xlabel("Epoca")
plt.ylabel("Output denormalizzato medio")
plt.title("Andamento dell'output medio durante il training")
plt.grid(True)
plt.tight_layout()
plt.show()

# Mostra le prime righe del DataFrame finale
print(df_training.head())
