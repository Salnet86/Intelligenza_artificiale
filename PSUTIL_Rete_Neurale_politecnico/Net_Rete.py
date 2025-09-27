import random
import math
import psutil as ps
import pandas as pd
import random 
import matplotlib as plt
import matplotlib.pyplot as plt


temperatura=ps.sensors_temperatures()
# Lista vuota per salvare i dati
dati_training = []
dato=[]
for te , item in temperatura.items():
    for dati in item:
        dato.append({
            "sensore": te,
            "etichetta": dati.label or "N/A",
            "corrente (°C)": dati.current,
            "massima (°C)": dati.high,
            "critica (°C)": dati.critical
        })
pf=pd.DataFrame(dato)
#pf.columns
temp_corrente = pf['corrente (°C)']
temp_massima = pf['massima (°C)']
temp_critica = pf['critica (°C)']
dati_rete = []

for tempC in temp_corrente:
    dati_rete.append(tempC)

for tempMax in temp_massima:
    dati_rete.append(tempMax)

for tempCritical in temp_critica:
    dati_rete.append(tempCritical)

dati_normalizzati = [d / 100 for d in dati_rete]
x = dati_normalizzati

H1 = []
B1 = []

#pesi = random.uniform(0, 0.1)
#bias = random.uniform(0, 0.1)
H1 = [random.uniform(0, 0.1) for _ in range(neuroni)]
B1 = [random.uniform(0, 0.2) for _ in range(neuroni)]

B_out = 0.2
W_out = 0.3
target = 1
rate = 0.0001

def relu(x):
    return max(0, x)

def relu_derivative(x):
    return 1 if x > 0 else 0




neuroni = 2
epoche = 100

for i in range(epoche):
    for j in range(neuroni):
        pesi = random.uniform(0, 0.1)
        bias = random.uniform(0, 0.2)
        H1.append(pesi)
        B1.append(bias)

        for dati in x:
            z1 = H1[j] * dati + B1[j]
            a1 = relu(z1)
            out = W_out * a1 + B_out


            
            errore = 0.5 * (target - out) ** 2
            delta_out = (target - out)

          
            
            delta_h = delta_out * W_out * relu_derivative(z1)
            
            W_out = W_out - rate * delta_out * a1
            H1[j] = H1[j] - rate * delta_h * dati
            B1[j] = B1[j] - rate * delta_h
            B_out = B_out - rate * delta_out
           
        
 # Salvo i valori nel dizionario
            dati_training.append({
                'Epoca': i + 1,
                'Neurone': j + 1,
                'Errore': errore,
                'Output': out
            })

# Creo DataFrame pandas
df = pd.DataFrame(dati_training)

  # Stampo le prime righe per verificare
                 
           
        
      
        
        
    
        
 print(f"Epoca {i+1}, Neurone {j+1}, Errore: {errore:.6f} , Out:{out}")


#output_denormalizzati = [val * 100 for val in df['Output']]
df['Output_denormalizzati'] = df['Output'] * 100
#print(df.head())


import matplotlib.pyplot as plt

output_denorm_medio = df.groupby('Epoca')['Output_denormalizzati'].mean()

plt.plot(output_denorm_medio.index, output_denorm_medio.values)
plt.xlabel('Epoca')
plt.ylabel('Output denormalizzato medio')
plt.title('Andamento output denormalizzato medio per epoca')
plt.grid(True)
plt.show()
